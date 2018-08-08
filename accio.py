#!/usr/bin/python3

import argparse
import configuration
import ls
import os

config = configuration.ConfigurationHelper()

parser = argparse.ArgumentParser(description='Open files and projects with a swish and a flick!')

subparsers = parser.add_subparsers(help='sub-command help', dest='command')


parser_ls = subparsers.add_parser('ls', help='list files that have been added: accio ls [<pattern>]' )
parser_ls.add_argument('pattern', help='pattern to match', nargs='?')

parser_add = subparsers.add_parser('add', help='add a file: accio <filepath> <nickname>')
parser_add.add_argument('file', help="file or folder")
parser_add.add_argument('fileNickName', help="nick name for this item")

parser_rm = subparsers.add_parser('rm', help='remove a file: accio <nickname>')
parser_rm.add_argument('fileNickName', help='nickName of file to run')

parser_run = subparsers.add_parser('run')
parser_run.add_argument('fileNickName', help='nickName of file to run')

parser_editor = subparsers.add_parser('editor', help="specify the editor you'd like to use: accio editor <command>")
parser_editor.add_argument('cmd', help='command to run your editor of choice')


args = parser.parse_args()

if args.command == 'ls':
    ls.listFiles(args.pattern)

elif args.command == 'add':
    print('adding a file ' + args.fileNickName + ' with nickname ' + args.file)
    print('./accio run ' + args.fileNickName + ' to retrive the file')
    config.writeFile(args.fileNickName, args.file)

elif args.command == 'rm':
    print('removing file ' + args.fileNickName + ' THIS DOES NOT DELETE THE FILE FROM YOUR SYSTEM')
    config.removeFile(args.fileNickName)

elif args.command == 'editor':
    print('Files will now be opened using command: ' + args.cmd)
    config.setEditor(args.cmd)

elif args.command == 'run':
    path = config.getFilePath(args.fileNickName)
    
    if path != False:
        print('opening ' + path)
        os.system(config.getEditor() + ' ' + path + ' &')