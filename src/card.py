import enum
import pathlib


class Suit(enum.Enum):
    spades = 0
    clubs = 1
    diamonds = 2
    hearts = 3

    @staticmethod
    def get_value_from_string(name_string):
        if Suit.clubs.name == name_string:
            return Suit.clubs

        elif Suit.diamonds.name == name_string:
            return Suit.diamonds

        elif Suit.hearts.name == name_string:
            return Suit.hearts

        elif Suit.spades.name == name_string:
            return Suit.spades

        else:
            raise ValueError('Suit.get_value_from_string() received invalid suit')


class CardValue(enum.IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    jack = 11
    queen = 12
    king = 13
    ace = 14

    @staticmethod
    def get_value_from_string(name_string):
        if name_string.isnumeric():
            if CardValue.TWO.value == int(name_string):
                return CardValue.TWO

            elif CardValue.THREE.value == int(name_string):
                return CardValue.THREE

            elif CardValue.FOUR.value == int(name_string):
                return CardValue.FOUR

            elif CardValue.FIVE.value == int(name_string):
                return CardValue.FIVE

            elif CardValue.SIX.value == int(name_string):
                return CardValue.SIX

            elif CardValue.SEVEN.value == int(name_string):
                return CardValue.SEVEN

            elif CardValue.EIGHT.value == int(name_string):
                return CardValue.EIGHT

            elif CardValue.NINE.value == int(name_string):
                return CardValue.NINE

            elif CardValue.TEN.value == int(name_string):
                return CardValue.TEN
        else:
            if CardValue.jack.name == name_string:
                return CardValue.jack

            elif CardValue.queen.name == name_string:
                return CardValue.queen

            elif CardValue.king.name == name_string:
                return CardValue.king

            elif CardValue.ace.name == name_string:
                return CardValue.ace


class Card:
    def __init__(self, value: CardValue, suit: Suit, decal: pathlib.WindowsPath):
        self.value = value
        self.suit = suit
        self.decal = decal

    def __str__(self):
        return f"value: {self.value}, suit: {self.suit}, decal: {self.decal}"
