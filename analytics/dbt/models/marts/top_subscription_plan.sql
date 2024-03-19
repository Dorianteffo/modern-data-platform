SELECT
    s.plan,
    SUM(t.net_revenue) AS total_net_revenue
FROM {{ ref('int_transactions') }} AS t 
JOIN {{ ref('int_subscription') }} AS s ON t.subscription_id = s.subscription_id
GROUP BY s.plan
