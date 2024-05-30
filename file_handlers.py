import os
from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext
import convert_files_api
from convert_files_api import download_file
from states import FileStates

router = Router()


@router.callback_query(F.data == 'convert_files')
async def convert_files(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(FileStates.waiting_for_file)
    await call.answer()
    await call.message.answer("Let's convert your files. Please send me a PDF, DOC, DOCX file "
                              "and choose the format to convert.")


async def convert(message: types.Message, convert_to, file_id, file_name):
    await message.answer("Please wait a few seconds before we send you a converted document")
    file_name = file_name
    await download_file(message, file_id, file_name)
    to_convert = convert_files_api.ConvertFilesApi(file_name, convert_to)
    converted = to_convert.convert()
    await message.reply_document(document=types.FSInputFile(path=f'./converted_files/{converted}'))
    os.remove(f'./converted_files/{converted}')
