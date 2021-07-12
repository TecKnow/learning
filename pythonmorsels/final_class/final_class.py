
class Unsubclassable():
    @classmethod
    def __init_subclass__(cls, **kwargs):
        raise TypeError(f"{cls.__name__} is not an appropriate parent class")