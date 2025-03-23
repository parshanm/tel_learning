from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup
from config import API_Key

bot = TeleBot(API_Key)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
keyboard.add('Button1', 'Button2')

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'welcome to my bot.', reply_markup=keyboard)

# keyboard handler
@bot.message_handler(func=lambda message:True)
def handler(message):
    if message.text == 'Button1':
        bot.send_message(message.chat.id, 'You clicked Button1')
    elif message.text == 'Button2':
        bot.send_message(message.chat.id, 'You clicked Button2')
    else:
        bot.send_message(message.chat.id, message.text)

bot.polling()
