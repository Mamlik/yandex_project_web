import flask
from flask import jsonify
from data import db_session
from data.user import User
from data.spots import Spot


blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/test')
def test():
    return "API test"


@blueprint.route('/users/select/all')
def select_all_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=('id', 'name', 'age', 'lat', 'lon'))
                 for item in users]
        }
    )


@blueprint.route('/users/select/<id_>/cords')
def select_one_user_cords_(id_):
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == id_)
    return jsonify(
        {
            'user':
                [item.to_dict(only=('lat', 'lon'))
                 for item in user]
        }
    )


@blueprint.route('/spots/select/all')
def select_all_spots():
    db_sess = db_session.create_session()
    spots = db_sess.query(Spot).all()
    return jsonify(
        {
            'spots':
                [item.to_dict(only=('id', 'user_id', 'name', 'lat', 'lon', 'photo', 'user'))
                 for item in spots]
        }
    )
