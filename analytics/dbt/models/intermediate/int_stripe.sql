SELECT
    stripe_id,
    token,
    ccv,
    ccv_amex
FROM {{ ref('stg_stripe') }}