"""
Vercel API handler for Reflex app
"""
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the Reflex app
from app import app

# Vercel expects a handler function
def handler(request):
    return app(request)
