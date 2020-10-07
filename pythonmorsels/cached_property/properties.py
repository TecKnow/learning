class cached_property:
    def __init__(self, original_function):
        self.original_function = original_function
        self.name = original_function.__name__

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.name not in instance.__dict__:
            computed_value = self.original_function(instance)
            instance.__dict__[self.name] = computed_value
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]
