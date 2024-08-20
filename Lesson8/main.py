def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phone.txt')

    while choice != 7:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('Введите фамилию: ')
            new_number = input('Введите новый номер: ')
            print(change_number(phone_book, last_name, new_number))
        elif choice == 4:
            last_name = input('Введите фамилию: ')
            print(delete_by_lastname(phone_book, last_name))
        elif choice == 5:
            number = input('Введите номер: ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('Введите новые данные (Фамилия, Имя, Телефон, Описание): ')
            add_user(phone_book, user_data)
            write_txt('phone.txt', phone_book)

        choice = show_menu()

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Изменить номер абонента по фамилии\n"
          "4. Удалить абонента по фамилии\n"
          "5. Найти абонента по номеру телефона\n"
          "6. Добавить абонента в справочник\n"
          "7. Закончить работу")
    choice = int(input("Введите номер действия: "))
    return choice

import os

def read_txt(filename):
    phone_book = []
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден.")
        return phone_book  # Возвращаем пустую телефонную книгу

    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)
    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for entry in phone_book:
            s = ','.join(entry.values())
            phout.write(f'{s}\n')

def print_result(phone_book):
    for entry in phone_book:
        print(f"{entry['Фамилия']}, {entry['Имя']}, {entry['Телефон']}, {entry['Описание']}")

def find_by_lastname(phone_book, last_name):
    results = [entry for entry in phone_book if entry['Фамилия'].lower() == last_name.lower()]
    return results if results else "Абонент с такой фамилией не найден."

def change_number(phone_book, last_name, new_number):
    for entry in phone_book:
        if entry['Фамилия'].lower() == last_name.lower():
            entry['Телефон'] = new_number
            return f"Номер для {last_name} успешно изменен на {new_number}."
    return "Абонент с такой фамилией не найден."

def delete_by_lastname(phone_book, last_name):
    for entry in phone_book:
        if entry['Фамилия'].lower() == last_name.lower():
            phone_book.remove(entry)
            return f"Абонент {last_name} успешно удален."
    return "Абонент с такой фамилией не найден."

def find_by_number(phone_book, number):
    results = [entry for entry in phone_book if entry['Телефон'] == number]
    return results if results else "Абонент с таким номером не найден."

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    new_entry = dict(zip(fields, user_data.split(',')))
    phone_book.append(new_entry)
    return "Новый абонент успешно добавлен."

# Запуск программы
work_with_phonebook()
