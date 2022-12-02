import readInput


def calculate_calories(instructions: list) -> list:
    all_calories = []
    current_calories = 0
    for line in instructions:
        if len(line) > 0:
            current_calories += int(line)
        else:
            all_calories.append(current_calories)
            current_calories = 0

    # Append the final calories if they haven't reset.
    if current_calories != 0:
        all_calories.append(current_calories)

    # Sort the calories from largest to smallest.
    all_calories.sort(reverse=True)

    return all_calories


def puzzle1(instructions: list) -> int:
    all_calories = calculate_calories(instructions)
    return all_calories[0]


def puzzle2(instructions: list) -> int:
    all_calories = calculate_calories(instructions)
    return all_calories[0] + all_calories[1] + all_calories[2]


if __name__ == '__main__':
    # TODO: Replace with readInput.fetch_input(1)
    parsed_instructions = readInput.read_input()
    print(f'Puzzle 1 solution: {puzzle1(instructions=parsed_instructions)}')
    print(f'Puzzle 2 solution: {puzzle2(instructions=parsed_instructions)}')
