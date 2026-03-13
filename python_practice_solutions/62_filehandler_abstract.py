
from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

class TextFileHandler(FileHandler):
    def read(self):
        print("Reading text file")

    def write(self, data):
        print("Writing text:", data)

class CSVFileHandler(FileHandler):
    def read(self):
        print("Reading CSV file")

    def write(self, data):
        print("Writing CSV:", data)
