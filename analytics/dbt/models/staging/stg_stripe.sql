SELECT 
    id::integer AS stripe_id,
    token AS token,
    ccv::integer AS ccv,
    ccv_amex::integer AS ccv_amex
FROM {{ source('app','stripe') }}
