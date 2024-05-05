from aiogram import Bot, Dispatcher, types, F
import asyncio
from handlers import router as router_callbacks
from choice_router import router as router_choice
import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


async def main():
    dp.include_routers(router_callbacks, router_choice)
    await dp.start_polling(bot)


asyncio.run(main())
