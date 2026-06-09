import json
import os
from dataclasses import dataclass


@dataclass
class WinningRun:
    character: str
    deck: list

    def add_card(self, card):
        self.deck.append(card)

    def print_deck(self):
        for card in self.deck:
            print(card)


def main():
    win = WinningRun('', [])
    for entry in os.scandir("/home/juicy/.local/share/SlayTheSpire2/steam/76561198243211320/profile1/saves/history/"):
        if entry.is_file():
            if '.backup' not in entry.name:
                get_cards(entry.path, win)
    win.print_deck()


def get_cards(path, win):
    # load file in
    file = open(path)
    loaded = json.load(file)
    print(f"Total Items: {len(loaded)}")

    if loaded['win'] is False:
        print("Run not won")
        return 0

    # iterating on player objects
    for items in loaded['players']:
        # iterating on cards objects
        # These objects are all card data
        win.character = 'regent'
        for card in items['deck']:
            print(f"Card Name: {card['id']}")
            win.add_card(card['id'])
            # iterating on card objects
            for meme in card:
                if meme == 'enchantment':
                    print(f"Enchant Amount : {card['enchantment']['amount']}")
                    print(f"Enchant Type: {card['enchantment']['id']}")
                if meme == 'current_upgrade_level':
                    print("Upgraded")
            print("")


if __name__ == "__main__":
    main()
