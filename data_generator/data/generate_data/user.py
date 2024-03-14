import random
from datetime import datetime
from typing import Dict, Optional

from faker import Faker

fake = Faker()


def get_user_ids_from_data(credit_card_data: list, subscription_data: list):
    data = credit_card_data + subscription_data
    return {item['user_id'] for item in data}


def generate_users_data(
    users_ids: list, credit_card_data: list, subscription_data: list
) -> list:
    users = []

    for user_id in users_ids:
        credit_card_info: Dict[str, Optional[str]] = next(
            (item for item in credit_card_data if item["user_id"] == user_id),
            {},
        )
        subscription_info: Dict[str, Optional[str]] = next(
            (item for item in subscription_data if item["user_id"] == user_id),
            {},
        )

        user_data = {
            "id": random.randint(1000, 9999),
            "user_id": user_id,
            "password": fake.password(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "username": fake.user_name(),
            "email": fake.email(),
            "avatar": fake.image_url(),
            "gender": random.choice(["Male", "Female", "Other"]),
            "phone_number": fake.phone_number(),
            "social_insurance_number": fake.ssn(),
            "date_of_birth": str(fake.date_of_birth()),
            "role": fake.job(),
            "city": fake.city(),
            "street_name": fake.street_name(),
            "street_address": fake.street_address(),
            "zip_code": fake.zipcode(),
            "state": fake.state(),
            "country": fake.country(),
            "lat": float(fake.latitude()),
            "lng": float(fake.longitude()),
            "credit_card_id": credit_card_info['id'],
            "subscription_id": subscription_info['id'],
            "dt_current_timestamp": int(datetime.now().timestamp()),
        }

        users.append(user_data)

    return users
