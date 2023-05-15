# rubiks cube encoding

ignoring orientation (corner twisting sucks!!) and one-color cubes (centre faces), 8! times 12! = 19313344512000

The highest power of 2 underneath 19313344512000 is 2^44, so 44 bits can be stored inside.

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

So, JADILHFGBCKE is represented as 465455 in decimal.
