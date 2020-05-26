def unwrap_lines(text: str) -> str:
    paragraphs = text.split("\n\n")
    unwrapped_paragraphs =  [" ".join(paragraph.splitlines()) for paragraph in paragraphs]
    reflowed_paragraphs = "\n\n".join(unwrapped_paragraphs)
    return reflowed_paragraphs















