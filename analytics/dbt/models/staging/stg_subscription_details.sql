SELECT
    id::integer AS subscription_details_id,
    revenue::float AS revenue,
    quantity::integer AS quantity,
    discount_amount::float AS discount_amount,
    rating::integer AS rating
FROM {{ source('app','subscription_details')}}