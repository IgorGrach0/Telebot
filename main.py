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
def spin(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = telebot.types.KeyboardButton('/spin_color')
    button2 = telebot.types.KeyboardButton('/spin_number')
    button3 = telebot.types.KeyboardButton('/spin_sector')
    keyboard.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выберите режим',reply_markup=keyboard)

@bot.message_handler(commands=['spin_color'])
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
    status ='spin_color'
    status_bet = 'bet'

    bot.send_message(message.chat.id, f'Ваш баланс: {balance}\nУкажите размер ставки: ', reply_markup=keyboard)
    num_people = None

@bot.message_handler(commands=['spin_number'])
def spin_number(message):
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
    status ='spin_number'
    status_bet = 'bet'

    bot.send_message(message.chat.id, f'Ваш баланс: {balance}\nУкажите размер ставки: ', reply_markup=keyboard)
    num_people = None

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'Cancel':
        spin(call.message)
    elif int(call.data) >= 0 and int(call.data) <= 36:
        num_people = int(call.data)
        result, Win_num = game_casino.number_game(num_people)
        username, balance = record.search('ID', call.message.chat.id)
        if result == True:
            bot.send_message(call.message.chat.id, f'Вы выиграли!\nВаш баланс: {balance}')
        else:
            bot.send_message(call.message.chat.id, f'Вы проиграли!\nВыпало число:: {Win_num},\nВаш баланс: {balance}')

        spin_number(call.message)
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

    elif status =='spin_number':
        global status_bet
        global num_people
        if status_bet == 'bet':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('0', callback_data='0'))
            markup.add(types.InlineKeyboardButton('1', callback_data='1'), types.InlineKeyboardButton('2', callback_data='2'), types.InlineKeyboardButton('3', callback_data='3'))
            markup.add(types.InlineKeyboardButton('4', callback_data='4'), types.InlineKeyboardButton('5', callback_data='5'), types.InlineKeyboardButton('6', callback_data='6'))
            markup.add(types.InlineKeyboardButton('7', callback_data='7'), types.InlineKeyboardButton('8', callback_data='8'), types.InlineKeyboardButton('9', callback_data='9'))
            markup.add(types.InlineKeyboardButton('10', callback_data='10'), types.InlineKeyboardButton('11', callback_data='11'), types.InlineKeyboardButton('12', callback_data='12'))
            markup.add(types.InlineKeyboardButton('13', callback_data='13'), types.InlineKeyboardButton('14', callback_data='14'), types.InlineKeyboardButton('15', callback_data='15'))
            markup.add(types.InlineKeyboardButton('16', callback_data='16'), types.InlineKeyboardButton('17', callback_data='17'), types.InlineKeyboardButton('18', callback_data='18'))
            markup.add(types.InlineKeyboardButton('19', callback_data='19'), types.InlineKeyboardButton('20', callback_data='20'), types.InlineKeyboardButton('21', callback_data='21'))
            markup.add(types.InlineKeyboardButton('22', callback_data='22'), types.InlineKeyboardButton('23', callback_data='23'), types.InlineKeyboardButton('24', callback_data='24'))
            markup.add(types.InlineKeyboardButton('25', callback_data='25'), types.InlineKeyboardButton('26', callback_data='26'), types.InlineKeyboardButton('27', callback_data='27'))
            markup.add(types.InlineKeyboardButton('28', callback_data='28'), types.InlineKeyboardButton('29', callback_data='29'), types.InlineKeyboardButton('30', callback_data='30'))
            markup.add(types.InlineKeyboardButton('31', callback_data='31'), types.InlineKeyboardButton('32', callback_data='32'), types.InlineKeyboardButton('33', callback_data='33'))
            markup.add(types.InlineKeyboardButton('34', callback_data='34'), types.InlineKeyboardButton('35', callback_data='35'), types.InlineKeyboardButton('36', callback_data='36'))
            markup.add(types.InlineKeyboardButton('Cancel', callback_data='Cancel'))

            bot.send_message(message.chat.id, 'Выберите число', reply_markup=markup)


    elif status =='spin_color':
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
            num_people = message.text

        if num_people:
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