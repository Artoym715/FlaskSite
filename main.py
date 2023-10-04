from flask import Flask, render_template, url_for, request

app = Flask(__name__)

menu = [
    {"name": "Главная", "url": "/"},
    {"name": "Магазин", "url": "/catalog/clothes"},
    {"name": "О сайте", "url": "/about"}
]


@app.route("/")
def index():
    return render_template('shop/Index.html', title='Главная', menu=menu)


@app.route("/catalog/<name>")
def catalog(name):
    context = {
        'category':
            [
                {
                    'id': 1,
                    'nameCategory': 'clothes',
                    'name': 'ОДЕЖДА',
                }
            ]
    }
    return render_template('shop/catalog.html', title='Магазин', menu=menu, context=context)


@app.route("/catalog/<name>/category")
def category(name):
    context = {
        'Posts':
            [
                {
                    'id': 1,
                    'nameCategory': 'clothes',
                    'name': 'КУРТКА',
                    'img': '/static//img/s-l1600.jpg'

                },
                {
                    'id': 2,
                    'nameCategory': 'clothes',
                    'name': 'БРЮКИ',
                    'img': '/static//img/bryuki-chinosy-regular-fit-straight-chernyj.jpg'
                },
                {
                    'id': 3,
                    'nameCategory': 'clothes',
                    'name': 'ОБУВЬ',
                    'img': '/static//img/png-clipart-shoe-leather-adidas-puma-men-s-big-shoes-png-material-brown.png'
                }
            ]
    }
    return render_template('shop/category.html', title='Одежда', menu=menu, context=context)


@app.route("/catalog/<name>/category/product/<int:id>")
def product(name, id):

    return render_template('shop/product.html', title='Одежда', menu=menu, id=id)


@app.route("/about")
def about():
    return render_template('shop/about.html', title='О сайте', menu=menu)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        print(request.form)
    return render_template('auth/login.html', title='Авторизация')

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('shop/page404.html', title='Страница не найдена!', menu=menu), 404


if __name__ == "__main__":
    app.run(debug=True)
