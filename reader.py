import csv
import pathlib
import json
import pickle
import sys


class FileReaderBase:
    ALLOWED_EXTENSIONS = (
        'json',
        'csv',
        'pickle',
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
        with open(self.get_filepath(), 'r') as file:
            if hasattr(self, f'get_{self.filetype}_data'):
                return getattr(self, f'get_{self.filetype}_data')(file)
            print(f"Konieczna implementacja metody: get_{self.filetype}_data na {self}")
            return []

    def change_data(self, changes):
        for change in changes:
            splitted_change = change.split(',')
            y = int(splitted_change[0])
            x = int(splitted_change[1])
            value = splitted_change[2]
            print(self.data)
            self.data[x][y] = value


class CSVReader(FileReaderBase):

    def get_csv_data(self, file):
        data = []
        for line in file.readlines():
            data.append(line.replace("\n", "").split(","))
        return data


class CSVWriter:

    def save_data(self, output_filename, data):
        with open(output_filename, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(data)

class JSONReader(FileReaderBase):

    def get_json_data(self, file):
        json_data = json.loads(file.read())
        return [[key, value] for key, value in json_data.items()]


class JSONWriter:

    def save_data(self, output_filename, data):
        with open(output_filename, 'w') as file:
            writer = json.dumps(file)
            writer.dumps(data)


class PICKLEReader(FileReaderBase):

    def get_pickle_data(self, file):
        pickle_data = pickle.loads(file.read())
        return [[key, value] for key, value in pickle_data.items()]


params = sys.argv[1:]

input_filename = params[0]
output_filename = params[1]
changes = params[2:]
input_suffix = pathlib.Path(input_filename).suffix[1:]
output_suffix = pathlib.Path(output_filename).suffix[1:]

if input_suffix == 'csv':
    reader = CSVReader(filename=input_filename)
    reader.set_data()
    reader.change_data(changes)


if output_suffix == 'csv':
    writer = CSVWriter()
    writer.save_data(output_filename, reader.data)

