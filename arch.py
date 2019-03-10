import os
import sys
import time
import re


class File(object):
    def __init__(self, filename=None, filepath=None, size=None, name=None,
                 date=None, content=None):
        self.name = filename
        self.filepath = filepath
        self.name = name
        self.date = date
        self.size = size
        self.content = content

    def set_content(self, content):
        self.content = content

    def add_file(self):
        self.name = os.path.basename(self.filepath)
        statinfo = os.stat(self.filepath)
        self.date = time.ctime(statinfo.st_ctime)
        with open(self.filepath, 'rb') as f:
            f = f.read()
        self.content = f
        self.size = len(f)

    def __str__(self):
        return "Name of the file: '{}';Date of creation:{};Size: {} bytes.".format(self.name, self.date, self.size)
