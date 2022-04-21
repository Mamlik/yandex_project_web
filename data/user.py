import datetime
import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    lat = sqlalchemy.Column(sqlalchemy.REAL, nullable=True)
    lon = sqlalchemy.Column(sqlalchemy.REAL, nullable=True)
    spots = orm.relation("Spot", back_populates='user')