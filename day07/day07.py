import re
import readInput


class Directory:
    parent = None
    size = 0

    def __init__(self, name: str, parent: object = None):
        self.name = name
        self.parent = parent


def build_filesystem(commands: list) -> list:
    current_directory: Directory = Directory(name='/')
    directories: list = [
        current_directory
    ]

    # Loop through all the commands to iteratively build the filesystem.
    for command in commands[1:]:
        # Ignore ls commands.
        if command == '$ ls':
            continue

        # Change directory.
        if command.startswith('$ cd'):
            # Update current directory to parent if requested.
            if command.endswith('..'):
                current_directory = current_directory.parent
            # Otherwise find the directory to change into.
            else:
                for directory in directories:
                    if directory.name == command[5:] \
                            and directory.parent is not None \
                            and directory.parent.name == \
                            current_directory.name:
                        current_directory = directory
                        break
        # Create new Directory.
        elif command.startswith('dir') and directories:
            directories.append(
                Directory(name=command[4:], parent=current_directory)
            )
        # Increment directory's size.
        elif re.match('\\d+', command) is not None:
            file_size = int(re.sub('[a-z\\.\\s]+', '', command))
            current_directory.size += file_size

            # Also update the sizes of parents and their parents.
            parent_directory = current_directory.parent

            while parent_directory is not None:
                parent_directory.size += file_size
                parent_directory = parent_directory.parent

    return directories


def puzzle1(directories: list) -> int:
    # Find the directory with size up to 100000
    total_size = 0

    for directory in directories:
        if directory.size <= 100000:
            total_size += directory.size

    return total_size


def puzzle2(directories: list) -> int:
    # Check how much space is unused via `/` directory.
    unused_space = 70000000 - directories[0].size

    # Sort directories on size ascending.
    directories.sort(key=lambda directory: directory.size)

    # Find the smallest directory that is bigger than the required space.
    for directory in directories:
        if directory.size >= 30000000 - unused_space:
            return directory.size


if __name__ == '__main__':
    directories = build_filesystem(commands=readInput.read_input())
    print(f'Puzzle 1 solution: {puzzle1(directories=directories)}')
    print(f'Puzzle 2 solution: {puzzle2(directories=directories)}')
