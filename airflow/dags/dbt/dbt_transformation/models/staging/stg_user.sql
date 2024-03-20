WITH user_occu AS (
    SELECT
        user_id AS user_id, 
        ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY dt_current_timestamp DESC) AS rn,  
        password AS password,
        first_name AS first_name,
        last_name AS last_name,
        username AS username,
        email AS email,
        avatar AS avatar,
        gender AS gender,
        phone_number AS phone_number,
        social_insurance_number AS social_insurance_number,
        date_of_birth AS date_of_birth,
        role AS role,
        city AS city,
        street_name AS street_name,
        street_address AS street_address,
        zip_code::integer AS zip_code,
        state AS state,
        country AS country,
        lat::float AS lat,
        lng::float AS long,
        DATEADD('SECOND', dt_current_timestamp, '1970-01-01') AS dt_timestamp
    FROM {{ dbt_unit_testing.source('app','user') }}
), 
    user_dedup AS (
        SELECT *
        FROM user_occu 
        WHERE rn=1
)
SELECT 
    user_id, 
    password,
    first_name,
    last_name,
    username,
    email,
    avatar,
    gender,
    phone_number,
    social_insurance_number,
    date_of_birth,
    role,
    city,
    street_name,
    street_address,
    zip_code,
    state,
    country,
    lat,
    long,
    dt_timestamp
FROM user_dedup 
ORDER BY dt_timestamp DESC

