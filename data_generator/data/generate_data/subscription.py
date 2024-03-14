import random
from datetime import datetime


def random_plan():
    plans = ["Standard", "Basic", "Platinum", "Gold", "Bronze"]
    return random.choice(plans)


def random_status():
    statuses = ["Active", "Idle", "Blocked", "Cancelled"]
    return random.choice(statuses)


def random_payment_method():
    methods = [
        "Google Pay",
        "Credit Card",
        "Paypal",
        "Bitcoins",
        "Money Transfer",
        "Alipay",
    ]
    return random.choice(methods)


def random_subscription_term():
    terms = ["Weekly", "Monthly", "Yearly", "Lifetime", "Quinquennal"]
    return random.choice(terms)


def random_payment_term():
    terms = [
        "Full Subscription",
        "Monthly Payment",
        "Payment in Advance",
        "Pay per Use",
    ]
    return random.choice(terms)


def generate_subscriptions_data(transactions: list) -> list:
    subscriptions = []
    for record in transactions:
        subscription_data = {
            "id": record["id"],
            "plan": random_plan(),
            "status": random_status(),
            "payment_method": random_payment_method(),
            "subscription_term": random_subscription_term(),
            "payment_term": random_payment_term(),
            "user_id": record['user_id'],
            "dt_current_timestamp": datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
        }
        subscriptions.append(subscription_data)

    return subscriptions
