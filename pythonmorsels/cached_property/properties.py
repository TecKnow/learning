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
        del instance.__dict__[self.name]
        self.fset(instance, value)

    def __delete__(self, instance):
        del instance.__dict__[self.name]
        if self.fdel is not None:
            self.fdel(instance)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)
