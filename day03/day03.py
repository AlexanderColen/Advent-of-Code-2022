import readInput


def calculate_priority(items: set) -> int:
    total_priority = 0
    options = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for item in items:
        total_priority += options.index(item) + 1

    return total_priority


def puzzle1(instructions: list) -> int:
    total_priority = 0
    for rucksack_items in instructions:
        # Split rucksack's items into equal halves.
        item_count = len(rucksack_items)
        compartment_a = set(rucksack_items[0:item_count//2])
        compartment_b = set(rucksack_items[item_count//2:])

        # Determine the common items.
        common_items = set(compartment_a & compartment_b)

        # Calculate the priority.
        total_priority += calculate_priority(common_items)

    return total_priority


def puzzle2(instructions: list) -> int:
    total_priority = 0
    group = []
    for rucksack_items in instructions:
        # Add the rucksack to the group
        group.append(set(rucksack_items))

        if len(group) == 3:
            # Determine the common items.
            common_items = set(group[0] & group[1] & group[2])

            # Calculate the priority.
            total_priority += calculate_priority(common_items)

            # Reset for the next group.
            group = []

    return total_priority


if __name__ == '__main__':
    # TODO: Replace with readInput.fetch_input(2)
    parsed_instructions = readInput.read_input()
    print(f'Puzzle 1 solution: {puzzle1(instructions=parsed_instructions)}')
    print(f'Puzzle 2 solution: {puzzle2(instructions=parsed_instructions)}')
