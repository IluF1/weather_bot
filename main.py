from aiogram import Bot, Dispatcher
from config import TOKEN
from app.handlers import router
import asyncio

dp = Dispatcher()
bot = Bot(token = TOKEN)


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())