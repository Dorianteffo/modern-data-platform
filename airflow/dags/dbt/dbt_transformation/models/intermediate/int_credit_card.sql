SELECT
    credit_card_id,
    credit_card_number,
    credit_card_expiry_date,
    credit_card_type
FROM {{ ref('stg_credit_card') }}