from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from handlers import convert
from keyboards import inline_keyboard
from handlers import FileWaiter
router = Router()

test_dict = {}

answer = "We have got your file. Please choose the format to convert"


@router.message(F.document)
async def convert_choice(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == FileWaiter.waiting_for_file:
        key = message.chat.id
        global test_dict
        test_dict[key] = [message.document.file_id, message.document.file_name]
        if message.document.file_name.endswith(".docx"):
            await message.answer(answer, reply_markup=await inline_keyboard(key, 'docx'))
        if message.document.file_name.endswith(".pdf"):
            await message.answer(answer, reply_markup=await inline_keyboard(key, 'pdf'))
        if message.document.file_name.endswith(".doc"):
            await message.answer(answer, reply_markup=await inline_keyboard(key, 'doc'))
        if message.document.file_name.endswith(".txt"):
            await message.answer(answer, reply_markup=await inline_keyboard(key, 'txt'))
        if message.document.file_name.endswith(".pages"):
            await message.answer(answer, reply_markup=await inline_keyboard(key, 'pages'))
        await state.clear()


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
