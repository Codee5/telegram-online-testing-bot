import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from database import init_db
from keyboards import get_main_keyboard
from handlers import admin, student


async def main() -> None:
    """
    Основная асинхронная функция запуска бота.
    """
    bot = Bot(token=BOT_TOKEN)
    dispatcher = Dispatcher()

    dispatcher.include_router(admin.router)
    dispatcher.include_router(student.router)

    await init_db()

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
