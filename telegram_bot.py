import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот запущен')

# клиентская часть
@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,
                           'Привет! я бот для пиццерии.')
        await message.delete()
    except:
        await message.reply(
            'Общение с ботом через ЛС, напишите ему:\nhttps://t.me/KittytwittyBot'
        )


@dp.message_handler(commands=['Режим работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00.')
    

@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Ул. Колбасная 17.')


@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(message.text)


executor.start_polling(dp, skip_updates=True, # игнорировать сообщения офлайн
                       on_startup=on_startup) # функция запуска бота