from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


router = Router()
class user_city(StatesGroup):
    city = State()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Введите комманду /weather, для того чтобы посмотреть погоду")

@router.message(Command('weather'))
async def weather_handler(message: Message, state: FSMContext):
    await state.set_state(user_city.city)
    await message.answer('Введите город, для просмотра погоды в нем:')
    
@router.message(user_city.city)
async def set_city(message: Message, state: FSMContext):
    await state.update_data(city = message.text)
    await state.clear()