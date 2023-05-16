from math import factorial
from itertools import permutations


def basil_from_decimal(dec_number: int, num_chars: int):
    """Convert decimal to string of ABC...XYZ"""
    factorials = [factorial(_f) for _f in range(1, 27)][num_chars-2::-1]
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[num_chars-1::-1]
    total = ""
    # shut up, it's real (a "fact")
    for fact in factorials:
        times_done = 0
        while dec_number-fact >= 0:
            times_done += 1
            dec_number -= fact
        total += letters.pop(times_done)
    total += letters[0]
    return total


def basil_to_decimal(basil_str: str, table=False):
    """Convert string of ABC...XYZ to decimal"""
    letters = list(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:len(basil_str)]).__reversed__())
    reversed_basil = basil_str
    worth_unfactorialed = len(basil_str)-1
    total = 0
    if table:
        print("""| Letter | Decimal Repr | Index | Column Value |
|--------|--------------|-------|--------------|""")
    for letter in reversed_basil:
        index_of_letter = letters.index(letter)
        letters.remove(letter)
        add = index_of_letter*factorial(worth_unfactorialed)
        if table:
            print(f"|{letter}|{add}|{index_of_letter}|{worth_unfactorialed}!|")
        total += add
        worth_unfactorialed -= 1
    return total


def rubiks_to_decimal(corners: str, edges: str) -> int:
    """
    Edges and corners are BASIL-encoded.

    Please have the green face facing you, the white face on the bottom, and the red face on the left

    Corner order for BASIL, using BROWGY codes:
    A,   B,   C,   D,   E,   F,   G,   H
    GRY, GYO, GOW, GWR, BRY, BYO, BOW, BWR

    Edge order for BASIL, using BROWGY codes:
    A,  B,  C,  D,  E,  F,  G,  H,  I,  J,  K,  L
    GY, GO, GW, GR, RY, OY, OW, RW, BY, BO, BW, BR
    """
    edge_dec = basil_to_decimal(edges)
    corner_dec = basil_to_decimal(corners)
    if edge_dec*40320+corner_dec >= 17592186044416:
        raise NotImplemented("Too high number!")
    return edge_dec*40320+corner_dec


def rubiks_from_decimal(n: int) -> tuple[str, str]:
    assert 0 <= n <= 17592186044415, f"rubiks_from_decimal must be in range 0-17592186044415 inclusive"
    corner_dec = n % 40320
    edge_dec = n // 40320
    return basil_from_decimal(corner_dec, 8), basil_from_decimal(edge_dec, 12)


def main():
    print(2**44, rubiks_to_decimal("DCBAEGFH", "DACBEFGHIJKL"))


if __name__ == '__main__':
    main()
