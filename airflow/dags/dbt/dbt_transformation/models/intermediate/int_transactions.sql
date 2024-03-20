WITH cte_user AS (
    SELECT 
        user_id, 
        dt_timestamp
    FROM {{ ref('stg_user') }}
), 

 cte_credit_card AS(
    SELECT
        user_id,
        credit_card_id
    FROM {{ ref('stg_credit_card') }}
),

 cte_subscription AS (
    SELECT
        user_id,
        subscription_id
    FROM {{ ref('stg_subscription') }}
 ),

 cte_stripe AS (
    SELECT
        user_id,
        stripe_id
    FROM {{ ref('stg_stripe') }}
 ),

 cte_bank AS (
    SELECT
        user_id, 
        bank_id
    FROM {{ ref('stg_bank') }}
 ),
    
 cte_date AS (
    SELECT
        date_id,
        dt_timestamp
    FROM {{ ref('int_date') }}
 )
SELECT
    sd.subscription_details_id AS transaction_id,
    sd.user_id,
    s.subscription_id,
    cd.credit_card_id,
    st.stripe_id,
    dt.date_id,
    sd.quantity,
    sd.revenue,
    sd.discount_amount,
    sd.revenue - sd.discount_amount AS net_revenue,
    sd.rating
FROM {{ ref('stg_subscription_details') }} AS sd
LEFT JOIN cte_user AS u ON sd.user_id = u.user_id
LEFT JOIN cte_subscription AS s ON sd.user_id = s.user_id
LEFT JOIN cte_credit_card AS cd ON sd.user_id = cd.user_id
LEFT JOIN cte_stripe AS st ON sd.user_id = st.user_id
LEFT JOIN cte_bank AS b ON sd.user_id = b.user_id
LEFT JOIN cte_date AS dt ON u.dt_timestamp = dt.dt_timestamp
