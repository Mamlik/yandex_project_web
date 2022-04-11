import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Trick(SqlAlchemyBase):
    __tablename__ = 'tricks_data'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    spot_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("spot_list.id"))
    spot = orm.relation('Spot')
    trick_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    trick_score = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    trick_img = sqlalchemy.Column(sqlalchemy.BLOB, nullable=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"), nullable=False)
    user = orm.relation('User')