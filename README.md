[![Build Status](https://dev.azure.com/andreasisnes/Elitekollektivet/_apis/build/status/Elitekollektivet.Minesweeper/Elitekollektivet.Minesweeper.Core?branchName=master)](https://dev.azure.com/andreasisnes/Elitekollektivet/_build/latest?definitionId=13&branchName=master)
[![PyPI - License](https://img.shields.io/pypi/l/pygame-minesweeper-core)](https://github.com/andreasisnes/Elitekollektivet.Minesweeper.Core/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/pygame-minesweeper-core)](https://pypi.org/project/pygame-minesweeper-core/)
[![Azure DevOps coverage](https://img.shields.io/azure-devops/coverage/andreasisnes/Elitekollektivet/13)](https://dev.azure.com/andreasisnes/Elitekollektivet/_build?definitionId=13)

# Introduction
This minesweeper core library contains the basic functionality of the game.

Minesweeper is a single-player puzzle computer game. The objective of the game is to clear a rectangular board containing hidden "mines" or bombs without detonating any of them, with help from clues about the number of neighboring mines in each field. The game originates from the 1960s, and has been written for many computing platforms in use today. It has many variations and offshoots.

# Motivation
The motivation of these minesweeper projects is to learn the tooling around python projects, how to create CI/CD pipelines for python projects, and distributing python eggs.

# Getting Started
## Installation

```bash
python3 -m pip install pygame-minesweeper-core
# or
pip install pygame-minesweeper-core
```

## General
There are two classes in this library Board and BoardTile. The Board class contains data of the whole board/game while the BoardTile class only contains data of a single tile. To initialize a new game create a Board class with the required params. A board will be always generated randomly and the first tile that gets opened will never contain a mine. If an empty tile gets opened, adjacent tiles will also get opened.

### Board
```python
from minesweeper import core

board = core.Board(rows=10, cols=10, mines=30)
```

There is only a handful of methods and properties you should care about when using the Board class and those are:

| methods | returns |
| ------- | ------- |
| game_new(self, rows: int, cols: int, mines: int): | initialize a new game with given parameters |
| game_reset() | initialize a new game with the same parameters |
| tile_open(i: int, j: int) -> List[BoardTile] | The value *i* is the row/y-axis and *j* is the col/x-axis. The function returns a list of BoardTiles objects that represents tiles that get opened. The function will return an empty list if you try to open a tile that is already opened, if the game is lost or won, or if you open tile that is out of bounds. The functions open adjacent tiles recursively if the tile has zero adjacent mines. The first tiles that get opened can never be a mine. |
| tile_valid(i : int, j : int) -> bool | Returns true if *i* and *j* is inside boundaries

| properties | returns |
| ---------- | ------- |
| __str__ -> str | string representation of the board
| is_game_over -> bool | returns true of the player has lost |
| is_game_finished -> bool | returns true if the player has won |
| rows -> int | number of rows in the game |
| cols -> int | number of column in the game |
| mines -> int | number of mines in the game |
| solution -> str | a string representation of the solution |
| timer -> float | a floating point number of play time. The timer will start when the first tile gets opened and when stops when either player has lost or won.

### BoardTile
| properties | returns |
| ---------- | ------- |
| i -> int   | The row of the tile |
| j -> int   | the columns of the tile |
| type -> str | string representation of the tile |
| number -> int | int representation of the tile |

| static | returns |
| ------ | ------- |
mine | "x"
unopened | "t"
zero | "0"
one | "1"
two | "2"
three | "3"
four | "4"
five | "5"
six | "6"
seven | "7"
eight | "8"

## Example
```python
from minesweeper import core


def main():
    board = core.Board(rows=10, cols=10, mines=30)

    tiles = board.tile_open(5, 5)
    for tile in tiles:
        print(f"tile={tile.type}, ({tile.i}, {tile.j})")
    print(board.is_game_over)
    print(board.is_game_finished)
    print(board)
    print(board.solution)


if __name__ == "__main__":
    main()
```
```bash
# Outputs
tile=0, (5, 5)
tile=1, (5, 6)
tile=0, (5, 4)
tile=2, (5, 3)
tile=1, (6, 4)
tile=0, (6, 5)
tile=0, (6, 6)
tile=0, (6, 7)
tile=1, (6, 8)
tile=1, (7, 7)
tile=1, (7, 8)
tile=2, (7, 6)
tile=1, (5, 7)
tile=2, (5, 8)
tile=1, (7, 5)
tile=2, (7, 4)
tile=3, (6, 3)
tile=1, (4, 4)
tile=0, (4, 5)
tile=1, (4, 6)
tile=1, (3, 5)
tile=2, (3, 6)
tile=2, (3, 4)
tile=4, (4, 3)

False

False

t t t t t t t t t t
t t t t t t t t t t
t t t t t t t t t t
t t t t 2 1 2 t t t
t t t 4 1 0 1 t t t
t t t 2 0 0 1 1 2 t
t t t 3 1 0 0 0 1 t
t t t t 2 1 2 1 1 t
t t t t t t t t t t
t t t t t t t t t t

x 3 3 x x 3 x 2 x x
3 x x 3 4 x 3 2 3 x
2 x 5 3 3 x 2 1 2 2
2 4 x x 2 1 2 2 x 1
x 5 x 4 1 0 1 x 3 2
x 5 x 2 0 0 1 1 2 x
x 4 3 3 1 0 0 0 1 1
1 2 x x 2 1 2 1 1 0
0 1 3 3 3 x 3 x 3 2
0 0 1 x 2 2 x 3 x x
```


## References
* https://en.wikipedia.org/wiki/Minesweeper_(video_game)
