from models import Transaction


def print_transactions_list(transactions: list[Transaction]):
    if len(transactions) == 0:
        print("Таких записей нет")
        return

    for i, t in enumerate(transactions):
        print_transaction(i, t)


def print_transaction(i: int, t: Transaction):
    print(f"{i + 1}.")
    print(f"Описание: {t.description}")
    print(f"Дата: {t.date}")
    print(f"Категория: {t.type}")
    print(f"Сумма: {t.value}")
    print()
