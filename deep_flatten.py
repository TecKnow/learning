import collections


def deep_flatten(collection):
    for item in collection:
        if isinstance(item, collections.Iterable) and not isinstance(item, str):
            yield from deep_flatten(item)
        else:
            yield item
