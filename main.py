import telebot
from telebot import types

import logs
import lists
import returns
import tokenbot

DEBUG = True
bot = telebot.TeleBot(tokenbot.TOKEN)

if(DEBUG):
    logs.start()
    print("Начало работы бота...")

##
## COMMANDS
##

@bot.message_handler(commands=['start'])
def start(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    games = types.KeyboardButton('Игры')
    help = types.KeyboardButton('Помощь')
    contact = types.KeyboardButton('Связаться')
    links = types.KeyboardButton('Ссылки')

    markup.add(games, help, contact, links)

    bot.send_message(m.chat.id, returns.start(0), reply_markup=markup)
    bot.send_message(m.chat.id, returns.start(1), reply_markup=markup)

    if(DEBUG):
        logs.save(chatid=m.chat.id, text="/start", code=1)

@bot.message_handler(commands=['help'])
def help(m):
    bot.send_message(m.chat.id, returns.help())

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("creagoo.ru", url="https://creagoo.ru"))
    bot.send_message(m.chat.id, 'Ссылка на сайт Creagoo', reply_markup=markup)

    markup1 = types.InlineKeyboardMarkup()
    markup1.add(types.InlineKeyboardButton("@ddybka", url="https://ddybka.t.me"))
    bot.send_message(m.chat.id, 'Связаться с автором', reply_markup=markup1)

    if(DEBUG):
        logs.save(chatid=m.chat.id, text="/help", code=1)


##
## DOCS
##

@bot.message_handler(content_types=['photo'])
def photo(m):
    bot.send_message(m.chat.id, returns.sended_document(), parse_mode='html')

    if(DEBUG):
        logs.save(chatid=m.chat.id, text="sended photo", code=2)

@bot.message_handler(content_types=['document'])
def document(m):
    bot.send_message(m.chat.id, returns.sended_document(), parse_mode='html')

    if(DEBUG):
        logs.save(chatid=m.chat.id, text="sended document", code=2)

@bot.message_handler(content_types=['video'])
def document(m):
    bot.send_message(m.chat.id, returns.sended_document(), parse_mode='html')

    if(DEBUG):
        logs.save(chatid=m.chat.id, text="sended video", code=2)

##
## PINNED
##

@bot.message_handler(content_types=['pinned_message'])
def get_pin_message(m):
    bot.send_message(m.chat.id, returns.pinned_message())

    if(DEBUG):
        logs.save(chatid=m.chat.id, text="pinned message", code=3)

##
## TEXT
##

@bot.message_handler(content_types=['text'])
def get_text(m):
    usertext = m.text.lower()

    if(DEBUG):
        logs.save(chatid=m.chat.id, text=usertext, code=0)

    if usertext in lists.list_hello:
        bot.send_message(m.chat.id, returns.text_hello(m.from_user.first_name))

    elif usertext in lists.list_lookatgames:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Babka On The Hunt: 2D Классика"))
        markup.add(types.KeyboardButton("Запомни эти карты"))
        markup.add(types.KeyboardButton("Камень ножницы бумага"))
        markup.add(types.KeyboardButton("Крестики нолики"))
        markup.add(types.KeyboardButton("Sweetness"))
        markup.add(types.KeyboardButton("Guess"))
        markup.add(types.KeyboardButton("Button pusher"))
        markup.add(types.KeyboardButton("Вернуться на главную"))
        bot.send_message(m.chat.id, 'Выберите интересующую игру Creagoo', reply_markup=markup)

    elif usertext in lists.text_help:
        bot.send_message(m.chat.id, returns.help())

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("creagoo.ru", url="https://creagoo.ru"))
        bot.send_message(m.chat.id, 'Ссылка на сайт Creagoo', reply_markup=markup)

        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton("@ddybka", url="https://ddybka.t.me"))
        bot.send_message(m.chat.id, 'Связаться с автором', reply_markup=markup1)

    elif usertext in lists.list_contact:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("creagoo.ru", url="https://creagoo.ru"))
        bot.send_message(m.chat.id, 'Ссылка на сайт Creagoo', reply_markup=markup)

        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton("@ddybka", url="https://ddybka.t.me"))
        bot.send_message(m.chat.id, 'Связаться с автором', reply_markup=markup1)

        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("it.dybka.ru", url="https://it.dybka.ru"))
        bot.send_message(m.chat.id, 'Другие разработки', reply_markup=markup2)

    elif usertext in lists.text_getlinks:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Сайт Creagoo", url="https://creagoo.ru"))
        markup.add(types.InlineKeyboardButton("Телеграм канал", url="https://creagoo.t.me"))
        markup.add(types.InlineKeyboardButton("Вконтакте паблик", url="https://vk.com/creagoo"))
        markup.add(types.InlineKeyboardButton("Читать новости", url="https://news.dybka.ru"))
        markup.add(types.InlineKeyboardButton("Слушать подкаст", url="https://youtu.be/lKLuwC9qb-w"))
        bot.send_message(m.chat.id, 'Ссылки Creagoo', reply_markup=markup)

    elif usertext in lists.text_getmainscreen:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        games = types.KeyboardButton('Игры')
        help = types.KeyboardButton('Помощь')
        contact = types.KeyboardButton('Связаться')
        links = types.KeyboardButton('Ссылки')

        markup.add(games, help, contact, links)
        bot.send_message(m.chat.id, 'Вы вернулись на главную', reply_markup=markup)

    elif usertext in lists.game_babkaonthehunt2dclassic:
        link = "media/babkaonthehuntclassic/screen"
        photos = [
            telebot.types.InputMediaPhoto(open(link + "1.jpg", 'rb')),
            telebot.types.InputMediaPhoto(open(link + "2.jpg", 'rb')),
            telebot.types.InputMediaPhoto(open(link + "3.jpg", 'rb')),
            telebot.types.InputMediaPhoto(open(link + "4.jpg", 'rb')),
            telebot.types.InputMediaPhoto(open(link + "5.jpg", 'rb'))
        ]

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Андроид скачать", url="https://s.creagoo.ru/?w=4tan36"))
        markup.add(types.InlineKeyboardButton("Windows скачать", url="https://s.creagoo.ru/?w=YWdM3Y"))
        markup.add(types.InlineKeyboardButton("macOS скачать", url="https://s.creagoo.ru/?w=b7RYYk"))
        markup.add(types.InlineKeyboardButton("Linux скачать", url="https://s.creagoo.ru/?w=UYG87tf7f"))
        markup.add(types.InlineKeyboardButton("Читать на сайте", url="https://creagoo.ru/games/babkaonthehuntclassic"))
        markup.add(types.InlineKeyboardButton("Стикеры телеграм", url="https://t.me/addstickers/babkaonthehunt"))

        bot.send_message(m.chat.id, returns.descgame_babkaonthehunt2dclassic(), parse_mode='html')
        bot.send_media_group(m.chat.id, photos)
        bot.send_message(m.chat.id, "Скачать сейчас:", reply_markup=markup)

    elif usertext in lists.game_tictactoe:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Андроид скачать", url="https://s.creagoo.ru/?w=mjbvVR"))
        markup.add(types.InlineKeyboardButton("Windows скачать", url="https://s.creagoo.ru/?w=wuOn3j"))
        markup.add(types.InlineKeyboardButton("macOS скачать", url="https://s.creagoo.ru/?w=W2CC67"))
        markup.add(types.InlineKeyboardButton("Читать на сайте", url="https://creagoo.ru/games/tictactoe"))

        bot.send_message(m.chat.id, returns.descgame_tictactoe(), parse_mode='html')
        bot.send_message(m.chat.id, "Скачать сейчас:", reply_markup=markup)

    elif usertext in lists.game_babkaonthehuntlight:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Андроид скачать", url="https://s.creagoo.ru/?w=xWBGHn"))
        markup.add(types.InlineKeyboardButton("Windows скачать", url="https://s.creagoo.ru/?w=GUPbCg"))
        markup.add(types.InlineKeyboardButton("macOS скачать", url="https://s.creagoo.ru/?w=gWs0nk"))
        markup.add(types.InlineKeyboardButton("Читать на сайте", url="https://creagoo.ru/games/babkaonthehuntlight"))

        bot.send_message(m.chat.id, returns.descgame_babkaonthehuntlight(), parse_mode='html')
        bot.send_message(m.chat.id, "Скачать сейчас:", reply_markup=markup)

    elif usertext in lists.game_babkaonthehunt:
        link = "media/babkaonthehunt/screen"
        photos = [
            telebot.types.InputMediaPhoto(open(link + "1.jpg", 'rb')),
            telebot.types.InputMediaPhoto(open(link + "2.jpg", 'rb')),
            telebot.types.InputMediaPhoto(open(link + "3.jpg", 'rb')),
            telebot.types.InputMediaPhoto(open(link + "4.jpg", 'rb')),
            telebot.types.InputMediaPhoto(open(link + "5.jpg", 'rb'))
        ]

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Андроид скачать", url="https://s.creagoo.ru/?w=zPcPOu"))
        markup.add(types.InlineKeyboardButton("Windows скачать", url="https://s.creagoo.ru/?w=82hQer"))
        markup.add(types.InlineKeyboardButton("macOS скачать", url="https://s.creagoo.ru/?w=rIznVk"))
        markup.add(types.InlineKeyboardButton("Читать на сайте", url="https://creagoo.ru/games/babkaonthehunt"))
        bot.send_message(m.chat.id, returns.descgame_babkaonthehunt(), parse_mode='html')
        bot.send_media_group(m.chat.id, photos)
        bot.send_message(m.chat.id, "Скачать сейчас:", reply_markup=markup)

    elif usertext in lists.game_guess:
        link = "media/guess/screen"
        photos = [
            telebot.types.InputMediaPhoto(open(link + "1.jpg", 'rb')),
            telebot.types.InputMediaPhoto(open(link + "2.jpg", 'rb')),
            telebot.types.InputMediaPhoto(open(link + "3.jpg", 'rb'))
        ]

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Андроид скачать", url="https://s.creagoo.ru/?w=84XLGz"))
        markup.add(types.InlineKeyboardButton("Windows скачать", url="https://s.creagoo.ru/?w=WBoeAo"))
        markup.add(types.InlineKeyboardButton("macOS скачать", url="https://s.creagoo.ru/?w=LYlIxt"))
        markup.add(types.InlineKeyboardButton("Читать на сайте", url="https://creagoo.ru/games/guess"))
        bot.send_message(m.chat.id, returns.descgame_guess(), parse_mode='html')
        bot.send_media_group(m.chat.id, photos)
        bot.send_message(m.chat.id, "Скачать сейчас:", reply_markup=markup)

    elif usertext in lists.game_rememberthesecards:
        link = "media/rememberthesecards/screen"
        photos = [
            telebot.types.InputMediaPhoto(open(link + "1.jpg", 'rb')),
            telebot.types.InputMediaPhoto(open(link + "2.jpg", 'rb')),
            telebot.types.InputMediaPhoto(open(link + "3.jpg", 'rb')),
            telebot.types.InputMediaPhoto(open(link + "4.jpg", 'rb')),
            telebot.types.InputMediaPhoto(open(link + "5.jpg", 'rb'))
        ]

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Андроид скачать", url="https://play.google.com/store/apps/details?id=com.Creagoo.RememberTheseCards"))
        markup.add(types.InlineKeyboardButton("Читать на сайте", url="https://creagoo.ru/games/rememberthesecards"))
        bot.send_message(m.chat.id, returns.descgame_rememberthesecards(), parse_mode='html')
        bot.send_media_group(m.chat.id, photos)
        bot.send_message(m.chat.id, "Скачать сейчас:", reply_markup=markup)

    elif usertext in lists.game_sweetness:
        link = "media/sweetness/screen"
        photos = [
            telebot.types.InputMediaPhoto(open(link + "1.jpg", 'rb')),
            telebot.types.InputMediaPhoto(open(link + "2.jpg", 'rb')),
            telebot.types.InputMediaPhoto(open(link + "3.jpg", 'rb'))
        ]

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Андроид скачать", url="https://s.creagoo.ru/?w=VqEGKs"))
        markup.add(types.InlineKeyboardButton("Windows скачать", url="https://s.creagoo.ru/?w=vukI06"))
        markup.add(types.InlineKeyboardButton("macOS скачать", url="https://s.creagoo.ru/?w=BK2gci"))
        markup.add(types.InlineKeyboardButton("Читать на сайте", url="https://creagoo.ru/games/sweetness"))
        bot.send_message(m.chat.id, returns.descgame_sweetness(), parse_mode='html')
        bot.send_media_group(m.chat.id, photos)
        bot.send_message(m.chat.id, "Скачать сейчас:", reply_markup=markup)

    elif usertext in lists.game_buttonpusher:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Андроид скачать", url="https://s.creagoo.ru/?w=99ZMJN"))
        markup.add(types.InlineKeyboardButton("Windows скачать", url="https://s.creagoo.ru/?w=aJpAG4"))
        markup.add(types.InlineKeyboardButton("macOS скачать", url="https://s.creagoo.ru/?w=Rmp432"))
        markup.add(types.InlineKeyboardButton("Читать на сайте", url="https://creagoo.ru/games/buttonpusher"))

        bot.send_message(m.chat.id, returns.descgame_buttonpusher(), parse_mode='html')
        bot.send_message(m.chat.id, "Скачать сейчас:", reply_markup=markup)

    elif usertext in lists.game_rockpaperscissors:
        link = "media/rockpaperscissors/screen"
        photos = [
            telebot.types.InputMediaPhoto(open(link + ".jpg", 'rb'))
        ]

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Андроид скачать", url="https://s.creagoo.ru/?w=apsw0v"))
        markup.add(types.InlineKeyboardButton("Windows скачать", url="https://s.creagoo.ru/?w=SaZ4Jk"))
        markup.add(types.InlineKeyboardButton("macOS скачать", url="https://s.creagoo.ru/?w=soVx0V"))
        markup.add(types.InlineKeyboardButton("Читать на сайте", url="https://creagoo.ru/games/rockpaperscissors"))

        bot.send_message(m.chat.id, returns.descgame_rockpaperscissors(), parse_mode='html')
        bot.send_media_group(m.chat.id, photos)
        bot.send_message(m.chat.id, "Скачать сейчас:", reply_markup=markup)

    elif returns.text_another(usertext) != False:
        bot.send_message(m.chat.id, returns.text_another(usertext))

    else:
        bot.send_message(m.chat.id, returns.text_else())

if __name__ == "__main__":
    bot.polling(none_stop=True)

if(DEBUG):
    logs.finish()
    print("Завершение работы бота...")
