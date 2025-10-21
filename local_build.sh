#!/bin/bash
# Shanghai Advent Journey - Local Development Build
set -e

echo "🏮 Building Shanghai Advent Journey (Local)..."

# Activate existing virtual environment
source .venv/bin/activate

# Install/update dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Initialize and export
reflex init
reflex export --frontend-only

# Extract to public directory
rm -rf public
unzip frontend.zip -d public
rm -f frontend.zip

# Clean up
deactivate

echo "✅ Local build completed successfully!"
echo "📁 Static files ready in public/ directory"
echo "🚀 Run 'reflex run' to start development server"