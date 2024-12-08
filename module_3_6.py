def find_max(list_):
    max_ = list_[0]
    for i in list_:
        if max_ < i:
            max_ = i
    return max_


def count_even(list_):
    counter = 0
    for i in list_:
        if i % 2 == 0 and i != 0:
            counter += 1
    return counter

def unique(list_):
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(find_max([1, 54, 31, 621-200, 1, -1, 0]))
print(count_even([1, 58, 32, 620, 1, -1, 0]))
print(unique([1, 54, 31, 0, 1, -1, 0]))