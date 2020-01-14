with open('test.txt', 'r') as rf:
    with open('test2.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

with open('google.png', 'rb') as google:
    with open('n.png', 'wb') as novak:
        chunk_size = 4096
        rf_chunk = google.read(chunk_size)
        while len(rf_chunk) > 0:
            novak.write(rf_chunk)
            rf_chunk = google.read(chunk_size)
