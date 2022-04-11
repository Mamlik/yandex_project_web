import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Spot(SqlAlchemyBase):
    __tablename__ = 'spot_list'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    spot_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    spot_location = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    spot_picture = sqlalchemy.Column(sqlalchemy.BLOB, nullable=True)
    spot_cords = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    trick = orm.relation("Trick", back_populates='spot')