class cached_property:

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.name = None
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        if self.name not in instance.__dict__ and self.fget is not None:
            instance.__dict__[self.name] = self.fget(instance)
        if self.name in instance.__dict__:
            return instance.__dict__[self.name]
        if self.fget is None:
            raise AttributeError("unreadable attribute")

    def __set__(self, instance, value):
        if self.fset is None:
            instance.__dict__[self.name] = value
            return
        self.fset(instance, value)
        del instance.__dict__[self.name]

    def __delete__(self, instance):
        del instance.__dict__[self.name]
        if self.fdel is not None:
            self.fdel(instance)

    def getter(self, fget):
        self.fget = fget
        return self

    def setter(self, fset):
        self.fset = fset
        return self

    def deleter(self, fdel):
        self.fdel = fdel
        return self
