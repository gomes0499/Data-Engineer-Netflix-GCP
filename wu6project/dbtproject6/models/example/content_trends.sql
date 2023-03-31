-- content_trends.sql
{{ config(materialized='view') }}

SELECT
  EXTRACT(MONTH FROM watch_date) AS watch_month,
  EXTRACT(YEAR FROM watch_date) AS watch_year,
  content_id,
  content_title,
  COUNT(*) AS num_views,
  AVG(rating) AS avg_rating,
  SUM(session_duration) AS total_watch_time
FROM wu6project.wu6datasetid.netflix_table
GROUP BY
  watch_month,
  watch_year,
  content_id,
  content_title
