"""
api/index.py - Vercel Serverless Function entrypoint.
Imports and exports the FastAPI application instance for Vercel's Python runtime.
"""

import sys
import os

# Add root directory to sys.path so backend module can be imported
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from backend.app import app

# Export app for Vercel
__all__ = ["app"]
