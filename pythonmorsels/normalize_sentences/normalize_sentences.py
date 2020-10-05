import re

endfinder = re.compile(r"([!?.]) (\w)")


def normalize_sentences(text: str) -> str:
    return re.sub(endfinder, r"\1  \2", text)
