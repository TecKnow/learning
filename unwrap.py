import re

one_break_str = r"(\S)\n(\S)"
one_break_re = re.compile(one_break_str)


def unwrap_lines(text: str) -> str:
    reflowed_paragraphs = one_break_re.sub(r"\1 \2", text)
    return reflowed_paragraphs
