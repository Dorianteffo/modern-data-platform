WITH user_occu AS (
    SELECT
        user_id AS id, 
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
        CAST(zip_code AS integer) AS zip_code,
        state AS state,
        country AS country,
        CAST(lat AS float) AS lat,
        CAST(lng AS float) AS long,
        dt_current_timestamp AS dt_timestamp
    FROM {{ source('app','user') }}
), 
    user_dedup AS (
        SELECT *
        FROM user_occu 
        WHERE rn=1
)
SELECT * 
FROM user_dedup 
ORDER BY dt_timestamp DESC

