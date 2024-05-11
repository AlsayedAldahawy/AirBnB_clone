from models.engine.file_storage import FileStorage

storage = FileStorage()

try:
    storage.reload()
except:
    pass
