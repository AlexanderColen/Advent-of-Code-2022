import re
from copy import deepcopy
from typing import Tuple
import readInput


class Monkey:
    items_inspected = 0
    modulo = 1

    def __init__(
        self,
        starting_items: list,
        operator: str,
        operation: str,
        test_number: int,
        true_recipient: int,
        false_recipient: int
    ):
        self.items = starting_items
        self.operator = operator
        self.operation = operation
        self.test_number = test_number
        self.true_recipient = true_recipient
        self.false_recipient = false_recipient

    def inspect(self, allow_worry_dropping: bool) -> Tuple[int, int]:
        if len(self.items) > 0:
            # Increment the items inspected for the Monkey.
            self.items_inspected += 1

            # Grab the last item.
            item = self.items.pop(0)

            # Take the modulo
            item = item % self.modulo

            # Execute Monkey's operation.
            if self.operator == '*':
                if self.operation == 'old':
                    item = item * item
                else:
                    item = item * int(self.operation)
            else:
                if self.operation == 'old':
                    item = item + item
                else:
                    item = item + int(self.operation)

            if allow_worry_dropping:
                # Monkey becomes bored.
                item = item // 3

            # Test what Monkey this gets thrown to.
            recipient = self.false_recipient
            if item % self.test_number == 0:
                recipient = self.true_recipient

            return recipient, item

    def catch_item(self, item: int):
        self.items.append(item)

    def __str__(self):
        return f'Items: {", ".join([str(item) for item in self.items])} - ' \
               f'Operation: {self.operator}{self.operation} - ' \
               f'Testing divisible by {self.test_number} - ' \
               f'Throwing to {self.true_recipient} if true or {self.false_recipient} if false'


def initialize_bully_circle(data: list) -> list:
    monkeys = []
    items = []
    operator = '+'
    operation = 0
    test_quantity = 0
    true_catcher = 0
    false_catcher = 0

    for line in data:
        if len(line) == 0 or line.startswith('Monkey'):
            continue

        if line.startswith('Starting items:'):
            for item in line.split('Starting items: ')[1].split(', '):
                items.append(int(item))
        elif line.startswith('Operation:'):
            if '*' in line:
                operator = '*'
            else:
                operator = '+'
            operation = line.split(f' {operator} ')[1]
        elif line.startswith('Test:'):
            test_quantity = int(re.sub('[a-zA-Z\\.\\s:]+', '', line))
        elif line.startswith('If true:'):
            true_catcher = int(re.sub('[a-zA-Z\\.\\s:]+', '', line))
        elif line.startswith('If false:'):
            false_catcher = int(re.sub('[a-zA-Z\\.\\s:]+', '', line))
            monkeys.append(
                Monkey(
                    starting_items=items,
                    operator=operator,
                    operation=operation,
                    test_number=test_quantity,
                    true_recipient=true_catcher,
                    false_recipient=false_catcher
                )
            )

            # Reset items for next monkey.
            items = []

    return monkeys


def execute_monkey_business(
    monkeys: list,
    rounds: int,
    do_monkeys_get_bored: bool = True
) -> int:
    for _ in range(rounds):
        for monkey in monkeys:
            for _ in range(len(monkey.items)):
                recipient, item = monkey.inspect(
                    allow_worry_dropping=do_monkeys_get_bored)
                monkeys[recipient].catch_item(item)

    # Sort monkeys on items inspected.
    monkeys.sort(key=lambda monkey: monkey.items_inspected, reverse=True)

    return monkeys[0].items_inspected * monkeys[1].items_inspected


def puzzle1(monkeys: list) -> int:
    return execute_monkey_business(monkeys=monkeys, rounds=20)


def puzzle2(monkeys: list) -> int:
    return execute_monkey_business(
        monkeys=monkeys, rounds=10000, do_monkeys_get_bored=False)


if __name__ == '__main__':
    # TODO: Replace with readInput.fetch_input(11)
    bullies = initialize_bully_circle(data=readInput.read_input())

    modulo = 1
    for bully in bullies:
        modulo *= bully.test_number

    for bully in bullies:
        bully.modulo = modulo

    print(f'Puzzle 1 solution: {puzzle1(monkeys=deepcopy(bullies))}')
    print(f'Puzzle 2 solution: {puzzle2(monkeys=bullies)}')
