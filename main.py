from flask import Flask, render_template

app = Flask(__name__)

menu = [
        {"name": "Главная", "url": "/"},
        {"name": "Блог", "url": "blog"},
        {"name": "Магазин", "url": "catalog"},
        {"name": "О сайте", "url": "about"}
       ]


@app.route("/")
def index():
    return render_template('Index.html', title='Главная', menu=menu)


@app.route("/blog")
def blog():
    return render_template('blog.html', title='Блог', menu=menu)


@app.route("/catalog")
def catalog():
    return render_template('catalog.html', title='Магазин', menu=menu)


@app.route("/about")
def about():
    return render_template('about.html', title='О сайте', menu=menu)


if __name__ == "__main__":
    app.run(debug=True)