from flask import Flask, render_template

app = Flask(__name__)

menu = [
    {"name": "Главная", "url": "/"},
    {"name": "Магазин", "url": "/catalog"},
    {"name": "О сайте", "url": "/about"}
]


@app.route("/")
def index():
    return render_template('shop/Index.html', title='Главная', menu=menu)


@app.route("/catalog")
def catalog():
    context = {
        'category':
            [
                {
                    'id': 1,
                    'name': 'ОДЕЖДА',
                }
            ]
    }
    return render_template('shop/catalog.html', title='Магазин', menu=menu, context=context)


@app.route("/catalog/category/")
def category():
    context = {
        'category':
            [
                {
                    'id': 1,
                    'name': 'КУРТКА',
                    'img': '/static//img/s-l1600.jpg'

                },
                {
                    'id': 2,
                    'name': 'БРЮКИ',
                    'img': '/static//img/bryuki-chinosy-regular-fit-straight-chernyj.jpg'
                },
                {
                    'id': 3,
                    'name': 'ОБУВЬ',
                    'img': '/static//img/png-clipart-shoe-leather-adidas-puma-men-s-big-shoes-png-material-brown.png'
                }
            ]
    }
    return render_template('shop/category.html', title='link.name', menu=menu, context=context)


@app.route("/about")
def about():
    return render_template('shop/about.html', title='О сайте', menu=menu)


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('shop/page404.html', title='Страница не найдена!', menu=menu), 404


if __name__ == "__main__":
    app.run(debug=True)
