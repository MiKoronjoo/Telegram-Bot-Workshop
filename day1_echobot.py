from pyrogram import Client
from pyrogram.types import Message

api_id = 0
api_hash = ''
bot_token = ''

client = Client(session_name='mybot', bot_token=bot_token, api_id=api_id, api_hash=api_hash)


@client.on_message()
def handle_message(bot: Client, message: Message):
    user_id = message.from_user.id
    if message.text:
        bot.send_message(user_id, message.text)
    elif message.voice:
        print(message.voice)
        # bot.send_voice(user_id, message.voice)


client.run()
