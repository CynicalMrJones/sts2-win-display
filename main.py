import json
import os
import sys
from dataclasses import dataclass


@dataclass
class Card:
    name: str
    enchant: str
    enchant_num: int
    upgraded: bool


@dataclass
class WinningRun:
    character: str
    deck: list
    seed: str

    def add_card(self, card):
        self.deck.append(card)

    def print_run(self):
        print(self.character)
        print(self.seed)
        for card in self.deck:
            print(card)


def main():
    print(sys.platform)
    path = "/home/juicy/.local/share/SlayTheSpire2/steam/76561198243211320/pr"\
        "ofile1/saves/history/"
    for entry in os.scandir(path):
        if entry.is_file():
            if '.backup' not in entry.name:
                win = WinningRun('', [], '')
                get_cards(entry.path, win)
                win.print_run()


def get_cards(path, win):
    # load file in
    file = open(path)
    loaded = json.load(file)

    # Only load wins
    if loaded['win'] is False:
        print("Run not won")
        return 0

    # The Sneed for the ran
    win.seed = loaded['seed']
    # iterating on player objects
    for items in loaded['players']:
        # iterating on cards objects
        # These objects are all card data
        win.character = items['character']
        for card in items['deck']:
            new_card = Card("", "", 0, False)
            new_card.name = card['id']
            # iterating on card objects
            for meme in card:
                if meme == 'enchantment':
                    new_card.enchant = card['enchantment']['id']
                    new_card.enchant_num = card['enchantment']['amount']
                if meme == 'current_upgrade_level':
                    new_card.upgraded = True
            win.add_card(new_card)


if __name__ == "__main__":
    main()
