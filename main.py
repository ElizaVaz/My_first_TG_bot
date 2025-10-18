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

# @bot.message_handler(commands=['start'])
# def welcome(message):
#     chat_id = message.chat.id
#     keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button_support = telebot.types.KeyboardButton(text="Выберете команду")
#     button1 = telebot.types.KeyboaoardButton(text="/encode")
#     button3 = telebot.types.KeyboardButton(text="/decode")
#     keyboard.add(buttrdButton(text="/help")
#     button2 = telebot.types.Keybon_support, button1, button2, button3)
#     bot.send_message(chat_id,
#                      'Добро пожаловать в бота кодировщика!',
#                      reply_markup=keyboard)


# Handle '/help'
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, """\
/encode - напиши текст и я его зашифрую;\n/decode- напиши зашифрованный текст и его расшифрую.\
""")


# Handle '/encode'
@bot.message_handler(commands=['encode'])
def com_encode(message):
    global FLAG
    FLAG = True
    bot.reply_to(message,"Напишите текст, котрый вы хотите зашифровать:")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(content_types=["text"])
def encoded_message(message):
    global FLAG
    if FLAG:
        list_message = list(message.text.lower())
        message1 = ""
        for x in list_message:
            if x in r_letters:
                message1 += r_letters[int(r_letters.index(x) + 3) % (len(r_letters) - 1)]
            elif x in e_letters:
                message1 += e_letters[int(e_letters.index(x) + 3) % (len(e_letters) - 1)]
            else:
                message1 += x
        bot.reply_to(message, message1)
        FLAG = False
    else:
        bot.reply_to(message, "Вы просто вводите текст, если хотите закодировать или декодировать текст используйте функции. Подробнее ищите в /help.")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)


bot.infinity_polling()
