from pathlib import Path

from src.card import Suit, Card, CardValue


class Game:
    def __init__(self):
        self.players = set({'player 1', 'player 2', 'player 3', 'player 4', 'player 5'})
        self.cards = set()

        self.add_cards()

    def add_player(self, player):
        self.players.add(player)

    def remove_player(self, player):
        self.players.remove(player)

    def add_cards(self):
        for decal_file_path in Path('../assets/img/svg_playing_cards/fronts').glob('*'):
            card_name = str(decal_file_path).split('\\')[-1]

            card_suit = card_name.split('_')[0]
            card_value = card_name.split('_')[-1].split('.')[0]

            if card_suit not in ['clubs', 'diamonds', 'hearts', 'spades']:
                continue

            card = Card(CardValue.get_value_from_string(card_value), Suit.get_value_from_string(card_suit), decal_file_path)

            self.cards.add(card)

    def shuffle_cards_into_decks(self):
        player_count = len(self.players)
        decks = tuple([] for _ in range(player_count))
        print(len(decks))

        i = 1
        for card in self.cards:
            print(card)
            print(i)
            decks[i%player_count].append(card)
            i += 1

        print(decks)
