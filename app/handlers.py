from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
import app.keyboard as kb

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}", reply_markup = kb.start_kb)