import telebot
from telebot import types
import random
import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Обновляем возраст пользователя "newuser"
cursor.execute('SELECT * FROM Test')
test = cursor.fetchall()

# Выводим результаты
for vo in test:
    idnt = list(vo)[0]

# Закрываем соединение   
connection.close()

bot = telebot.TeleBot('6132095425:AAFM6_v_g2talA-UXKhHva778jKL8fRuDuM')
m1 = {'Укажи сумму чисел 9 и 8':'17', 'Укажи разность чисел 13 и 3':'10',
      'Реши цепочку примеров. Укажи результат вычислений. 5 - 3 + 1 - 1 + 4 - 2 + 3 + 3':'10', 'На аэродроме было 4 вертолёта и сколько-то самолётов. Всего 11 самолетов и вертолетов вместе. Сколько самолётов было на аэродроме?':'7','В букете 7 ромашек, а васильков на 2 меньше, чем ромашек. Сколько всего цветов в букете?':'12','Укажи, чему равно вычитаемое, если известно, что уменьшаемое 16, а разность 4.':'12'}
m1v = list(m1.keys())
viz = 0
vknp = 0
kv = 0
print(m1v)
kpo = 0
kno = 0
idnt += 1
v = 0
cuv = dict()
print(v)
@bot.message_handler(commands=['start']) 
def start(message):
    bot.send_message(message.from_user.id, 'Привет, я не бот, а ты бот')
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Помощь')
    itembtn2 = types.KeyboardButton('Тесты')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)

@bot.message_handler(content_types = 'text')
def one_cl(message):
    if message.text=="Тесты":
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtnm1 = types.KeyboardButton('Индивидуальные')
        itembtr1 = types.KeyboardButton('Школьные')
        itembtback = types.KeyboardButton('Назад в меню')
        markup.add(itembtnm1, itembtr1, itembtback)
        bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)
    if message.text=="Индивидуальные":
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtnm1 = types.KeyboardButton('Создать свой тест')
        itembtr1 = types.KeyboardButton('Пройти индивидуальный тест')
        itembtback = types.KeyboardButton('Назад в меню')
        markup.add(itembtnm1, itembtr1, itembtback)
        bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)
    if message.text=="Школьные":
        markup = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
        itembt1 = types.KeyboardButton('1 класс')
        itembtback = types.KeyboardButton('Назад в меню')
        markup.add(itembt1, itembtback)
        bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)
    if message.text=="1 класс":
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtnm1 = types.KeyboardButton('Математика 1 класс')
        itembtr1 = types.KeyboardButton('Русский язык 1 класс')
        itembtback = types.KeyboardButton('Назад в меню')
        markup.add(itembtnm1, itembtr1, itembtback)
        bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)
    
    if message.text=="Математика 1 класс":
        global m1v, v
        v = random.choice(m1v)
        m1v = list(m1.keys())
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtback = types.KeyboardButton('Назад в меню')
        markup.add(itembtback)
        bot.send_message(message.chat.id, "Тест по математике1")
        bot.send_message(message.chat.id, "Первый вопрос:", reply_markup=markup)
        sent = bot.send_message(message.chat.id, v)
        if sent.text == 'Назад в меню':
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Помощь')
            itembtn2 = types.KeyboardButton('Тесты')
            markup.add(itembtn1, itembtn2)
            bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)
        else:
            bot.register_next_step_handler(sent, hello)
    if message.text=="Русский язык 1 класс":
        bot.send_message(message.chat.id, "Тест по Русскому языку")
        bot.send_message(message.chat.id, "Первый вопрос:")
        sent = bot.send_message(message.chat.id, 'Правильно ли написано слово машина?')
        bot.register_next_step_handler(sent, hellor1)
    if message.text=="Создать свой тест":
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        itembtnm1 = types.KeyboardButton('Помощь')
        itembtr1 = types.KeyboardButton('Создать тест')
        itembtback = types.KeyboardButton('Назад в меню')
        markup.add(itembtnm1, itembtr1, itembtback)
        bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)
    if message.text=="Создать тест":
        sent = bot.send_message(message.chat.id, "Введите сколько будет вопросов в тесте\n(Можно только 2 и больше вопросов)")
        bot.register_next_step_handler(sent, cruv1)
    if message.text=="Пройти индивидуальный тест":
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        itembtnm1 = types.KeyboardButton('Помощь')
        itembtr1 = types.KeyboardButton('Пройти тест')
        itembtback = types.KeyboardButton('Назад в меню')
        markup.add(itembtnm1, itembtr1, itembtback)
        bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)
    if message.text=="Пройти тест":
        sent = bot.send_message(message.chat.id, "Введите id теста который хочешь пройти")
        bot.register_next_step_handler(sent, ptpid)
    if message.text == 'Помощь':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtnm1 = types.KeyboardButton('Как создать тест')
        itembtr1 = types.KeyboardButton('Как пройти тест')
        itemerror = types.KeyboardButton('Вы нашли ошибку?')
        itembtback = types.KeyboardButton("Назад в меню")
        markup.add(itembtnm1, itembtr1, itembtback, itemerror)
        bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)
    if message.text == 'Как создать тест':
        pass
    if message.text == 'Как пройти тест':
        pass
    if message.text == 'Вы нашли ошибку?':
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        itembtback = types.KeyboardButton("Назад в меню")
        markup.add(itembtback)
        bot.send_message(message.chat.id, "Вы можете написать об ошибке разработчику по тегу: @SHIZIK_XD", reply_markup=markup)
    if message.text == 'Назад в меню':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Помощь')
        itembtn2 = types.KeyboardButton('Тесты')
        markup.add(itembtn1, itembtn2)
        bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)

def cruv1(message):
    global cuv, clvvt
    clvvt = int(message.text)
    if clvvt <= 1:
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtback = types.KeyboardButton('Назад в меню')
        markup.add(itembtback)
        bot.send_message(message.chat.id, "Можно ввести только 2 и больше вопросов", reply_markup=markup)
    else:
        sent = bot.send_message(message.chat.id, "Пожалуйста вводите вопросы следуя примеру:\nвопрос:ответ\nвопрос:ответ\nвопрос:ответ и т.д.")
        print(sent)
        bot.register_next_step_handler(sent, recurs1)
def ptpid(message):
    global vknp, viz, v
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    # Обновляем возраст пользователя "newuser"
    cursor.execute('SELECT * FROM Test')
    test = cursor.fetchall()
    vknp = 0
    # Закрываем соединение   
    
    try:
        for vo in test:
            if list(vo)[0] == int(message.text):
                vknp = list(vo)[1]
                print(list(vo)[1])
                break
        print(vknp)
        vknp = eval(vknp)
        print(type(vknp))
        viz = list(vknp.keys())
        connection.close()
        v = random.choice(viz)
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtback = types.KeyboardButton('Назад в меню')
        markup.add(itembtback)
        bot.send_message(message.chat.id, "Тест", reply_markup=markup)
        sent = bot.send_message(message.chat.id, v)
        if sent.text == 'Назад в меню':
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Помощь')
            itembtn2 = types.KeyboardButton('Тесты')
            markup.add(itembtn1, itembtn2)
            bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)
        else:
            bot.register_next_step_handler(sent, ptpid1)
    except IndexError:
        bot.send_message(message.chat.id, "Вы ввели неправильный id")
        connection.close()
def ptpid1(message):
    try:
        global v, viz, vknp, kpo, kno, kv
        message_to_save = message.text
        print(v)
        if message_to_save == vknp.get(v):
            viz.remove(v)
            kv += 1
            kpo += 1
            v = random.choice(viz)
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            itembtback = types.KeyboardButton('Назад в меню')
            markup.add(itembtback)
            bot.send_message(message.from_user.id, 'Правильно! Идём дальше', reply_markup=markup)
            sent = bot.send_message(message.chat.id, v)
            bot.register_next_step_handler(sent, ptpid2)
        elif message_to_save == 'Назад в меню':
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Помощь')
            itembtn2 = types.KeyboardButton('Тесты')
            markup.add(itembtn1, itembtn2)
            bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)
        else:
            bot.send_message(message.from_user.id, 'Неправильно')
            kno += 1
            kv += 1
            viz.remove(v)
            v = random.choice(viz)
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            itembtback = types.KeyboardButton('Назад в меню')
            markup.add(itembtback)
            bot.send_message(message.from_user.id, 'Идём дальше', reply_markup=markup)
            sent = bot.send_message(message.chat.id, v)
            bot.register_next_step_handler(sent, ptpid2)
    except IndexError:
        bot.send_message(message.from_user.id, 'Правильно, ты прошел тест!')
        bot.send_message(message.from_user.id, f'Ты ответил правильно на {kpo} вопросов и неправильно на {kno} вопросов и твой результат составляет {int(((kpo) // kpo) * 100)}%')
        kno, kpo, kv = 0, 0, 0

def ptpid2(message):
    try:
        global v, viz, vknp, kno, kpo, kv
        message_to_save = message.text
        print(v)
        if message_to_save == vknp.get(v):
            viz.remove(v)
            kpo += 1
            kv += 1
            v = random.choice(viz)
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            itembtback = types.KeyboardButton('Назад в меню')
            markup.add(itembtback)
            bot.send_message(message.from_user.id, 'Правильно! Идём дальше', reply_markup=markup)
            sent = bot.send_message(message.chat.id, v)
            bot.register_next_step_handler(sent, ptpid1)
        elif message_to_save == 'Назад в меню':
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Помощь')
            itembtn2 = types.KeyboardButton('Тесты')
            markup.add(itembtn1, itembtn2)
            bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)
        else:
            bot.send_message(message.from_user.id, 'Неправильно')
            kno += 1
            kv += 1
            viz.remove(v)
            v = random.choice(viz)
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            itembtback = types.KeyboardButton('Назад в меню')
            markup.add(itembtback)
            bot.send_message(message.from_user.id, 'Идём дальше', reply_markup=markup)
            sent = bot.send_message(message.chat.id, v)
            bot.register_next_step_handler(sent, ptpid1)
    except IndexError:
        bot.send_message(message.from_user.id, 'Ты прошел тест!')
        bot.send_message(message.from_user.id, f'Ты ответил правильно на {kpo} вопросов и неправильно на {kno} вопросов и твой результат составляет {int(((kpo) / kv) * 100)}%')
        kno, kpo, kv = 0, 0, 0
    
def recurs1(message):
    global cuv, clvvt, idnt
    vo = message.text
    vo = vo.split(':')
    cuv[vo[0]] = vo[1]
    if clvvt == 1:
        bot.send_message(message.chat.id, f"Я записал ваш тест {cuv}")
        bot.send_message(message.chat.id, f"Вот ваш id {idnt}")
        
        connection = sqlite3.connect('my_database.db')
        cursor = connection.cursor()

        cursor.execute('INSERT INTO Test (ind, quest) VALUES (?, ?)', (idnt, str(cuv)))
        

        connection.commit()
        connection.close()
        idnt += 1

    else:
        sent = bot.send_message(message.chat.id, "Принял")
        bot.register_next_step_handler(sent, recurs2)
        clvvt -= 1


def recurs2(message):
    global cuv, clvvt, idnt
    vo = message.text
    vo = vo.split(':')
    cuv[vo[0]] = vo[1]
    if clvvt == 1:
        bot.send_message(message.chat.id, f"Я записал ваш тест {cuv}")
        bot.send_message(message.chat.id, f"Вот ваш id {idnt}")
        connection = sqlite3.connect('my_database.db')
        cursor = connection.cursor()

        cursor.execute('INSERT INTO Test (ind, quest) VALUES (?, ?)', (idnt, str(cuv)))

        connection.commit()
        connection.close()
        idnt += 1
    else:
        sent = bot.send_message(message.chat.id, "Принял")
        bot.register_next_step_handler(sent, recurs1)
        clvvt -= 1

def hello(message):
    global v, kno, kpo
    message_to_save = message.text
    print(v)
    if message_to_save == m1.get(v):
        m1v.remove(v)
        kpo += 1
        v = random.choice(m1v)
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtback = types.KeyboardButton('Назад в меню')
        markup.add(itembtback)
        bot.send_message(message.from_user.id, 'Правильно! Идём дальше')
        bot.send_message(message.chat.id, "Второй вопрос:", reply_markup=markup)
        sent = bot.send_message(message.chat.id, v)
        bot.register_next_step_handler(sent, hello1)
    elif message_to_save == 'Назад в меню':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Помощь')
        itembtn2 = types.KeyboardButton('Тесты')
        markup.add(itembtn1, itembtn2)
        bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'Неправильно')
        kno += 1
        m1v.remove(v)
        v = random.choice(m1v)
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtback = types.KeyboardButton('Назад в меню')
        markup.add(itembtback)
        bot.send_message(message.from_user.id, 'Идём дальше')
        bot.send_message(message.chat.id, "Второй вопрос:", reply_markup=markup)
        sent = bot.send_message(message.chat.id, v)
        bot.register_next_step_handler(sent, hello1)

def hello1(message):
    global v, kpo, kno
    message_to_save = message.text
    if message_to_save == m1.get(v):
        m1v.remove(v)
        kpo += 1
        v = random.choice(m1v)
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtback = types.KeyboardButton('Назад в меню')
        markup.add(itembtback)
        bot.send_message(message.from_user.id, 'Правильно! Идём дальше')
        bot.send_message(message.chat.id, "Третий вопрос:", reply_markup=markup)
        sent = bot.send_message(message.chat.id, v)
        bot.register_next_step_handler(sent, hello2)
    elif message_to_save == 'Назад в меню':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Помощь')
        itembtn2 = types.KeyboardButton('Тесты')
        markup.add(itembtn1, itembtn2)
        bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'Неправильно')
        m1v.remove(v)
        kno += 1
        v = random.choice(m1v)
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtback = types.KeyboardButton('Назад в меню')
        markup.add(itembtback)
        bot.send_message(message.from_user.id, 'Идём дальше')
        bot.send_message(message.chat.id, "Третий вопрос:", reply_markup=markup)
        sent = bot.send_message(message.chat.id, v)
        bot.register_next_step_handler(sent, hello2)

def hello2(message):
    global m1v, kpo, kno
    message_to_save = message.text
    if message_to_save == m1.get(v):
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        kpo += 1
        itembtback = types.KeyboardButton('Назад в меню')
        markup.add(itembtback)
        bot.send_message(message.from_user.id, 'Правильно! Ты прошёл тест')
        bot.send_message(message.from_user.id, f'Ты ответил правильно на {kpo} вопросов и неправильно на {kno} вопросов и твой результат составляет {int(((kpo) // 3) * 100)}%', reply_markup=markup)
        kno, kpo = 0, 0
        m1v = list(m1.keys())
    elif message_to_save == 'Назад в меню':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Помощь')
        itembtn2 = types.KeyboardButton('Тесты')
        markup.add(itembtn1, itembtn2)
        bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'Неправильно')
        kno += 1
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtback = types.KeyboardButton('Назад в меню')
        markup.add(itembtback)
        bot.send_message(message.from_user.id, 'Ты прошёл тест', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Ты ответил правильно на {kpo} вопросов и неправильно на {kno} вопросов и твой результат составляет {int(((kpo) // 3) * 100)}%', reply_markup=markup)
        kno, kpo = 0, 0
        m1v = list(m1.keys())
def hellor1(message):
    message_to_save = message.text
    if message_to_save.lower() == 'да':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtback = types.KeyboardButton('Назад в меню')
        markup.add(itembtback)
        bot.send_message(message.from_user.id, 'Правильно! Идём дальше')
        bot.send_message(message.chat.id, "Второй вопрос:", reply_markup=markup)
        sent = bot.send_message(message.chat.id, "Сколько букв в слове арбуз?")
        bot.register_next_step_handler(sent, hellor2)
    elif message_to_save == 'Назад в меню':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Помощь')
        itembtn2 = types.KeyboardButton('Тесты')
        markup.add(itembtn1, itembtn2)
        bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'Неправильно')
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtback = types.KeyboardButton('Назад в меню')
        markup.add(itembtback)
        bot.send_message(message.from_user.id, 'Идём дальше')
        bot.send_message(message.chat.id, "Второй вопрос:", reply_markup=markup)
        sent = bot.send_message(message.chat.id, "Сколько букв в слове арбуз?")
        bot.register_next_step_handler(sent, hellor2)
def hellor2(message):
    message_to_save = message.text
    if message_to_save.lower() == '5' or message_to_save.lower().lower() == 'пять':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtback = types.KeyboardButton('Назад в меню')
        markup.add(itembtback)
        bot.send_message(message.from_user.id, 'Правильно! Идём дальше')
        bot.send_message(message.chat.id, "Третий вопрос:", reply_markup=markup)
        sent = bot.send_message(message.chat.id, "Какая буква пропущена в слове П(а/о)льто")
        bot.register_next_step_handler(sent, hellor3)
    elif message_to_save == 'Назад в меню':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Помощь')
        itembtn2 = types.KeyboardButton('Тесты')
        markup.add(itembtn1, itembtn2)
        bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'Неправильно')
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtback = types.KeyboardButton('Назад в меню')
        markup.add(itembtback)
        bot.send_message(message.from_user.id, 'Идём дальше')
        bot.send_message(message.chat.id, "Третий вопрос:", reply_markup=markup)
        sent = bot.send_message(message.chat.id, "Какая буква пропущена в слове П(а/о)льто")
        bot.register_next_step_handler(sent, hellor3)
def hellor3(message):
    message_to_save = message.text
    if message_to_save.lower() == 'а':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtback = types.KeyboardButton('Назад в меню')
        markup.add(itembtback)
        bot.send_message(message.from_user.id, 'Правильно! Ты прошёл тест')
        bot.send_message(message.from_user.id, f'Ты ответил правильно на {kpo} вопросов и неправильно на {kno} вопросов и твой результат составляет {int(((kpo) // 3) * 100)}%', reply_markup=markup)
        kno, kpo = 0, 0
    elif message_to_save == 'Назад в меню':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Помощь')
        itembtn2 = types.KeyboardButton('Тесты')
        markup.add(itembtn1, itembtn2)
        bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'Неправильно')
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtback = types.KeyboardButton('Назад в меню')
        markup.add(itembtback)
        bot.send_message(message.from_user.id, 'Ты прошёл тест')
        bot.send_message(message.from_user.id, f'Ты ответил правильно на {kpo} вопросов и неправильно на {kno} вопросов и твой результат составляет {int(((kpo) // 3) * 100)}%', reply_markup=markup)
        kno, kpo = 0, 0
bot.polling(non_stop=True)