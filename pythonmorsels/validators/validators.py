from numbers import Number
from typing import Any, Optional


class PositiveNumber:

    _default_initial_value = object()

    def __set_name__(self, owner: Any, name: str):
        self.private_name = f"_{name}"

    def __init__(self, initial_value: Optional[int] = None):
        self.initial_value = initial_value if initial_value is not None else self._default_initial_value

    def __get__(self, instance, owner):
        attr_value = getattr(instance, self.private_name, self.initial_value)
        if attr_value is not self._default_initial_value:
            return attr_value
        else:
            raise AttributeError(f"'{owner}' object has no attribute '{self.private_name[1:]}'")

    def __set__(self, instance, value):
        setattr(instance, self.private_name, self.validate(value))

    @staticmethod
    def validate(value):
        if isinstance(value, Number) and value > 0:
            return value
        else:
            raise ValueError("Positive number required")
