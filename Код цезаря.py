def is_valid_ansver():  # защита. Проверяет да или нет. Выводит True или False
    text = input()
    while text != 'ш' and text != 'д':
        print("пожалуйста введите конкретно, 'ш' или 'д'. Мы хотим вам помочь ")
        text = input().lower()
        continue
    if text.lower() == 'ш':
        return True
    else:
        return False


def is_valid_and_int():  # защита. Проверяет цифры ли введены. Выводим в int()
    num = input()
    while True:
        if num.isdigit():
            return int(num)
        else:
            print('Напоминаю нужно ввести простое число')
            num = input()


def anain_line():


eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

print("Привет! Это программа шифрования цезаря")

while True:
    print('Шифрование или дешифрование?, ответте "ш" или "д"')
    code = is_valid_ansver()

    print('Русский или Английский ? Ответ записывать в форме "Р" или "А"? ')
    leng = input().lower()

    print("шаг сдвига, ввести простое число")
    num = is_valid_and_int()
    print(num)

    if code:
        print('Ведите текст который будем шифровать')
    else:
        print('Ведите текст который будем дкшифровать')
    text = input()

    answer = ""
    if leng == 'р':  # если русский алфавит.
        if code:  # если кодирование (а не декод)
            for i in range(len(text)):
                if text[i] in rus_lower_alphabet:
                    answer += rus_lower_alphabet[i + num]
                elif text[i] in rus_upper_alphabet:
                    answer += rus_lower_alphabet[i + num]
                elif text[i] == " ":
                    answer += " "
                else:
                    answer += text[i]

        else:  # если декодирование русского
            for i in range(len(text)):
                if text[i] in rus_lower_alphabet:
                    answer += rus_lower_alphabet[i - num]
                elif i in rus_upper_alphabet:
                    answer += rus_lower_alphabet[i - num]
                elif i == " ":
                    answer += " "
                else:
                    answer += text[i]
    else:  # работа с английским алфавитом
        if code:  # если кодирование (а не декод)
            for i in range(len(text)):
                if text[i] in rus_eng_lower_alphabet:
                    answer += eng_lower_alphabet[i + num]
                elif i in rus_upper_alphabet:
                    answer += rus_lower_alphabet[i + num]
                elif i == " ":
                    answer += " "
                else:
                    answer += text[i]
        else:  # если декодирование русского
            for i in range(len(text)):
                if text[i] in rus_lower_alphabet:
                    answer += eng_lower_alphabet[i - num]
                elif i in rus_upper_alphabet:
                    answer += eng_lower_alphabet[i - num]
                elif i == " ":
                    answer += " "
                else:
                    answer += text[i]
    print(answer)
    print("Нужно расшифровать ещё? Да, нет")
    text = input().lower()
    if text == "да":
        continue
    else:
        print('спасибо, да прибудет сила')
        break