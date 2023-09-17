def body_type():#телосложение
    text = ["Худой","Полный","Стройный"]
    return text

def sex():#пол
    text = ["Мужской", "Женский"]
    return text

def inventory():#инвентарь
    text = ['Запас воды на 1 неделю',
            'Запас воды на 2 недели',
            'Запас воды на 3 недели',
            'Запас воды на месяц',
            'Запас воды на полгода',
            'Запас консервированной еды на 1 неделю',
            'Запас консервированной еды на 2 недели',
            'Запас консервированной еды на 3 недели',
            'Запас консервированной еды на месяц',
            'Запас консервированной еды на полгода',
            'Медицинский кит',
            'Постельное белье',
            'Мобильная связь',
            'Рация',
            'Фонарик с запасными батареями',
            'Спички и зажигалка',
            'Аптечка первой помощи',
            'Пленка для укрытия',
            'Рации на случай экстренной связи',
            'Солнечные панели и аккумуляторы для зарядки устройств',
            'Радиоприемник',
            'Портативный генератор',
            'Спальники',
            'Приборы для очистки воздуха',
            'Печь или плита на газе',
            'Лом и инструменты для ремонтных работ',
            'Резервные запчасти',
            'Мультитул',
            'Книги и настольные игры',
            'Радиоактивный детектор']
    return text

def hobby():#хобби
    text = ["Готовить новые блюда",
          "Читать книги разных жанров",
          "Заниматься йогой",
          "Рисовать или рисовать",
          "Играть на музыкальных инструментах",
          "Собирать пазлы",
          "Заниматься садоводством",
          "Фотографировать природу или людей",
          "Заниматься рукоделием",
          "Пробовать новые виды спорта",
          "Лазить по горам или путешествовать",
          "Читать о звездах и астрономии",
          "Собирать марки или монеты",
          "Участвовать в театральных постановках или музыкальных концертах",
          "Ухаживать за домашними животными",
          "Посещать выставки и художественные галереи",
          "Заниматься паркуром или спортивной гимнастикой",
          "Заниматься активными играми на открытом воздухе",
          "Играть в настольные игры с друзьями",
          "Разрабатывать приложения или создавать веб-сайты",
          "Заниматься фотографией пейзажей или архитектуры",
          "Учить новые языки или изучать культуры разных стран",
          "Заниматься реставрацией старой мебели или предметов",
          "Собирать модели кораблей или самолетов",
          "Пробовать новые виды медитации или релаксации",
          "Заниматься сноубордом или горными лыжами",
          "Заниматься искусством переплетения"]
    return text

def phobia():#фобия
    text = ["Арахнофобия",
            "Клаустрофобия",
            "Гловофобия",
            "Акрофобия",
            "Агорафобия",
            "Гемофобия",
            "Танатофобия",
            "Клаунофобия",
            "Некрофобия",
            "Зоофобия",
            "Ксенофобия",
            "Эметофобия",
            "Белофобия",
            "Энтомофобия",
            "Офидиофобия",
            "Кариесофобия",
            "Картегофобия",
            "Социофобия",
            "Хромофобия",
            "Дентофобия",
            "Офтальмофобия",
            "Фармакофобия"]
    return text

def phobia_explanation():#фобия поясненик
    text = {"Арахнофобия":"страх перед пауками",
            "Клаустрофобия":"страх перед замкнутыми пространствами",
            "Гловофобия":"страх общения с незнакомыми людьми",
            "Акрофобия":"страх высоты",
            "Агорафобия":"страх открытых пространств",
            "Гемофобия":"страх крови или ее просмотр",
            "Танатофобия":"страх смерти",
            "Клаунофобия":"страх перед клоунами",
            "Некрофобия":"страх перед трупами",
            "Зоофобия":"страх перед животными",
            "Ксенофобия":"страх перед незнакомцами и иностранцами",
            "Эметофобия":"страх перед рвотой или видом рвоты",
            "Белофобия":"страх перед миром",
            "Энтомофобия":"страх насекомых",
            "Офидиофобия":"страх змей",
            "Кариесофобия":"страх перед кариесом",
            "Картегофобия":"страх перед действиями",
            "Социофобия":"страх перед обществом",
            "Хромофобия":"страх перед цветом",
            "Дентофобия":"страх перед стоматологическим лечением",
            "Офтальмофобия":"страх перед глазами",
            "Фармакофобия":"страх перед медицинскими препаратами"}
    return text

def health():#болезни
    text = ["Грипп",
            "Насморк",
            "Бронхит",
            "Гастрит",
            "Ангина",
            "Артрит",
            "Диабет",
            "Кашель",
            "Мигрень",
            "Астма",
            "Гепатит",
            "ОРВИ",
            "Отит",
            "Энцефалит",
            "Инсульт",
            "Анемия",
            "Эпилепсия",
            "Аллергия",
            "Остеопороз",
            "Ревматизм",
            "Пневмония",
            "Гастроэнтерит",
            "Панкреатит",
            "Холера",
            "Бронхиальная астма",
            "Оссификация",
            "Глаукома",
            "Гипертония",
            "Диарея",
            "Бронхит",
            "Корь",
            "Туберкулез",
            "Опсессивно-компульсивное расстройство",
            "Экзема",
            "Сердечная недостаточность",
            "Аутоиммунное заболевание",
            "Токсический шок",
            "Печеночная недостаточность",
            "Гепатит С",
            "Варикозное расширение вен",
            "Малярия",
            "Дизентерия",
            "Болезнь Паркинсона",
            "Эбола",
            "Шизофрения",
            "Ожирение",
            "Булемия",
            "Дефицит внимания и гиперактивность",
            "Сифилис",
            "Кариес",
            "Хроническая обструктивная болезнь легких (ХОБЛ)",
            "Болезнь Альцгеймера",
            "Биполярное расстройство"]
    return text

def trait():#черта
    text = ["Щедрость",
            "Искренность",
            "Терпение",
            "Ответственность",
            "Эмпатия",
            "Коммуникабельность",
            "Оптимизм",
            "Творческий мышление",
            "Стойкость",
            "Честность",
            "Уверенность",
            "Дружелюбие",
            "Самоотверженность",
            "Гибкость",
            "Умение анализировать",
            "Самоконтроль",
            "Инициативность",
            "Справедливость",
            "Самодисциплина",
            "Самобытность",
            "Позитивный настрой",
            "Целеустремленность",
            "Общительность",
            "Доброта",
            "Креативность",
            "Решительность",
            "Принципиальность"]
    return text

def work():#работа
    text = ["Биолог",
            "Винодел",
            "Повар",
            "Хирург",
            "Программист",
            "Хакер",
            "Матрос",
            "Биохимик",
            "Таксист",
            "Художник",
            "Предприниматель",
            "Режиссёр",
            "Писатель",
            "Психолог",
            "Депутат",
            "Полицейский",
            "Физик",
            "Экономист",
            "Инженер",
            "Охранник",
            "Пилот",
            "Грузчик",
            "Бухгалтер",
            "Военный врач",
            "Гробовщик",
            "Священник",
            "Акушер"]
    return text

def work_explanation():#работа пояснение
    text = {"Биолог":"Добавляет семена культур, овощей в свой 'Инвентарь'",
            "Винодел":"При прохождении в бункер может пронести с собой ящик с вином.",
            "Повар":"Может добавить себе в 'Инвентарь' коробку с дошираком.",
            "Хирург":"Может вылечить любую болезнь другому игроку.",
            "Программист":"Может изменить 'Специальность' другого игрока.",
            "Хакер":"Может добавить себе в 'Инвентарь' ноутбук с зарядным устройством.",
            "Матрос":"Может добавить себе в 'Инвентарь' канат 60 метров.",
            "Биохимик":"При прохождении в бункер может сделать витамины на месяц.",
            "Таксист":"Добавляет себе в 'Инвентарь' автомобиль с полностью залитым баком.",
            "Художник":"Если в бункере присутствуют любые проблемы с сухостью, то может исправить их.",
            "Предприниматель":"Может добавить себе в 'Инвентарь' 2 небольших предмета.",
            "Режиссёр":"Может поменять местами характеристику двух других игроков.",
            "Писатель":"Может изменить 'Дополнительные сведения' или 'Хобби / Увлечение' любому игроку.",
            "Психолог":"Может вылечить 'Фобию / Страх' другого игрока.",
            "Депутат":"Может увеличить время своего высказывания на 30 секунд.",
            "Полицейский":"Может перенаправить чужой голос против себя после голосования.",
            "Физик":"Может обменять 'Специальность' двух других игроков.",
            "Экономист":"Может увеличить количество еды в бункере на 10%.",
            "Инженер":"При прохождении в бункер может создать оборудованную теплицу для выращивания растений в бункере.",
            "Охранник":"Может перенаправить чужой голос против себя после голосования.",
            "Пилот":"Пилот - Неуязвим к 'Фобиям / Страхам', связанными с высотой, воздухом, скоростью и движением.",
            "Грузчик":"Грузчик - Может изменить своё 'Телосложение' на 'крепкий'.",
            "Бухгалтер":"Бухгалтер - Может изменить количество еды в бункере в 1,5 раза.",
            "Военный врач":"Военный врач - Может вылечить любое заболевание 'Легкой степени' и 'Средней степени' до 'Идеально здоров' другому игроку.",
            "Гробовщик":"Гробовщик - Может сказать фразу 'Он еще жив!' и оживить изгнанного игрока.",
            "Священник":"Может отменить направленную на себя карту специальной возможности другого игрока.",
            "Акушер":"При прохождении в бункер может помочь родить женщинам с любым телосложением."}
    return text