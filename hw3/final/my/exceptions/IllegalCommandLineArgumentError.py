
from IllegalArgumentError import IllegalArgumentError

class IllegalCommandLineArgumentError (IllegalArgumentError):
    def __init__(self, msg=""):
        IllegalArgumentError.__init__(self)
        self.msg = msg

    def __str__(self):
        return " actual arguments num = " + str(len(super(IllegalCommandLineArgumentError, self).args) -1) + "\n " + str(self.msg)

if __name__ == '__main__':
    import sys
    ex = IllegalCommandLineArgumentError()

    print ex.__dict__

    print str(ex)