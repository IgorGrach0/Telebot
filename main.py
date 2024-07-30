import telebot
from telebot import types
import sqlite3

import record
import game_casino

import sqlite3
import random
import setings

conn = sqlite3.connect('users.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users
                     (ID TEXT, login TEXT, balance INTEGER)''')
conn.commit()
conn.close()

token = setings.TOKEN
bot = telebot.TeleBot(token)
spin_Status = ''
status = ''


@bot.message_handler(commands=['start'])
def start_message(message):
    username, balance = record.search('ID', message.chat.id)
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = telebot.types.KeyboardButton('/start')
    button2 = telebot.types.KeyboardButton('/spin')
    keyboard.add(button1, button2)

    if username != None:
        bot.send_message(message.chat.id, f'Добро пожаловать, {username} \nВаш баланс: {balance}', reply_markup=keyboard)
    else:
        global status
        status = 'login'
        bot.send_message(message.chat.id, 'Вы  ещё не зарегистрированы. \nВведите имя пользователя:', reply_markup=keyboard)


@bot.message_handler(commands=['spin'])
def spining(message):
    global spin_Status
    global status
    global status_bet
    global num_people
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = telebot.types.KeyboardButton('50')
    button2 = telebot.types.KeyboardButton('100')
    button3 = telebot.types.KeyboardButton('200')
    button4 = telebot.types.KeyboardButton('500')
    button5 = telebot.types.KeyboardButton('1000')
    keyboard.add(button1, button2, button3, button4, button5)

    username, balance = record.search('ID', message.chat.id)
    spin_Status = 'Straight_Up'
    status ='spin'
    status_bet = 'bet'

    bot.send_message(message.chat.id, f'Ваш баланс: {balance}\nУкажите размер ставки: ', reply_markup=keyboard)
    num_people = None

@bot.message_handler(content_types=['text'])
def handle_text(message):
    global status
    global bet
    username, balance = record.search('ID', message.chat.id)
    if status == 'login':
        import sqlite3
        b = 10000
        ID = message.chat.id
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS users
                     (ID TEXT, login TEXT, balance INTEGER)''')
        cur.execute("INSERT INTO users VALUES (?, ?, ?)", (ID, message.text, b))
        conn.commit()
        conn.close()
        bot.send_message(message.chat.id, 'Вы успешно зарегистрированы')

    elif status == 'spin_color':
        global status_bet
        global color_people
    elif status =='spin':
        global status_bet
        global num_people
        if status_bet == 'bet':
            keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            button1 = telebot.types.KeyboardButton('Red')
            button2 = telebot.types.KeyboardButton('Black')
            button3 = telebot.types.KeyboardButton('Zero')
            keyboard.add(button1, button2, button3)

            bet = message.text
            bot.send_message(message.chat.id, 'На что ставим? ', reply_markup=keyboard)
            status_bet = 'input_number'
        elif status_bet == 'input_number':
            global num_people
            num_people = message.text

        if num_people:
            '''num = random.randint(0, 36)'''
            num_people = num_people.lower()
            win_color, win_Number, WIN_COLOR = game_casino.Black_or_Red(num_people)
            if num_people == 'red' or num_people == 'black' or num_people == 'zero':
                if win_color == True:
                    username, balance = record.search('ID', message.chat.id)
                    bot.send_message(message.chat.id, f'Вы выиграли!\nВаш баланс: {balance}')
                    spining(message)
                else:
                    bot.send_message(message.chat.id, f'Вы проиграли!\nВыпало число:: {win_Number}, {WIN_COLOR}\nВаш баланс: {balance}')
                    spining(message)
            else:
                bot.send_message(message.chat.id, 'Вы ввели неверное значение')
                spining(message)
        elif spin_Status == 'Split ':
            bot.send_message(message.chat.id, 'Split!')

    elif status == 'balance':
        username, balance = record.search('ID', message.chat.id)
        bot.send_message(message.chat.id, f'Ваш баланс: {balance}')

if __name__ == '__main__':
    bot.polling()