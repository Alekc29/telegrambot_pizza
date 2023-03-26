import json, string

from aiogram import Dispatcher, types

from create_bot import dp


# @dp.message_handler()
async def echo_send(message: types.Message):
    if {word.lower().translate(
            str.maketrans('', '', string.punctuation)
        ) for word in message.text.split(' ')}.intersection(
            set(json.load(open('cenz.json')))
        ) != set():
        await message.reply('Маты запрещены!')
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)