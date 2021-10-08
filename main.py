import pathlib
import json

class FileReaderBase:

    ALLOWED_EXTENSIONS = (
        'json',
        'csv',
    )

    def __init__(self, filename, path=""):
        self.filename = filename
        self.path = path
        self.filetype = self.set_filetype()
        self.validated = self.validate()
        self.data = self.set_data()

    def validate(self):
        if self.filetype not in self.ALLOWED_EXTENSIONS:
            print("Nieobsługiwany format")
            return False
        return True

    def set_filetype(self):
        # return self.filename.split(".")[-1]
        return pathlib.Path(self.filename).suffix[1:]

    def get_filepath(self):
        if self.path:
            return f'{self.path}/{self.filename}'
        return self.filename

    def set_data(self):
        with open(self.get_filepath()) as file:
            if hasattr(self, f'get_{self.filetype}_data'):
                return getattr(self, f'get_{self.filetype}_data')(file)
            print(f"Konieczna implementacja metody: get_{self.filetype}_data na {self}")
            return []


class CSVReader(FileReaderBase):
    
    def get_csv_data(self, file):
        data = []
        for line in file.readlines():
            data.append(line.replace("\n", "").split(","))
        return data

class JSONReader(FileReaderBase):
    
    def get_json_data(self, file):
        json_data = json.loads(file.read())
        return [[key, value] for key, value in json_data.items()]


reader = JSONReader(filename="data.json")
print(reader.data)