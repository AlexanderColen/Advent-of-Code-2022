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
