my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

#my_list = [42, 69, 322, 13, 0, 99, 5, 9, 8, 7, 6, 5]

index_elem = 0
while index_elem < len(my_list):
    elem = my_list[index_elem]
    index_elem += 1
    if elem == 0:
        continue
    elif elem < 0:
        break
    else:
        print(elem)



