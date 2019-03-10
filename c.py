import os
import sys
import time
import re
import arch
import argparse
import pdb


def add_to_archive(archive_name, filepath):
    try:
         os.path.exists(filepath)
         file_to_add = arch.File(filepath= filepath)
         file_to_add.add_file()
         with open(archive_name, 'a+') as archive:
             archive.write("{};{};{};{}".format(file_to_add.size, file_to_add.name, file_to_add.date, file_to_add.content))
    except Exception as e:
         print e


def list_archive(archive_name):
    files_list = []
    counter = 0
    with open(archive_name, 'rb') as archive:
        archive = archive.read()
        while counter <= len(archive):
            info = archive.split(';', 3)[:3]
            file = arch.File(size= info[0], name= info[1], date= info[2])
            print file
            counter += sum(len(i) for i in info)
            file.size = int(file.size)
            file.content = archive[counter: file.size]
            counter += file.size






def main(archive_name, action, filepath):
    if args.action == 'add':
        add_to_archive(archive_name, filepath)
    elif args.action == 'list':
        list_archive(archive_name)





if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--archive_name', help='The name of the archive.')
    parser.add_argument('--action', help='Action to do on the archive.', choices=['add', 'list'])
    parser.add_argument('--filepath', help='The file you want to be entered to the archive.')
    args = parser.parse_args()
    main(args.archive_name, args.action, args.filepath)
