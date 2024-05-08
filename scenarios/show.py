from data import get_balance_and_transaction_from_file
from utils.print import print_transactions_list


def show_scenario():
    current_balance, transactions = get_balance_and_transaction_from_file()

    inc = []
    exp = []

    for t in transactions:
        if t.type == "Расход":
            exp.append(t)
        else:
            inc.append(t)

    print("-" * 100)

    print("Ваши доходы: \n")

    print_transactions_list(inc)

    print("-" * 100)

    print("Ваши расходы: \n")

    print_transactions_list(exp)

    print("-" * 100)

    print(f"Ваш баланс: {current_balance}")

    print("-" * 100)
