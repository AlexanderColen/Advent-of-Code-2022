import time
from copy import deepcopy
from typing import Tuple
import readInput


def determine_bounds(line_instructions: list) -> list:
    x_bounds: list = []
    y_bounds: list = []

    for lines in line_instructions:
        for line in lines.split(' -> '):
            x, y = line.split(',')
            x_bounds.append(int(x))
            y_bounds.append(int(y))

    return [x_bounds, y_bounds]


def build_cave_grid(line_instructions: list, bounds: list, start_x: int):
    min_x = min(bounds[0])
    max_x = max(bounds[0])
    max_y = max(bounds[1])

    grid = []

    for y in range(max_y):
        row = []
        for x in range(max_x - min_x + 1):
            row.append('.')
        grid.append(row)

    for lines in line_instructions:
        previous_x = None
        previous_y = None
        for line in lines.split(' -> '):
            x, y = line.split(',')
            x = int(x) - min_x
            y = int(y)

            if previous_x is not None and previous_y is not None:
                # Draw Y line.
                if previous_x == x:
                    start = previous_y
                    end = y
                    # Swap if line goes backwards.
                    if start > end:
                        start, end = end, start
                    for draw_y in range(start, end + 1):
                        grid[draw_y - 1][x] = '#'
                # Draw X line.
                elif previous_y == y:
                    start = previous_x
                    end = x
                    # Swap if line goes backwards.
                    if start > end:
                        start, end = end, start
                    for draw_x in range(start, end + 1):
                        grid[y - 1][draw_x] = '#'

            # Set the current line as the new previous.
            previous_x = x
            previous_y = y

    return grid


def drop_sand_grain(grid: list, start_x: int) -> Tuple[list, bool]:
    start_grain_count = 0
    for row in grid:
        start_grain_count += row.count('o')

    try:
        current_y = 0
        current_x = start_x
        at_rest = False

        while not at_rest:
            # Try to drop straight down.
            if grid[current_y + 1][current_x] == '.':
                current_y += 1
            # Try to go diagonal down left.
            elif grid[current_y + 1][current_x - 1] == '.':
                current_y += 1
                current_x -= 1
            # Try to go diagonal down right.
            elif grid[current_y + 1][current_x + 1] == '.':
                current_y += 1
                current_x += 1
            else:
                grid[current_y][current_x] = 'o'
                at_rest = True
    except IndexError:
        return grid, False

    # See if the amount of sand changed.
    end_grain_count = 0
    for row in grid:
        end_grain_count += row.count('o')

    return grid, start_grain_count != end_grain_count


def puzzle1(grid: list, start_x: int) -> int:
    grains_dropped = 0
    room_left = True
    while room_left:
        grid, room_left = drop_sand_grain(grid=grid, start_x=start_x)

        if room_left:
            grains_dropped += 1

    return grains_dropped


def puzzle2(grid: list, bounds: list) -> int:
    # Extend the grid to add an infinite floor 2 under the lowest rock.
    max_y = max(bounds[1])

    # Add height amount to each side of existing rows.
    for i in range(len(grid)):
        extension = list('.' * max_y)
        grid[i] = extension + grid[i] + extension

    # Add the empty air and floor row.
    grid.append(list('.' * len(grid[0])))
    grid.append(list('#' * len(grid[0])))

    # Move the start to an extra row at the top to drop at.
    grid.insert(0, list('.' * len(grid[0])))

    # Update the start position to account for the shift.
    start_x = 500 - min(bounds[0]) + max_y

    # Start dropping sand.
    grains_dropped = 0
    room_left = True

    while room_left:
        grid, room_left = drop_sand_grain(grid=grid, start_x=start_x)

        if room_left:
            grains_dropped += 1

            if grains_dropped % 100 == 0:
                print(f'Dropped {grains_dropped} grains of sand')

    return grains_dropped


if __name__ == '__main__':
    # TODO: Replace with readInput.fetch_input(14)
    parsed_instructions = readInput.read_input()
    bounds = determine_bounds(line_instructions=parsed_instructions)
    start_x = 500 - min(bounds[0])
    cave_grid = build_cave_grid(
        line_instructions=parsed_instructions,
        bounds=bounds,
        start_x=start_x
    )
    print(f'Puzzle 1 solution: {puzzle1(grid=deepcopy(cave_grid), start_x=start_x)}')  # noqa
    print(f'Puzzle 2 solution: {puzzle2(grid=deepcopy(cave_grid), bounds=bounds)}')  # noqa
