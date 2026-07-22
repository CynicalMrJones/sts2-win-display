from flask import Flask, render_template
import os
from run import main
from markupsafe import Markup

app = Flask(__name__)

img_folder = os.path.join('static', 'cards', 'colorless')
app.config["UPLOAD_FOLDER"] = img_folder


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/win")
def win():
    main()
    # Create deck variable with the html content
    test_pic = os.path.join(app.config["UPLOAD_FOLDER"], "splash.png")
    deck = winhtml(test_pic)
    return render_template("win.html", user_pic=test_pic, deck=deck)


def winhtml(user_pic):
    # Need to rewrite .txt to custom jsons to make
    # this easier

    # meme = []
    # with open('defect.txt') as f:
    #     for e in f:
    #         if e == '\n':
    #             break
    #         meme.append(e.strip())
    #     # Wow this looks dumb
    #     del meme[0]
    #     del meme[0]
    #     print(meme)
    return Markup(
            f'<img src="{user_pic}" height="342" width="280">'
            f'<img src="{user_pic}" height="342" width="280">'
            f'<img src="{user_pic}" height="342" width="280">'
            f'<img src="{user_pic}" height="342" width="280">'
            )


if __name__ == "__main__":
    app.run(debug=True)
