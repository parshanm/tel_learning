import telebot

bot = telebot.TeleBot('7896516364:AAGpiaoDKDvhqfHADJCpKc8jyHWFA7O7CDg')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello, Please enter your name.')
    bot.register_next_step_handler(message, process_name)

def process_name(message):
    name = message.text
    bot.send_message(message.chat.id, f'Hello, {name}\nHow old are you?')
    bot.register_next_step_handler(message, process_age)

def process_age(message):
    age = message.text
    bot.send_message(message.chat.id, f'You are {age}, years old\nThanks')

bot.polling()
