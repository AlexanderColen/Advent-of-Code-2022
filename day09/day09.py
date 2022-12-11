from copy import deepcopy
import readInput


def move_knot(knot: dict, following: dict) -> dict:
    x_difference = following['x'] - knot['x']
    y_difference = following['y'] - knot['y']

    if abs(x_difference) <= 1 and abs(y_difference) <= 1:
        return knot

    # Move knot if following is further than 1 away in x or y.
    if x_difference > 1 and y_difference > 1:
        knot['x'] = following['x'] - 1
        knot['y'] = following['y'] - 1
    elif x_difference < -1 and y_difference < -1:
        knot['x'] = following['x'] + 1
        knot['y'] = following['y'] + 1
    elif x_difference > 1 and y_difference < -1:
        knot['x'] = following['x'] - 1
        knot['y'] = following['y'] + 1
    elif x_difference < -1 and y_difference > 1:
        knot['x'] = following['x'] + 1
        knot['y'] = following['y'] - 1
    else:
        if x_difference > 1:
            knot['x'] = following['x'] - 1
            knot['y'] = following['y']
        elif x_difference < -1:
            knot['x'] = following['x'] + 1
            knot['y'] = following['y']

        if y_difference > 1:
            knot['x'] = following['x']
            knot['y'] = following['y'] - 1
        elif y_difference < -1:
            knot['x'] = following['x']
            knot['y'] = following['y'] + 1

    return knot


def simulate_bridge(knot_count: int, instructions: list) -> int:
    knots = [{'x': 0, 'y': 0} for _ in range(knot_count)]
    visited = [{'x': 0, 'y': 0}]

    for instruction in instructions:
        direction, steps = instruction.split(' ')

        # Move the head
        for _ in range(int(steps)):
            if direction == 'R':
                knots[0]['x'] += 1
            elif direction == 'L':
                knots[0]['x'] -= 1
            elif direction == 'U':
                knots[0]['y'] += 1
            else:
                knots[0]['y'] -= 1

            # Move all the other knots.
            for i in range(1, len(knots)):
                knots[i] = move_knot(knot=knots[i], following=knots[i-1])

            # Note down all the locations that the tail has visited.
            visited.append(deepcopy(knots[-1]))

    return len(set((point['x'], point['y']) for point in visited))


def puzzle1(instructions: list) -> int:
    return simulate_bridge(knot_count=2, instructions=instructions)


def puzzle2(instructions: list) -> int:
    return simulate_bridge(knot_count=10, instructions=instructions)


if __name__ == '__main__':
    # TODO: Replace with readInput.fetch_input(9)
    parsed_instructions = readInput.read_input()
    print(f'Puzzle 1 solution: {puzzle1(instructions=parsed_instructions)}')
    print(f'Puzzle 2 solution: {puzzle2(instructions=parsed_instructions)}')
