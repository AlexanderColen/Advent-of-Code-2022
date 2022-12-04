import readInput


def create_range(assignment: str) -> set:
    start, end = assignment.split('-')
    return set(range(int(start), int(end) + 1))


def puzzle1(instructions: list) -> int:
    total_contains = 0

    for pair in instructions:
        elf_a, elf_b = pair.split(',')

        range_a = create_range(elf_a)
        range_b = create_range(elf_b)

        intersection = range_a & range_b
        if range_a == intersection or range_b == intersection:
            total_contains += 1

    return total_contains


def puzzle2(instructions: list) -> int:
    total_overlaps = 0

    for pair in instructions:
        elf_a, elf_b = pair.split(',')

        range_a = create_range(elf_a)
        range_b = create_range(elf_b)

        intersection = range_a & range_b
        if len(intersection) > 0:
            total_overlaps += 1

    return total_overlaps


if __name__ == '__main__':
    # TODO: Replace with readInput.fetch_input(2)
    parsed_instructions = readInput.read_input()
    print(f'Puzzle 1 solution: {puzzle1(instructions=parsed_instructions)}')
    print(f'Puzzle 2 solution: {puzzle2(instructions=parsed_instructions)}')
