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

def look_folder(root_folder):
    dict_ext = {}
    dir_list = []
    for name in os.listdir(root_folder):
        full_name = join(root_folder, name)
        if isdir(full_name):
            for result in look_folder(full_name):
                yield result
            continue
        name, ext = splitext(full_name)
        if ext in dict_ext:
            dict_ext[ext] += getsize(full_name)
        else:
            dict_ext[ext]  = getsize(full_name)
    yield __formatOutput(root_folder, dict_ext)

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
