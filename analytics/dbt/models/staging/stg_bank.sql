SELECT
    id::integer AS bank_id,
    user_id AS user_id,
    account_number::integer AS account_number,
    iban AS iban,
    bank_name AS bank_name,
    routing_number::integer AS routing_number,
    swift_bic AS swift_bic
FROM {{ source('app','bank') }}
