from data import db_session, tg_bot_api
from data.user import User
from data.spots import Spot
from flask import Flask
import flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


if __name__ == '__main__':
    db_session.global_init("data/tg_bot.db")
    user = User()
    user.id = 1488
    user.name = 'alexfriedman'
    user.age = 16
    user.lat = 0.11
    user.lon = 0.11111
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    app.register_blueprint(tg_bot_api.blueprint)
    app.run()
