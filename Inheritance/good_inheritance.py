# custom exception defitionName SHOULD end in 'Error'
class InvalidOperatioError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperatioError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperatioError("Stream is already closed")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

# A Good Example of Inheritance.
#   -SRP
#   -No multi-level inheritance
#   -No multiple inheritance
