from aiogram.utils import executor

from create_bot import dp
from handlers import admin, client, other


async def on_startup(_):
    print('Бот запущен')

client.register_handlers_client(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, # игнорировать сообщения офлайн
                       on_startup=on_startup) # функция запуска бота