from aiogram import types

start_kb = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text='Convert files', callback_data='convert_files'),
            types.InlineKeyboardButton(text='Convert currencies', callback_data='convert_currency')
        ]
    ]
)
docx_kb = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text='to PDF', callback_data='docx_to_pdf'),
            types.InlineKeyboardButton(text='to DOC', callback_data='docx_to_doc'),
            types.InlineKeyboardButton(text='to TXT', callback_data='docx_to_txt'),
            types.InlineKeyboardButton(text='to Pages', callback_data='docx_to_pages')
        ]
    ]
)