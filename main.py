import os

from aiogram import Bot, Dispatcher, types, F
import asyncio

from callbacks import router
from aiogram.filters import CommandStart

import config

import convert_files_api
import keyboards

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


async def convert(message: types.Message, convert_to):
    await message.answer("Please wait a few seconds before we send you a converted document")
    file_name = message.document.file_name
    await download_file(message)
    to_convert = convert_files_api.ConvertFilesApi(file_name, convert_to)
    converted = to_convert.convert()
    await message.reply_document(document=types.FSInputFile(path=f'./converted_files/{converted}'))
    os.remove(f'./converted_files/{converted}')


async def download_file(message: types.Message):
    file_name = message.document.file_name
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, f'./files_to_convert/{file_name}')


@router.message(F.document)
async def convert_choice(message: types.Message):
    if message.document.file_name.endswith(".docx"):
        await message.answer("We have got your file. Please choose "
                             "the format to convert", reply_markup=keyboards.docx_kb)
        await convert(message, "pdf")
    if message.document.file_name.endswith(".pdf"):
        await convert(message, "docx")


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


asyncio.run(main())
