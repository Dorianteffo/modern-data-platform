import random
import string
import uuid
from datetime import datetime

# list of fake banks
bank_names = [
    "Global Trust Bank",
    "Silverline Financial",
    "Oceanic Capital",
    "Liberty Banking Corp",
    "Pinnacle Funds",
    "Banque du Soleil",
    "Finance Royale",
    "Banco del Futuro",
    "Zhongxin Jinrong",
]


def random_uuid():
    return str(uuid.uuid4())


def random_number(length=10):
    numbers = string.digits
    return ''.join(random.choice(numbers) for i in range(length))


def random_iban():
    return 'IBAN' + random_number(20)


def random_swift_bic():
    return 'SWIFT' + ''.join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(8)
    )


def generate_bank_data() -> list:
    bank_data = []
    for i in range(500):
        common_record = {
            "id": random.randint(1000, 9999),
            "account_number": random_number(),
            "iban": random_iban(),
            "bank_name": random.choice(bank_names),
            "routing_number": random_number(),
            "swift_bic": random_swift_bic(),
            "user_id": str(uuid.uuid4()),
            "dt_current_timestamp": datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
        }

        bank_data.append(common_record)
    return bank_data
