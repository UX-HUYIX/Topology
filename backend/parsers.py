class QlogParser:
    def __init__(self, filepath):
        self.filepath = filepath

    def parse(self):
        with open(self.filepath, 'r') as file:
            data = file.readlines()
        # Implement parsing logic here
        return data

    def display(self):
        data = self.parse()
        for line in data:
            print(line.strip())
