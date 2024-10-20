# ИТ школа, ДЗ №1, Электронные часы

# Запрашиваем у пользователя количество секунд
try:
 N = int(input("Введите количество секунд: "))
except ValueError:
    print('Ошибка! Введенное значение не является числом!')
else:
    Hours = 0
    Minutes = 0
    Seconds = 0

    MinutesTemp = N // 60 # считаем число минут без остатка
    Seconds = N % 60 # получаем остаток секунд
    Hours = MinutesTemp // 60 # преобразуем минуты в целое число часов
    Minutes = MinutesTemp % 60 # считаем оставшиеся минуты

    # Делаем значения ЧЧ:ММ:СС
    SecondsStr = str(Seconds).zfill(2)
    HoursStr = str(Hours).zfill(2)
    MinutesStr = str(Minutes).zfill(2)

    print(f'{HoursStr}:{MinutesStr}:{SecondsStr}')


