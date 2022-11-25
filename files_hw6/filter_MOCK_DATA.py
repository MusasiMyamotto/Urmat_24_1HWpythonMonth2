import re

while True:
    with open("MOCK_DATA.txt", "r", encoding='UTF-8') as file:
        content = file.read()
    user_input = input('1 - Считать имена и фамилии\n'
                       '2 - Считать все емайлы\n'
                       '3 - Считать названия файлов\n'
                       '4 - Считать цвета\n'
                       '5 - Выход\n')

    if user_input == '5':
        print("пока")
        break


    elif user_input == '1':
        full_name_mock = re.findall(r"\b[A-Z][A-Za-z-]+\s[A-Za-z\' ]+\b\s", content)
        with open("full_names.txt", "w", encoding='UTF-8') as file:
            print('посмотрите в файл full_names')
            for i in full_name_mock:
                file.write(f"{i}\n")


    elif user_input == '2':
        email_mock = re.findall(r"\b([\w\-]+)(@)[\w]+(\.[\w]+)+", content)
        with open("emails.txt", "w", encoding='UTF-8') as file:
            print('посмотрите в файл emails.txt')
            for i in email_mock:
                file.write(f"{i}\n")


    elif user_input == '3':
        file_name_mock = re.findall(r"\t[A-Za-z][a-zA-Z]+\.[a-z]+", content)
        with open("file_names.txt", "w", encoding='UTF-8') as file:
            print('посмотрите в файл file_names.txt')
            for i in file_name_mock:
                file.write(f"{i}\n")

    elif user_input == '4':
        colors_mock = re.findall(r"#[0-9A-Fa-f]{6}", content)
        with open("colors.txt", "w", encoding='UTF-8') as file:
            print('посмотрите в файл colors.txt')
            for i in colors_mock:
                file.write(f"{i}\n")

    else:
        print('вы не правильно ввели команду')
