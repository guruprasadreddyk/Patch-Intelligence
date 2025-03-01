# tests/conftest.py
import sys
import os

# Add the project root (one level above the tests folder) to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
