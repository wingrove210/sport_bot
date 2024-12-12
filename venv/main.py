from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from aiogram import F
import asyncio

# Вставьте ваш токен от BotFather
BOT_TOKEN = "7863678094:AAG_MYJuot-l5xFZ90dNSgAL7x2obRds9N8"

# Создаем экземпляр бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()

# Обработчик команды /start
@router.message(F.text == "/start")
async def send_welcome(message: Message):
    await message.answer("Привет!")

# Регистрация роутера
dp.include_router(router)

async def main():
    # Настройка диспетчера и запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
