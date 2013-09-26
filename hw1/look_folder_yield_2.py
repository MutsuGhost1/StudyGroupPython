#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     06/09/2013
# Copyright:   (c) Administrator 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os, sys
from os.path import isdir, join, splitext, getsize

def __formatOutput(root, dict):
    output  = ""
    output += "-" * 10 + os.linesep
    output += ("In Folder: " + str(root) + os.linesep)
    for ext, size in dict.items() :
        output += ("\t "+ ext + " total size:"+ str(size) + os.linesep)
    output += ("-" * 10 + os.linesep)
    return output

def myWalk(root, topdown=False):
    names = os.listdir(root)
    dirs, non_dirs = [], []
    for name in names:
        if isdir(join(root, name)):
            dirs.append(name)
        else:
            non_dirs.append(name)
    if topdown:
        yield root, dirs, non_dirs
    for name in dirs:
        new_path = join(root, name)
        for x in myWalk(new_path, topdown):
            yield x
    if not topdown:
        yield root, dirs, non_dirs

def look_folder(root):
    for root_path, dirs, non_dirs in myWalk(root):
        dict_ext = {}
        for file_name in non_dirs:
            full_file_path = join(root_path, file_name)
            name, ext = splitext(full_file_path)
            if ext in dict_ext:
                dict_ext[ext] += getsize(full_file_path)
            else:
                dict_ext[ext]  = getsize(full_file_path)
        yield __formatOutput(root_path, dict_ext)

def main():
    if(2 == len(sys.argv)):
        if isdir(sys.argv[1]):
            for result in look_folder(sys.argv[1]):
                print result
        else:
            print "Invalud Full Path!"
            print "Usage: python look_folder_recursive.py [full-path]"
    else:
        print "Usage: python look_folder_recursive.py [full-path]"

if __name__ == '__main__':
    main()
