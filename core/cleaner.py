import re

def clean_text(text: str) -> str:
    text = re.sub(r"[\x00-\x1f\x7f-\x9f]", " ", text)
    boilerplate = [
        r"Jump to content",
        r"From Wikipedia, the free encyclopedia",
        r"Navigation menu",
    ]
    for b in boilerplate:
        text = re.sub(b, " ", text, flags=re.IGNORECASE)

    text = re.sub(r"\s+", " ", text)
    return text.strip()
