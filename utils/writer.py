class FileWriter:
    def __init__(self):
        pass

    def append(self, file, data):
        with open(file, "a") as f:
            f.write(f"{data}\n")
