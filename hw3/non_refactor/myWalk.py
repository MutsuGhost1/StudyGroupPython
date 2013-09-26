#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     25/09/2013
# Copyright:   (c) Administrator 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from my.util import Stack
from my.util import Queue
from my.exceptions import IllegalCommandLineArgumentError

import os, sys

# tupple(dirpath, dirnames, filenames)
def __myWalkDfs(root):
    stack = Stack()

    dirs=[]
    for item in os.listdir(root):
        if(os.path.isdir(os.path.join(root,item))):
            dirs.append(os.path.join(root,item))
    stack.push((root, dirs))

    while not stack.isEmpty():
        root, dirs = stack.peek1()
        if 0 == len(dirs):
            dirs, nondirs = [],[]
            for item in os.listdir(root):
                if os.path.isdir(os.path.join(root, item)):
                    dirs.append(item)
                else:
                    nondirs.append(item)
            stack.pop()
            yield root, dirs, nondirs
        else:
            currentRoot = dirs[0]
            sub_dirs = []
            for item in os.listdir(currentRoot):
                if os.path.isdir(os.path.join(currentRoot, item)):
                    sub_dirs.append(os.path.join(currentRoot, item))
            stack.push((currentRoot, sub_dirs))
            del dirs[0]

# tupple(dirpath, dirnames, filenames)
def __myWalkBfs(root):
    queue = Queue()
    queue.enqueue(root)
    while not queue.isEmpty():
        currentRoot = queue.dequeue()
        dirs, nondirs = [], []
        for item in os.listdir(currentRoot):
            if os.path.isdir(os.path.join(currentRoot, item)):
                dirs.append(item)
                queue.enqueue(os.path.join(currentRoot, item))
            else:
                nondirs.append(item)
        yield currentRoot, dirs, nondirs

# tupple(dirpath, dirnames, filenames)
def myWalk(root, bBfs=True):
    if bBfs:
        return __myWalkBfs(root)
    else:
        return __myWalkDfs(root)

def main():
    if(2 <= len(sys.argv) <= 3 ):
        if os.path.isdir(sys.argv[1]):
            bBfs=False
            if 3 == len(sys.argv):
                bBfs = True
            for item in myWalk(sys.argv[1], bBfs):
                print item
        else:
            raise IllegalCommandLineArgumentError("Usage: python arg1-root-folder [arg2-traversal-method], arg1 isn't a folder")
    else:
        raise IllegalCommandLineArgumentError("Usage: python arg1-root-folder [arg2-traversal-method]")


if __name__ == '__main__':
    main()
