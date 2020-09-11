from pathlib import Path
import tempfile
import os
from typing import NamedTuple


class Dirs(NamedTuple):
    current: str
    previous: str


class cd:
    def __init__(self, path=None):
        self.temp_dir = None
        if path is None:
            self.temp_dir = tempfile.TemporaryDirectory()
            self.new_path = self.temp_dir.name
        else:
            self.new_path = Path(path)

    def __enter__(self):
        self.old_path = os.getcwd()
        os.chdir(self.new_path)
        return Dirs(current=str(self.new_path), previous=str(self.old_path))

    def __exit__(self, exc_type=None, exc_value=None, exc_traceback=None):
        os.chdir(self.old_path)
        if self.temp_dir:
            self.temp_dir.cleanup()

    enter = __enter__
    exit = __exit__
