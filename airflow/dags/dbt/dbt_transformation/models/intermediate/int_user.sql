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
FROM {{ ref('stg_user') }}