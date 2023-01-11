import random

import telebot
from telebot import types
from random import shuffle


bot = telebot.TeleBot('5886265811:AAFyIIGaJzICuITu426SRu_9Az0nSP6cgmk')
bot.set_webhook()

#agent_photo = open(f"{new_agent_photo}.jpeg","rb")

Sage_photo = open("Sage.jpeg","rb")
Brimstone_photo = open("Brimstone.jpeg","rb")
Viper_photo = open("viper.jpeg","rb")
Omen_photo = open("omen.jpeg","rb")
Killjoy_photo = open("killjoy.jpeg","rb")
Cypher_photo = open("cypher.jpeg","rb")
Sova_photo = open("sova.jpeg","rb")
Phoenix_photo = open("phoenix.jpeg","rb")
Jett_photo = open("jett.jpeg", "rb")
Reyna_photo = open("reyna.jpeg", "rb")
Raze_photo = open("raze.jpeg", "rb")
Breach_photo = open("breach.jpeg", "rb")
Skye_photo = open("skye.jpeg", "rb")
Yoru_photo = open("yoru.jpeg", "rb")
Astra_photo = open("astra.jpeg", "rb")
KAYO_photo = open("kayo.jpeg", "rb")
Chamber_photo = open("chamber.jpeg", "rb")
Neon_photo = open("neon.jpeg", "rb")
Fade_photo = open("fade.jpeg", "rb")
Harbor_photo = open("harbor.jpeg","rb")


agents = {
'Brimstone' : ['Пассивный','Командный игрок','Много общаюсь','Саппорт','Легкий','Скиллы'],
'Viper' : ['Пассивный','Командный игрок/Полагаюсь на себя','Много общаюсь/Молча концентрируюсь','Люркер','Сложный','Скиллы'],
'Omen' : ['Активный/Пассивный','Командный игрок/Полагаюсь на себя','Много общаюсь','Саппорт','Легкий','Скиллы'],
'Killjoy' : ['Пассивный','Командный игрок/Полагаюсь на себя','Много общаюсь/Молча концентрируюсь','Люркер','Легкий','Скиллы'],
'Cypher' : ['Пассивный','Полагаюсь на себя','Много общаюсь/Молча концентрируюсь','Люркер','Сложный','Скиллы'],
'Sova' : ['Пассивный','Командный игрок','Много общаюсь','Саппорт','Сложный','Скиллы'],
'Sage' : ['Пассивный/Активный','Полагаюсь на себя/Командный игрок','Много общаюсь','Саппорт/Керри','Легкий','Аим'],
'Phoenix' : ['Активный','Полагаюсь на себя','Много общаюсь/Молча концентрируюсь','Керри','Легкий','Скиллы'],
'Jett' : ['Активный','Полагаюсь на себя','Много общаюсь/Молча концентрируюсь','Керри','Сложный','Аим'],
'Reyna' : ['Активный','Полагаюсь на себя','Много общаюсь/Молча концентрируюсь','Керри','Легкий','Аим'],
'Raze' : ['Активный','Полагаюсь на себя/Командный игрок','Много общаюсь/Молча концентрируюсь','Керри','Сложный','Аим'],
'Breach' : ['Активный','Командный игрок','Много общаюсь','Саппорт','Легкий','Скиллы'],
'Skye' : ['Активный','Командный игрок','Много общаюсь','Саппорт','Легкий','Скиллы'],
'Yoru' : ['Активный','Командный игрок/Полагаюсь на себя','Много общаюсь/Молча концентрируюсь','Люркер/Керри','Сложный','Скиллы'],
'Astra' : ['Пассивный','Командный игрок','Много общаюсь','Саппорт','Сложный','Скиллы'],
'KAY/O' : ['Активный','Полагаюсь на себя/Командный игрок','Много общаюсь/Молча концентрируюсь','Саппорт/Керри','Легкий','Скиллы'],
'Chamber' : ['Пассивный/Активный','Полагаюсь на себя','Много общаюсь/Молча концентрируюсь','Люркер','Легкий','Аим'],
'Neon' : ['Активный','Полагаюсь на себя','Много общаюсь/Молча концентрируюсь','Керри','Сложный','Аим'],
'Fade' : ['Пассивный/Активный','Командный игрок/Полагаюсь на себя','Много общаюсь/Молча концентрируюсь','Саппорт','Сложный','Скиллы'],
'Harbor' : ['Пассивный','Командный игрок','Много общаюсь','Саппорт','Сложный','Скиллы']
}

id = 0

def make_pair(x,y):
    return lambda n: x if n==0 else y
def first_element(p):
    return p(0)

def second_element(p):
    return p(1)

first_question = "Имеется ли у вас опыт в шутерах? (н-р: CS:GO,Warface,Warzone и проч.)"
second_qeustion = "Где бы вы предпочли находиться? В гуще событий или координировать действия команды из тыла?"
third_qeustion = "Полагаетесь ли вы на своих сокомандников или чаще надеетесь только на себя?"
forth_question = "Много ли вы говорите во время игры или стараетесь оставаться немногословным?"
fifth_question = "Какой стиль ведения игры вам ближе?"
six_question = "При возникновении опастной ситуации на что вы будете полагаться: стрельба(аим) или способнойсти персонажа(скиллы)?"


first_answers = (make_pair('Да, я давно играю', 'Сложный'),
                 make_pair('Нет, я новичок в этом жанре игр', 'Легкий'),)

second_answers = (make_pair('Я люблю быть в гуще событий', 'Активный'),
                  make_pair('Я люблю оставаться в тылу', 'Пассивный'),
                  make_pair('И то и другое', 'Пассивный/Активный'),)

third_answers =  (make_pair('Я люблю играть в команде', 'Командный игрок'),
                  make_pair('Нет, я чаще играю один', 'Полагаюсь на себя'),
                  make_pair('Зависит от ситуации', 'Командный игрок/Полагаюсь на себя'),)

forth_answers =  (make_pair('Я люблю много общаться', 'Много общаюсь'),
                  make_pair('Молча концетрируюсь', 'Молча концентрируюсь'),
                  make_pair('По настроению', 'Много общаюсь/Молча концентрируюсь'),)

fifth_answers =  (make_pair('Расчитываю на свои силы', 'Керри'),
                  make_pair('Предпочту проработанную тактику', 'Саппорт'),
                  make_pair('Могу пойти на риск, если надо', 'Саппорт/Керри'),
                  make_pair('Расчитываю на стратегию', 'Люркер'),)

six_answers =  (make_pair('Аим', 'Аим'),
                make_pair('Скиллы', 'Скиллы'))


question_one = make_pair(first_question,first_answers)
question_two = make_pair(second_qeustion,second_answers)
question_three = make_pair(third_qeustion,third_answers)
question_four = make_pair(forth_question,forth_answers)
question_five = make_pair(fifth_question,fifth_answers)
question_six = make_pair(six_question,six_answers)


list_of_questions = [question_one,question_two,question_three,question_four,question_five,question_six]

keywords = []
id_of_first = 0

def get_question_by_id(id):
    return list_of_questions[id]

@bot.message_handler(commands=["start"])
def get_start(message):
    global id
    global keywords
    global id_of_first

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #btn1 = types.KeyboardButton("Старт")
    #markup.add(btn1)
    message1 = bot.send_message(message.chat.id,
                     text="Привет! Я тестовый бот для Valorant!".format(
                         message.from_user), reply_markup=markup)
    id_of_first = message1.id
    id = 0
    keywords.clear()
    i = 0
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for i in range(0,len(second_element(list_of_questions[id]))):
        keyboard.row(telebot.types.InlineKeyboardButton(first_element(second_element(list_of_questions[id])[i]),
                                                        callback_data = f"{i}"))
        i+=1

    bot.send_message(message.chat.id,first_element(list_of_questions[id]), reply_markup=keyboard)

def get_next_question():
    print('a')

@bot.callback_query_handler(func = lambda call:True)
def call(call):
    global id
    global keywords
    global agents_photo
    print(id,len(list_of_questions))
    if call.data == 'restart':
        print("call.data == restart")
        bot.delete_message(call.message.chat.id, id_of_first) #Удаление приветствия
        bot.delete_message(call.message.chat.id, call.message.id-1) # Удаление фото агента
        bot.delete_message(call.message.chat.id, call.message.id) # Удаление кнопки "пройти заново"

        id = 0
        keywords.clear()
        get_start(call.message)
        return

    if call.message:

        list_of_current_keys = []
        i = 0
        for i in range(0, len(second_element(list_of_questions[id]))):
            list_of_current_keys.append(i)
            i += 1

        if int(call.data) in list_of_current_keys:

            keywords.append(second_element(second_element(list_of_questions[id])[int(call.data)]))
            id+=1
            if id == len(list_of_questions):
                bot.delete_message(call.message.chat.id, call.message.id) #Удаление последнего сообщения

                best_agent = get_analize(keywords)

                markup = types.InlineKeyboardMarkup(row_width=2)
                restart_button = types.InlineKeyboardButton("Пройти заново",
                                                      callback_data='restart')
                markup.add(restart_button)

                if best_agent == "KAY/O":
                    print(best_agent)
                    best_agent = "KAYO"
                    #new_best_agent_photo = best_agent + "_photo"
                    #print(new_best_agent_photo)
                    #new_best_agent_photo = "KAYO_photo"
                    agent_photo = open(f"{best_agent}.jpeg", "rb")
                    bot.send_photo(call.message.chat.id,agent_photo)
                    message1 = bot.send_message(call.message.chat.id, f"Вам лучше играть на {best_agent}",
                                     reply_markup=markup)

                else:
                    print(best_agent)
                    #new_best_agent_photo = best_agent + "_photo"
                    agent_photo = open(f"{best_agent}.jpeg", "rb")
                    print(best_agent)
                    bot.send_photo(call.message.chat.id,agent_photo)
                    print(best_agent)
                    print(keywords)
                    message1 = bot.send_message(call.message.chat.id, f"Вам лучше играть на {best_agent}",
                                                reply_markup=markup)

            else:
                i = 0
                keyboard = types.InlineKeyboardMarkup(row_width=2)
                for i in range(0, len(second_element(list_of_questions[id]))):
                    keyboard.row(
                        telebot.types.InlineKeyboardButton(first_element(second_element(list_of_questions[id])[i]),
                                                               callback_data = f"{i}"))
                    i += 1
                message1 = bot.send_message(call.message.chat.id, first_element(list_of_questions[id]), reply_markup=keyboard)
                bot.delete_message(call.message.chat.id, message1.id-1) #удаление предпоследнего сообщения


def get_analize(keywords):
    global agents
    agents_score = {agent: 0 for agent in agents}
    max_score = 0
    #print(keywords)
    for key in keywords:
        for agent,features in agents.items():
            #print(agents.items())
            if key in features:
                print(agent)
                agents_score[agent] +=1
                max_score = max(agents_score[agent],max_score)
    best_agents = []
    print(agents_score)
    for agent, score in agents_score.items():
        if score == max_score:
            best_agents.append(agent)
    idx = 0
    if len(best_agents)>1:
        idx = random.randint(0,len(best_agents)-1)
    return best_agents[idx]


if __name__ == '__main__':
     bot.polling()