import telebot
from telebot import types
import sqlite3
import record

# Создание соединения с SQLite3 базой данных

 # Создание таблицы

token = "6055757564:AAHWHabIsBJlwTaWVZbhJEhvL2JhH5p40sA"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет, я игровой бот, для начала новой игры введите команду  /start_new_game. \n '
                                     'Для продолжения введите команду  /continue_game.')
@bot.message_handler(commands=['start_new_game'])
def button_message(message):
    global status
    status = 'login'
    bot.send_message(message.chat.id,'Введите имя пользователя')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    global status
    if status == 'login':
        import sqlite3
        b = 10000
        ID = message.chat.id
        conn = sqlite3.connect('../users.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS users
                     (ID TEXT, login TEXT, balance INTEGER)''')
        cur.execute("INSERT INTO users VALUES (?, ?, ?)", (ID, message.text, b))
        conn.commit()
        conn.close()


if __name__ == '__main__':
    bot.polling()