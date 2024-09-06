with open("error.log") as log:
    log.seek(10)
    print(log.read(25))
    print(log.read(35))