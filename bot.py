import os
from balethon import Client
from balethon.objects.chat import Chat
from balethon.objects.message import Message

from BeautifulRequest import *

DATA_CHAT_ID = 5117523172
bot = Client(os.environ.get('BOT_TOKEN'))
chat_ids = []


async def save_chat(chat: Chat) -> None:
    if chat.id not in chat_ids:
        await bot.send_message(DATA_CHAT_ID, f'{chat.id}')
        chat_ids.append(chat.id)


@bot.on_message()
async def greet(message: Message):
    if message.text.lower() == 'ping':
        await message.reply("Pong")
    if is_request(message.text):
        request_dict: dict = convert_request_to_dict(message.text)
        await message.reply(json.dumps(request_dict, ensure_ascii=False, indent=4))
    if message.text.isnumeric():
        await message.reply(f'{int(message.text) + 1}')

    # await save_chat(message.chat)

bot.run()
