
def print_contacts(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
        if len(all_cont) != 0:
            for line in all_cont:
                print(line.strip(), end= '\n\n')
        else:
            print('Список контактов пустой!')


def connect_with_user():
    print('Введите имя, фамилию и телефон (например: Иван Иванов 89654561234 ): ')
    cont_info = str(input())
    return cont_info


def add_contact(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
    new_cont = connect_with_user()
    all_cont.append('\n' + new_cont)
    with open(file_name, 'w', encoding='utf8') as file:
        file.writelines(all_cont)


def find_contact(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()

    print("Выберите критерий для поиска:" +
        '1 - Имя' +
        '2 - Фамилия' +
        '3 - Телефон'
        )  
    command = int(input())
    print('Введите строку для поиска: ')
    data = input()
    print('Найденные контакты: ')
    for cont in all_cont:
        cont_as_list = cont.strip().split()
        if cont_as_list[command - 1] == data:
            print(*cont_as_list)




