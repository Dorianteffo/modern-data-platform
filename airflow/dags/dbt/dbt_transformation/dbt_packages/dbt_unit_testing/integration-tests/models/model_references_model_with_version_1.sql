{% if dbt_unit_testing.version_bigger_or_equal_to("1.5.0") %}
  select * from {{ ref('model_with_version', v=1) }} where a > 1
{% endif %} 
