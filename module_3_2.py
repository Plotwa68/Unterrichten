def send_email(message, recipient, sender = "university.help@gmail.com"):
    problem = ['@gmail.com', '@gmail.ru', '@gmail.net']
    res = 0
    for i in range(len(problem)):
        if problem[i] in sender:
            res += 1
        if problem[i] in recipient:
            res += 1

    if res == 2:
        print('Письмо успешно отправлено с адреса {0} на адрес {1}'.format(sender, recipient))

    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')

    elif res == 1:
        print('Невозможно отправить письмо с адреса {0} на адрес {1}'.format(sender, recipient))
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {0} на адрес {1}'.format(sender, recipient))


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
