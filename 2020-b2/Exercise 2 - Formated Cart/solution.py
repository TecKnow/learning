from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    quantity: float
    measure: str
    name: str
    price: float

    def __str__(self):
        # '    2 grain rice       @ $1.0...$2.0'
        return f'    {self.quantity} {self.measure} {self.name}       @ ${self.price:.1f}...${self.price * self.quantity:.1f}'


class Cart:
    def __init__(self):
        self.items = list()

    def add(self, item: Item):
        self.items.append(item)

    def __format__(self, format_spec):
        if format_spec == "short":
            return ', '.join(sorted(item.name for item in self.items))
        elif format_spec == "long":
            return "\n".join(str(item) for item in self.items)
