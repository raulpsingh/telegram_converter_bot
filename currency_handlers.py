from aiogram import types, F, Router

import keyboards
from convert_currencies_api import ConvertCurrenciesAPI
from states import CurrencyStates
from aiogram.fsm.context import FSMContext

router = Router()


@router.callback_query(F.data == "convert_currency")
async def callback_query(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(CurrencyStates.waiting_for_sum)
    await call.answer()
    await call.message.answer("Let's convert your currencies. Please enter the sum")


@router.message(F.text)
async def convert_sum(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == CurrencyStates.waiting_for_sum:
        amount = message.text.strip()
        if amount.isnumeric():
            amount = float(amount)
            await state.update_data(waiting_for_sum=amount)
            await message.answer("Now please choose from what currency to convert",
                                 reply_markup=await keyboards.inline_keyboard('currency'))
            await state.set_state(CurrencyStates.convert_from)
        else:
            await message.answer("Please enter a valid sum")
            await state.set_state(CurrencyStates.waiting_for_sum)

    elif current_state == CurrencyStates.currency_pair:
        try:
            amount = await state.get_data()
            conversion = ConvertCurrenciesAPI(amount['waiting_for_sum'], message.text)
            converted = conversion.convert_currencies()
            await message.answer(f"Yes, it is {converted}")
            await state.clear()
        except Exception:
            await message.answer("Please enter a valid pair")


@router.callback_query(F.data.in_(('usd', 'eur', 'gbp', 'else')))
async def convert_currency(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    current_state = await state.get_state()
    if current_state == CurrencyStates.convert_to:
        amount = await state.get_data()
        currencies = amount['convert_from'] + "/" + callback.data
        conversion = ConvertCurrenciesAPI(amount['waiting_for_sum'], currencies)
        converted = conversion.convert_currencies()
        await callback.message.answer(f"Yes, it is {converted}")
        await state.clear()
    elif callback.data == 'else':
        await state.set_state(CurrencyStates.currency_pair)
        await callback.message.answer("Input a pair of currencies using slash")
    else:
        await callback.message.answer("Now please choose what currency to convert to",
                                      reply_markup=await keyboards.inline_keyboard('currency'))
        await state.update_data(convert_from=callback.data.strip())
        await state.set_state(CurrencyStates.convert_to)
