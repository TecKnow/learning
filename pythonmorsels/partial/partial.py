import typing

SKIP = object()


class partial:

    def __init__(self, func: typing.Callable, *args, **kwargs):
        self.func = func
        self.saved_args = args
        self.saved_kwargs = kwargs

    def __call__(self, *args, **kwargs) -> typing.Any:
        return self.func(*self.saved_args, *args, **kwargs, **self.saved_kwargs)
