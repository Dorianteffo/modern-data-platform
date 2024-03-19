SELECT
    id::integer AS subscription_id,
    user_id AS user_id,
    plan AS plan,
    status AS status,
    payment_method AS payment_method,
    subscription_term AS subscription_term,
    payment_term AS payment_term
FROM {{ source('app','subscription') }}
