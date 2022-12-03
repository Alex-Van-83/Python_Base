"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
import aiohttp


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def get_data(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        data = await response.json()
        return data


def get_users():
    return asyncio.run(get_data(USERS_DATA_URL))


def get_posts():
    return asyncio.run(get_data(POSTS_DATA_URL))







