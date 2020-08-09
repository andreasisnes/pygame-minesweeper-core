import unittest
import random

try:
    from context import minesweeper
except ImportError:
    from .context import minesweeper
core = minesweeper.core


class TestBoard(unittest.TestCase):
    num_random_test = 10
    lower_bound = 10
    upper_bound = 30

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

    def test_Board_NoMineWhereTileGetsOpen_VerifySpreadOfMines(self):
        for _ in range(self.num_random_test):
            rows, cols, mines = self.random_params
            board = core.Board(rows, cols, mines)
            tile_i, tile_j = random.randint(0, rows - 1), random.randint(0, cols - 1)
            board.tile_open(tile_i, tile_j)
            for i in [tile_i + 1, tile_i - 1, tile_i]:
                for j in [tile_j + 1, tile_j - 1, tile_j]:
                    if board.tile_valid(i, j):
                        self.assertNotEqual(board._board[i][j], core.BoardTile.mine)

    def test_Board_VerifyNumberOfCloseMines_VerifyNumberOfMines(self):
        for _ in range(self.num_random_test):
            rows, cols, mines = self.random_params
            board = core.Board(rows, cols, mines)
            tile_i, tile_j = random.randint(0, rows - 1), random.randint(0, cols - 1)
            board.tile_open(tile_i, tile_j)
            for row in range(rows):
                for col in range(cols):
                    tile_result = board._board[row][col]
                    tile_expected = 0
                    if tile_result.type != core.BoardTile.mine:
                        for i in [row + 1, row - 1, row]:
                            for j in [col + 1, col - 1, col]:
                                if (
                                    board.tile_valid(i, j)
                                    and board._board[i][j] == core.BoardTile.mine
                                ):
                                    tile_expected += 1
                        self.assertEqual(tile_result.number, tile_expected)

    def test_Tiles_SetTileFromBoardWhenOpen_TileShouldBeSet(self):
        for _ in range(self.num_random_test):
            rows, cols, mines = self.random_params
            board = core.Board(rows, cols, mines)
            tile_i, tile_j = random.randint(0, rows - 1), random.randint(0, cols - 1)
            tile = board.tile_open(tile_i, tile_j)
            self.assertEqual(tile[0], board._tiles[tile_i][tile_j])
            self.assertEqual(tile[0], board._board[tile_i][tile_j])

    def test_IsGameFinished_OpenAllTile_IsGameFinishedShouldBeSetToTrue(self):
        for _ in range(self.num_random_test):
            rows, cols, mines = self.random_params
            board = core.Board(rows, cols, mines)
            tile_i, tile_j = random.randint(0, rows - 1), random.randint(0, cols - 1)
            self.assertFalse(board.is_game_finished)
            self.assertFalse(board.is_game_over)
            board.tile_open(tile_i, tile_j)
            for i in range(rows):
                for j in range(cols):
                    if board._board[i][j].type != core.BoardTile.mine:
                        board.tile_open(i, j)
                        self.assertEqual(0, len(board.tile_open(i, j)))
            self.assertTrue(board.is_game_finished)
            self.assertFalse(board.is_game_over)
            self.assertEqual(0, len(board.tile_open(tile_i, tile_j)))

    def test_IsGameOver_OpenMine_IsGameOverShouldBeSetToTrue(self):
        for _ in range(self.num_random_test):
            rows, cols, mines = self.random_params
            board = core.Board(rows, cols, mines)
            tile_i, tile_j = random.randint(0, rows - 1), random.randint(0, cols - 1)
            board.tile_open(tile_i, tile_j)
            self.assertFalse(board.is_game_over)
            for i in range(rows):
                for j in range(cols):
                    if board._board[i][j] == core.BoardTile.mine:
                        mine = board.tile_open(i, j)
                        self.assertEqual(mine[0].type, mine[0].mine)
                        if not board.is_game_finished:
                            self.assertTrue(board.is_game_over)
                            return

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

    def test_StrBoard_Board_VerifyString(self):
        for _ in range(self.num_random_test):
            rows, cols, mines = self.random_params
            board = core.Board(rows, cols, mines)
            tile_i, tile_j = random.randint(0, rows - 1), random.randint(0, cols - 1)
            board.tile_open(tile_i, tile_j)
            strBoard = str(board)
            entries = strBoard.replace("\n", " ").split(" ")
            for i in range(rows):
                for j in range(cols):
                    self.assertEqual(entries[(i * cols) + j], board._tiles[i][j].type)

    def test_StrSolution_Board_VerifyString(self):
        for _ in range(self.num_random_test):
            rows, cols, mines = self.random_params
            board = core.Board(rows, cols, mines)
            tile_i, tile_j = random.randint(0, rows - 1), random.randint(0, cols - 1)
            board.tile_open(tile_i, tile_j)
            strBoard = str(board.solution)
            entries = strBoard.replace("\n", " ").split(" ")
            for i in range(rows):
                for j in range(cols):
                    self.assertEqual(entries[(i * cols) + j], board._board[i][j].type)

    def test_InitBoard_InvalidParameters_RaiseTypeError(self):
        with self.assertRaises(ValueError):
            core.Board(5, 5, 20)

    def test_OpenTile_Timer_ShouldStart(self):
        for _ in range(self.num_random_test):
            rows, cols, mines = self.random_params
            board = core.Board(rows, cols, mines)
            tile_i, tile_j = random.randint(0, rows - 1), random.randint(0, cols - 1)
            board.tile_open(tile_i, tile_j)
            self.assertGreaterEqual(board.timer, 0.0)

    @property
    def random_params(self):
        return self.random_rows, self.random_cols, self.random_mines

    @property
    def random_cols(self):
        return random.randint(self.lower_bound + 3, self.upper_bound)

    @property
    def random_rows(self):
        return random.randint(self.lower_bound + 3, self.upper_bound)

    @property
    def random_mines(self):
        return random.randint(self.lower_bound, self.lower_bound * self.lower_bound)


if __name__ == "__main__":
    unittest.main()
