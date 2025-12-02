FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g @redocly/cli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /docs

COPY dft-theme /tmp/dft-theme

RUN pip install --no-cache-dir sphinx==8.2.3 sphinx-autobuild sphinx-tabs
RUN pip install --no-cache-dir -e /tmp/dft-theme
