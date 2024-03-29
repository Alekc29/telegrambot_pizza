from aiogram import Dispatcher, types
from aiogram.types import ReplyKeyboardRemove

from create_bot import bot, dp
from data_base import sqlite_db
from keyboards import kb_client

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,
                           'Привет! я бот для пиццерии.',
                           reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply(
            'Общение с ботом через ЛС, напишите ему:\nhttps://t.me/KittytwittyBot'
        )


# @dp.message_handler(commands=['Режим работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00.')
    

# @dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Ул. Колбасная 17.')


# @dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])