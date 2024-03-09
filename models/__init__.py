#!/usr/bin/python3
"""The models __init__  method directory"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
