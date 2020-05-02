from telebot import types
import COVID19Py
import telebot

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('')###BotApi


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('США')
    btn2 = types.KeyboardButton('Украина')
    btn3 = types.KeyboardButton('Россия')
    btn4 = types.KeyboardButton('Беларусь')
    btn5 = types.KeyboardButton('Новая Зеландия')
    markup.add(btn1, btn2, btn3, btn4, btn5, )
    send_message = f"<b>Привет {message.from_user.first_name}!</b>\nНапишите название страны с маленькой буквы"
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "украина":
        location = covid19.getLocationByCountryCode("UA")
    elif get_message_bot == "россия":
        location = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "беларусь":
        location = covid19.getLocationByCountryCode("BY")
    elif get_message_bot == "казахстан":
        location = covid19.getLocationByCountryCode("KZ")
    elif get_message_bot == "италия":
        location = covid19.getLocationByCountryCode("IT")
    elif get_message_bot == "франция":
        location = covid19.getLocationByCountryCode("FR")
    elif get_message_bot == "германия":
        location = covid19.getLocationByCountryCode("DE")
    elif get_message_bot == "япония":
        location = covid19.getLocationByCountryCode("JP")
    elif get_message_bot == "канада":
        location = covid19.getLocationByCountryCode("CA")
    elif get_message_bot == "мексика":
        location = covid19.getLocationByCountryCode("MX")
    elif get_message_bot == "кипр":
        location = covid19.getLocationByCountryCode("CY")
    elif get_message_bot == "великобритания":
        location = covid19.getLocationByCountryCode("GB")
    elif get_message_bot == "дания":
        location = covid19.getLocationByCountryCode("DK")
    elif get_message_bot == "китай":
        location = covid19.getLocationByCountryCode("CN")
    elif get_message_bot == "новая зеландия":
        location = covid19.getLocationByCountryCode("NZ")
    else:
        location = covid19.getLocationByCountryCode('UA')


    if final_message == "":
            date = location[0]['last_updated'].split("T")
            time = date[1].split(".")
            final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
                            f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
                            f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Смертей: </b>" \
                            f"{location[0]['latest']['deaths']:,}" \



    bot.send_message(message.chat.id, final_message, parse_mode='html')

bot.polling(none_stop=True)
