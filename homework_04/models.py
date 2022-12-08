"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import asyncio

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
    Integer,
    ForeignKey,
)


class Base():
    id = Column(Integer, primary_key=True)
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"


PG_CONN_URI = "postgresql+asyncpg://username:passwd!@localhost/blog"
engine = create_async_engine(url=PG_CONN_URI, echo=False)
Base = declarative_base(bind=engine, cls=Base)
session_factory = sessionmaker(engine, class_=AsyncSession, expire_on_commit=True)
Session = scoped_session(session_factory)


class User(Base):
    name = Column(String(256), nullable=False)
    username = Column(String(256), nullable=False)
    email = Column(String(256), nullable=True)
    posts = relationship("Post", back_populates="user", uselist=True)


class Post(Base):
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(512), nullable=False)
    body = Column(String(1024), nullable=False)
    user = relationship("User", back_populates="posts", uselist=False)


async def create_user(session: AsyncSession, new_user) -> User:
    user = User(id=new_user['id'],
                name=new_user['name'],
                username=new_user['username'],
                email=new_user['email']
                )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def create_post(session: AsyncSession, new_post) -> Post:
    post = Post(id=new_post['id'],
                user_id=new_post['userId'],
                title=new_post['title'],
                body=new_post['body']
                )
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post


async def create_users(session, users):
    for user in users:
        await create_user(session, user)
    return session


async def create_posts(session, posts):
    for post in posts:
        await create_post(session, post)
    return session



async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
