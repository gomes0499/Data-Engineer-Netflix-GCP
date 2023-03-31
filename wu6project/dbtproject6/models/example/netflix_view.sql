-- netflix_view.sql
{{ config(materialized='view') }}

SELECT
  user_id,
  content_id,
  content_title,
  content_category,
  genre,
  watch_date,
  rating,
  session_duration
FROM wu6project.wu6datasetid.netflix_table
