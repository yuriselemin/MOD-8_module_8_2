
# Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции".


def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for number in numbers:
        try:
            if isinstance(number, int):
                result += number
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        num = []

        for number in numbers:
            if isinstance(number, (int, float)):
                num.append(number)
            else:
                print(f'Некорректный тип данных для подсчёта суммы: {number}')

        summ = sum(personal_sum(numbers))
        total = summ / len(num)
        return total

    except ZeroDivisionError as z:
        print(f'Список пуст, среднее значение не может быть вычислено: {z}')
        return 0
    except TypeError as t:
        print(f'В numbers записан некорректный тип данных: {t}')
        return None




print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')


