from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
  pass


db = None


def get_database(app = None):
    global db
    if db is None:
        if app is None:
            raise ValueError("app must be provided on first call to get_database")

        db = SQLAlchemy(app, model_class=Base)

    return db