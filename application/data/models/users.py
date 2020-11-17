import json

from sqlalchemy.orm import relationship

from data.db import Base, engine
import sqlalchemy as sa
from data.models.privileges import Privilege


class User(Base):
    __tablename__ = 'users'

    user_id = sa.Column(sa.Integer, primary_key=True)
    user_name = sa.Column(sa.String(50), nullable=False)
    user_first_name = sa.Column(sa.String(50), nullable=False)
    user_last_name = sa.Column(sa.String(50), nullable=False)
    user_age = sa.Column(sa.Integer)
    priv_id = sa.Column(sa.Integer, sa.ForeignKey('privileges.priv_id'))
    privilege = relationship('Privilege', back_populates='users')

    def __repr__(self):
        return f"User({self.user_id}, {self.user_name}, {self.user_first_name}, {self.user_last_name}, {self.privilege})"

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'user_first_name': self.user_first_name,
            'user_last_name': self.user_last_name,
            'user_age': self.user_age,
            'priv': self.privilege.priv_name
        }




def main():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()