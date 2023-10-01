from flask import Flask, render_template

app = Flask(__name__)

menu = [
    {"name": "Главная", "url": "/"},
    {"name": "Магазин", "url": "catalog"},
    {"name": "О сайте", "url": "about"}
]


@app.route("/")
def index():
    return render_template('shop/Index.html', title='Главная', menu=menu)


@app.route("/catalog")
def catalog():
    return render_template('shop/catalog.html', title='Магазин', menu=menu)


@app.route("/about")
def about():
    return render_template('shop/about.html', title='О сайте', menu=menu)


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('shop/page404.html', title='Страница не найдена!', menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
