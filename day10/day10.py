import readInput


def check_cycle_signal(x: int, cycle: int, signal_strengths: list) -> list:
    if (cycle + 20) % 40 == 0:
        signal_strengths.append(cycle * x)

    return signal_strengths


def puzzle1(instructions: list) -> int:
    x = 1
    cycle = 0
    signal_strengths = []

    for instruction in instructions:
        if instruction == 'noop':
            cycle += 1
            signal_strengths = check_cycle_signal(
                x=x, cycle=cycle, signal_strengths=signal_strengths)
        else:
            cycle += 1
            signal_strengths = check_cycle_signal(
                x=x, cycle=cycle, signal_strengths=signal_strengths)

            cycle += 1
            signal_strengths = check_cycle_signal(
                x=x, cycle=cycle, signal_strengths=signal_strengths)
            x += int(instruction.split(' ')[1])

    return sum(signal_strengths)


def draw_on_crt(x: int, cycle: int, crt_lines: list) -> list:
    character = ' '

    if (cycle - 1) % 40 in [x-1, x, x+1]:
        character = '#'

    crt_lines[(cycle - 1) // 40].append(character)

    return crt_lines


def puzzle2(instructions: list) -> list:
    x = 1
    cycle = 0
    crt_lines = [[], [], [], [], [], []]

    for instruction in instructions:
        if instruction == 'noop':
            cycle += 1
            crt_lines = draw_on_crt(x=x, cycle=cycle, crt_lines=crt_lines)
        else:
            cycle += 1
            crt_lines = draw_on_crt(x=x, cycle=cycle, crt_lines=crt_lines)

            cycle += 1
            crt_lines = draw_on_crt(x=x, cycle=cycle, crt_lines=crt_lines)
            x += int(instruction.split(' ')[1])

    return crt_lines


if __name__ == '__main__':
    # TODO: Replace with readInput.fetch_input(10)
    parsed_instructions = readInput.read_input()
    print(f'Puzzle 1 solution: {puzzle1(instructions=parsed_instructions)}')

    print('Puzzle 2 solution:')
    for line in puzzle2(instructions=parsed_instructions):
        print("".join(line))
