from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from app.server.api import get_weather as api
import app.keyboard as kb


router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Нажмите на кнопку ниже, для того чтобы узнать погоду или введите команду /weather", reply_markup = kb.start_kb)

@router.message(Command('weather'))
@router.message(F.text == 'Погода')
async def weather_handler(message: Message):
    await message.answer('Введите желаемый город, для просмотра погоды в нем:')
    
@router.message()
async def catch_city(message: Message):
    global user_city
    user_city = message.text
    temperature = api(user_city)
    await message.answer(f'Данные по погоде в {user_city}е:\n Температура равна {temperature}c')