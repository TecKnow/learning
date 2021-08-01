import collections
import typing

SKIP = object()


class partial:

    def __init__(self, func: typing.Callable, *args, **kwargs):
        self.func = func
        self.saved_args = args
        self.saved_kwargs = kwargs
        self.skip_count = sum(1 for x in self.saved_args if x == SKIP)

    def __call__(self, *args, **kwargs) -> typing.Any:
        if len(args) < self.skip_count:
            raise TypeError("Not enough positional arguments given")
        supplied_args = collections.deque(args)
        combined_args = []
        for arg in self.saved_args:
            if arg == SKIP:
                combined_args.append(supplied_args.popleft())
            else:
                combined_args.append(arg)
        combined_args.extend(supplied_args)
        return self.func(*combined_args, **kwargs, **self.saved_kwargs)

    def partial(self, *args, **kwargs):
        new_args = self.saved_args + args
        new_kwargs = self.saved_kwargs | kwargs
        return self.__class__(self.func, *new_args, **new_kwargs)

    def __repr__(self):
        args_str = ', '.join(str(x) for x in self.saved_args)
        kwargs_str = ', '.join(f"{k}={v}" for k, v in self.saved_kwargs.items())
        param_str = ', '.join((args_str, kwargs_str))
        return f"partial({self.func.__name__}({param_str})),"
