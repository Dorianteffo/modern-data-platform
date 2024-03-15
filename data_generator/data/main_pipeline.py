import time

import pandas as pd
import schedule
from generate_data.bank import generate_bank_data
from generate_data.credit_card import generate_credit_card_data
from generate_data.stripe_transactions import generate_transactions_data
from generate_data.subscription import generate_subscriptions_data, generate_random_subscription_details
from generate_data.user import generate_users_data, get_user_ids_from_data
from load_to_postgres import close_conn, create_conn, load_table
from utils.db import WarehouseConnection, get_warehouse_creds


def main():
    # create dataframes
    bank_data = generate_bank_data()
    bank_df = pd.DataFrame(bank_data)

    credit_card_data = generate_credit_card_data(bank_data)
    credit_card_df = pd.DataFrame(credit_card_data)

    transactions_data = generate_transactions_data(credit_card_data)
    transactions_df = pd.DataFrame(transactions_data)

    subscriptions_data = generate_subscriptions_data(transactions_data)
    subscriptions_df = pd.DataFrame(subscriptions_data)

    subscriptions_details_data = generate_random_subscription_details(transactions_data)
    subscriptions_details_df = pd.DataFrame(subscriptions_details_data)

    users_data = generate_users_data(
        get_user_ids_from_data(credit_card_data, subscriptions_data),
        credit_card_data,
        subscriptions_data,
    )
    users_df = pd.DataFrame(users_data)

    engine = create_conn(
        WarehouseConnection(get_warehouse_creds()).connection_string()
    )

    load_mode = 'append'
    schema_name = 'app'  # database schema name

    # load tables to app schema
    load_table(bank_df, engine, 'bank', schema_name, load_mode)
    load_table(credit_card_df, engine, 'credit_card', schema_name, load_mode)
    load_table(transactions_df, engine, 'stripe', schema_name, load_mode)
    load_table(
        subscriptions_df, engine, 'subscription', schema_name, load_mode
    )
    load_table(subscriptions_details_df, engine, 'subscription_details', schema_name, load_mode)
    load_table(users_df, engine, 'user', schema_name, load_mode)

    close_conn(engine)


if __name__ == '__main__':
    # generate data every 2 hours
    schedule.every(2).hours.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)

    # main()
