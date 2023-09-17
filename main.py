import telebot
from telebot import types
import keyboard
import config
import random
import game

token = config.token()
bot = telebot.TeleBot(token, num_threads=config.threads())

people = [] #id 
nick_name = [] #ники
people_message = {} #id чата
people_message_id = {}#id сообщения
global_message = {} #id сообщений в группе
people_status = {}#стата
kick_message = {}# сообщение кика
vote = {}#колво голосов голосования
stats = ["возраст","пол","тип телосложения","рост","работу","фобия","состояние здоровья","хобби","черту характера","инвентарь"]#Название статов
stats_id = [0,1,2,3,4,5,6,7,8,9]


print(config.commands())

def randomizer(probabilities):
    # Получить сумму всех значений вероятностей
    total = sum(probabilities.values())

    # Сгенерировать случайное число от 0 до суммы вероятностей
    rand_num = random.uniform(0, total)

    # Итерироваться по вероятностям и возвращать соответствующее значение
    cumulative_sum = 0
    for key, value in probabilities.items():
        cumulative_sum += value
        if rand_num <= cumulative_sum:
            return key

def choice():
    global people, people_status, nick_name, vote
    bot.send_message(config.chat_id(),"Игра началась!")
    for i in range(0,len(people)):
        bot.send_message(people[i],"Игра началась!")
        inventory0 = game.inventory()
        inventory = [inventory0[random.randint(0,len(inventory0) - 1)],0]#предмет 
        sex0 = game.sex()
        sex = [sex0[random.randint(0,len(sex0) - 1)],0]#пол
        age = [random.randint(18,60),0]#возраст
        body_type0 = game.body_type()
        body_type = [body_type0[random.randint(0,len(body_type0) - 1)],0]#телосложение
        height = [random.randint(150,200),0]
        hobby0 = game.hobby()
        hobby = [hobby0[random.randint(0,len(hobby0) - 1)],0]#хобби
        phobia0 = game.phobia()
        phobia = [phobia0[random.randint(0,len(phobia0) - 1)],0]#фобия
        phobia_explanation0 = game.phobia_explanation()
        phobia_explanation = phobia_explanation0[phobia[0]]#фобия пояснение
        probabilities = {'A': 0.6, 'B': 0.4}
        health0 = game.health()
        health = [health0[random.randint(0,49)] if randomizer(probabilities) == "B" else "Здоров",0]
        trait0 = game.trait()
        trait = [trait0[random.randint(0,len(trait0) - 1)],0]#черта характера
        work0 = game.work()
        work = [work0[random.randint(0,len(work0) - 1)],0]#работа
        work_explanation0 = game.work_explanation()
        work_explanation = work_explanation0[work[0]]#работа пояснение
        people_status[people[i]] = [age,sex,body_type,height,work,phobia,health,hobby,trait,inventory,work_explanation,phobia_explanation]
        bot.send_message(people[i],config.personal_message(people_status[people[i]]))
    for i in range(0, len(people)):
        chat = bot.get_chat_member(people[i],people_message[people[i]])
        username = chat.user.username
        nick_name.append(username)
        message = bot.send_message(config.chat_id(),config.global_message(username,people_status[people[i]]))
        global_message[people[i]] = message.message_id
keyboard.add_hotkey("ctrl+space", choice)

def menu():
    global stats
    for i in range(0,len(people)):
        keyboard = types.InlineKeyboardMarkup()
        stats_user = people_status[people[i]]
        for n in range(0,len(stats)):
            if stats_user[n][1] == 0:
                keyboard.add(types.InlineKeyboardButton(text=f"Открыть {stats[n]}", callback_data=stats[n]))
        bot.send_message(people[i], "Меню взаимодействий:", reply_markup=keyboard)
        keyboard = 0
keyboard.add_hotkey("ctrl+1",menu)

def vote_menu():
    global kick_message
    for i in range(0,len(people)):
        keyboard0 = types.InlineKeyboardMarkup()
        for n in range(0,len(people)):
            chat = bot.get_chat_member(people[i],people_message[people[i]])
            username = chat.user.username
            keyboard0.add(types.InlineKeyboardButton(text=f"{username}", callback_data=username))
        msg = bot.send_message(people[i], "Кого вы хотите кикнуть?:", reply_markup=keyboard0)
        kick_message[people[i]] = msg.message_id
        keyboard0 = 0
keyboard.add_hotkey("ctrl+2", vote_menu)

def kick():
    global vote,people,nick_name
    max_votes = max(vote.values())  # Наибольшее количество голосов
    max_indices = [i for i, v in vote.items() if v == max_votes]  # Индексы наибольших элементов
    print(max_indices)  # Индексы наибольших элементов
    for index in max_indices:
        print("Игрок", index, "был выбран голосованием")
    kick = int(input("Введите номер игрока, который будет изгнан")) - 1
    kick_index = nick_name.index(max_indices[int(kick)])
    print(kick_index)
    bot.send_message(people[kick_index],config.personal_lose())
    bot.send_message(config.chat_id(),config.global_lose(nick_name[kick_index]))
    people.remove(people[kick_index])
    nick_name.remove(nick_name[kick_index])
keyboard.add_hotkey("ctrl+3",kick)


@bot.message_handler(commands=["check"])
def handle_text(message):
    print(len(vote), len(people))
    print(vote)

@bot.message_handler(commands=["start"])
def handle_text(message):
    people.append(message.chat.id)
    people_message[message.chat.id] = message.from_user.id

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    global stats, vote, people, nick_name, people, global_message, kick_message
    chat = bot.get_chat_member(call.from_user.id,people_message[call.from_user.id])
    username = chat.user.username
    if call.data in stats:
        stats_user = people_status[call.from_user.id]
        edit_stats = stats_user[stats.index(call.data)]
        edit_stats[1] = 1
        stats_user[stats.index(call.data)] = edit_stats
        people_status[call.from_user.id] = stats_user
        text = config.personal_message(people_status[call.from_user.id])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text)
        chat = bot.get_chat_member(call.message.chat.id,people_message[call.message.chat.id])
        username = chat.user.username
        text1 = config.global_message(username,people_status[call.message.chat.id])
        bot.edit_message_text(chat_id=config.chat_id(), message_id=global_message[call.message.chat.id], text=text1)
    elif call.data in nick_name:
        if vote.get(username, "None") == "None": 
            vote[username] = 1
            bot.edit_message_text(chat_id=call.from_user.id,message_id=kick_message[call.from_user.id],text=config.vote_message())
        else:
            summ = vote[username]
            vote[username] = summ + 1
            bot.edit_message_text(chat_id=call.from_user.id,message_id=kick_message[call.from_user.id],text=config.vote_message())
        print(vote)

bot.polling(none_stop=True)