from flask import Flask, render_template
import os

app = Flask(__name__)

img_folder = os.path.join('static', 'cards', 'colorless')
app.config["UPLOAD_FOLDER"] = img_folder

@app.route("/")
def img_display():
    test_pic = os.path.join(app.config["UPLOAD_FOLDER"], "splash.png")
    print(test_pic)
    return render_template("index.html", user_pic=test_pic)


if __name__ == "__main__":
    app.run(debug=True)
