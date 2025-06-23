from src.db import Session
from src.models.user import User


def get_users():
    with Session() as session:
        users = session.query(User).all()
        return users


def get_user(user_id):
    with Session() as session:
        user = session.query(User).get(user_id)
        return user


def add_user(user_data):
    with Session() as session:
        book = User(
            name=user_data.get("name"),
            email=user_data.get("email"),
            role=user_data.get("role"),
        )
        session.add(book)
        session.commit()
        session.refresh(book)
        return book


def remove_user(user_id):
    with Session() as session:
        user = get_user(user_id)
        session.delete(user)
        session.commit()
        return user
