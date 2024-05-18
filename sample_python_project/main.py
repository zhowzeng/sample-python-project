import argparse
import os

from dotenv import load_dotenv


load_dotenv()
ENV = os.environ["ENV"]


def cli():
    parser = argparse.ArgumentParser(description='My Git-like CLI')
    subparsers = parser.add_subparsers(dest='command', help='sub-command help')

    # Create a subparser for the "init" command
    init_parser = subparsers.add_parser('init', help='Initialize a new repository')
    init_parser.add_argument('--directory', help='Specify the directory to initialize')

    # Create a subparser for the "add" command
    add_parser = subparsers.add_parser('add', help='Add files to the repository')
    add_parser.add_argument('files', nargs='+', help='Files to add')

    # Create a subparser for the "commit" command
    commit_parser = subparsers.add_parser('commit', help='Commit changes to the repository')
    commit_parser.add_argument('-m', '--message', help='Commit message')

    args = parser.parse_args()

    print(f"{ENV=}")

    match args.command:
        case 'init':
            print(f'Initializing repository in {args.directory}')
        case 'add':
            print(f'Adding files: {args.files}')
        case 'commit':
            print(f'Committing with message: {args.message}')

