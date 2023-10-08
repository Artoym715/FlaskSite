from flask import Flask, render_template, url_for, request,  flash, make_response, redirect
from models import db, Users, Posts
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, login_required, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dcad0b50abb077fe5acec19aa63e4f42d48c1396baef601f6cf5464f469661c0'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mydatabase.db"
db.init_app(app)
csrf = CSRFProtect(app)
manager = LoginManager(app)

adminMenu = [

    {"name": "Главная", "url": "/"}
]
menu = [
    {"name": "Главная", "url": "/"},
    {"name": "Магазин", "url": "/catalog/clothes"},
    {"name": "О сайте", "url": "/about"}
]


@app.route("/")
def index():
    return render_template('shop/Index.html', title='Главная', menu=menu)


@app.route("/catalog/<name>")
@login_required
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
@login_required
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
@login_required
def product(name, id):
    return render_template('shop/product.html', title='Одежда', menu=menu, id=id)


@app.route("/about")
@login_required
def about():
    return render_template('shop/about.html', title='О сайте', menu=menu)


@app.route("/login", methods=["POST", "GET"])
def login():
    email = request.form.get('useremail')
    password = request.form.get('userpassword')

    if email and password:
        user = Users.query.filter_by(email=email).first()

        if check_password_hash(user.password, password):
            login_user(user)
            return redirect('admin')
    return render_template('auth/login.html', title='Авторизация')


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        name = request.form.get('username')
        email = request.form.get('useremail')
        password = request.form.get('userpassword')
        password2 = request.form.get('userсonfirmpassword')
        if len(name) > 4 and len(email) > 4 and len(password) > 4 and password == password2:
            hash_pwd = generate_password_hash(password)
            new_user = Users(username=name, email=email, password=hash_pwd)  # type: ignore
            db.session.add(new_user)
            db.session.commit()
            flash('Регистрация прошла успешно!', category='alert-success')
            return redirect('login')
        else:
            db.session.rollback()
            flash('Произошла ошибка!', category='alert-danger')
            return redirect('register')
    return render_template('auth/register.html', title='Регистрация')


@manager.user_loader
def load_user(users_id):
    return Users.query.get(users_id)


@app.route("/admin", methods=["POST", "GET"])
@login_required
def admin():
    info = []
    try:
        info = Users.query.all()
    except:
        flash('Произошла ошибка чтения БД!', category='alert-danger')
    return render_template('admin/admin.html', title='Админка', menu=adminMenu, list=info)


@app.route("/logout")
def logout():
    logout_user()
    return redirect('/')


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('shop/page404.html', title='Страница не найдена!', menu=menu), 404


if __name__ == "__main__":
    app.run(debug=True)
