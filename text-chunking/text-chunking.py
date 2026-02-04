def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    step = chunk_size - overlap
    i = 0
    res = []

    for i in range(0, len(tokens), step):
        if i+chunk_size >= len(tokens):
            res.append(tokens[i:].copy())
            break
        res.append(tokens[i : i+chunk_size].copy())

    return res