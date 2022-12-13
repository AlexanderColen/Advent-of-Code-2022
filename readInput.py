from urllib.request import urlopen


def fetch_input(day: int) -> list:
    # TODO: Add login token
    puzzle_input = urlopen(
        "https://adventofcode.com/2022/day/{day_number}/input".format(
            day_number=day
        )
    )

    lines = []
    for line in puzzle_input:
        lines.append(line.strip())

    return lines


def read_input(file_name: str = 'input') -> list:
    """Read the 'input' file and return it as a list of strings stripped of any
    whitespace characters.

    Returns `list` A list of strings containing the input file's data.
    """
    puzzle_input = []

    with open(file_name, 'r') as file:
        for line in file:
            puzzle_input.append(line.strip())

    return puzzle_input
