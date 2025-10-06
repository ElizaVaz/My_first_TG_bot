#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
import config
import letters

API_TOKEN = config.token
bot = telebot.TeleBot(API_TOKEN)
e_letters = letters.e_letters
r_letters = letters.r_letters


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет, я ЭхоБот.
Я здесь, чтобы ответить вам тем же. Просто скажите что-нибудь приятное, и я отвечу вам тем же!\
""")


# 
@bot.message_handler(commands=['encode'])
def encoded_message(message, n=1):

    list_message = list(message.text.lower())
    if list_message[0] in e_letters:
        list_message = [e_letters[int(e_letters.index(x) + n) % len(e_letters)] if x in list_message else x for x in list_message]
    elif list_message[0] in r_letters:
        list_message = [e_letters[int(e_letters.index(x) + n) % len(e_letters)] if x in list_message else x for x in list_message]
    
    message1 = ''.join(list_message)
    bot.reply_to(message, message1.text)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)


bot.infinity_polling()
