from aiogram.fsm.state import StatesGroup, State


class CurrencyStates(StatesGroup):
    waiting_for_click = State()
    waiting_for_sum = State()
    convert_from = State()
    convert_to = State()
    currency_pair = State()


class FileStates(StatesGroup):
    waiting_for_file = State()
    converting = State()
