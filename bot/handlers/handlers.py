from aiogram import Router
from aiogram.types import Message
from aiogram.types import WebAppInfo
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import WEB_APP_URL


router = Router()


@router.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer(
        "Привет! Это бот для запуска игры 'Змейка'. Для запуска игры используйте коману '/play'")


@router.message(Command("play"))
async def send_welcome(message: Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="Начать игру", web_app=WebAppInfo(url=WEB_APP_URL))

    await message.answer(
        "Нажмите на кнопку ниже, чтобы начать игру.",
        reply_markup=builder.as_markup(),
        resize_keyboard=True,
        one_time_keyboard=True,
    )
