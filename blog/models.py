# coding=utf-8

from __future__ import unicode_literals
import datetime


from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    DateTime,
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)
from zope.sqlalchemy import ZopeTransactionExtension
from passlib.apps import custom_app_context as blogger_pwd_context

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class User(Base):
    """Create user class for registration and login."""

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(Unicode(255), unique=True, nullable=False)
    password = Column(Unicode(255), nullable=False)
    last_logged = Column(DateTime, default=datetime.datetime.utcnow)

    def verify_password(self, password):
        """Verify that given cleartext matches stored hashed password."""
        if password == self.password:
            self.set_password(password)

        return blogger_pwd_context.verify(password, self.password)

    def set_password(self, password):
        """Hash provided password to compare to user provided value later."""
        self.password = blogger_pwd_context.encrypt(password)
