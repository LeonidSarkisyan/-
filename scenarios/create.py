import datetime

from models import Transaction, types_ext
from data import save_transaction_to_file


def create_scenario():
    t = Transaction()

    t.value = ask_value()
    t.type = ask_type()
    t.description = ask_description()
    t.date = ask_date()

    save_transaction_to_file(t)

    print("Запись сохранена!\n")


def ask_value() -> int:
    while True:
        try:
            value = int(input("Введите сумму: \n\n"))
            print()

            if value <= 0:
                print("Введите положительное число! \n\n")
                continue

            return value
        except ValueError:
            print("Введите число! \n\n")


def ask_type() -> str:
    while True:
        try:
            type_num = int(input("Выберите тип (1 - Расход, 2 - Доход) \n\n"))
        except ValueError:
            print("Введите число! \n\n")
            continue

        type_transaction = types_ext.get(type_num)

        if not type_transaction:
            print("Введите число 1 или 2!\n\n")
            continue

        print()
        return type_transaction


def ask_description() -> str:
    desc = input("Напишите описание к записи: \n\n")
    print()
    return desc


def ask_date() -> str:
    while True:
        try:
            date_input = input(
                "Введите дату в формате DD-MM-YYYY (или отправьте 0, если хотите использовать сегодняшнюю дату): \n\n"
            )

            print()

            if date_input == "0":
                return datetime.date.today().strftime("%d-%m-%Y")

            datetime.datetime.strptime(date_input, "%d-%m-%Y")
            return date_input
        except ValueError:
            print("Введите корректную дату!\n\n")


