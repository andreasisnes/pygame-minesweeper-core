import unittest
import random

try:
    from .context import minesweeper
except ImportError:
    from context import minesweeper
core = minesweeper.core


class TestBoard(unittest.TestCase):
    num_random_test = 100
    lower_bound = 15
    upper_bound = 50

    def test_GameNew_NewParams_NewParamsAreSet(self):
        rows, cols, mines = self.random_params
        board = core.Board(self.random_rows, self.random_cols, self.random_mines)
        board.game_new(rows, cols, mines)
        self.assertEqual(rows, board.rows)
        self.assertEqual(cols, board.cols)
        self.assertEqual(mines, board.mines)

    def test_GameReset_NewParams_UnchangedParams(self):
        rows, cols, mines = self.random_params
        board = core.Board(rows, cols, mines)
        board.game_reset()
        self.assertEqual(rows, board.rows)
        self.assertEqual(cols, board.cols)
        self.assertEqual(mines, board.mines)

    def test_InitBoard_RandomMines_VerifyQuantity(self):
        for _ in range(self.num_random_test):
            rows, cols, mines = self.random_params
            board = core.Board(rows, cols, mines)
            result = len(
                list(
                    filter(
                        lambda x: x == core.BoardTile.mine,
                        [j for i in board._board for j in i],
                    )
                )
            )
            self.assertEqual(mines, result)

    def test_InitBoard_NewBoard_VerifyDims(self):
        rows, cols, mines = self.random_params
        board = core.Board(rows, cols, mines)
        self.assertEqual(len(board._board), rows)
        self.assertEqual(len(board._board[0]), cols)

    def test_InitTiles_NewTiles_VerifyDims(self):
        rows, cols, mines = self.random_params
        board = core.Board(rows, cols, mines)
        self.assertEqual(len(board._tiles), rows)
        self.assertEqual(len(board._tiles[0]), cols)

    @property
    def random_params(self):
        return self.random_rows, self.random_cols, self.random_mines

    @property
    def random_cols(self):
        return random.randint(self.lower_bound, self.upper_bound)

    @property
    def random_rows(self):
        return random.randint(self.lower_bound, self.upper_bound)

    @property
    def random_mines(self):
        return random.randint(self.lower_bound, self.lower_bound * self.lower_bound)
