from collections import UserString
from unicodedata import normalize


class FuzzyString(UserString):
    def __eq__(self, other):
        if not isinstance(other, (FuzzyString, str)):
            return self.data.__eq__(other)
        return normalize("NFKD", self.data.casefold()).__eq__(normalize("NFKD", other.casefold()))

    def __lt__(self, other):
        if not isinstance(other, (FuzzyString, str)):
            return self.data.__lt__(other)
        return normalize("NFKD", self.data.casefold()).__lt__(normalize("NFKD", other.casefold()))

    def __le__(self, other):
        if not isinstance(other, (FuzzyString, str)):
            return self.data.__le__(other)
        return normalize("NFKD", self.data.casefold()).__le__(normalize("NFKD", other.casefold()))

    def __gt__(self, other):
        if not isinstance(other, (FuzzyString, str)):
            return self.data.__gt__(other)
        return normalize("NFKD", self.data.casefold()).__gt__(normalize("NFKD", other.casefold()))

    def __ge__(self, other):
        if not isinstance(other, (FuzzyString, str)):
            return self.data.__ge__(other)
        return normalize("NFKD", self.data.casefold()).__ge__(normalize("NFKD", other.casefold()))

    def __contains__(self, item):
        if not isinstance(item, (FuzzyString, str)):
            return self.data.__contains__(item)
        return normalize("NFKD", self.data.casefold()).__contains__(normalize("NFKD", item.casefold()))
