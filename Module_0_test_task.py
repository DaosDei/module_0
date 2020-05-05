import numpy as np

count = 0
number = np.random.randint(1, 100)  # загадали число


def game_core_v3(number):
    """Задаем нижнюю и верхнюю границы возможных исходов,
    в каждой следуующей итерации уменьшаем одну из границ в зависимости от того было ли предсказание больше/меньше
    загадоного значения"""
    min_value = 1
    max_value = 99
    count = 0
    while True:
        predict = (min_value + max_value) // 2  # наш ответ будет равняться среднему межну значений заданных границ
        count += 1
        if predict == number:
            break
        else:
            if predict < number:
                min_value = predict + 1
            elif predict > number:
                max_value = predict - 1
    return (count)


def score_game(game_core_v3):
    """Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(100, size=1000)
    for number in random_array:
        count_ls.append(game_core_v3(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


score_game(game_core_v3)
