from basil import rubiks_from_decimal
from enum import Enum

rcencoding_alphabet = "abdefghijklmnprstuvwyz0123456789"


def encode_rcencoded_data_to_basil(data: str):
    assert 1 <= len(data) <= 8, "Too much (or none!) data, 8 chars max"
    for letter in data:
        if letter not in rcencoding_alphabet:
            raise NotImplemented(f"Character not found ({letter})")
    data_bits = 0
    for letter in data:
        letter_index = rcencoding_alphabet.index(letter)
        data_bits = letter_index ^ data_bits << 5
    bits = ((len(data)-1) << 41) ^ (sum(map(int, "{0:b}".format(data_bits))) & 1) << 40 ^ data_bits
    return rubiks_from_decimal(bits)


def main():
    print(encode_rcencoded_data_to_basil("urkiddng"))


if __name__ == '__main__':
    main()
