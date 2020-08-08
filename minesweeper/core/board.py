try:
    from .board_tile import BoardTile
except ImportError:
    from .board_tile import BoardTile
from typing import List
import random
import time


class Board:
    def __init__(self, rows: int, cols: int, mines: int):
        self._cols = cols
        self._rows = rows
        self._mines = mines

        self._board = self.__init__board__()
        self._tiles = self.__init__tiles__()

        self._is_game_over = False
        self._is_game_finished = False
        self._opened = 0
        self._timer = time.time()
        self._timer1 = time.time()

    def game_new(self, rows: int, cols: int, mines: int):
        self.__init__(rows, cols, mines)

    def game_reset(self):
        self.__init__(self._rows, self._cols, self._mines)

    def tile_open(self, i, j) -> List[BoardTile]:
        if self._is_game_over or self._is_game_finished or not self.tile_valid(i, j):
            return []
        if self._tiles[i][j].type != BoardTile.unopened:
            return []
        if self._opened == 0:
            self.__tiles_adjust__(i, j)
            self.__tiles_numerate__()

        self._opened += 1
        self._tiles[i][j] = self._board[i][j]
        if (self._opened + self.mines) == (self.rows * self.cols):
            self._is_game_finished = True
            self.timer1 = time.time()
        if self._tiles[i][j].type == BoardTile.mine:
            self._is_game_over = True
            self._timer1 = time.time()
        elif self._tiles[i][j].number >= 0:
            if self._tiles[i][j].number == 0:
                return self.__tiles_open_adjacent__(i, j, [self._tiles[i][j]])
            return [self._tiles[i][j]]

    def tile_valid(self, row, col):
        return (
            True
            if (row >= 0 and row < self.rows) and (col >= 0 and col < self.cols)
            else False
        )

    @property
    def is_game_over(self):
        return self._is_game_over

    @property
    def is_game_finished(self):
        return self._is_game_finished

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols

    @property
    def mines(self):
        return self._mines

    @property
    def solution(self) -> str:
        return "\n".join(
            ["".join([f"{str(j):2}" for j in i]).rstrip() for i in self._board]
        )

    @property
    def timer(self):
        if self.is_game_over or self.is_game_finished:
            return self._timer1 - self._timer if self._opened > 0 else 0.0
        return time.time() - self._timer if self._opened > 0 else 0.0

    def __init__board__(self) -> List[List[BoardTile]]:
        mines = random.sample(range(0, self.rows * self.cols), self.mines)
        rowf = (
            lambda i, j: BoardTile.mine
            if i * self.cols + j in mines
            else BoardTile.zero
        )
        return [
            [BoardTile(rowf(i, j), i, j) for j in range(self.cols)]
            for i in range(self.rows)
        ]

    def __init__tiles__(self) -> List[List[BoardTile]]:
        return [
            [BoardTile(BoardTile.unopened, i, j) for j in range(self.cols)]
            for i in range(self.rows)
        ]

    def __tiles_open_adjacent__(self, row: int, col: int, opened: List[BoardTile]):
        if self.tile_valid(row, col):
            if self._board[row][col].type == BoardTile.mine:
                return [self._board[row][col]]
            for i in [row, row + 1, row - 1]:
                for j in [col, col + 1, col - 1]:
                    if (
                        self.tile_valid(i, j)
                        and self._tiles[i][j].type == BoardTile.unopened
                    ):
                        self._opened += 1
                        self._tiles[i][j] = self._board[i][j]
                        opened.append(self._board[i][j])
                        if (self._opened + self.mines) == (self.rows * self.cols):
                            self._is_game_finished = True
                            self._timer1 = time.time()
                        if self._board[i][j].type == BoardTile.zero:
                            self.__tiles_open_adjacent__(i, j, opened)
        return opened

    def __tiles_adjust__(self, row: int, col: int):
        for i in [row + 1, row - 1, row]:
            for j in [col + 1, col - 1, col]:
                if self.tile_valid(i, j) and self._board[i][j].type == BoardTile.mine:
                    rand_i = random.randint(0, self.rows - 1)
                    rand_j = random.randint(0, self.cols - 1)
                    while self._board[rand_i][rand_j].type == BoardTile.mine or (
                        abs(row - rand_i) <= 1 and abs(col - rand_j) <= 1
                    ):
                        rand_i = random.randint(0, self.rows - 1)
                        rand_j = random.randint(0, self.cols - 1)
                    self._board[rand_i][rand_j] = BoardTile(
                        BoardTile.mine, rand_i, rand_j
                    )
                    self._board[i][j] = BoardTile(BoardTile.zero, i, j)

    def __tiles_numerate__(self) -> List[List[BoardTile]]:
        for row in range(self.rows):
            for col in range(self.cols):
                if self._board[row][col].type == BoardTile.mine:
                    continue
                adjacent_bombs = 0
                for i in [row + 1, row - 1, row]:
                    for j in [col + 1, col - 1, col]:
                        if (
                            self.tile_valid(i, j)
                            and self._board[i][j].type == BoardTile.mine
                        ):
                            adjacent_bombs += 1
                self._board[row][col] = BoardTile(str(adjacent_bombs), i, j)

    def __str__(self) -> str:
        return "\n".join(
            [
                "".join([f"{str(tile):2}" for tile in row]).rstrip()
                for row in self._tiles
            ]
        )
