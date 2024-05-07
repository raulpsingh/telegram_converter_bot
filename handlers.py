import os
from aiogram import types, F, Router
from aiogram.filters import CommandStart

import convert_files_api
import keyboards

router = Router()


@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Hello, this is a friendly bot "
                         "that will help you to convert your files and currencies. You can select "
                         "below what type "
                         "of conversion do you want", reply_markup=await keyboards.inline_keyboard(message.chat.id,
                                                                                                   'start'))


@router.callback_query(F.data == 'convert_files')
async def convert_files(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer("Let's convert your files. Please send me a PDF, DOC, DOCX file "
                              "and choose the format to convert.")


@router.callback_query(F.data == "convert_currency")
async def callback_query(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer("Let's convert your currencies. Please enter the sum")


async def download_file(message: types.Message, document_id, file_name):
    file_name = file_name
    file_id = document_id
    bot = message.bot
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, f'./files_to_convert/{file_name}')


async def convert(message: types.Message, convert_to, file_id, file_name):
    await message.answer("Please wait a few seconds before we send you a converted document")
    file_name = file_name
    await download_file(message, file_id, file_name)
    to_convert = convert_files_api.ConvertFilesApi(file_name, convert_to)
    converted = to_convert.convert()
    await message.reply_document(document=types.FSInputFile(path=f'./converted_files/{converted}'))
    os.remove(f'./converted_files/{converted}')
