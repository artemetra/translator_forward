import telebot
from telebot import types
import config
import json
import datetime

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """so uhh yeah um h- i am uh h 👉👈👉👈 :((((""")

@bot.message_handler(commands=['_poc'])
def forward(message: types.Message):
    if not message.get('reply_to_message'):
        bot.reply_to(message, "Usage: reply to translator's message")
    else:
        if not message['reply_to_message']['from']['username'] == 'TgTranslatorBot':
            bot.reply_to(message, "Usage: reply to translator's message")
        else:
            pass
            # bot.forward_message('StuffTranslatorSays', 
            #                     )

@bot.message_handler(commands=['bruhh'])
def bruh(message: types.Message):
    print(f"new message at {datetime.datetime.now()}!")
    #print(message)
    

    #bot.reply_to(message, json.dumps(json.loads(str(message)), indent=4))

bot.polling()