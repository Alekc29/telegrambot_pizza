import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)