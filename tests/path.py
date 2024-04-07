import os.path

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
TEMP = os.path.join(CURRENT_DIR, "temp")
RESOURCE = os.path.join(CURRENT_DIR, "resource")
ZIP_FILE = os.path.join(RESOURCE, 'file.zip')
