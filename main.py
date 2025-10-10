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
FLAG = False


# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет, я ЦезарьБот.
Я здесь, чтобы зашифровать или расшифровать ваше сообщение. Просто напишите что-нибудь и я зашифрую ваше сообщение!\
""")


# Handle '/help'
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, """\
- напиши текст и я его зашифрую;\n- напиши зашифрованный текст и его расшифрую.\
""")


# Handle '/encode'
@bot.message_handler(commands=['encode'])
def com_encode(message):
    global FLAG
    FLAG = True
    bot.reply_to("Напишите текст, котрый вы хотите зашифровать:")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(content_types=["text"])
def encoded_message(massage):
    global FLAG
    if FLAG:
        list_message = list(message.text.lower())
        if list_message[0] in e_letters:
            list_message = [e_letters[int(e_letters.index(x) + 3) % len(e_letters)] if x in list_message else x for x in list_message]
        elif list_message[0] in r_letters:
            list_message = [e_letters[int(e_letters.index(x) + 3) % len(e_letters)] if x in list_message else x for x in list_message]
    
        message1 = ''.join(list_message)
        bot.reply_to(massage, message1.text)
        FLAG = False
    else:
        bot.reply_to(message, message.text)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)


bot.infinity_polling()
