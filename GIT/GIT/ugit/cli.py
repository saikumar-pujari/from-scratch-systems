import argparse
import os
import sys
from . import data


def test() -> None:
    print("This is a test function for cli.py")


def main() -> None:
    # process the command line arguments and return a Namespace object containing the arguments
    args = parse_args()
    # print the Namespace object to the console (Namespace(command='init', func=<function init>))
    # print(args)
    args.func(args)


def parse_args() -> argparse.Namespace:
    # here the command line arguments are defined using the argparse module. The parser is created and configured to accept subcommands, with 'init' being one of them. When the 'init' command is used, the init function will be called with the parsed arguments.
    parser = argparse.ArgumentParser()
    # its like adding all them under the same roof man like args.command=="init"
    commands = parser.add_subparsers(dest='command')
    commands.required = True  # their shuld be at least one command provided
    init_parser = commands.add_parser('init')  # creats a sub command
    # equal to if args.command=="init": init(args) or args.func = init
    init_parser.set_defaults(func=init)

    hash_object_parser = commands.add_parser('add')
    hash_object_parser.set_defaults(func=hash_object)
    hash_object_parser.add_argument('file')

    cat_file_parser = commands.add_parser('read')
    cat_file_parser.set_defaults(func=cat_file)
    cat_file_parser.add_argument('object')

    return parser.parse_args()


def hash_object(args) -> None:
    with open(args.file, 'rb') as f:
        print(data.hash_object(f.read()))


def cat_file(args):
    sys.stdout.flush()
    sys.stdout.buffer.write(data.get_object(args.object, expected=None))


def init(args) -> None:
    data.init()
    # it will create a .ugit directory in the current working directory and print the message to the console.
    print(f'Initialized empty ugit repository in {os.getcwd()}/{data.GIT_DIR}')
