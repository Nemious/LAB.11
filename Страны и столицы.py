import datetime

# Создаем словарь с государствами и их соответствующими столицами
countries = {
    'Россия': 'Москва',
    'Германия': 'Берлин',
    'Франция': 'Париж',
    'Япония': 'Токио',
    'Китай': 'Пекин',
    'Великобритания': 'Лондон',

}

# Открываем log-файл для записи
log_file = open('log.txt', 'a')


# Функция для записи информации в log-файл
def log_info(info):
    now = datetime.datetime.now()
    log_file.write(f'{now}: {info}\n')


# Функция для получения информации о столице по введенному государству
def get_capital_by_country(user_input):
    if user_input.lower() == 'выход':
        return "Программа завершена"
    elif user_input in countries:
        result = f'Государство: {user_input}, Столица: {countries[user_input]}'
    elif user_input in countries.values():
        result = f'Столица: {user_input}, Государство: {list(countries.keys())[list(countries.values()).index(user_input)]}'
    else:
        result = f'Информация о государстве или столице отсутствует в базе данных'

    log_info(f'Поиск информации для "{user_input}": {result}')
    return result


# Основной цикл программы
while True:
    user_input = input('Введите название государства или столицу или "выход", чтобы завершить программу: ')
    result = get_capital_by_country(user_input)
    print(result)
    if user_input.lower() == 'выход':
        break

# Закрываем log-файл
log_file.close()