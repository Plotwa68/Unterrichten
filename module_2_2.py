einz = int(input('Введите перво число: '))
zwei = int(input('Введите второе число: '))
drei = int(input('Введите третье число: '))

if einz == zwei and einz == drei:
    print(3)

elif einz == zwei or einz == drei:
    print(2)

else:
    print(0)