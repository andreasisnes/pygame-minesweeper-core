import unittest

try:
    from context import minesweeper
except ImportError:
    from .context import minesweeper
core = minesweeper.core


class TestBoardTile(unittest.TestCase):
    def test_Init_BoardTileMine_ToString(self):
        tile = core.BoardTile(core.BoardTile.mine, 0, 0)
        self.assertEqual(core.BoardTile.mine, str(tile))

    def test_Init_BoardTileUnopened_ToString(self):
        tile = core.BoardTile(core.BoardTile.unopened, 0, 0)
        self.assertEqual(core.BoardTile.unopened, str(tile))

    def test_Init_BoardTileZero_ToString(self):
        tile = core.BoardTile(core.BoardTile.zero, 0, 0)
        self.assertEqual(core.BoardTile.zero, str(tile))

    def test_Init_BoardTileOne_ToString(self):
        tile = core.BoardTile(core.BoardTile.one, 0, 0)
        self.assertEqual(core.BoardTile.one, str(tile))

    def test_Init_BoardTileTwo_ToString(self):
        tile = core.BoardTile(core.BoardTile.two, 0, 0)
        self.assertEqual(core.BoardTile.two, str(tile))

    def test_Init_BoardTileThree_ToString(self):
        tile = core.BoardTile(core.BoardTile.three, 0, 0)
        self.assertEqual(core.BoardTile.three, str(tile))

    def test_Init_BoardTileFour_ToString(self):
        tile = core.BoardTile(core.BoardTile.four, 0, 0)
        self.assertEqual(core.BoardTile.four, str(tile))

    def test_Init_BoardTileFive_ToString(self):
        tile = core.BoardTile(core.BoardTile.five, 0, 0)
        self.assertEqual(core.BoardTile.five, str(tile))

    def test_Init_BoardTileSix_ToString(self):
        tile = core.BoardTile(core.BoardTile.six, 0, 0)
        self.assertEqual(core.BoardTile.six, str(tile))

    def test_Init_BoardTileSeven_ToString(self):
        tile = core.BoardTile(core.BoardTile.seven, 0, 0)
        self.assertEqual(core.BoardTile.seven, str(tile))

    def test_Init_BoardTileEight_ToString(self):
        tile = core.BoardTile(core.BoardTile.eight, 0, 0)
        self.assertEqual(core.BoardTile.eight, str(tile))

    def test_Init_BoardTileInvalidString_RaiseValueError(self):
        self.assertRaises(ValueError, core.BoardTile, "testing", 0, 0)

    def test_Init_IAndJ_GivenParams(self):
        tile1 = core.BoardTile(core.BoardTile.zero, 25, 15)
        self.assertEqual(25, tile1.i)
        self.assertEqual(15, tile1.j)

    def test_Equality_ZeroAndZero_True(self):
        tile1 = core.BoardTile(core.BoardTile.zero, 0, 0)
        tile2 = core.BoardTile(core.BoardTile.zero, 0, 0)
        self.assertTrue(tile1 == tile2)
        self.assertTrue(tile1 == str(tile2))

    def test_InEquality_ZeroAndOne_False(self):
        tile1 = core.BoardTile(core.BoardTile.zero, 0, 0)
        tile2 = core.BoardTile(core.BoardTile.one, 0, 0)
        self.assertFalse(tile1 == tile2)
        self.assertFalse(tile1 == str(tile2))
