from telebot import TeleBot
from config import API_Key
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = TeleBot(API_Key)

btn1 = InlineKeyboardButton('Button1', callback_data='btn1')
btn2 = InlineKeyboardButton('Button2', callback_data='btn2')
mark_up = InlineKeyboardMarkup(row_width=1)
mark_up.add(btn1, btn2)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'this is a bot', reply_markup=mark_up)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.data == 'btn1':
        bot.answer_callback_query(call.id, 'Button1 clicked', show_alert=True)
    elif call.data == 'btn2':
        bot.answer_callback_query(call.id, 'button is tapped')

bot.polling()
