def token():
    text="6681458209:AAGV0sZP32UxB25rX5K5DhMuw1I46rY6nKA"
    return text

def threads():
    text=32
    return text

def chat_id():
    text=-1001951370230
    return text

def commands():
    text="Комманды:\nctrl+space - старт игры (выдача характеристик)\nctrl+1 - открытие характеристик\nctrl+2 - меню голосования\nctrl+3 - кик игрока"
    return text

def personal_message(people_status):
    people_status = people_status
    age = people_status[0]
    sex = people_status[1]
    body_type = people_status[2]
    height = people_status[3]
    work = people_status[4]
    phobia = people_status[5]
    health = people_status[6]
    hobby = people_status[7]
    trait = people_status[8]
    inventory = people_status[9]
    work_explanation = people_status[10]
    phobia_explanation = people_status[11]
    age_status = "Скрыт" if age[1] == 0 else "Открыт"
    sex_status = "Скрыт" if sex[1] == 0 else "Открыт"
    body_type_status = "Скрыт" if people_status[2][1] == 0 else "Открыт"
    height_status = "Скрыт" if people_status[3][1] == 0 else "Открыт"
    phobia_status = "Скрыт" if people_status[5][1] == 0 else "Открыт"
    health_status = "Скрыт" if people_status[6][1] == 0 else "Открыт"
    work_status = "Скрыт" if people_status[4][1] == 0 else "Открыт"
    trait_status = "Скрыт" if people_status[8][1] == 0 else "Открыт"
    inventory_status = "Скрыт" if people_status[9][1] == 0 else "Открыт"
    hobby_status = "Скрыт" if people_status[7][1] == 0 else "Открыт"
    text = f"Ваша статистика:\nВозраст: {age[0]} - {age_status}\nПол: {sex[0]} - {sex_status}\nТип телосложения: {body_type[0]} - {body_type_status}\nРост: {height[0]} - {height_status}\nРабота: {work[0]} - {work_status}\nФобия: {phobia[0]} - {phobia_status}\nСостояние здоровья: {health[0]} - {health_status}\nХобби: {hobby[0]} - {hobby_status}\nЧерта характера: {trait[0]} - {trait_status}\nВ инвентаре: {inventory[0]} - {inventory_status}\n‼Пояснение‼:\n{work[0]} - {work_explanation}\n{phobia[0]} - {phobia_explanation}"
    return text

def global_message(username,people_status):
    people_status = people_status
    age = people_status[0]
    sex = people_status[1]
    body_type = people_status[2]
    height = people_status[3]
    work = people_status[4]
    phobia = people_status[5]
    hobby = people_status[7]
    trait = people_status[8]
    health = people_status[6]
    inventory = people_status[9]
    age_status = "Скрыт" if people_status[0][1] == 0 else age[0]
    sex_status = "Скрыт" if people_status[1][1] == 0 else sex[0]
    body_type_status = "Скрыт" if people_status[2][1] == 0 else body_type[0]
    height_status = "Скрыт" if people_status[3][1] == 0 else height[0]
    work_status = "Скрыт" if people_status[4][1] == 0 else work[0]
    phobia_status = "Скрыт" if people_status[5][1] == 0 else phobia[0]
    hobby_status = "Скрыт" if people_status[7][1] == 0 else hobby[0]
    trait_status = "Скрыт" if people_status[8][1] == 0 else trait[0]
    health_status = "Скрыт" if people_status[6][1] == 0 else health[0]
    inventory_status = "Скрыт" if people_status[9][1] == 0 else inventory[0]
    text = f"Статистика {username}:\nВозраст: {age_status}\nПол: {sex_status}\nТип телосложения: {body_type_status}\nРост: {height_status}\nРабота: {work_status}\nФобия: {phobia_status}\nСостояние здоровья: {health_status}\nХобби: {hobby_status}\nЧерта характера: {trait_status}\nВ инвентаре: {inventory_status}"
    return text

def vote_message():
    text = "Ваш голос был учитан."
    return text

def global_lose(name):
    text = f"Игрок {name} был исключён голосованием."
    return text

def personal_lose():
    text = "Вы были исключены голосованием."
    return text

def pass_vote():
    text = "Вы пропустили голосование"
    return text

class error:
    def dontstartgame():
        text = "Ошибка. Игра ещё не началась!"
        return text
    def startgame():
        text = "Ошибка. Игра уже началась!"
        return text
    def emptyvotelist():
        text = "Ошибка. Список голования пуст!"
        return text
    def emptyplayerlist():
        text = "Ошибка. Список игроков пуст!"
        return text