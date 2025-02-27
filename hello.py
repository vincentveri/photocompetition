from flask import Flask, render_template
from .utils import cartelle, get_photos

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', cartelle=cartelle)

@app.route("/<destination>/")
def detail(destination):
    photos = get_photos(destination=destination)
    return render_template('photos.html', photos=photos)


if __name__ == '__main__':
	app.run(debug=True)