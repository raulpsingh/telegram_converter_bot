from aiogram import Bot, Dispatcher
import asyncio
from start_handler import router as router_callbacks
from choice_router import router as router_choice
from currency_handlers import router as router_currency
from file_handlers import router as router_file
import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


async def main():
    print("Bot is running...")
    dp.include_routers(router_callbacks,  router_file,router_currency, router_choice)
    await dp.start_polling(bot)


asyncio.run(main())
