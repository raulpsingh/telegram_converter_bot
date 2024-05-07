
from aiogram.types import InlineKeyboardButton

from aiogram.utils.keyboard import InlineKeyboardBuilder

list1 = ()
list2 = ()

start_keyboard = ('Convert files', 'Convert currencies')
start_keyboard_callback = ('convert_files', 'convert_currency')

docx_keyboard = ('to PDF', 'to DOC', 'to TXT', 'to Pages')
docx_keyboard_callback = ('docx_to_pdf', 'docx_to_doc', 'docx_to_txt', "docx_to_pages")

doc_keyboard = ('to PDF', 'to DOCX', 'to TXT', 'to Pages')
doc_keyboard_callback = ('doc_to_pdf', 'doc_to_docx', 'doc_to_txt', "doc_to_pages")

pdf_keyboard = ('to DOCX',)
pdf_keyboard_callback = ('pdf_to_docx',)

txt_keyboard = ('to PDF', 'to DOCX', 'to DOC', 'to Pages')
txt_keyboard_callback = ('txt_to_pdf', 'txt_to_docx', 'txt_to_doc', "txt_to_pages")

pages_keyboard = ('to PDF', 'to DOCX', 'to DOC', 'to TXT')
pages_keyboard_callback = ('pages_to_pdf', 'pages_to_docx', 'pages_to_doc', "pages_to_txt")

currency_keyboard = ('USD/EUR', 'EUR/USD', 'EUR/GBP', 'GBP/EUR', 'Else')
currency_keyboard_callback = ('usd/eur', 'eur/usd', 'eur/gbp', 'gbp/eur', 'else')


async def inline_keyboard(key, type_of_file):
    global list1, list2
    keyboard = InlineKeyboardBuilder()
    if type_of_file == 'start':
        list1 = start_keyboard
        list2 = start_keyboard_callback
        for a, b in zip(list1, list2):
            keyboard.add(InlineKeyboardButton(text=a, callback_data=b))
        return keyboard.as_markup()
    else:
        if type_of_file == 'docx':
            list1 = docx_keyboard
            list2 = docx_keyboard_callback
        if type_of_file == 'pdf':
            list1 = pdf_keyboard
            list2 = pdf_keyboard_callback
        if type_of_file == 'doc':
            list1 = doc_keyboard
            list2 = docx_keyboard_callback
        if type_of_file == 'txt':
            list1 = txt_keyboard
            list2 = txt_keyboard_callback
        if type_of_file == 'pages':
            list1 = pages_keyboard
            list2 = pages_keyboard_callback
        if type_of_file == 'currency':
            list1 = currency_keyboard
            list2 = currency_keyboard_callback
        if type_of_file == 'start':
            list1 = start_keyboard
            list2 = start_keyboard_callback
        for a, b in zip(list1, list2):
            keyboard.add(InlineKeyboardButton(text=a, callback_data=b + " " + str(key)))
        return keyboard.as_markup()


