#!/usr/bin/python3
"""
module that initialize
FileStorage object
"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
