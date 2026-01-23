from typing import List, Dict

def chunk_text(
    text: str,
    source_url: str,
    page_title: str,
    chunk_size: int = 200,
    overlap: int = 50
) -> List[Dict]:

    sentences = text.split(". ")
    chunks = []
    current = []
    length = 0
    cid = 0

    for s in sentences:
        w = len(s.split())

        if length + w > chunk_size:
            chunks.append({
                "chunk_id": cid,
                "text": ". ".join(current).strip(),
                "metadata": {
                    "source_url": source_url,
                    "page_title": page_title
                }
            })
            cid += 1
            current = current[-max(1, overlap // 20):]
            length = sum(len(x.split()) for x in current)

        current.append(s)
        length += w

    if current:
        chunks.append({
            "chunk_id": cid,
            "text": ". ".join(current).strip(),
            "metadata": {
                "source_url": source_url,
                "page_title": page_title
            }
        })

    return chunks
