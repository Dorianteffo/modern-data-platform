SELECT
    {{ dbt_utils.generate_surrogate_key([
        'city', 
        'street_name',
        'zip_code', 
        'lat',
        'long'
        ]) 
        }} AS address_id,
    city,
    street_name,
    street_address,
    zip_code,
    state,
    country,
    lat,
    long
FROM {{ ref('stg_user') }}