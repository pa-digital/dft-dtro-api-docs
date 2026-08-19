#!/usr/bin/env bash

set -euo pipefail

if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <documentation-path>" >&2
    exit 1
fi

DOCS_ROOT="$1"

IGNORE_HEADER=false
IGNORE_FOOTER=false

SRC="$DOCS_ROOT/build/html"
INPUT_DIR_NAME="$(basename "$DOCS_ROOT")"
OUT="output/$INPUT_DIR_NAME"
CSS_DIR="$DOCS_ROOT/source/_static/css"

ASSET_SEARCH_ROOT="$DOCS_ROOT"

mkdir -p "$OUT"

if [[ ! -d "$SRC" ]]; then
    echo "Source HTML directory not found: $SRC" >&2
    exit 1
fi

if [[ ! -d "$CSS_DIR" ]]; then
    echo "CSS directory not found: $CSS_DIR" >&2
    exit 1
fi

shopt -s nullglob
CSS_FILES=("$CSS_DIR"/*.css)
shopt -u nullglob

if (( ${#CSS_FILES[@]} == 0 )); then
    echo "No CSS files found in: $CSS_DIR" >&2
    exit 1
fi

CSS_FILE="$(mktemp)"
PERL_SCRIPT="$(mktemp)"
trap 'rm -f "$CSS_FILE" "$PERL_SCRIPT"' EXIT

###############################################################################
# Build one CSS block, embedding font files and CSS image URLs as base64 data URLs.
###############################################################################

{
    echo "<style>"

    perl - "$ASSET_SEARCH_ROOT" "${CSS_FILES[@]}" <<'PERL'
use strict;
use warnings;

use Cwd qw(abs_path);
use File::Basename qw(dirname basename);
use File::Find;
use File::Spec;
use MIME::Base64 qw(encode_base64);

my $asset_search_root = shift @ARGV;

sub mime_for_asset {
    my ($path) = @_;

    return "font/woff2"     if $path =~ /\.woff2$/i;
    return "font/woff"      if $path =~ /\.woff$/i;
    return "font/ttf"       if $path =~ /\.ttf$/i;
    return "font/otf"       if $path =~ /\.otf$/i;

    return "image/png"      if $path =~ /\.png$/i;
    return "image/jpeg"     if $path =~ /\.jpe?g$/i;
    return "image/gif"      if $path =~ /\.gif$/i;
    return "image/svg+xml"  if $path =~ /\.svg$/i;
    return "image/webp"     if $path =~ /\.webp$/i;
    return "image/avif"     if $path =~ /\.avif$/i;
    return "image/x-icon"   if $path =~ /\.ico$/i;
    return "image/bmp"      if $path =~ /\.bmp$/i;

    return undef;
}

sub url_decode {
    my ($value) = @_;
    $value =~ s/%([0-9A-Fa-f]{2})/chr(hex($1))/eg;
    return $value;
}

my %basename_cache;

sub find_asset_by_basename {
    my ($root, $name) = @_;

    return $basename_cache{$name} if exists $basename_cache{$name};

    my $found;

    find(
        sub {
            return if defined $found;
            return unless -f $_;

            if ($_ eq $name) {
                $found = $File::Find::name;
            }
        },
        $root
    );

    $basename_cache{$name} = $found;
    return $found;
}

sub resolve_asset_path {
    my ($base_dir, $url, $asset_search_root) = @_;

    my $clean_url = $url;
    $clean_url =~ s/[?#].*$//;

    my $decoded_url = url_decode($clean_url);

    return undef unless mime_for_asset($decoded_url);

    my @candidates;

    if (File::Spec->file_name_is_absolute($decoded_url)) {
        my $without_leading_slash = $decoded_url;
        $without_leading_slash =~ s{^/+}{};

        push @candidates, File::Spec->catfile($asset_search_root, $without_leading_slash);
    }
    else {
        push @candidates, File::Spec->rel2abs($decoded_url, $base_dir);
    }

    for my $candidate (@candidates) {
        return $candidate if -f $candidate;
    }

    my $base = basename($decoded_url);
    my $found = find_asset_by_basename($asset_search_root, $base);

    return $found if defined $found && -f $found;

    return undef;
}

sub asset_to_data_url {
    my ($path) = @_;

    my $mime = mime_for_asset($path);
    return undef unless defined $mime;

    open my $fh, "<:raw", $path or die "Cannot open asset file: $path\n";
    my $bytes = do { local $/; <$fh> };
    close $fh;

    my $base64 = encode_base64($bytes, "");

    return "data:$mime;base64,$base64";
}

for my $css_path (@ARGV) {
    open my $fh, "<", $css_path or die "Cannot open CSS file: $css_path\n";
    my $css = do { local $/; <$fh> };
    close $fh;

    my $css_dir = dirname(abs_path($css_path));

    $css =~ s{
        url\(
            \s*
            (?:
                "([^"]*)"
                |
                '([^']*)'
                |
                ([^)]+?)
            )
            \s*
        \)
    }{
        my $url = defined $1 ? $1 : defined $2 ? $2 : $3;
        $url =~ s/^\s+|\s+$//g;

        if ($url eq "" || $url =~ m{^(data:|https?:|//|#)}i) {
            qq{url("$url")};
        }
        else {
            my $asset_path = resolve_asset_path($css_dir, $url, $asset_search_root);

            if (defined $asset_path && -f $asset_path) {
                my $data_url = asset_to_data_url($asset_path);
                defined $data_url ? qq{url("$data_url")} : qq{url("$url")};
            }
            else {
                qq{url("$url")};
            }
        }
    }gex;

    print "\n/* Inlined from $css_path */\n";
    print $css;
    print "\n";
}
PERL

    echo "</style>"
} > "$CSS_FILE"

###############################################################################
# HTML processing script.
###############################################################################

cat > "$PERL_SCRIPT" <<'PERL'
use strict;
use warnings;

use Cwd qw(abs_path);
use File::Basename qw(dirname basename);
use File::Find;
use File::Spec;
use MIME::Base64 qw(encode_base64);

my $css_file = $ENV{"CSS_FILE"};
my $html_root = $ENV{"HTML_ROOT"};
my $asset_search_root = $ENV{"ASSET_SEARCH_ROOT"};

open my $css_fh, "<", $css_file or die "Cannot open CSS file: $css_file\n";
my $css = do { local $/; <$css_fh> };
close $css_fh;

my $input_file = $ARGV[0];
my $input_dir = dirname(abs_path($input_file));

my $html = do { local $/; <> };

sub mime_for_image {
    my ($path) = @_;

    return "image/png"      if $path =~ /\.png$/i;
    return "image/jpeg"     if $path =~ /\.jpe?g$/i;
    return "image/gif"      if $path =~ /\.gif$/i;
    return "image/svg+xml"  if $path =~ /\.svg$/i;
    return "image/webp"     if $path =~ /\.webp$/i;
    return "image/avif"     if $path =~ /\.avif$/i;
    return "image/x-icon"   if $path =~ /\.ico$/i;
    return "image/bmp"      if $path =~ /\.bmp$/i;

    return undef;
}

sub url_decode {
    my ($value) = @_;
    $value =~ s/%([0-9A-Fa-f]{2})/chr(hex($1))/eg;
    return $value;
}

my %basename_cache;

sub find_asset_by_basename {
    my ($root, $name) = @_;

    return $basename_cache{$name} if exists $basename_cache{$name};

    my $found;

    find(
        sub {
            return if defined $found;
            return unless -f $_;

            if ($_ eq $name) {
                $found = $File::Find::name;
            }
        },
        $root
    );

    $basename_cache{$name} = $found;
    return $found;
}

sub resolve_image_path {
    my ($url) = @_;

    my $clean_url = $url;
    $clean_url =~ s/[?#].*$//;

    my $decoded_url = url_decode($clean_url);

    return undef unless mime_for_image($decoded_url);

    my @candidates;

    if (File::Spec->file_name_is_absolute($decoded_url)) {
        my $without_leading_slash = $decoded_url;
        $without_leading_slash =~ s{^/+}{};

        push @candidates, File::Spec->catfile($html_root, $without_leading_slash);
        push @candidates, File::Spec->catfile($asset_search_root, $without_leading_slash);
    }
    else {
        # Most Sphinx image paths are relative to the current HTML file.
        push @candidates, File::Spec->rel2abs($decoded_url, $input_dir);

        # Your raw HTML image paths look like:
        #   _static/images/linestring.png
        # so also resolve relative to the built HTML root.
        push @candidates, File::Spec->catfile($html_root, $decoded_url);

        # Also try relative to the wider project root.
        push @candidates, File::Spec->catfile($asset_search_root, $decoded_url);
    }

    for my $candidate (@candidates) {
        return $candidate if -f $candidate;
    }

    my $base = basename($decoded_url);
    my $found = find_asset_by_basename($asset_search_root, $base);

    return $found if defined $found && -f $found;

    return undef;
}

sub image_to_data_url {
    my ($path) = @_;

    my $mime = mime_for_image($path);
    return undef unless defined $mime;

    open my $fh, "<:raw", $path or die "Cannot open image file: $path\n";
    my $bytes = do { local $/; <$fh> };
    close $fh;

    my $base64 = encode_base64($bytes, "");

    return "data:$mime;base64,$base64";
}

sub tag_has_exact_class {
    my ($tag, $wanted_class) = @_;

    return 0 unless $tag =~ /\bclass\s*=\s*(['"])(.*?)\1/is;

    my $class_value = $2;
    my @classes = split /\s+/, $class_value;

    for my $class (@classes) {
        return 1 if $class eq $wanted_class;
    }

    return 0;
}

sub remove_blocks_with_class {
    my ($html, $wanted_class) = @_;

    pos($html) = 0;

    while ($html =~ m{<([a-zA-Z][\w:-]*)(?=[^>]*\bclass\s*=)[^>]*>}gis) {
        my $tag_name = lc $1;
        my $opening_tag = $&;
        my $block_start = $-[0];
        my $opening_tag_end = $+[0];

        next unless tag_has_exact_class($opening_tag, $wanted_class);

        if ($opening_tag =~ m{/>\s*$}) {
            substr($html, $block_start, $opening_tag_end - $block_start) = "";
            pos($html) = $block_start;
            next;
        }

        my $depth = 1;
        pos($html) = $opening_tag_end;

        while ($html =~ m{</?$tag_name\b[^>]*>}gis) {
            my $tag = $&;
            my $tag_end = $+[0];

            if ($tag =~ m{^</}i) {
                $depth--;

                if ($depth == 0) {
                    substr($html, $block_start, $tag_end - $block_start) = "";
                    pos($html) = $block_start;
                    last;
                }
            }
            elsif ($tag !~ m{/>\s*$}) {
                $depth++;
            }
        }

        last if $depth > 0;
    }

    return $html;
}

# Remove existing stylesheet links.
$html =~ s{
    <link\b
    (?=[^>]*\bstylesheet\b)
    [^>]*>
    \s*
}{}gix;

# Inject combined CSS before </head>. If </head> is missing, prepend it.
if ($html =~ m{</head>}i) {
    $html =~ s{</head>}{$css\n</head>}i;
}
else {
    $html = $css . "\n" . $html;
}

if (($ENV{"IGNORE_HEADER"} // "") eq "true") {
    $html = remove_blocks_with_class($html, "govuk-header");
}

if (($ENV{"IGNORE_FOOTER"} // "") eq "true") {
    $html = remove_blocks_with_class($html, "govuk-footer");
}

# Inline quoted <img src="..."> or <img src='...'> attributes.
$html =~ s{
    (<img\b[^>]*?\bsrc\s*=\s*)
    (["'])
    ([^"']+)
    \2
    ([^>]*?>)
}{
    my ($prefix, $quote, $src, $suffix) = ($1, $2, $3, $4);

    if ($src eq "" || $src =~ m{^(data:|https?:|//|#)}i) {
        qq{$prefix$quote$src$quote$suffix};
    }
    else {
        my $image_path = resolve_image_path($src);

        if (defined $image_path && -f $image_path) {
            my $data_url = image_to_data_url($image_path);

            if (defined $data_url) {
                qq{$prefix$quote$data_url$quote$suffix};
            }
            else {
                warn "Could not create data URL for image: $src in $input_file\n";
                qq{$prefix$quote$src$quote$suffix};
            }
        }
        else {
            warn "Could not resolve image: $src in $input_file\n";
            qq{$prefix$quote$src$quote$suffix};
        }
    }
}gexis;

# Inline unquoted <img src=...> attributes, just in case.
$html =~ s{
    (<img\b[^>]*?\bsrc\s*=\s*)
    ([^\s>]+)
    ([^>]*?>)
}{
    my ($prefix, $src, $suffix) = ($1, $2, $3);

    if ($src eq "" || $src =~ m{^(data:|https?:|//|#)}i) {
        qq{$prefix$src$suffix};
    }
    else {
        my $image_path = resolve_image_path($src);

        if (defined $image_path && -f $image_path) {
            my $data_url = image_to_data_url($image_path);

            if (defined $data_url) {
                qq{$prefix"$data_url"$suffix};
            }
            else {
                warn "Could not create data URL for image: $src in $input_file\n";
                qq{$prefix$src$suffix};
            }
        }
        else {
            warn "Could not resolve image: $src in $input_file\n";
            qq{$prefix$src$suffix};
        }
    }
}gexis;

# Remove srcset attributes, because they may still point to external image files.
$html =~ s{\s+srcset\s*=\s*"[^"]*"}{}gis;
$html =~ s{\s+srcset\s*=\s*'[^']*'}{}gis;

sub resolve_js_path {
    my ($url) = @_;

    my $clean_url = $url;
    $clean_url =~ s/[?#].*$//;

    my @candidates = (
        File::Spec->rel2abs($clean_url, $input_dir),
        File::Spec->catfile($html_root, $clean_url),
        File::Spec->catfile($asset_search_root, $clean_url),
    );

    for my $candidate (@candidates) {
        return $candidate if -f $candidate;
    }

    return undef;
}

$html =~ s{
    <script\b([^>]*?)src=(["'])([^"']+)\2([^>]*)></script>
}{
    my $src = $3;

    if ($src =~ m{^(https?:|//)}i) {
        $&;
    }
    else {
        my $js_path = resolve_js_path($src);

        if (defined $js_path && -f $js_path) {
            open my $fh, "<", $js_path
                or die "Cannot open JS file: $js_path\n";

            my $js = do { local $/; <$fh> };
            close $fh;

            qq{<script>\n$js\n</script>};
        }
        else {
            warn "Could not resolve JS: $src\n";
            $&;
        }
    }
}gexis;

print $html;
PERL

export CSS_FILE
export IGNORE_HEADER
export IGNORE_FOOTER
export HTML_ROOT="$SRC"
export ASSET_SEARCH_ROOT

###############################################################################
# Process all HTML files, preserving relative paths.
###############################################################################

find "$SRC" -type f -name '*.html' \
    ! -name 'index.html' \
    ! -name 'genindex.html' \
    ! -name 'search.html' \
    -print0 | while IFS= read -r -d '' html; do
    rel="${html#$SRC/}"
    out="$OUT/$rel"

    mkdir -p "$(dirname "$out")"

    perl "$PERL_SCRIPT" "$html" > "$out"

    echo "Processed: $rel"
done

echo "Done. Output written to: $OUT"