from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустити бота"),
            types.BotCommand("help", "Отримати список команд"),
            types.BotCommand('add_user', 'Додати користувача'),
            types.BotCommand('get_users', 'Переглянути список всіх користувачів')
        ]
    )
