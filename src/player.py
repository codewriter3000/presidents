import enum


class PlayerStatus(enum.Enum):
    PRESIDENT = 0
    VICE_PRESIDENT = 1
    NEUTRAL = 2
    VICE_SCUM = 3
    SCUM = 4


class Player:
    def __init__(self, name: str):
        self.name = name
        self.status = PlayerStatus.NEUTRAL
        self.deck = []
