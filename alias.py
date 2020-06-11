class alias:
    def __init__(self, target: str, write: bool = False) -> None:
        self.target = target
        self.write = write

    def __get__(self, instance, owner):
        if instance is not None:
            return getattr(instance, self.target)
        return getattr(owner, self.target)

    def __set__(self, instance, value):
        if not self.write:
            raise AttributeError
        return setattr(instance, self.target, value)
