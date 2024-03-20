{{ config(tags=['unit-test']) }}

{% call dbt_unit_testing.test ('stg_user','test_timestamp_conversion') %}
  {% call dbt_unit_testing.mock_source('app','user') %}
    SELECT 
        '4534222feféE33RD' AS user_id, 
        'fake_password' AS password,
        'dorian' AS first_name,
        'dorian' AS last_name,
        'dor' AS username,
        'dor@example.com' AS email,
        'https//placekitten.com/34343' AS avatar,
        'Male' AS gender,
        '677-123-3242' AS phone_number,
        '637-24-8293' AS social_insurance_number,
        '1983-02-04' AS date_of_birth,
        'data eng' AS role,
        'East Evan' AS city,
        'Stone Groves' AS street_name,
        '8393 Jason Key Suite 089' AS street_address,
        '20759' AS zip_code,
        'New York' AS state,
        'Vietnam' AS country,
        '23.343422'AS lat,
        '-134.33439' AS lng,
        '1710598506' AS dt_current_timestamp
  {% endcall %}

  {% call dbt_unit_testing.expect() %}
    SELECT 
        '4534222feféE33RD' AS user_id, 
        'fake_password' AS password,
        'dorian' AS first_name,
        'dorian' AS last_name,
        'dor' AS username,
        'dor@example.com' AS email,
        'https//placekitten.com/34343' AS avatar,
        'Male' AS gender,
        '677-123-3242' AS phone_number,
        '637-24-8293' AS social_insurance_number,
        '1983-02-04' AS date_of_birth,
        'data eng' AS role,
        'East Evan' AS city,
        'Stone Groves' AS street_name,
        '8393 Jason Key Suite 089' AS street_address,
        20759 AS zip_code,
        'New York' AS state,
        'Vietnam' AS country,
         23.343422 AS lat,
        -134.33439 AS long,
        '2024-03-16 14:15:06'::TIMESTAMP AS dt_timestamp

  {% endcall %}

{% endcall %}