# Usage

## Example 

Given the input file:

```console
❯ cat test/fixtures/grid_s_1.txt
O
X
OX   X
 XX
   OO
XXO
```

for clarity showing the dump to expose the regularity:

```console
❯ xxd -c 7 test/fixtures/grid_s_1.txt
00000000: 4f20 2020 2020 0a  O     .
00000007: 5820 2020 2020 0a  X     .
0000000e: 4f58 2020 2058 0a  OX   X.
00000015: 2058 5820 2020 0a   XX   .
0000001c: 2020 204f 4f20 0a     OO .
00000023: 5858 4f20 2020 0a  XXO   .
```

`xoxo` will try to solve the puzzle in a diverse but balanced way:

```console
❯ xoxo test/fixtures/grid_s_1.txt
Problem:

,---+---+---+---+---+---,
| O |   |   |   |   |   |  1
|---+---+---+---+---+---|
| X |   |   |   |   |   |  2
|---+---+---+---+---+---|
| O | X |   |   |   | X |  3
|---+---+---+---+---+---|
|   | X | X |   |   |   |  4
|---+---+---+---+---+---|
|   |   |   | O | O |   |  5
|---+---+---+---+---+---|
| X | X | O |   |   |   |  6
*---+---+---+---+---+---*
  1   2   3   4   5   6


Solution:

,---+---+---+---+---+---,
| O | O | X | O | X | X |  1
|---+---+---+---+---+---|
| X | O | O | X | X | O |  2
|---+---+---+---+---+---|
| O | X | O | X | O | X |  3
|---+---+---+---+---+---|
| O | X | X | O | X | O |  4
|---+---+---+---+---+---|
| X | O | X | O | O | X |  5
|---+---+---+---+---+---|
| X | X | O | X | O | O |  6
*---+---+---+---+---+---*
  1   2   3   4   5   6

```

Even less balanced input files with easier to inspect indicators for empty fields like:

```console
❯ cat test/fixtures/tic_tac_toe.txt
o
x
OX=-+X
yXx?!_
   oO,
XXO... THIS OVERRUN DOES NOT MATTER
```

again a dump shown here to help follow the transforms:

```console
❯ xxd -c 7 test/fixtures/tic_tac_toe.txt
00000000: 6f20 2020 2020 0a  o     .
00000007: 7820 2020 2020 0a  x     .
0000000e: 4f58 3d2d 2b58 0a  OX=-+X.
00000015: 7958 783f 215f 0a  yXx?!_.
0000001c: 2020 206f 4f2c 0a     oO,.
00000023: 5858 4f2e 2e2e 20  XXO...
0000002a: 5448 4953 204f 56  THIS OV
00000031: 4552 5255 4e20 44  ERRUN D
00000038: 4f45 5320 4e4f 54  OES NOT
0000003f: 204d 4154 5445 52   MATTER
00000046: 0a                 .
```

Will find a balanced and filled treatment from `xoxo`:

```console
❯ xoxo test/fixtures/tic_tac_toe.txt
Problem:

,---+---+---+---+---+---,
| O |   |   |   |   |   |  1
|---+---+---+---+---+---|
| X |   |   |   |   |   |  2
|---+---+---+---+---+---|
| O | X |   |   |   | X |  3
|---+---+---+---+---+---|
|   | X | X |   |   |   |  4
|---+---+---+---+---+---|
|   |   |   | O | O |   |  5
|---+---+---+---+---+---|
| X | X | O |   |   |   |  6
*---+---+---+---+---+---*
  1   2   3   4   5   6


Solution:

,---+---+---+---+---+---,
| O | O | X | O | X | X |  1
|---+---+---+---+---+---|
| X | O | O | X | X | O |  2
|---+---+---+---+---+---|
| O | X | O | X | O | X |  3
|---+---+---+---+---+---|
| O | X | X | O | X | O |  4
|---+---+---+---+---+---|
| X | O | X | O | O | X |  5
|---+---+---+---+---+---|
| X | X | O | X | O | O |  6
*---+---+---+---+---+---*
  1   2   3   4   5   6

```
