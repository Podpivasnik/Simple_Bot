import telebot

from telebot import types

token = "2114060884:AAEbiwtwRq_2NKxNtEISh8Gq3c0L-fy2QM8"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help","vuz","/git", '/dis')
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['/help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Список комманд на которые я отвечу'
                                      '1. git - выдаю ссылку на гитхаб автора'
                                      '2. weather - выдаю ссылку на погоду'
                                      '3. vuz - ссылка на википедию вуза')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "/vuz":
        bot.send_message(message.chat.id, 'https://ru.wikipedia.org/wiki/Московский_технический_университет_связи_и_информатики')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "/git":
        bot.send_message(message.chat.id, 'Держи ссылку на гит: https://github.com/Podpivasnik')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "/weather":
        bot.send_message(message.chat.id, 'https://www.accuweather.com')