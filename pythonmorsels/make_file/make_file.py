from pathlib import Path
import tempfile
from contextlib import contextmanager
import locale

@contextmanager
def make_file(contents=None, *, directory=None, **options):
    try:
        if "mode" not in options:
            options["mode"] = "a"
        named_temp_file = tempfile.NamedTemporaryFile(delete=False, dir=directory, **options)
        if contents is not None:
            named_temp_file.write(contents)
        named_temp_file.close()
        yield named_temp_file.name
    finally:
        named_temp_file.close()
        Path(named_temp_file.name).unlink()

