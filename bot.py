import telebot
import random
from telebot import apihelper
bot = telebot.TeleBot('1080980675:AAFDKQsxPOdmd0EOYTm-6IZ7vOV4FarQ5PM')
apihelper.proxy = {'https': 'https://213.32.21.9:8080'}
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'ха ха ха':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMZXtjpUKsDDTxhd6fY-6c61K4dw7QAAvsBAAKc1ucK9AEBfuemTckaBA')
@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)
bot.polling(none_stop=True, interval=0)
