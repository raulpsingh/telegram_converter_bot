import os

from aiogram import Bot, Dispatcher, types, F, Router
import asyncio

from aiogram.filters import CommandStart

import config

import convert_files_api
import keyboards

router = Router()


@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Hello, this is a friendly bot "
                         "that will help you to convert your files and currencies. You can select "
                         "below what type "
                         "of conversion do you want", reply_markup=keyboards.start_kb)


@router.callback_query(F.data == 'convert_files')
async def convert_files(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer("Let's convert your files. Please send me a PDF, DOC, DOCX, PNG, JPG or JPEG file "
                              "and choose the format to convert.")


@router.callback_query(F.data == "convert_currency")
async def callback_query(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer("Let's convert your currencies. Please enter the sum")
