from pyrogram import Client
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent


client = Client('ramin')


def dec(ss):
    return ''.join(map(lambda x: chr(int(x)), ss.split()))


def enc(ss):
    return ' '.join(str(ord(c)).rjust(3, '0') for c in ss)


@client.on_inline_query()
def handle_inline_query(bot: Client, query: InlineQuery):
    if not query.query:
        return
    if query.query.replace(' ', '').isdigit():
        res = [
            InlineQueryResultArticle('DECODE', InputTextMessageContent(dec(query.query)), 'dec'),
            InlineQueryResultArticle('ENCODE', InputTextMessageContent(enc(query.query)), 'enc'),
        ]
        bot.answer_inline_query(query.id, res)
    else:
        res = [InlineQueryResultArticle('ENCODE', InputTextMessageContent(enc(query.query)), 'enc')]
        bot.answer_inline_query(query.id, res)


client.run()
