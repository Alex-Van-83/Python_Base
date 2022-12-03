"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)

from sqlalchemy.orm import (
    sessionmaker,
    relationship,
    declarative_base,
    scoped_session,
    declared_attr,
)

from sqlalchemy import (
    Column,
    String,
    Boolean,
    Integer, ForeignKey,
)
import os


class Base:
    id = Column(Integer, primary_key=True)


class User(Base):
    name = Column(String(20), nullable=False)
    username = Column(String(20), nullable=False)
    email = Column(String(20), nullable=False)
    posts = relationship("Post", back_populates="user", uselist=True)
    __tablename__ = "users",


class Post(Base):
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    title = Column(String(20), nullable=False)
    body = Column(String(20), nullable=False)
    author = relationship("User", back_populates="post", uselist=False)
    __tablename__ = "posts",


PG_CONN_URI = "postgresql+asyncpg://username:passwd!@localhost/blog"

engine = create_async_engine(url=PG_CONN_URI)
session_factory = sessionmaker(engine, class_=AsyncSession)

Base = declarative_base(bind=engine, cls=Base)
Session = scoped_session(session_factory)


def main():
    Base.metadata.create_all()


if __name__=='__main__':
    main()