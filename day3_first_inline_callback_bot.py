from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQuery, \
    InlineQueryResultArticle, InputTextMessageContent


def IKM(data):
    return InlineKeyboardMarkup([[InlineKeyboardButton(text, cbd)] for text, cbd in data])


client = Client('mybot')


@client.on_callback_query()
def handle_callback_query(bot: Client, query: CallbackQuery):
    if query.data == 'start':
        bot.edit_inline_text(query.inline_message_id, 'توضیحات بازی', reply_markup=IKM([('پایان', 'end')]))
    elif query.data == 'end':
        bot.edit_inline_text(query.inline_message_id, 'بازی تمام شد!!')


@client.on_inline_query()
def handle_inline_query(bot: Client, query: InlineQuery):
    results = [InlineQueryResultArticle('شروع بازی جدید', InputTextMessageContent('متن بلند'),
                                        reply_markup=IKM([('قبول بازی!', 'start')]))]
    bot.answer_inline_query(query.id, results)


client.run()
