from abc import ABC, abstractmethod


class DataSource(ABC):

    @abstractmethod
    def writeData(self, data):
        pass

    @abstractmethod
    def readData(self) -> str:
        pass


class FileDataSource(DataSource):
    def __init__ (self, filename):
        self._file = filename

    def writeData(self, data):
        # write data to file.
        with open (self._file, "w") as file:
            file.write(data)

    def readData(self) -> str:
        # read data from file.
        with open(self._file, "r") as file:
            return file.readline()


class EncryptionDecorator(DataSource):
    def __init__(self, writer):
        self.writer = writer

    def writeData(self, data):
        # encrypt the data
        # pass encrypted data to wrapper
        data = f"Encrypted {data}"
        self.writer.writeData(data)

    def readData(self) -> str:
        # get encrypted data
        # decrypt it
        # return it
        line = self.writer.readData()
        line = line.replace("Encrypted ", "")
        return line


encryption = EncryptionDecorator(FileDataSource("example.txt"))
encryption.writeData("Hello")
print(encryption.readData())