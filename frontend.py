from flask import Flask, render_template
import os
from lib.run import main
from markupsafe import Markup

app = Flask(__name__)

img_folder = os.path.join('static', 'cards')
app.config["UPLOAD_FOLDER"] = img_folder


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/silent")
def silent():
    main()
    # Create deck variable with the html content
    deck = winhtml("silent.txt")
    return render_template("silent.html", deck=deck)


@app.route("/ironclad")
def ironclad():
    main()
    # Create deck variable with the html content
    deck = winhtml("ironclad.txt")
    return render_template("ironclad.html", deck=deck)


@app.route("/defect")
def defect():
    main()
    # Create deck variable with the html content
    deck = winhtml("defect.txt")
    return render_template("defect.html", deck=deck)


@app.route("/regent")
def regent():
    main()
    # Create deck variable with the html content
    deck = winhtml("regent.txt")
    return render_template("regent.html", deck=deck)


@app.route("/necrobinder")
def necrobinder():
    main()
    # Create deck variable with the html content
    deck = winhtml("necrobinder.txt")
    return render_template("necrobinder.html", deck=deck)


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
        # print(stripped)
        del stripped[0]
        # print(stripped)
        seed = stripped[0]
        del stripped[0]
        # print('End')
        big_string = big_string + f'<h1 class="deckseed">Seed: {seed}</h1>'
        big_string = big_string + '<div class="deckbox">'

        for e in stripped:
            big_string = big_string + f'<img src="static/cards/{e.split(',')[0].replace('card.', '')}.png" height="342" width="280">'

        stripped = []
        big_string += '</div>'
        print(big_string)
        print("")
    return Markup(big_string)


if __name__ == "__main__":
    app.run()
