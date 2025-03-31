#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

from random import randint
import telebot

from config import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

randonJoke = ['Одну девочку в школе называли Крокодилом. Но не потому, что она была некрасивая, а потому, что один раз она затащила в реку оленя и сожрала его.', 
              'Всякая женщина знает, что нет ничего полезнее в хозяйстве, чем мужчина, чувствующий свою вину.', 
              'Выпускница сельхозтехникума стоит посреди поля с кабачками, чешет затылок и бормочет: «Как же эти твари икру то мечут?!»', 
              'Мало кто знает, что преподаватели после экзамена ведут себя точно так же, как новобрачные после свадьбы – рассматривают подарки.',
              'Лекция на филфаке. «В английском языке, – говорит профессор, '+
              '– двойное отрицание дает утверждение. В других языках, например в русском, двойное отрицание всё равно обозначает отрицание. '+
              'Но нет ни одного языка, в котором двойное утверждение обозначало бы отрицание».Голос с задней парты: «Ага, конечно».', 
              'Интервью с Биллом Гейтсом. '+
              '– Я разработал абсолютное, стопроцентно эффективное средство против спама и выложил его на своём сайте для бесплатного скачивания.'+
              '– А вы уверены, что оно стопроцентное?'+
              '– Конечно! Ведь уже через несколько дней на мой ящик пришло 26 175 095 писем от благодарных пользователей!',
              'Я вообще оптимист. А оптимист - это человек, который приходит на кладбище и вместо крестов там видит плюсы.',
              'Только американцы уверены, что от их санкций может опечалиться народ, который собирается толпой вокруг сапера - рванет или нет.',
              'Только наш человек, наступая на грабли второй раз, радуется, что их еще не украли.',
              'Как можно было назвать слабым пол, который отнимает столько сил?',
              'Только наш человек заходит в музей, чтобы согреться.',
              'Согласно классической русской диете есть надо один раз в день. Но с утра до вечера!',
              'Толстый человек это звучит оскорбительно. Надо говорить «горизонтально ориентированный».',
              'Как же надо было разочароваться в людях, чтобы словом «Дружба» назвать бензопилу?',
              'Интересно, почему американцы показывают средний палец, а русские руку по локоть?']

randomMath = [{"Question":"2x \\= 10",
               "Answer":"Ответ x \\= 5"},
               {"Question":"12x \\= 1",
               "Answer":"Ответ x \\= 1/12"},
               {"Question":"2x \\- 1 \\= 5",
               "Answer":"Ответ x \\= 3"},
               {"Question":"20x \\+ 1 \\= 1",
               "Answer":"Ответ x \\= 0"},
               {"Question":"x \\+ 1 \\= 10",
               "Answer":"Ответ x \\= 9"},
               {"Question":"5x \\= 10",
               "Answer":"Ответ x \\= 2"}]

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "На данный момоент бот может обрабатывать следующе команды: /start, /joke, /math, /about, 'Привет', 'Как дела?', 'Доброе утро'")
# Handle '/math'
@bot.message_handler(commands=['math'])
def send_welcome(message):
    example = randomMath[randint(0,len(randomMath)-1)]
    bot.send_message(message.chat.id, f"{example['Question']} || {example['Answer']}||", parse_mode='MarkdownV2')

# Handle '/joke'
@bot.message_handler(commands=['joke'])
def send_welcome(message):
    Joke = randonJoke[randint(0,len(randonJoke)-1)]
    bot.send_message(message.chat.id, Joke)

# Handle '/about'
@bot.message_handler(commands=['about'])
def send_welcome(message):
    bot.send_message(message.chat.id, """Куратова Анна Евгеньевна Группа Т-233902у""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text== 'Привет':
        bot.reply_to(message, f"Привет, {message.from_user.first_name}")
    elif message.text=='Как дела?':
        bot.reply_to(message, "Пока еще нормально")
    elif message.text=='Доброе утро':
        bot.reply_to(message, "Что вы хотите этим сказать? Просто желаете мне доброго утра? Или утверждаете, что утро сегодня доброе — неважно, что я о нём думаю? Или имеете в виду, что нынешним утром все должны быть добрыми?")
    else:
        bot.reply_to(message, "Я могу вам ответить только на такие слова: 'Привет', 'Как дела?', 'Доброе утро' ")

bot.infinity_polling()