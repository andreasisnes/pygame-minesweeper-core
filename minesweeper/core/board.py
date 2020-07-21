from .board_tile import BoardTile


class Board:
    def __init__(self, columns: int, rows: int, mines: int):
        self._columns = columns
        self._rows = rows
        self._mines = mines

        self._board = self.__init__board__()
        self._sheet = None

        self._is_game_over = False
        self._is_game_done = False
        self._opened = 0

    def game_new(self, columns: int, rows: int, mines: int):
        self.__init__(columns, rows, mines)

    def game_reset(self):
        self.__init__(self._columns, self._rows, self._mines)

    def tile_open(self):
        pass

    def tile_valid(self):
        pass

    @property
    def timer(self):
        pass

    @property
    def columns(self):
        return self._columns

    @property
    def mines(self):
        return self._mines

    @property
    def rows(self):
        return self._rows

    def __generate_board__(self) -> list:
        pass

    def __generate_sheet__(self) -> list:
        pass

    def __init__sheet__(self):
        pass

    def __init__board__(self):
        pass

    def __open__adjacent(self):
        pass
