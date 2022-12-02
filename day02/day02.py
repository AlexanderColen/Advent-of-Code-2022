import readInput


def score_round(opponent: str, me: str):
    score = 0

    # Add score for played hand.
    if me == 'A':
        score += 1
    elif me == 'B':
        score += 2
    else:
        score += 3

    # Add score for outcome/
    if opponent == me:
        score += 3
    elif (opponent == 'A' and me == 'B') \
            or (opponent == 'B' and me == 'C') \
            or (opponent == 'C' and me == 'A'):
        score += 6

    return score


def puzzle1(instructions: list) -> int:
    total_score = 0
    for match in instructions:
        opponent, me = match.split(' ')

        # Format me same as opponent.
        me = 'A' if me == 'X' else 'B' if me == 'Y' else 'C'

        total_score += score_round(opponent, me)

    return total_score


def puzzle2(instructions: list):
    total_score = 0
    for match in instructions:
        opponent, outcome = match.split(' ')

        # Format me based on required outcome.
        if outcome == 'Y':  # Tie
            me = opponent
        elif outcome == 'Z':  # Win
            if opponent == 'A':
                me = 'B'
            elif opponent == 'B':
                me = 'C'
            else:
                me = 'A'
        else:  # Lose
            if opponent == 'A':
                me = 'C'
            elif opponent == 'B':
                me = 'A'
            else:
                me = 'B'

        total_score += score_round(opponent, me)

    return total_score


if __name__ == '__main__':
    # TODO: Replace with readInput.fetch_input(2)
    parsed_instructions = readInput.read_input()
    print(f'Puzzle 1 solution: {puzzle1(instructions=parsed_instructions)}')
    print(f'Puzzle 2 solution: {puzzle2(instructions=parsed_instructions)}')
