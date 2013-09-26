
import sys

class IllegalArgumentError (Exception):
    def __init__(self):
        self.args = sys.argv
        print str(len(self.args))

    def __str__(self):
        return str(self.args)

class IllegalCommandLineArgumentError (IllegalArgumentError):
    def __init__(self, msg=""):
        IllegalArgumentError.__init__(self)
        self.msg = msg

    def __str__(self):
        return " actual arguments num = " + str(len(super(IllegalCommandLineArgumentError, self).args) -1) + "\n " + str(self.msg)
