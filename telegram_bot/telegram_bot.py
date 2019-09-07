import telebot
import requests
import config


NBRB_API = "http://www.nbrb.by/API/ExRates/Rates/145"
bot = telebot.TeleBot(config.TOKEN)
r = requests.request("GET", NBRB_API).json() #timeout


@bot.message_handler(content_types=['text'])
def handle_answer(message):
    print(message.text)
    if message.text.isalpha():
        bot.send_message(
            message.chat.id, "Привет, введи сумму которую ты хотел бы поменять?"
        )
    elif message.text.isdigit():
        bot.send_message(
            message.chat.id, r['Cur_OfficialRate'] * float(message.text)
        )


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
