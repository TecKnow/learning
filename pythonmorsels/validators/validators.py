from abc import ABC, abstractmethod
from numbers import Number


class Validator(ABC):
    _no_value = object()

    def __init__(self, initial_value=_no_value):
        self.initial_value = initial_value

    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, instance, owner=None):
        attr_value = getattr(instance, self.private_name, self.initial_value)
        if attr_value is not self._no_value:
            return attr_value
        else:
            raise AttributeError(f"'{owner}' object has no attribute '{self.private_name[1:]}'")

    def __set__(self, instance, value):
        validated_value = self.validate(value)
        set_value = validated_value if validated_value is not None else value
        setattr(instance, self.private_name, set_value)

    @abstractmethod
    def validate(self, value):
        pass


class PositiveNumber(Validator):

    @staticmethod
    def validate(value):
        if isinstance(value, Number) and value > 0:
            return value
        else:
            raise ValueError("Positive number required")
