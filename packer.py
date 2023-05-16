from basil import rubiks_from_decimal, rubiks_to_decimal
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


def decode_basil_to_rcencoded_data(corners: str, edges: str):
    dec = rubiks_to_decimal(corners, edges)
    length = (dec & 0b111 << 41) >> 41
    parity = (dec & 0b1 << 40) >> 40
    rest = (dec & 0b1111111111111111111111111111111111111111)
    if sum(map(int, "{0:b}".format(rest))) ^ parity == 0:
        raise NotImplemented("Parity failure!")
    message = ""
    for _ in range(length+1):
        chunk_data = rest & 0b11111
        rest = rest >> 5
        message += rcencoding_alphabet[chunk_data]
    return message[::-1]


def main():
    # print(encode_rcencoded_data_to_basil("urkiddng"))
    print(decode_basil_to_rcencoded_data('GCFEHABD', 'CAILHBJKGDFE'))


if __name__ == '__main__':
    main()
