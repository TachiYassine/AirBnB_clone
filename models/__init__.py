#!/usr/bin/python3

"""
This file will be used to initialize our storage system for
the airbnb clone  project (for storing and managing data persistently).
The FileStorage class is instantiated, and we wll be using its reload method
to ensure that any existing data used in this project is loaded into memory
when the application starts.
"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
