from typing import Union


class BoardTile:
    mine = "x"
    unopened = "t"
    zero = "0"
    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"
    six = "6"
    seven = "7"
    eight = "8"

    __tiles__ = [mine, unopened, zero, one, two, three, four, five, six, seven, eight]

    __map__ = {
        mine: -2,
        unopened: -1,
        zero: 0,
        one: 1,
        two: 2,
        three: 3,
        four: 4,
        five: 5,
        six: 6,
        seven: 7,
        eight: 8,
    }

    def __init__(self, tile: Union[str, int], i: int, j: int):
        self._i = i
        self._j = j
        if str(tile) not in self.__tiles__:
            raise ValueError(
                "Argument 'tile = {}' is not valid. Must be either {}".format(
                    tile, self.__tiles__
                )
            )
        self.__tile = str(tile)

    @property
    def i(self):
        return self._i

    @property
    def j(self):
        return self._j

    @property
    def type(self) -> str:
        return self.__tile

    @property
    def number(self) -> int:
        return self.__map__[str(self.__tile)]

    def __str__(self):
        return self.__tile

    def __eq__(self, tile: Union[str, int, "BoardTile"]):
        return str(self) == str(tile)
