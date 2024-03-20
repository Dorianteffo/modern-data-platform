SELECT
    s.plan,
    AVG(t.discount_amount) AS avg_discount_amount
FROM {{ ref('int_transactions') }} AS t 
JOIN {{ ref('int_subscription') }} AS s ON t.subscription_id = s.subscription_id
GROUP BY s.plan
