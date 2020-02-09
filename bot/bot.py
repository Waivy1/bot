import os
import telebot


bot = telebot.TeleBot(os.environ.get('BOT_API_TOKEN'))

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hi, you've entered /start command")

bot.polling()
