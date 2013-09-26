
import sys

class IllegalArgumentError (Exception):
    def __init__(self):
        self.args = sys.argv
        print str(len(self.args))

    def __str__(self):
        return str(self.args)

# please implement subclass IllegalCommandLineArgumentError for IllegalArgumentError
