import json
from typing import Tuple

import readInput


def build_pairs(lines: list) -> list:
    pairs = []
    packet_a = None

    for i, line in enumerate(lines, start=1):
        # Skip every 3rd line because it is empty.
        if len(line) == 0:
            continue

        # Parse the packet.
        parsed_packet = json.loads(line)

        # Assign the packet depending on which was not filled yet.
        if packet_a is None:
            packet_a = parsed_packet
        else:
            pairs.append([packet_a, parsed_packet])

            # Reset the dangling packet afterwards.
            packet_a = None

    return pairs


def convert_value(value) -> list:
    if type(value) is list:
        return value

    return [value]


def compare_item(item_a, item_b) -> Tuple[bool, bool]:
    # Handle types being the same.
    if type(item_a) == type(item_b):
        # Directly compare integers.
        if type(item_a) is int:
            if item_a == item_b:
                return True, False
            elif item_a < item_b:
                return True, True
            else:
                return False, True

        # Loop through each item in list values.
        go_until = max(len(item_a), len(item_b))
        for i in range(go_until):
            # Check if both items have enough values.
            try:
                value_a = item_a[i]
            except IndexError:
                return True, True

            try:
                value_b = item_b[i]
            except IndexError:
                return False, True

            # Compare the actual values.
            is_ordered, has_finished = compare_item(
                item_a=value_a, item_b=value_b)

            if has_finished:
                return is_ordered, has_finished

        return True, False
    else:
        return compare_item(
            item_a=convert_value(item_a), item_b=convert_value(item_b))


def compare_packets(packet_a: list, packet_b: list) -> bool:
    is_ordered = True

    # Loop through each item in list values.
    go_until = max(len(packet_a), len(packet_b))
    for limit in range(go_until):
        # Check if both items have enough values.
        try:
            pair_item_a = packet_a[limit]
        except IndexError:
            break

        try:
            pair_item_b = packet_b[limit]
        except IndexError:
            is_ordered = False
            break

        is_ordered, has_finished = compare_item(
            item_a=pair_item_a, item_b=pair_item_b)

        if has_finished:
            break

    return is_ordered


def bubble_sort(packets: list) -> list:
    n = len(packets)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            # Swap the packets if the order is wrong.
            if not compare_packets(packets[j], packets[j+1]):
                packets[j], packets[j + 1] = packets[j + 1], packets[j]

                already_sorted = False

        if already_sorted:
            break

    return packets


def puzzle1(pairs: list) -> int:
    ordered_indices = []

    for i, pair in enumerate(pairs, start=1):
        if compare_packets(packet_a=pair[0], packet_b=pair[1]):
            ordered_indices.append(i)

    return sum(ordered_indices)


def puzzle2(pairs: list) -> int:
    # Compile the packets to a single list.
    packets = []
    for pair in pairs:
        packets.append(pair[0])
        packets.append(pair[1])

    # Add the new divider packets.
    divider_packets = [[[2]], [[6]]]
    packets.extend(divider_packets)

    # Sort the packets.
    packets = bubble_sort(packets=packets)

    # Find the decoder keys by looking for the divider packets.
    decoder_keys = []
    for i, packet in enumerate(packets, start=1):
        if str(packet) in [str(divider_packets[0]), str(divider_packets[1])]:
            decoder_keys.append(i)

    return decoder_keys[0] * decoder_keys[1]


if __name__ == '__main__':
    # TODO: Replace with readInput.fetch_input(13)
    parsed_instructions = readInput.read_input()
    parsed_pairs = build_pairs(lines=parsed_instructions)
    print(f'Puzzle 1 solution: {puzzle1(pairs=parsed_pairs)}')
    print(f'Puzzle 2 solution: {puzzle2(pairs=parsed_pairs)}')
