chunk_size = 700
with open("notas.pdf", "rb") as archivo:
    chunk = archivo.read(chunk_size)
    while chunk:
        print(chunk)    
        chunk = archivo.read(chunk_size)