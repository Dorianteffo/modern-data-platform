import random
from datetime import datetime


def random_credit_card_number():
    return (
        f"{random.randint(1000, 9999)}-"
        f"{random.randint(1000, 9999)}-"
        f"{random.randint(1000, 9999)}-"
        f"{random.randint(1000, 9999)}"
    )


def random_credit_card_expiry_date():
    year = random.randint(2021, 2030)
    month = random.randint(1, 12)
    return f"{year}-{month:02d}-01"



def random_credit_card_type():
    return random.choice(
        ["visa", "mastercard", "discover", "diners_club", "laser"]
    )


def generate_credit_card_data(bank_data: list) -> list:
    credit_cards = []
    for record in bank_data:
        credit_card_data = {
            "id": random.randint(1000, 9999),
            "credit_card_number": random_credit_card_number(),
            "credit_card_expiry_date": random_credit_card_expiry_date(),
            "credit_card_type": random_credit_card_type(),
            "user_id": record['user_id'],
            "dt_current_timestamp": datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
        }
        credit_cards.append(credit_card_data)
    return credit_cards
