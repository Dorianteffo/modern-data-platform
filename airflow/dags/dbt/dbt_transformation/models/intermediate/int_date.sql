WITH date_occu AS (
    SELECT 
        {{ dbt_utils.generate_surrogate_key([
            'dt_timestamp'
            ]) 
        }} AS date_id,
        HOUR(dt_timestamp) AS hour,
        DAY(dt_timestamp) AS day_of_month,
        DAYOFWEEKISO(dt_timestamp) AS day_of_week,
        WEEK(dt_timestamp) AS week,
        MONTH(dt_timestamp) AS month,
        CEIL(MONTH(dt_timestamp) / 3) AS quarter,
        YEAR(dt_timestamp) AS year,
        dt_timestamp,
        ROW_NUMBER() OVER(PARTITION BY dt_timestamp ORDER BY dt_timestamp DESC) as rn
    FROM {{ dbt_unit_testing.ref('stg_user') }}
), 

 date_dedup AS (
    SELECT *
    FROM date_occu
    WHERE rn = 1 
)

SELECT
    date_id,
    hour,
    day_of_month,
    day_of_week,
    week,
    month,
    quarter,
    year,
    dt_timestamp
FROM date_dedup
ORDER BY dt_timestamp DESC