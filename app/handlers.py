from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import app.keyboard as kb


router = Router()
class UserCity(StatesGroup):
    city = State()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Нажмите на кнопку ниже, для того чтобы узнать погоду или введите команду /weather", reply_markup = kb.start_kb)

@router.message(Command('weather'))
@router.message(F.text == 'Погода')
async def weather_handler(message: Message, state: FSMContext):
    await state.set_state(UserCity.city)
    await message.answer('Введите желаемый город, для просмотра погоды в нем:')
    
@router.message(UserCity.city)
async def set_city(message: Message, state: FSMContext):
    await state.update_data(city = message.text)
    await state.clear()
    
    
    