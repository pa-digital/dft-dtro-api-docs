import os
import shutil

def copy_shared_pages():
    # Get the path to the current file (inside dft_theme/utils/)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Go up one level to reach dft_theme/
    theme_root = os.path.abspath(os.path.join(current_dir, '..'))

    # Path to the shared pages inside the theme
    pages_dir = os.path.join(theme_root, 'pages')

    if not os.path.exists(pages_dir):
        raise FileNotFoundError(f"Shared pages directory not found: {pages_dir}")

    # Assume the Sphinx project is calling this, and we want to copy into its source/shared/
    # Get the current working directory (should be the Sphinx project root)
    project_root = os.getcwd()
    target_dir = os.path.join(project_root, 'shared')

    os.makedirs(target_dir, exist_ok=True)

    # Copy all .rst files
    for filename in os.listdir(pages_dir):
        if filename.endswith('.rst'):
            src = os.path.join(pages_dir, filename)
            dst = os.path.join(target_dir, filename)
            shutil.copyfile(src, dst)
            print(f"Copied {filename} to {target_dir}")
