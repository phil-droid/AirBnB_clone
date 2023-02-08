"""
Initializes a variable `storage` to create a
unique `FileStorage` instance for the AirBnB application.
"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
