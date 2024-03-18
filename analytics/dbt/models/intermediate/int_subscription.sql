SELECT 
    subscription_id,
    plan,
    status,
    payment_method,
    subscription_term,
    payment_term
FROM {{ ref('stg_subscription') }}