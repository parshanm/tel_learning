import telebot

bot = telebot.TeleBot('7896516364:AAGpiaoDKDvhqfHADJCpKc8jyHWFA7O7CDg')

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'happy birthday maman joonam')

bot.polling()
