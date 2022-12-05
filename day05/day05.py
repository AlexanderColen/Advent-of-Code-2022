import re
from copy import deepcopy
from typing import Tuple


def parse_input() -> Tuple[list, list]:
    stack_lines = []
    move_instructions = []
    stack_count = 0

    with open('input', 'r') as file:
        for line in file:
            # Remove ending newlines.
            line = line.replace('\n', '')

            # Skip empty lines
            if len(line) == 0:
                continue

            # Add the move instructions to their own list.
            if line.startswith('move'):
                move_instructions.append(line)
            # Find lines containing part of the stack.
            elif '[' in line:
                stack_lines.append(line)
            # Note down the number of stacks.
            else:
                stack_count = [c for c in re.split('\\s+', line) if c != ''][-1]

    initial_stacks = []
    for _ in range(int(stack_count)):
        initial_stacks.append([])

    # Parse the stacks based on columns of 3 with a space divider.
    for stack_line in stack_lines:
        for i in range(int(stack_count)):
            stack_item = stack_line[i*4:i*4+4].strip()
            if len(stack_item) > 0:
                initial_stacks[i].insert(0, stack_item[1])

    return initial_stacks, move_instructions


def parse_move_instruction(instruction: str) -> Tuple[int, int, int]:
    quantity, stack_from, stack_to = [
        int(num) for num in re.split('[a-z]+', instruction)[1:]
    ]

    # Decrement stack_from and stack_to to start counting at 0.
    stack_from -= 1
    stack_to -= 1

    return quantity, stack_from, stack_to


def determine_stack_tops(stacks: list) -> str:
    return ''.join([stack[len(stack) - 1] for stack in stacks])


def puzzle1(stacks: list, instructions: list) -> str:
    # Follow the move instructions.
    for instruction in instructions:
        # Parse how many to move from which stack to which stack.
        quantity, stack_from, stack_to = parse_move_instruction(
            instruction=instruction
        )

        # Move the requested items one by one.
        for _ in range(quantity):
            stack_item = stacks[stack_from].pop()
            stacks[stack_to].append(stack_item)

    # Return the top item of every stack.
    return determine_stack_tops(stacks=stacks)


def puzzle2(stacks: list, instructions: list) -> str:
    # Follow the move instructions.
    for instruction in instructions:
        # Parse how many to move from which stack to which stack.
        quantity, stack_from, stack_to = parse_move_instruction(
            instruction=instruction
        )

        # Move the requested items all at once.
        moved_items = stacks[stack_from][len(stacks[stack_from]) - quantity:]
        stacks[stack_from] = stacks[stack_from][:-quantity]
        stacks[stack_to].extend(moved_items)

    # Return the top item of every stack.
    return determine_stack_tops(stacks=stacks)


if __name__ == '__main__':
    stacks, instructions = parse_input()
    print(f'Puzzle 1 solution: {puzzle1(stacks=deepcopy(stacks), instructions=instructions)}')  # noqa
    print(f'Puzzle 2 solution: {puzzle2(stacks=deepcopy(stacks), instructions=instructions)}')  # noqa
