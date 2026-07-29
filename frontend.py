from flask import Flask, render_template
import os
from run import main
from markupsafe import Markup

app = Flask(__name__)

img_folder = os.path.join('static', 'cards', 'defect')
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


def winhtml(user_pic):
    old_list = []
    stripped = []
    with open('defect.txt') as f:
        for e in f:
            if e == '\n':
                break
            old_list.append(e.lower().strip())
        # Wow this looks dumb
        del old_list[0]
        del old_list[0]
        for e in old_list:
            stripped.append(e.replace("card.", ""))

        big_string = ""
        for e in stripped:
            big_string = big_string + f'<img src="static/cards/{e.split(',')[0]}.png" height="342" width="280">'

    return Markup(big_string)


if __name__ == "__main__":
    app.run()
