from aiogram import executor

from loader import dp, cr
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)

    cr.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            first_name TEXT,
            last_name TEXT
        )
    ''')

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

