#-------------------------------------------------------------------------------
# Name:        look_folder
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
    print "-" * 10
    print "In Folder: ", root
    for ext, size in dict.items() :
        print "\t ", ext, " total size:", size
    print "-" * 10

def look_folder(root_folder):
    dict_ext = {}
    for name in os.listdir(root_folder):
        full_name = join(root_folder, name)
        if isdir(full_name):
            look_folder(full_name)
            continue
        name, ext = splitext(full_name)
        if ext in dict_ext:
            dict_ext[ext] += getsize(full_name)
        else:
            dict_ext[ext]  = getsize(full_name)
    __formatOutput(root_folder, dict_ext);

def main():
    if(2 == len(sys.argv)):
        if isdir(sys.argv[1]):
            look_folder(sys.argv[1])
        else:
            print "Invalud Full Path!"
            print "Usage: python look_folder_recursive.py [full-path]"
    else:
        print "Usage: python look_folder_recursive.py [full-path]"

if __name__ == '__main__':
    main()
