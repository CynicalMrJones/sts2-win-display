from flask import Flask, render_template
import os
from lib.run import main
from markupsafe import Markup
import webbrowser


app = Flask(__name__)

img_folder = os.path.join('static', 'cards')
app.config["UPLOAD_FOLDER"] = img_folder

webbrowser.open('http://localhost:5000')


@app.route("/")
def home():
    main()
    most_used_list = most_used()
    return render_template("index.html", ironclad=most_used_list[0],
                           silent=most_used_list[1], regent=most_used_list[2],
                           necrobinder=most_used_list[3],
                           defect=most_used_list[4])


@app.route("/silent")
def silent():
    main()
    # Create deck variable with the html content
    deck = winhtml("runs/silent.run")
    return render_template("silent.html", deck=deck)


@app.route("/ironclad")
def ironclad():
    main()
    # Create deck variable with the html content
    deck = winhtml("runs/ironclad.run")
    return render_template("ironclad.html", deck=deck)


@app.route("/defect")
def defect():
    main()
    # Create deck variable with the html content
    deck = winhtml("runs/defect.run")
    return render_template("defect.html", deck=deck)


@app.route("/regent")
def regent():
    main()
    # Create deck variable with the html content
    deck = winhtml("runs/regent.run")
    return render_template("regent.html", deck=deck)


@app.route("/necrobinder")
def necrobinder():
    main()
    # Create deck variable with the html content
    deck = winhtml("runs/necrobinder.run")
    return render_template("necrobinder.html", deck=deck)


@app.route("/multiplayer")
def multiplayer():
    main()
    # Create deck variable with the html content
    deck = winhtml("runs/multiplayer.run")
    return render_template("multiplayer.html", deck=deck)


def get_wins_arr(character: str):
    win_list = []
    win = []
    file = open(character)
    for line in file:
        if line == '\n':
            win_list.append(win)
            win = []
        else:
            win.append(line.strip())
    return win_list


# This shit is so ass
def winhtml(character):
    big_string = ''
    win_list = get_wins_arr(character)
    stripped = []

    # Wow this looks dumb
    for win in win_list:
        for entry in win:
            stripped.append(entry.lower())
        del stripped[0]
        seed = stripped[0]
        del stripped[0]
        ascension = stripped[0]
        del stripped[0]

        big_string = big_string + f'<h1 class="deckseed">Seed: {seed} Ascension: {ascension}</h1>'
        big_string += '<h1 class="deckseed">'
        for ent in stripped:
            if ent.find('relic.') != -1:
                big_string = big_string + f'<img src="static/relics/{ent.replace("relic.", "")}.png" height="72" width"72"">'
        big_string += '</h>'
        big_string = big_string + '<div class="deckbox">'

        for e in stripped:
            if e.find('card.') != -1:
                temp = e.split(',')
                if temp[3] == 'false':
                    big_string = big_string + f'<img src="static/cards/{temp[0].replace("card.", "")}.png" height="302" width="240">'
                else:
                    big_string = big_string + f'<img src="static/cards/{temp[0].replace("card.", "")}_plus.png" height="302" width="240">'

        stripped = []
        big_string += '</div>'
    return Markup(big_string)


def most_used():
    char_list = ['runs/ironclad.run', 'runs/silent.run', 'runs/regent.run',
                 'runs/necrobinder.run', 'runs/defect.run']
    most_used = []
    fixed = []
    for item in char_list:
        win_list = get_wins_arr(item)
        most_used.append(counter(win_list))
    for item in most_used:
        for t in item:
            fixed.append(t.replace('card.', ''))
    return fixed


# This is even worse
def counter(arr):
    count_list = dict()
    most_used = []
    for item in arr:
        maximum = 0
        for element in item:
            element = element.lower()
            if element.find('card.') != -1:
                test = element.split(',')
                # This will read all other cards until it finds clone.
                # It needs to ignore cards that have clone and continue otherwise
                if test[1] == 'enchantment.clone':
                    print('Found')
                    break
                if test[3] == 'true':
                    test[0] = f'{test[0]}_plus'
                if test[0] in count_list:
                    count = count_list.get(test[0])
                    count_list[test[0]] = count + 1
                else:
                    count_list[test[0]] = 1

    clean = clean_list(count_list)
    print(clean)
    maximum = max(clean, key=clean.get)
    most_used.append(maximum)
    return most_used


def clean_list(count_list):
    clean = count_list
    # ironclad cards
    clean.pop('card.strike_ironclad', None)
    clean.pop('card.defend_ironclad', None)
    clean.pop('card.strike_ironclad_plus', None)
    clean.pop('card.defend_ironclad_plus', None)
    clean.pop('card.bash', None)
    clean.pop('card.bash_plus', None)

    # silent cards
    clean.pop('card.strike_silent', None)
    clean.pop('card.defend_silent', None)
    clean.pop('card.strike_silent_plus', None)
    clean.pop('card.defend_silent_plus', None)
    clean.pop('card.neutralize', None)
    clean.pop('card.neutralize_plus', None)
    clean.pop('card.survivor', None)
    clean.pop('card.survivor', None)

    # regent cards
    clean.pop('card.strike_regent', None)
    clean.pop('card.defend_regent', None)
    clean.pop('card.strike_regent_plus', None)
    clean.pop('card.defend_regent_plus', None)
    clean.pop('card.falling_star', None)
    clean.pop('card.falling_star_plus', None)
    clean.pop('card.venerate', None)
    clean.pop('card.venerate_plus', None)

    # necrobinder cards
    clean.pop('card.strike_necrobinder', None)
    clean.pop('card.defend_necrobinder', None)
    clean.pop('card.strike_necrobinder_plus', None)
    clean.pop('card.defend_necrobinder_plus', None)
    clean.pop('card.bodyguard', None)
    clean.pop('card.bodyguard_plus', None)
    clean.pop('card.unleash', None)
    clean.pop('card.unleash_plus', None)

    # defect cards
    clean.pop('card.strike_defect', None)
    clean.pop('card.defend_defect', None)
    clean.pop('card.strike_defect_plus', None)
    clean.pop('card.defend_defect_plus', None)
    clean.pop('card.zap', None)
    clean.pop('card.zap_plus', None)
    clean.pop('card.dualcast', None)
    clean.pop('card.dualcast_plus', None)

    # ascenders bane
    clean.pop('card.ascenders_bane', None)

    return clean


if __name__ == "__main__":
    app.run()
