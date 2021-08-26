from pyrogram import Client
from pyrogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove


client = Client('mybot')
data = []
MAIN_KEYBOARD = ReplyKeyboardMarkup([['set name', 'set age'], ['my profile']], resize_keyboard=True)


class MyUser:
    def __init__(self, user_id):
        self.id = user_id
        self.state = 0
        self.name = None
        self.age = None


def check_user(user_id):
    for user in data:
        if user_id == user.id:
            return user
    new_user = MyUser(user_id)
    data.append(new_user)
    return new_user


@client.on_message()
def handle_message(bot: Client, message: Message):
    user = check_user(message.from_user.id)
    if message.chat.type != 'private':
        return
    if message.text:
        if message.text == '/start':
            user.state = 0
            bot.send_message(user.id, 'welcome', reply_markup=MAIN_KEYBOARD)
        elif user.state == 0 and message.text == 'set name':
            user.state = 1
            bot.send_message(user.id, 'enter your name:', reply_markup=ReplyKeyboardRemove())
        elif user.state == 0 and message.text == 'set age':
            user.state = 2
            bot.send_message(user.id, 'enter your age:', reply_markup=ReplyKeyboardRemove())
        elif user.state == 0 and message.text == 'my profile':
            bot.send_message(user.id, f'Name: {user.name}\nAge: {user.age}')
        elif user.state == 1:
            user.name = message.text
            user.state = 0
            bot.send_message(user.id, 'your name saved', reply_markup=MAIN_KEYBOARD)
        elif user.state == 2:
            user.age = message.text
            user.state = 0
            bot.send_message(user.id, 'your age saved', reply_markup=MAIN_KEYBOARD)


client.run()
