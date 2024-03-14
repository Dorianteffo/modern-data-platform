import random
from datetime import datetime


def random_token():
    tokens = ["tok_visa", "tok_mastercard", "tok_discover"]
    return random.choice(tokens)


def random_ccv():
    return str(random.randint(100, 999))


def random_ccv_amex():
    return str(random.randint(1000, 9999))


def generate_transactions_data(credit_cards: list) -> list:
    transactions = []
    for record in credit_cards:
        transaction_data = {
            "id": random.randint(1000, 9999),
            "valid_card": record['credit_card_number'],
            "token": random_token(),
            "month": record['credit_card_expiry_date'].split("-")[1],
            "year": record['credit_card_expiry_date'].split("-")[0],
            "ccv": random_ccv(),
            "ccv_amex": random_ccv_amex(),
            "user_id": record['user_id'],
            "dt_current_timestamp": datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
        }
        transactions.append(transaction_data)

    return transactions
