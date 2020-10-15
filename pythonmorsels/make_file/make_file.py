from pathlib import Path
import tempfile
from contextlib import contextmanager

@contextmanager
def make_file(contents=None):
    try:
        named_temp_file = tempfile.NamedTemporaryFile(delete=False)
        if contents is not None:
            named_temp_file.write(contents)
        named_temp_file.close()
        yield named_temp_file.name
    finally:
        Path(named_temp_file.name).unlink()

