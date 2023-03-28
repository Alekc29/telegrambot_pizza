from aiogram.utils import executor

from create_bot import dp
from handlers import admin, client, other
from data_base import sqlite_db


async def on_startup(_):
    print('Бот запущен')
    sqlite_db.sql_start()

admin.register_handlers_admin(dp)
client.register_handlers_client(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, # игнорировать сообщения офлайн
                       on_startup=on_startup) # функция запуска бота