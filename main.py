# - *- coding: utf -8 - *-
import telebot

bot = telebot.TeleBot("801959899:AAFMdgRhIra49udqIgC2lvEqI5WtW_3y3jQ")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Welcome to the translator bot! Change your language in the Setting.")

@bot.message_handler(func=lambda message: True)
def translate_message(message):
    bot.send_message(message.chat.id, message.text)
    
print("yes")
bot.polling()









