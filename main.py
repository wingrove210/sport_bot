from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram import F
import asyncio
import random

# Вставьте ваш токен от BotFather
BOT_TOKEN = "7863678094:AAG_MYJuot-l5xFZ90dNSgAL7x2obRds9N8"

# Создаем экземпляр бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()

# Списки с цитатами и упражнениями
QUOTES = [
    "Жизнь - это 10% того, что с нами происходит, и 90% того, как мы на это реагируем.",
    "Будь тем изменением, которое хочешь видеть в мире.",
    "Не останавливайся на достигнутом. Всё самое интересное впереди!"
]

EXERCISES = [
    "Сделайте 10 отжиманий.",
    "Сделайте 15 приседаний.",
    "Сделайте 30 секунд планки."
]

# Клавиатуры
quote_button = KeyboardButton(text="Получить цитату")
exercise_button = KeyboardButton(text="Получить упражнение")
completed_button = KeyboardButton(text="Выполнил")
not_completed_button = KeyboardButton(text="Не выполнил")

quote_keyboard = ReplyKeyboardMarkup(keyboard=[[quote_button]], resize_keyboard=True)
exercise_keyboard = ReplyKeyboardMarkup(keyboard=[[exercise_button]], resize_keyboard=True)
completion_keyboard = ReplyKeyboardMarkup(keyboard=[[completed_button, not_completed_button]], resize_keyboard=True)

# Обработчик команды /start
@router.message(F.text == "/start")
async def send_welcome(message: Message):
    await message.reply("Привет! Нажми на кнопку, чтобы получить вдохновение.", reply_markup=quote_keyboard)

# Обработчик кнопки "Получить цитату"
@router.message(F.text == "Получить цитату")
async def send_quote(message: Message):
    quote = random.choice(QUOTES)
    await message.answer(quote, reply_markup=exercise_keyboard)

# Обработчик кнопки "Получить упражнение"
@router.message(F.text == "Получить упражнение")
async def send_exercise(message: Message):
    exercise = random.choice(EXERCISES)
    await message.answer(exercise, reply_markup=completion_keyboard)

# Обработчик кнопки "Выполнил"
@router.message(F.text == "Выполнил")
async def send_completed(message: Message):
    await message.answer("Отличная работа! Продолжайте в том же духе!", reply_markup=quote_keyboard)

# Обработчик кнопки "Не выполнил"
@router.message(F.text == "Не выполнил")
async def send_not_completed(message: Message):
    await message.answer("Ничего страшного, главное — не сдавайтесь! Попробуйте ещё раз!", reply_markup=quote_keyboard)

# Регистрация роутера
dp.include_router(router)

async def main():
    # Настройка диспетчера и запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())