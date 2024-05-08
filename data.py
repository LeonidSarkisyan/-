import json

from models import Transaction

FILENAME_DATA = "data.json"


def save_transaction_to_file(transaction: Transaction):
    try:
        with open(FILENAME_DATA, 'r', encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {"current_balance": 0, "transactions": []}

    data["transactions"].append(transaction.__dict__)

    if transaction.type == "Расход":
        data["current_balance"] -= transaction.value
    else:
        data["current_balance"] += transaction.value

    with open(FILENAME_DATA, 'w', encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def get_balance_and_transaction_from_file() -> (int, list[Transaction]):
    try:
        with open(FILENAME_DATA, 'r', encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return 0, []

    transactions = []

    for item in data['transactions']:
        transactions.append(Transaction(
            date=item['date'],
            value=item['value'],
            type=item['type'],
            description=item['description']
        ))

    return data["current_balance"], transactions


def save_edited_transactions(current_balance: int, transactions: list[Transaction]):
    data = {"current_balance": current_balance, "transactions": []}

    for t in transactions:
        data["transactions"].append(t.__dict__)

    with open(FILENAME_DATA, 'w', encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
