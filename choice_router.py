from aiogram import Router, F, types
from aiogram.types import CallbackQuery

from handlers import convert
from keyboards import inline_keyboard

router = Router()

test_dict = {}


@router.message(F.document)
async def convert_choice(message: types.Message):
    key = message.chat.id
    global test_dict
    test_dict[key] = [message.document.file_id, message.document.file_name]
    if message.document.file_name.endswith(".docx"):
        await message.answer("We have got your file. Please choose "
                             "the format to convert", reply_markup=await inline_keyboard(key, 'docx'))
    if message.document.file_name.endswith(".pdf"):
        await message.answer("We have got your file. Please choose "
                             "the format to convert", reply_markup=await inline_keyboard(key, 'pdf'))
    if message.document.file_name.endswith(".doc"):
        await message.answer("We have got your file. Please choose "
                             "the format to convert", reply_markup=await inline_keyboard(key, 'doc'))
    if message.document.file_name.endswith(".txt"):
        await message.answer("We have got your file. Please choose "
                             "the format to convert", reply_markup=await inline_keyboard(key, 'txt'))
    if message.document.file_name.endswith(".pages"):
        await message.answer("We have got your file. Please choose "
                             "the format to convert", reply_markup=await inline_keyboard(key, 'pages'))


@router.callback_query(F.data.contains)
async def docx_to_pdf(call: CallbackQuery):
    await call.answer()
    global test_dict
    data = call.data.split()
    convert_to = data[0].split('_')
    convert_to = convert_to[2]
    key = int(data[1])
    file_id = test_dict[key][0]
    name = test_dict[key][1]
    await convert(call.message, convert_to, file_id, name)
