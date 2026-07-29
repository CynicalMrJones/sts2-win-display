from flask import Flask, render_template
import os
from lib.run import main
from markupsafe import Markup

app = Flask(__name__)

img_folder = os.path.join('static', 'cards', 'ironclad')
app.config["UPLOAD_FOLDER"] = img_folder


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/win")
def win():
    main()
    # Create deck variable with the html content
    test_pic = os.path.join(app.config["UPLOAD_FOLDER"])
    deck = winhtml(test_pic)
    return render_template("win.html", deck=deck)


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


def winhtml(user_pic):
    big_string = ""
    win_list = get_wins_arr('ironclad.txt')
    stripped = []

    # Wow this looks dumb
    for win in win_list:
        for entry in win:
            stripped.append(entry.lower())
        print(stripped)
        del stripped[0]
        print(stripped)
        seed = stripped[0]
        del stripped[0]
        print('End')
        big_string = big_string + f'<h1>Seed: {seed}'

        for e in stripped:
            big_string = big_string + f'<img src="static/cards/{e.split(',')[0].replace('card.', '')}.png" height="342" width="280">'

        stripped = []
    return Markup(big_string)


if __name__ == "__main__":
    app.run()
