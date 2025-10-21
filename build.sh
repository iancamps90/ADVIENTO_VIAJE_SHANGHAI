#!/bin/bash
# Shanghai Advent Journey - Optimized Build Script
set -e

echo "🏮 Building Shanghai Advent Journey..."

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Clean previous builds
rm -rf public

# Initialize and export
reflex init
reflex export --frontend-only

# Extract to public directory
rm -rf public
unzip frontend.zip -d public
rm -f frontend.zip

# Clean up
deactivate

echo "✅ Build completed successfully!"
echo "📁 Static files ready in public/ directory"