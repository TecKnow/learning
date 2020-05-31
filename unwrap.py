import re

one_break_str = r"(?<=\S)(?P<leading_space>\s*?)\n(?P<trailing_space>\s*?)(?=\S)"
one_break_re = re.compile(one_break_str)


def substitution_function(match):
    whole_match, leading_space, trailing_space = match.group(0, "leading_space", "trailing_space")
    if leading_space.endswith("  "):
        return whole_match
    if "\n" in trailing_space:
        return whole_match
    return " "


def unwrap_lines(text: str) -> str:
    return one_break_re.sub(substitution_function, text)


if __name__ == "__main__":
    from textwrap import dedent

    multiple_paragraphs = dedent("""
                Whether I'm teaching new Pythonistas or long-time Python
                programmers, I frequently find that **Python programmers
                underutilize multiple assignment**.

                Multiple assignment (also known as tuple unpacking or iterable
                unpacking) allows you to assign multiple variables at the same
                time in one line of code. This feature often seems simple after
                you've learned about it, but **it can be tricky to recall
                multiple assignment when you need it most**.

                In this article we'll see what multiple assignment is, we'll take
                a look at common uses of multiple assignment, and then we'll look
                at a few uses for multiple assignment that are often overlooked.

                Note that in this article I will be using [f-strings][] which are
                a Python 3.6+ feature. If you're on an older version of Python,
                you'll need to mentally translate those to use the string
                `format` method.
            """).strip()

    extra_linebreaks = dedent("""
            This is a line
            that is followed by another line


            There are 2 blank lines before this
            And there was 1 before this



            And three before this one
        """).lstrip()

    print(unwrap_lines(extra_linebreaks))
