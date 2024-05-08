import datetime

from models import Transaction, types_ext
from data import get_balance_and_transaction_from_file
from utils.print import print_transactions_list, print_transaction


search_options = {
    1: "lte",
    2: "gte",
    3: "equal"
}


def search_scenario():
    _, transactions = get_balance_and_transaction_from_file()

    print("Доступные поля для поиска: ")
    print("1 - Сумма")
    print("2 - Описание")
    print("3 - Дата \n")

    while True:
        try:
            search_fields_number = int(input("Введите число нужного вам поля: \n\n"))
            print()
        except ValueError:
            print("Введите число! \n\n")
            continue

        search_field = search_fields.get(search_fields_number)

        if not search_field:
            print("Введите число от 1 до 3! \n\n")
            continue

        search_field(transactions)
        break


def search_by_value(transactions: list[Transaction]):
    while True:
        try:
            value = int(input("Введите сумму, по которой хотите найти запись:  \n\n"))
            print()
        except ValueError:
            print("Введите число!\n\n")
            continue
        else:
            print("Найденные записи:")
            transactions = [t for t in transactions if t.value == value]
            print_transactions_list(transactions)
            break


def search_by_description(transactions: list[Transaction]):
    desc = input("Введите описание, по которому хотите найти запись: \n\n").lower()
    print()
    print("Найденные записи:")
    transactions = [t for t in transactions if desc in t.description.lower()]
    print_transactions_list(transactions)


def search_by_date(transactions: list[Transaction]):
    while True:
        try:
            date_input = input(
                "Введите дату в формате DD-MM-YYYY: \n\n"
            )
            print()
            datetime.datetime.strptime(date_input, "%d-%m-%Y")
        except ValueError:
            print("Введите корректную дату!\n\n")
        else:
            print("Найденные записи:")
            transactions = [t for t in transactions if date_input == t.date]
            print_transactions_list(transactions)
            break


search_fields = {
    1: search_by_value,
    2: search_by_description,
    3: search_by_date
}
