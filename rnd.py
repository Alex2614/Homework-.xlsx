import random

# Счетчики для правильных и неправильных ответов
correct_answers = 0
incorrect_answers = 0

# Список для хранения предыдущих чисел (ограничен до 10 последних)
previous_numbers = []

# Флаг для пропуска текущего вопроса
skip_current_question = False
print('Для выхода введите "q"')
print('Для смены множителя введите "c"')
print("Это авторский метод заучивания или повторения таблицы умножения v.0.11")
print("Developed by Dr_Alex")
# Проверка ввода первого множителя
while True:
    b_input = input("Введите первый множитель (2-9) или 'q' для выхода: ")
    if b_input.lower() == 'q':
        print("Программа завершена.")
        exit()
    try:
        b = int(b_input)
        if 2 <= b <= 9:
            break
        else:
            print("Множитель должен быть в диапазоне 2-9!")
    except ValueError:
        print("Пожалуйста, введите целое число!")

while True:
    # Генерация нового числа a, отличного от последних 10
    while True:
        a = random.randint(2, 9)
        if a not in previous_numbers[-10:] or len(previous_numbers) < 10:
            break
    
    # Обновление списка предыдущих чисел
    previous_numbers.append(a)
    if len(previous_numbers) > 10:
        previous_numbers.pop(0)

    # Получение ответа от пользователя
    while True:
        user_input = input(f"{a} * {b} будет: ")
        if user_input.lower() == 'q':
            print("Программа завершена.")
            exit()
        elif user_input.lower() == 'c':  # Команда для смены множителя
            while True:
                new_b = input("Введите новый множитель (2-9): ")
                try:
                    new_b = int(new_b)
                    if 2 <= new_b <= 9:
                        b = new_b
                        previous_numbers.clear()  # Очистка истории
                        correct_answers = 0  # Обнуление статистики
                        incorrect_answers = 0
                        skip_current_question = True  # Флаг для пропуска текущего вопроса
                        print(f"Множитель изменен на {b}.")
                        break
                    else:
                        print("Множитель должен быть в диапазоне 2-9!")
                except ValueError:
                    print("Пожалуйста, введите целое число!")
            break  # Выйти из цикла ввода ответа после изменения множителя
        try:
            u = int(user_input)
            break
        except ValueError:
            print("Пожалуйста, введите число!")

    # Пропуск текущего вопроса при смене множителя
    if skip_current_question:
        skip_current_question = False
        continue

    # Проверка правильности ответа
    if u == a * b:
        print("Правильно!")
        correct_answers += 1
    else:
        print(f"Неправильно. Правильный ответ: {a * b}")
        incorrect_answers += 1

    # Вывод статистики
    total = correct_answers + incorrect_answers
    accuracy = (correct_answers / total * 100) if total > 0 else 0
    print(f"\nСтатистика: "
          f"Правильных: {correct_answers}, "
          f"Неправильных: {incorrect_answers}, "
          f"Точность: {accuracy:.1f}%")
