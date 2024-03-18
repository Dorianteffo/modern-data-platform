SELECT
    id::integer AS credit_card_id,
    credit_card_number AS credit_card_number,
    credit_card_expiry_date AS credit_card_expiry_date,
    credit_card_type AS credit_card_type
FROM {{ source('app','credit_card') }}
