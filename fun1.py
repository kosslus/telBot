import telebot
import types
from telebot import types

bot = telebot.TeleBot('1036484441:AAEjqVXd8UEAtmC8qOT6YctUrxa9-_fed9c')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока', 'Как дела?', 'Что делаешь?')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой БОГ!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, ПОВЕЛИТЕЛЬ!')
    elif message.text.lower() == 'что делаешь?':
        bot.send_message(message.chat.id, 'С Тобой переписываюсь!')
    elif message.text.lower() == 'я кушаю':
        bot.send_message(message.chat.id, 'Приятного аппетита!')
    elif message.text.lower() == 'гифка':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')

    elif message.text == 'как дела?':
        markup = types.InlineKeyboardButtonMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
        item2 = types.InlineKeyboardButton("Такое", callback_data='bad')

        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Лучше всех!А у тебя?', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'такое')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()
