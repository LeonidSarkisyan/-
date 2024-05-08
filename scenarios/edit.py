import datetime

from models import Transaction, types_ext
from data import get_balance_and_transaction_from_file, save_edited_transactions
from utils.print import print_transactions_list


def edit_scenario():
    current_balance, transactions = get_balance_and_transaction_from_file()

    print("-" * 100)
    print("Ваши записи:\n")

    print_transactions_list(transactions)

    while True:
        try:
            index = int(input("Введите порядковый номер записи, которую хотите изменить: \n\n"))
        except ValueError:
            print("Введите число! \n\n")
            continue

        index -= 1

        if index < 0 or index > len(transactions) - 1:
            print(f"Введите число от 1 до {len(transactions)})! \n\n")
            continue

        update_transaction = transactions[index]

        old_value = update_transaction.value
        old_type = update_transaction.type

        change_value(update_transaction)
        change_type(update_transaction)

        # Корректировка текущего баланса после изменений суммы и типа записи

        if old_value != update_transaction.value:
            if update_transaction.type == "Расход":
                current_balance += old_value
                current_balance -= update_transaction.value
            else:
                current_balance -= old_value
                current_balance += update_transaction.value
        elif old_type != update_transaction.type:
            if update_transaction.type == "Расход":
                current_balance -= old_value * 2
            else:
                current_balance += old_value * 2

        change_description(update_transaction)
        change_date(update_transaction)

        transactions[index] = update_transaction

        save_edited_transactions(current_balance, transactions)

        print("Запись успешно обновлена!\n")
        break


def change_value(t: Transaction):
    print(f"Текущая сумма: {t.value}\n")
    while True:
        try:
            new_value = int(input("Введите новую сумму (Если хотите оставить прежнюю, напишите 0): \n\n"))
            print()

            if new_value < 0:
                print("Введите положительное число! \n\n")
                continue

            if new_value != 0:
                t.value = new_value
            break
        except ValueError:
            print("Введите число! \n\n")


def change_type(t: Transaction):
    print(f"Текущий тип: {t.type}\n")
    while True:
        try:
            type_num = int(input("Выберите тип (1 - Расход, 2 - Доход), (Если хотите оставить прежний, напишите 0) \n\n"))
        except ValueError:
            print("Введите число! \n\n")
            continue

        if type_num == 0:
            break

        type_transaction = types_ext.get(type_num)

        if not type_transaction:
            print("Введите число 1 или 2!\n\n")
            continue

        t.type = type_transaction
        print()
        break


def change_description(t: Transaction):
    print(f"Текущее описание: {t.description}\n")
    desc = input("Напишите описание к записи (Если хотите оставить прежний, напишите 0): \n\n")

    if desc != "0":
        t.description = desc

    print()


def change_date(t: Transaction):
    print(f"Текущая дата: {t.date}\n")
    while True:
        try:
            date_input = input(
                "Введите дату в формате DD-MM-YYYY (Если хотите оставить прежнию, напишите 0): \n\n"
            )

            print()

            if date_input != "0":
                datetime.datetime.strptime(date_input, "%d-%m-%Y")
                t.date = date_input

            break
        except ValueError:
            print("Введите корректную дату!\n\n")
