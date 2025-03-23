import telebot

bot = telebot.TeleBot('7896516364:AAGpiaoDKDvhqfHADJCpKc8jyHWFA7O7CDg')

@bot.message_handler(regexp='tas')
def find_serial(message):
    bot.reply_to(message, 'this message contain tas')

@bot.message_handler(content_types=['audio', 'document'])
def file_type(message):
    if message.audio:
        bot.reply_to(message, 'this is audio file')
    elif message.document:
        bot.reply_to(message, 'This is an document')

bot.polling()
