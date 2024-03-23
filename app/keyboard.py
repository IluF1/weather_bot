from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_kb = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = "Поделиться геолокацией", request_location = True)]
], resize_keyboard = True)