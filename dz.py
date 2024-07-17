import csv
import os


def get_data():
    first_name = "Иван"
    last_name = "Иванов"
    phone = "+79932287549"
    return [first_name, last_name, phone]


def create_file(filename):
    with open(filename, "w", encoding='utf-8') as data:
        f_w = csv.DictWriter(data, fieldnames=["Имя", "Фамилия", "Телефон"])
    f_w.writeheader()


def read_file(filename):
    with open(filename, "r", encoding='utf-8') as data:
        f_r = csv.DictReader(data)
    return list(f_r)


def write_file(filename, lst):
    res = read_file(filename)
    obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}
    res.append(obj)
    with open(filename, "w", encoding='utf-8') as data:
        f_w = csv.DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
    f_w.writeheader()
    f_w.writerows(res)


def exist(filename):
    return os.path.exists(filename)


def copy_row(src_file, dest_file, row_number):
    rows = read_file(src_file)
    if row_number < 1 or row_number > len(rows):
        print(f"Некорректный номер строки: {row_number}")
    return
    row_to_copy = rows[row_number - 1]
    dest_rows = read_file(dest_file)
    dest_rows.append(row_to_copy)
    with open(dest_file, "w", encoding='utf-8') as data:
        f_w = csv.DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
    f_w.writeheader()
    f_w.writerows(dest_rows)
    print(f"Строка {row_number} успешно скопирована из {src_file} в {dest_file}")


filename = 'phone.csv'


def main():
    while True:
        command = input("Введите команду: ")
    if command == 'q':
        break
    elif command == 'w':
        if not exist(filename):
            create_file(filename)
        write_file(filename, get_data())
    elif command == 'r':
        if not exist(filename):
            print("Файл не существует. Создайте его.")
        continue
        print(read_file(filename))
    elif command == 'c':
        src_file = input("Введите имя исходного файла: ")
        dest_file = input("Введите имя файла назначения: ")
        row_number = int(input("Введите номер строки для копирования: "))
        if not exist(src_file):
            print(f"Файл {src_file} не существует.")
        continue
        if not exist(dest_file):
            create_file(dest_file)
        copy_row(src_file, dest_file, row_number)


if __name__ == "__main__":
    main()
