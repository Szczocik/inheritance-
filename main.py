import pathlib
import json
import pickle

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
        with open(self.get_filepath(), 'rb') as file:
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


class PICKLEReader(FileReaderBase):

    def get_pickle_data(self, file):
        print(pickle.load(file))


reader = PICKLEReader(filename="data2.pickle")

print(reader.data)

# with open('data.pickle','wb') as fout:
#     pickle.dump([1,2,3],fout)

# read data from a file
# with open('myfile.pickle') as fin:
#     print(pickle.load(fin))


data_file = {}
#
# pickled_data_file = pickle.dumps(data_file)
# print(pickled_data_file)

with open('data.pickle') as data_file:
    pickle.load(data_file)

# with open('data.pickle', 'wb') as file:
#     pickle.dump(data_file, file)

# print(data_file)
#
# # f = open('data2.pickle', 'wb')
# # pickle.dump(data2_file, f)
# # f.close()
# # print(data2_file)
# # data_file = pickle.loads(pickled_data_file)
# # print(data_file)
