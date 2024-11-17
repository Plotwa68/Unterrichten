my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

result = True

while result:
    number = int(input('Введите целое неотрицательное цисло: '))

    if isinstance(number, int) and number <= len(my_list) and number > 0:
        result = False
        while number != 0:
            number -= 1
            print(my_list[number])
    else:
        continue



