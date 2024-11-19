my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

result = True
i = 0
while result:

    if my_list[i] < 0:
        result = False
    else:
        print(my_list[i])

    i += 1



