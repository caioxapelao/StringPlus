import json
import hashlib
from io import StringIO, BytesIO

class StringPlus:
    def __init__(self, string):
        self.string = string
        self.length = len(string)
        self.bytes = bytes(string.encode())
        self.md5 = hashlib.md5(string.encode('utf-8')).hexdigest()
    def json(self):
        self.json = json.loads(self.string)
