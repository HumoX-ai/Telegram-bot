import telebot
from telebot import types
import random
TOKEN = '1835122693:AAGvWIlOyfUY7T-jbybSgjDgPgasiB9Hk7A'
 
bot = telebot.TeleBot(TOKEN)
 
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('🔸 Tasodifiy raqam')
    item2 = types.KeyboardButton('📈 Valyuta kurslari')
    item3 = types.KeyboardButton('📚 Qo`shimcha')
    item4 = types.KeyboardButton('➡️ Keyingisi')
 
    markup.add(item1, item2, item3, item4)
 
    bot.send_message(message.chat.id, 'Hayrli kun, {0.first_name}!'.format(message.from_user), reply_markup = markup)
 
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '🔸 Tasodifiy raqam':
            bot.send_message(message.chat.id, 'Sizning raqamingiz: ' + str(random.randint(0, 1000)))
        elif message.text == '📈 Valyuta kurslari':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🇺🇸 Dollar kursi')
            item2 = types.KeyboardButton('🇪🇺 Evro kursi')
            back = types.KeyboardButton('⬅️ Orqaga')
            markup.add(item1, item2, back)
 
            bot.send_message(message.chat.id, '📈 Valyuta kurslari', reply_markup = markup)
        
        elif message.text == '📚 Qo`shimcha':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('💾 Bot haqida')
            item2 = types.KeyboardButton('♐️ Burjlar haqida ma`lumot')
            back = types.KeyboardButton('⬅️ Orqaga')
            markup.add(item1, item2, back)
 
            bot.send_message(message.chat.id, '📚Qo`shimcha', reply_markup = markup)
 
        elif message.text == '➡️ Keyingisi':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🛠 Sozlamalar')
            item2 = types.KeyboardButton('✉️ Obuna')
            item3 = types.KeyboardButton('🧸 Stiker')
            back = types.KeyboardButton('⬅️ Orqaga')
            markup.add(item1, item2, item3, back)
 
            bot.send_message(message.chat.id, '➡️ Keyingisi', reply_markup = markup)
        
        elif message.text == '⬅️ Orqaga':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🔸 Tasodifiy raqam')
            item2 = types.KeyboardButton('📈 Valyuta kurslari')
            item3 = types.KeyboardButton('📚 Qo`shimcha')
            item4 = types.KeyboardButton('➡️ Keyingisi')
 
            markup.add(item1, item2, item3, item4)
 
            bot.send_message(message.chat.id, '⬅️ Orqaga', reply_markup = markup)
        
        elif message.text == '🧸 Стикер':
            stick = open('static/sticker.webp', 'rb')
            bot.send_sticker(message.chat.id, stick)
 
 
 
bot.polling(none_stop = True)