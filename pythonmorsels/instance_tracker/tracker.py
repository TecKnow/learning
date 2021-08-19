from weakref import WeakSet


def instance_tracker(registry_attribute_name: str = "instances"):
    class instance_tracking_class:
        def __new__(cls, *args, **kwargs):
            registry = getattr(cls, registry_attribute_name)  # type: WeakSet
            new_instance = super().__new__(cls)
            registry.add(new_instance)
            return new_instance

    setattr(instance_tracking_class, registry_attribute_name, WeakSet())
    return instance_tracking_class
