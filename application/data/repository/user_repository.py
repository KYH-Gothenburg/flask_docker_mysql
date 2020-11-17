from data.db import session
from data.models.users import User


def get_all_users():
    return session.query(User).all()

