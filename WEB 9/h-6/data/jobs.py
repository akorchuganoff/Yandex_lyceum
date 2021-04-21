import sqlalchemy
import datetime
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin


class Jobs(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    job = sqlalchemy.Column(sqlalchemy.String)
    work_size = sqlalchemy.Column(sqlalchemy.Integer)
    collaborators = sqlalchemy.Column(sqlalchemy.String)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, default=None, nullable=True)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime, default=None, nullable=True)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean)

    user = orm.relation('User')

    def __repr__(self):
        return f'<Job> {self.job}'