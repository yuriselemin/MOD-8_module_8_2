
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
        summ = sum(personal_sum(numbers))
        total = summ / len(numbers)
        return total
    except ZeroDivisionError:
        print("Список пуст, среднее значение не может быть вычислено.")
        return None
    except TypeError:
        print("В numbers записан некорректный тип данных.")
        return None



print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать


