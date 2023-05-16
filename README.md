# rubiks cube encoding

ignoring orientation (too complicated for me) and one-color cubes (centre faces), 8! times 12! = 19313344512000

i was thinking that if we do upgrade this specification to include orientation, we leave one corner and one edge to prevent corner-twisting so it is possible on regular rubiks cube

The highest power of 2 underneath 19313344512000 is 2^44, so 44 bits can be stored inside.

## BROWGY codes

blue, red, orange, white, green, yellow for faces on rubiks cube<br>
3-letter codes for corners<br>
2-letter codes for edges<br>
never use one letter codes!!

## BASIL encoding scheme

(probably has been done before under a different name but i cannot find it online)<br>
(named basil because basil is very tasty)

to make this encoding, we must introduce the BASE-IL encoding scheme.<br>
acronyms are BASIL (base at some increasing length) or BASE-IL (base-increasing length)

here's how it works:

if you are arranging letters A to L and want to generate orders and number equivalents, you do the following:<br>
1 possibilities for the last letter, so the first ones (0!=1) digit. Multiply this by 1<br>
2 possibilities for the second to last letter, so the second ones (1!) digit. Multiply this by 1<br>
3 possibilities for the third to last letter, so the twos (2!) digit. Multiply this by 2<br>
etc

So, with letters ABCDEFGHIJKL being the chunks, we can represent them as:

A is highest, L is lowest

So, JADILHFGBCKE is represented as:

| Letter | Decimal Repr | Index | Column Value |
|--------|--------------|-------|--------------|
| J      | 79833600     | 2     | 11!          |
| A      | 36288000     | 10    | 10!          |
| D      | 2540160      | 7     | 9!           |
| I      | 80640        | 2     | 8!           |
| L      | 0            | 0     | 7!           |
| H      | 720          | 1     | 6!           |
| F      | 240          | 2     | 5!           |
| G      | 24           | 1     | 4!           |
| B      | 18           | 3     | 3!           |
| C      | 4            | 2     | 2!           |
| K      | 0            | 0     | 1!           |
| E      | 0            | 0     | 0!           |
For a grand total of **118743406**

We can use this strange BASIL factorial base thing to represent permutations of rubiks cube edges (there are 12)

Likewise, we can reverse this operation because by keep subtracting the next factorial and see how many times we can subtract it from the number we decode until we get below 0

See `basil.py` for implementation

## rubiks cube encoding spec

There are ~15 controllable bits in the corners, and ~28 bits of data in the edges. This is counting the permutations separately, however. To get more out of the data, we can have a 1s digit going up to 40320 replacing for the ones place and a 40320s digits place going up to 479001599*40320=19313344471680 where the 10s place should be. Therefore, we have a range of 0-17592186044415 that we can represent, which is at 44 bits in base 2.

We want to maximize data, so we will only allow alphanumeric characters. Because there are 36 alphanumeric characters, we must cut off 4 alphabet letters. Therefore: our alphabet has the following codes:

| Decimal | Binary | Char |
|---------|--------|------|
| 0       | 00000  | a    |
| 1       | 00001  | b    |
| 2       | 00010  | d    |
| 3       | 00011  | e    |
| 4       | 00100  | f    |
| 5       | 00101  | g    |
| 6       | 00110  | h    |
| 7       | 00111  | i    |
| 8       | 01000  | j    |
| 9       | 01001  | k    |
| 10      | 01010  | l    |
| 11      | 01011  | m    |
| 12      | 01100  | n    |
| 13      | 01101  | p    |
| 14      | 01110  | r    |
| 15      | 01111  | s    |
| 16      | 10000  | t    |
| 17      | 10001  | u    |
| 18      | 10010  | v    |
| 19      | 10011  | w    |
| 20      | 10100  | y    |
| 21      | 10101  | z    |
| 22      | 10110  | 0    |
| 23      | 10111  | 1    |
| 24      | 11000  | 2    |
| 25      | 11001  | 3    |
| 26      | 11010  | 4    |
| 27      | 11011  | 5    |
| 28      | 11100  | 6    |
| 39      | 11101  | 7    |
| 30      | 11110  | 8    |
| 31      | 11111  | 9    |

Each character is represented in 5 bits. Notice how we skipped over some characters like c? We have to save space so c is basically the same thing as K, and so it Q (and X is just "KS" and very rare). 0 and O are identical. So now we are left with 32 chars.

We want to fit as many possible bits of info in the cube, so we use 40 bits for the data, and 4 bits for format info.

Here, the format info will be 3 bits for length, and 1 for parity check. If the sum of the binary digits of the data XORed with the parity check results in 0, it is correct. This is a minimal but useful amount of error checking.

Also, this uses big endian (length biggest, parity middle, data progressively gets "smaller" each letter).
