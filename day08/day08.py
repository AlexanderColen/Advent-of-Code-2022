import readInput


class Tree:
    def __init__(self, height: int, x: int, y: int, is_visible: bool = None):
        self.height = height
        self.x = x
        self.y = y
        self.is_visible = is_visible


def build_tree_grid(heights: list) -> list:
    grid = []

    for y, row in enumerate(heights):
        tree_row = []

        for x, height in enumerate(row):
            can_be_seen = y == 0 \
                          or y == len(heights)-1 \
                          or x == 0 \
                          or x == len(row)-1
            tree_row.append(
                Tree(height=int(height), x=x, y=y, is_visible=can_be_seen)
            )

        grid.append(tree_row)

    return grid


def determine_tree_visibility(tree_grid: list) -> list:
    for y, row in enumerate(tree_grid):
        # Skip first and last rows.
        if y == 0 or y == len(tree_grid) - 1:
            continue

        for x, current in enumerate(row):
            # Skip first and last columns.
            if x == 0 or x == len(row) - 1:
                continue

            # Don't bother calculating for already visible trees or 0 height.
            if current.is_visible or current.height == 0:
                continue

            # Check for the highest tree to the left and right.
            max_left = max(tree.height for tree in row[:x])
            max_right = max(tree.height for tree in row[x+1:])

            above = []
            below = []
            for y2 in range(len(tree_grid)):
                # Above
                if y2 < y:
                    above.append(tree_grid[y2][x])
                # Below
                elif y2 > y:
                    below.append(tree_grid[y2][x])

            max_above = max(tree.height for tree in above)
            max_below = max(tree.height for tree in below)

            if max_left < current.height \
                    or max_right < current.height \
                    or max_above < current.height \
                    or max_below < current.height:
                current.is_visible = True

    return tree_grid


def puzzle1(tree_grid: list) -> int:
    total_visible = 0

    for tree_row in tree_grid:
        total_visible += len([tree for tree in tree_row if tree.is_visible])

    return total_visible


def puzzle2(tree_grid: list) -> int:
    max_scenic_score = 0

    for y, row in enumerate(tree_grid):
        # Skip first and last rows.
        if y == 0 or y == len(tree_grid) - 1:
            continue

        for x, current in enumerate(row):
            # Skip first and last columns.
            if x == 0 or x == len(row) - 1:
                continue

            # Check horizontal visible trees.
            left_blocked = [x]
            right_blocked = [len(row) - (x + 1)]
            for x2 in range(len(row)):
                # Left
                if x2 < x:
                    if row[x2].height >= row[x].height:
                        left_blocked.append(x - x2)
                # Right
                elif x2 > x:
                    if row[x2].height >= row[x].height:
                        right_blocked.append(x2 - x)

            # Check vertical visible trees.
            above_blocked = [y]
            below_blocked = [len(tree_grid) - (y + 1)]
            for y2 in range(len(tree_grid)):
                # Above
                if y2 < y:
                    if tree_grid[y2][x].height >= tree_grid[y][x].height:
                        above_blocked.append(y - y2)
                # Below
                elif y2 > y:
                    if tree_grid[y2][x].height >= tree_grid[y][x].height:
                        below_blocked.append(y2 - y)

            # Calculate the scenic score for the current tree.
            current_scenic_score = min(left_blocked) * min(right_blocked) * \
                                   min(above_blocked) * min(below_blocked)

            if current_scenic_score > max_scenic_score:
                max_scenic_score = current_scenic_score

    return max_scenic_score


if __name__ == '__main__':
    # TODO: Replace with readInput.fetch_input(8)
    parsed_instructions = readInput.read_input()
    trees = build_tree_grid(heights=parsed_instructions)
    trees = determine_tree_visibility(tree_grid=trees)
    print(f'Puzzle 1 solution: {puzzle1(tree_grid=trees)}')
    print(f'Puzzle 2 solution: {puzzle2(tree_grid=trees)}')
