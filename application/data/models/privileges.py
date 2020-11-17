from sqlalchemy.orm import relationship

from data.db import Base
import sqlalchemy as sa





class Privilege(Base):
    __tablename__ = 'privileges'

    priv_id = sa.Column(sa.Integer, primary_key=True)
    priv_name  = sa.Column(sa.String(50), nullable=False)
    users = relationship('User', back_populates='privilege')

    def __repr__(self):
        return f"{self.priv_name}, {self.users}"