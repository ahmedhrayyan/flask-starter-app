from datetime import datetime
from database import db
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import DateTime, func
from sqlalchemy.exc import SQLAlchemyError


class Base(db.Model):
    """ Helper class witch adds basic methods & columns to sub models """
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now())

    def update(self, **kwargs):
        """ update element in db  """

        # update fields using python dict
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

        try:
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    def delete(self):
        """ delete item from db """
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    def insert(self):
        """ insert item into db """
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

class User(Base):
    __tablename__ = 'users'
    name: Mapped[str]
    age: Mapped[int]