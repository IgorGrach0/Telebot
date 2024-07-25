import telebot
from telebot import types
import sqlite3
import record
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
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поздороваться")
    btn2 = types.KeyboardButton("Задать вопрос")
    markup.add(btn1, btn2)
    if username != None:
        bot.send_message(message.chat.id, f'Добро пожаловать, {username} \nВаш баланс: {balance}')
    else:
        global status
        status = 'login'
        bot.send_message(message.chat.id, 'Вы  ещё не зарегистрированы. \nВведите имя пользователя:')


@bot.message_handler(commands=['spin'])
def spining(message):
    global spin_Status
    global status
    global status_bet
    global num_people

    username, balance = record.search('ID', message.chat.id)
    spin_Status = 'Straight_Up'
    status ='spin'
    status_bet = 'bet'
    bot.send_message(message.chat.id, f'Ваш баланс: {balance}\nУкажите размер ставки: ')
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
    elif status =='spin':
        global status_bet
        global num_people
        if status_bet == 'bet':
            bet = message.text
            bot.send_message(message.chat.id, 'На что ставим? ')
            status_bet = 'input_number'
        elif status_bet == 'input_number':
            global num_people
            num_people = message.text
        global num_peopl
        if num_people:
            num = random.randint(0, 36)
            bet = int(bet)
            if int(num_people) >= 0 and int(num_people) <= 36:
                if num == int(num_people):
                    username, balance = record.search('ID', message.chat.id)
                    bot.send_message(message.chat.id, f'Вы выиграли!Ваш баланс: {balance}')
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    btn1 = types.KeyboardButton("Поздороваться")
                    btn2 = types.KeyboardButton("Задать вопрос")

                    markup.add(btn1, btn2)
                    spining(message)


                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    btn1 = types.KeyboardButton("Поздороваться")
                    btn2 = types.KeyboardButton("Задать вопрос")
                    markup.add(btn1, btn2)
                    
                    bot.send_message(message.chat.id, f'Вы проиграли! \nВыпало число:: {num} \n Ваш баланс: {balance}')
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