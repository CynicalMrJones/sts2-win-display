
import json
import os
def main():
    for entry in os.scandir("/home/juicy/.local/share/SlayTheSpire2/steam/76561198243211320/profile1/saves/history/"):
        if entry.is_file():
            if not '.backup' in entry.name:
                get_cards(entry.path)

    # get_cards("")

def get_cards(path):
    #load file in 
    file = open(path)
    loaded = json.load(file)
    print(f"Total Items: {len(loaded)}")

    if loaded['win'] == False:
        print("Run not won")
        return 0

    fullstring = ""
    #iterating on player objects
    for items in loaded['players']:
        #iterating on cards objects
        #These objects are all card data
        for card in items['deck']:
            teststring= ""
            print(f"Card Name: {card['id']}")
            #iterating on card objects
            for meme in card:
                if meme == 'enchantment':
                    print(f"Enchant Amount : {card['enchantment']['amount']}")
                    print(f"Enchant Type: {card['enchantment']['id']}")
                if meme == 'current_upgrade_level':
                    print(f"Upgraded")
            print("")


if __name__ == "__main__":
    main()
