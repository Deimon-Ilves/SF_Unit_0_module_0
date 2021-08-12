import numpy as np

number = np.random.randint(1, 101)  # загадали число
print("Загадано число от 1 до 100")
for count in range(1, 101):  # более компактный вариант счетчика
    if number == count: break  # выход из цикла, если угадали
print(f"Вы угадали число {number} за {count} попыток.")


def game_core_v1(number):
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали


def score_game(game_core) -> object:
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


score_game(game_core_v1)


def game_core_v2(number):
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return (count)  # выход из цикла, если угадали


score_game(game_core_v2)


def game_core_v3(number):
    count = 1
    predict = len(range(1, 101)) // 2  # Используем эту форму, чтобы разбить диапазон поиска пополам
    while number != predict:
        count += 1
        if number > predict and count < 3:  # Сокращаем границы поиска
            predict = (len(range(predict, 101)) + predict) // 2
        elif number < predict and count < 3:  # Сокращаем границы поиска
            predict = len(range(1, predict)) // 2
        elif number > predict:  # После 3-го сокращения переходим к варианту game_core_v2
            predict += 1
        elif number < predict:
            predict -= 1
    return (count)  # Выходим из цикла, фиксируя число попыток


score_game(game_core_v3)
