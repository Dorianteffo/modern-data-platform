SELECT
    bank_id,
    account_number,
    iban,
    bank_name,
    routing_number,
    swift_bic
FROM {{ ref('stg_bank') }}