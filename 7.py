from telebot import TeleBot
from config import API_Key
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
import sqlite3

bot = TeleBot(API_Key)

with sqlite3.connect('user.db') as connection:
    cursor = connection.cursor()
    create_table_query = """
        CREATE TABLE IF NOT EXISTS users(
            id integer primary key,
            first_name text,
            last_name text,
            phone_number text
            )
    """
    cursor.execute(create_table_query)

markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
Button = KeyboardButton(text='Share my info', request_contact=True)
markup.add(Button)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Welcome to my bot!', reply_markup=markup)

@bot.message_handler(content_types=['contact'])
def get_contact(message):
    # bot.send_message(message.chat.id, text=f'{message.contact}')
    # data base Save
    with sqlite3.connect('user.db') as connection:
        cursor = connection.cursor()
        insert_data_query = """
            INSERT INTO users(id, first_name, last_name, phone_number)
            VALUES (?, ?, ?, ?)
        """
        data = (
            message.contact.user_id,
            f'{message.contact.first_name}',
            f'{message.contact.last_name}',
            f'{message.contact.phone_number}',
        )
        cursor.execute(insert_data_query, data)

bot.polling()
