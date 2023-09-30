from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, cr, connect

@dp.message_handler(commands='add_user')
async def add_user(msg: types.Message):
    cr.execute('INSERT INTO users (username, first_name, last_name) VALUES (?, ?, ?)', (msg.from_user.username, msg.from_user.first_name, msg.from_user.last_name))
    connect.commit()
    if msg.from_user.last_name != None:
        await msg.answer(f'Супер! Користувача @{msg.from_user.username} - {msg.from_user.first_name} {msg.from_user.last_name} додано')
    else:
        await msg.answer(f'Супер! Користувача @{msg.from_user.username} - {msg.from_user.first_name} додано')



@dp.message_handler(commands='get_users')
async def get_users(msg: types.Message):
    cr.execute('SELECT * FROM users')
    for row in cr.fetchall():
        row = str(row)
        user_data = row.split(', ')
        if user_data[3][:-1:] != 'None':
            await msg.answer(f'@{user_data[1][1:-1:]} - {user_data[2][1:-1:]} {user_data[3][:-1:]}')
        else:
            await msg.answer(f'@{user_data[1][1:-1:]} - {user_data[2][1:-1:]}')
            await msg.answer('Немає інформації про прізвище користувача')