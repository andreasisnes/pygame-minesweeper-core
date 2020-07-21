from typing import Union


class BoardTile:
    mine = 'x'
    unopened = 't'
    zero = '0'
    one = '1'
    two = '2'
    three = '3'
    four = '4'
    five = '5'
    six = '6'
    seven = '7'
    eight = '8'

    __tiles__ = [
        mine,
        unopened,
        zero,
        one,
        two,
        three,
        four,
        five,
        six,
        seven,
        eight
    ]

    def __init__(self, tile: Union[str, int]):
        if str(tile) not in self.__tiles__:
            raise ValueError("Argument 'tile = {}' is not valid. Must be either {}".format(
                tile, self.__tiles__))
        self.__tile = tile

    def __str__(self):
        return self.__tile
