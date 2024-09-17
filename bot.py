import json
import os

from balethon import Client
from balethon.objects.message import Message

from BeautifulJWT import BeautifulJWT
from BeautifulRequest import is_request, convert_request_to_dict
from BeautifulTime import BeautifulTime
from LiaraApi import LiaraApi

bot = Client(os.environ.get('BOT_TOKEN'))
releases_count = LiaraApi.get_current_releases().get('total')


@bot.on_message()
async def greet(message: Message):
    if message.text.lower() == 'ping':
        await message.reply("Pong")
        return None

    if BeautifulTime.is_now_command(message.text):
        await message.reply(BeautifulTime.get_readable_now())
        return None

    if is_request(message.text):
        request_dict: dict = convert_request_to_dict(message.text)
        await message.reply(json.dumps(request_dict, ensure_ascii=False, indent=4))
        return None

    if BeautifulJWT.is_jwt_token(message.text):
        await message.reply(BeautifulJWT.create_readable_jwt(message.text))
        return None

    if BeautifulTime.is_unix_time(message.text):
        unix_time = int(message.text)
        await message.reply(BeautifulTime.create_readable_time(unix_time))
        return None

    if message.text.isnumeric():
        await message.reply(f'{int(message.text) + releases_count}')
        return None

    if LiaraApi.is_release_command(message.text):
        releases: dict = LiaraApi.get_current_releases()
        await message.reply(json.dumps(releases, ensure_ascii=False, indent=4))
        return None


bot.run()
