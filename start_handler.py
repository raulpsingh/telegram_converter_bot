from aiogram import types, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
import keyboards
from states import CurrencyStates

router = Router()


@router.message(CommandStart())
async def start(message: types.Message, state: FSMContext):
    await state.set_state(CurrencyStates.waiting_for_click)
    await message.answer("Hello, this is a friendly bot "
                         "that will help you to convert your files and currencies. You can select "
                         "below what type "
                         "of conversion do you want", reply_markup=await keyboards.inline_keyboard('start'))



