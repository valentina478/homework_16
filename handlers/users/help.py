from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
                "/start - Запустити бота",
                "/help - Отримати список команд",
                '/add_user - Додати користувача',
                '/get_users - Переглянути список всіх користувачів')
    
    await message.answer("\n".join(text))
