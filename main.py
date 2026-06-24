import json
import os
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

    def add_card(self, card):
        self.deck.append(card)

    def print_run(self):
        print(self.character)
        for card in self.deck:
            print(card)


def main():
    for entry in os.scandir("/home/juicy/.local/share/SlayTheSpire2/steam/76561198243211320/profile1/saves/history/"):
        if entry.is_file():
            if '.backup' not in entry.name:
                win = WinningRun('', [])
                get_cards(entry.path, win)
                win.print_run()


def get_cards(path, win):
    # load file in
    file = open(path)
    loaded = json.load(file)
    print(f"Total Items: {len(loaded)}")

    if loaded['win'] is False:
        print("Run not won")
        return 0

    print(loaded['seed'])
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
