from contextlib import contextmanager


class supress_context:
    def __init__(self):
        self.exception = None
        self.traceback = None


@contextmanager
def suppress(*exception_types):
    current_exception = supress_context()
    current_exception.exception = None
    current_exception.traceback = None
    try:
        yield current_exception
    except Exception as ex:
        if not isinstance(ex, exception_types):
            raise ex
        else:
            current_exception.traceback = ex.__traceback__
            current_exception.exception = ex
