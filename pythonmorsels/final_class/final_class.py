class UnsubclassableType(type):
    def __new__(mcs, name, bases, dct, *args, **kwargs):
        x = super().__new__(mcs, name, bases, dct, *args, **kwargs)
        for parent_class in bases:
            if isinstance(parent_class, mcs):
                raise TypeError(f"{parent_class.__name__} is not an appropriate base class")
        return x


def final_class(cls):
    """Make a class unavailable for subclassing"""
    new_class = UnsubclassableType(cls.__name__, cls.__bases__, dict(cls.__dict__))
    return new_class


@final_class
class Unsubclassable():
    pass
