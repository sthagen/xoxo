# xoxo

Balanced diversity solver xoxo to the square.

[License: MIT](https://git.sr.ht/~sthagen/xoxo/tree/default/item/LICENSE)

[![version](https://img.shields.io/pypi/v/xoxo.svg?style=flat)](https://pypi.python.org/pypi/xoxo/)
[![downloads](https://pepy.tech/badge/xoxo/month)](https://pepy.tech/project/xoxo)
[![wheel](https://img.shields.io/pypi/wheel/xoxo.svg?style=flat)](https://pypi.python.org/pypi/xoxo/)
[![supported-versions](https://img.shields.io/pypi/pyversions/xoxo.svg?style=flat)](https://pypi.python.org/pypi/xoxo/)
[![supported-implementations](https://img.shields.io/pypi/implementation/xoxo.svg?style=flat)](https://pypi.python.org/pypi/xoxo/)

## Documentation

User and developer [documentation of xoxo](https://codes.dilettant.life/docs/xoxo).

## Bug Tracker

Feature requests and bug reports are bested entered in the [todos of xoxo](https://todo.sr.ht/~sthagen/xoxo).

## Primary Source repository

The primary source repository of [xoxo is at sourcehut](https://git.sr.ht/~sthagen/xoxo)
a collection of tools useful for software development.

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

More in the [usage documentation](https://codes.dilettant.life/docs/xoxo/usage/)

# Status

Experimental.

**Note** The default branch is `default`.
