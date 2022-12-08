"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from jsonplaceholder_requests import (
    get_users,
    get_posts,
)
from models import (init_models,
                    create_users,
                    create_posts,
                    session_factory,
                    scoped_session,
)


async def async_main():
    users, posts = await asyncio.gather(get_users(), get_posts())
    await init_models()
    users_session, posts_session = await asyncio.gather(create_users(scoped_session(session_factory), users),
                                                        create_posts(scoped_session(session_factory), posts),
                                                        )
    await users_session.close()
    await posts_session.close()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
