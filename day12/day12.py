import readInput


def puzzle1(heightmap: list) -> int:
    # Count all the uppercase points.
    uppercase = 0
    for row in heightmap:
        for p in row:
            if p.isupper():
                uppercase += 1
    # Subtract 1 because both start and end counted.
    return uppercase - 1


def puzzle2(heightmap: list) -> int:
    # Count all the uppercase points.
    uppercase = 0
    for row in heightmap:
        for p in row:
            if p.isupper():
                uppercase += 1
    # Subtract 1 because both start and end counted.
    return uppercase - 1


if __name__ == '__main__':
    # TODO: Replace with readInput.fetch_input(12)
    parsed_instructions_1 = readInput.read_input()
    parsed_instructions_2 = readInput.read_input(file_name='input_b')
    print(f'Puzzle 1 solution: {puzzle1(heightmap=parsed_instructions_1)}')
    print(f'Puzzle 2 solution: {puzzle2(heightmap=parsed_instructions_2)}')
