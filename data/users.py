import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    login = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    sex = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    adress = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    cords = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    bio = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    avatar = sqlalchemy.Column(sqlalchemy.BLOB, nullable=True)
    score = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    is_admin = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)
    tricks_data = orm.relation("Trick", back_populates='user')
