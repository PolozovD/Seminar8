from main import *

CONTACTS = 'Contacts.txt'

def interface():
    while True:
        print('Выберите действие:\
            \n 1 - Добавить контакт \
            \n 2 - Вывести все контакты \
            \n 3 - Найти контакт \
            \n 0 - Выйти')
        command = int(input())
        match command:
            case 0:
                break
            case 1:
                add_contact(CONTACTS)
            case 2:
                print_contacts(CONTACTS)
            case 3:
                find_contact(CONTACTS)

if __name__ == '__main__':
    interface()