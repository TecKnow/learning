from functools import wraps
from collections import namedtuple

NO_RETURN = object()

Call_Record = namedtuple("Call_Record", "args kwargs return_value, exception")


def record_calls(func):
    @wraps(func)
    def record_calls_wrapper(*args, **kwargs):
        record_calls_wrapper.call_count += 1
        exception = None
        ret_val = NO_RETURN
        try:
            ret_val = func(*args, **kwargs)
        except Exception as ex:
            exception = ex
            raise
        finally:
            record_calls_wrapper.calls.append(Call_Record(args, kwargs, ret_val, exception))
        return ret_val

    # include exception tracking.

    record_calls_wrapper.call_count = 0
    record_calls_wrapper.calls = list()
    return record_calls_wrapper
