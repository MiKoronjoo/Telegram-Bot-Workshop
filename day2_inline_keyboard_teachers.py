from pyrogram import Client
from pyrogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton, CallbackQuery


def IKM(data):
    return InlineKeyboardMarkup([[InlineKeyboardButton(text, cbd)] for text, cbd in data])


client = Client('mybot')
data = []
MAIN_KEYBOARD = ReplyKeyboardMarkup([['set name', 'set age'], ['my profile']], resize_keyboard=True)
TEACHERS_INLINEKB = IKM([('Dr Keshtkaran', 'TCH0'), ('Dr Hamze', 'TCH1'), ('Dr Sami', 'TCH2')])


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
            bot.send_message(user.id, 'welcome', reply_markup=TEACHERS_INLINEKB)


teachers = ['دکتر کشتکاران', 'دکتر حمزه', 'دکتر سامی']


@client.on_callback_query()
def handle_callback_query(bot: Client, query: CallbackQuery):
    if query.data.startswith('TCH'):
        i = int(query.data[3:])
        bot.edit_message_text(query.message.chat.id, query.message.message_id, teachers[i],
                              reply_markup=TEACHERS_INLINEKB)


client.run()
