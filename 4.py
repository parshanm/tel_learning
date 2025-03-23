from telebot import TeleBot
from config import API_Key

bot = TeleBot(API_Key)

user_id = []

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Wellcome to my bot.')
    if message.chat.id not in user_id:
        user_id.append(message.chat.id)

@bot.message_handler(commands=['brodcast'])
def brodcast(message):
    bot.send_message(message.chat.id, 'what do you wantt to brodcast:')
    bot.register_next_step_handler(message, brodcasting)

def brodcasting(message):
    p = message.text
    for user in user_id:
        bot.send_message(user, p)

bot.polling()
