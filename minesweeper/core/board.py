from .board_tile import BoardTile
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
        self._is_game_done = False
        self._opened = 0
        self._timer = time.time()
        self._timer1 = time.time()

    def game_new(self, rows: int, cols: int, mines: int):
        self.__init__(rows, cols, mines)

    def game_reset(self):
        self.__init__(self._rows, self._cols, self._mines)

    def tile_open(self, row, col):
        pass

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
    def is_game_done(self):
        return self._is_game_done

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
    def solution(self):
        return "\n".join(
            ["".join([f"{str(j):2}" for j in i]).rstrip() for i in self._board]
        )

    @property
    def timer(self):
        if self.is_game_over or self.is_game_done:
            return self._timer1 - self._timer if self._opened > 0 else 0.0
        return time.time() - self._timer if self._opened > 0 else 0.0

    def __init__board__(self):
        mines = random.sample(range(0, self.rows * self.cols), self.mines)
        rowf = (
            lambda i, j: BoardTile.mine
            if i * self.cols + j in mines
            else BoardTile.zero
        )

        return [
            [BoardTile(rowf(i, j)) for j in range(self.cols)] for i in range(self.rows)
        ]

    def __init__tiles__(self):
        return [
            [BoardTile(BoardTile.unopened) for _ in range(self.cols)]
            for _ in range(self.rows)
        ]

    def __str__(self):
        return "\n".join(
            [
                "".join([f"{str(tile):2}" for tile in row]).rstrip()
                for row in self._tiles
            ]
        )
