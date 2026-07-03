import json
import os
import sys
from dataclasses import dataclass

# I don't know how I want to handle seeds
# Maybe a file that contains all played seeds
# Load in the file on run time


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
        if self.seed == '':
            return
        print(self.character)
        print(self.seed)
        for card in self.deck:
            print(card)

    def to_string(self):
        string = self.character + '\n' + self.seed + '\n'
        for card in self.deck:
            string = string + str(card) + '\n'
        return string


def main():
    # Find os and adjust path accordingly
    system = sys.platform
    if system == 'linux':
        path = os.path.expanduser("~") + "/.local/share/SlayTheSpire2/steam/76561198243211320/pr"\
        "ofile1/saves/history/"
    elif system == 'win32':
        # This should work. Im not on windows
        path = os.path.expanduser("~") + "\\AppData\\Local\\SlayTheSpire2\\saves\\history\\"
    else:
        print('Unable to find sts2 dir')
        exit(0)

    seed_arr = []
    with open('win_seeds.txt', 'r') as file:
        for line in file:
            seed_arr.append(line.strip())

    for entry in os.scandir(path):
        if entry.is_file():
            if '.backup' not in entry.name:
                win = WinningRun('', [], '')
                get_cards(entry.path, win)
                # win.print_run()
                if win.seed not in seed_arr:
                    win_writer(win)


def get_cards(path, win):
    # load file in
    file = open(path)
    loaded = json.load(file)

    # Only load wins
    if loaded['win'] is False:
        return 0

    # The Sneed for the ran
    win.seed = loaded['seed']
    # iterating on player objects
    # print(f"Size of players: {len(loaded['players'])}")
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


def win_writer(winning_run):
    # Empty runs
    if winning_run.seed == '':
        return

    with open("win_seeds.txt", "a") as sf:
        sf.write(winning_run.seed + '\n')

    with open("Winning.txt", "a") as f:
        f.write(winning_run.to_string())
    f.close()


if __name__ == "__main__":
    main()
