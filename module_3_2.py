def send_email(message, recipient, sender = "university.help@gmail.com"):

    if "@" not in recipient or "@" not in sender \
            or not recipient.endswith((".com", ".ru", ".net")) \
            or not sender.endswith((".com", ".ru", ".net")):
        print('Невозможно отправить письмо с адреса {0} на адрес {1}'.format(sender, recipient))

    elif sender in recipient:
        print('Нельзя отправить письмо самому себе!')

    elif sender != "university.help@gmail.com":
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {0} на адрес {1}'.format(sender, recipient))

    else:
        print('Письмо успешно отправлено с адреса {0} на адрес {1}'.format(sender, recipient))

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

