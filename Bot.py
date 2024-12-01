from config_bot import TOKEN_bot
from bot_logic import gen_pass

import random
import os


import telebot

bot = telebot.TeleBot(TOKEN_bot)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['pass'])
def gen_pass_tg(message):
    parol = gen_pass(10)
    bot.reply_to(message, f'Ваш пароль: {parol}')

@bot.message_handler(commands=['mem'])
def send_mem(message):
    meme_name = random.choice(os.listdir('meme/images'))
    with open(f'meme/images/{meme_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['cat'])
def send_cat(message):
    cat_name = random.choice(os.listdir('cats'))
    with open(f'cats/{cat_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['goat'])
def send_goat(message):
    goat_name = random.choice(os.listdir('goat'))
    with open(f'goat/{goat_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(func=lambda message: True) #<- <- Это эхо его надо в самый низ"
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
