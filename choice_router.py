from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from file_handlers import convert
from keyboards import inline_keyboard
from states import FileStates

router = Router()

answer = "We have got your file. Please choose the format to convert"


@router.message(F.document)
async def convert_choice(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == FileStates.waiting_for_file:
        await state.update_data(waiting_for_file=[message.document.file_id, message.document.file_name])
        if message.document.file_name.endswith(".docx"):
            await message.answer(answer, reply_markup=await inline_keyboard('docx'))
        elif message.document.file_name.endswith(".pdf"):
            await message.answer(answer, reply_markup=await inline_keyboard('pdf'))
        elif message.document.file_name.endswith(".doc"):
            await message.answer(answer, reply_markup=await inline_keyboard('doc'))
        elif message.document.file_name.endswith(".txt"):
            await message.answer(answer, reply_markup=await inline_keyboard('txt'))
        elif message.document.file_name.endswith(".pages"):
            await message.answer(answer, reply_markup=await inline_keyboard('pages'))
        await state.set_state(FileStates.converting)


@router.callback_query(F.data.contains)
async def conversion(call: CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state == FileStates.converting:
        await call.answer()
        state_data = await state.get_data()
        file_data = state_data['waiting_for_file']
        file_id = file_data[0]
        file_name = file_data[1]
        data = call.data.split()
        convert_to = data[0].split('_')
        convert_to_ext = convert_to[2]
        await convert(call.message, convert_to_ext, file_id, file_name)
        await state.clear()
