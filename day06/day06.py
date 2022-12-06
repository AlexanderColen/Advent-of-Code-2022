import readInput


def find_marker_start(datastream: str, marker_size: int) -> int:
    potential_marker = datastream[0:marker_size]
    for index, char in enumerate(datastream[marker_size:]):
        # Replace the first character with the newest.
        potential_marker = potential_marker[1:] + char

        # Check if the last 4 characters have any duplicates.
        has_dupes = False
        for c in potential_marker:
            if potential_marker.count(c) > 1:
                has_dupes = True

        # Return the index if no dupes were found.
        if not has_dupes:
            return index + 1 + marker_size


def puzzle1(instructions: str) -> int:
    return find_marker_start(datastream=instructions, marker_size=4)


def puzzle2(instructions: str) -> int:
    return find_marker_start(datastream=instructions, marker_size=14)


if __name__ == '__main__':
    # TODO: Replace with readInput.fetch_input(6)
    parsed_instructions = readInput.read_input()[0]
    print(f'Puzzle 1 solution: {puzzle1(instructions=parsed_instructions)}')
    print(f'Puzzle 2 solution: {puzzle2(instructions=parsed_instructions)}')
