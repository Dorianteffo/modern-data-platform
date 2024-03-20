{{ config(tags=['unit-test']) }}

{% call dbt_unit_testing.test ('int_date','test_date_manip') %}
  {% call dbt_unit_testing.mock_ref('stg_user') %}
    SELECT 
      '2024-03-16 14:15:06'::TIMESTAMP AS dt_timestamp
    UNION ALL 
    SELECT 
      '2024-05-17 16:15:06'::TIMESTAMP AS dt_timestamp
  {% endcall %}


  {% call dbt_unit_testing.expect() %}
    WITH dt_timestamp_cte AS (
      SELECT 
        '2024-03-16 14:15:06'::TIMESTAMP AS dt_timestamp1,
        '2024-05-17 16:15:06'::TIMESTAMP AS dt_timestamp2
    )
    SELECT
      {{ dbt_utils.generate_surrogate_key([
        'dt_timestamp1'
        ]) 
        }} AS date_id,
      14 AS hour,
      16 AS day_of_month,
      6 AS day_of_week,
      11 AS week,
      3 AS month,
      1 AS quarter,
      2024 AS year,
      dt_timestamp1 AS dt_timestamp
    FROM dt_timestamp_cte
    UNION ALL 
    SELECT
      {{ dbt_utils.generate_surrogate_key([
        'dt_timestamp2'
        ]) 
        }} AS date_id,
      16 AS hour,
      17 AS day_of_month,
      5 AS day_of_week,
      20 AS week,
      5 AS month,
      2 AS quarter,
      2024 AS year,
      dt_timestamp2 AS dt_timestamp
    FROM dt_timestamp_cte

  {% endcall %}

{% endcall %}