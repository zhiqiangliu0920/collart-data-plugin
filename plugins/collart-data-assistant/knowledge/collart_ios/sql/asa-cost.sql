-- DATE start_date/end_date; keyword-level ASA cost, not the default company operating-cost contract.
SELECT event_date, campaign_id, campaign_name, adgroup_id, adgroup_name,
  IFNULL(CAST(keyword_id AS STRING), '(no_keyword)') AS keyword_id, country,
  SUM(cost_usd) AS cost_usd, SUM(cost_cny) AS cost_cny,
  SUM(impressions) AS impressions, SUM(clicks) AS clicks, SUM(installs) AS installs
FROM `aidata2025.dws.dws_oper_asa_delivery_di`
WHERE event_date BETWEEN @start_date AND @end_date
  AND package_name = 'ai.photo.video.generator.fotos.ai.image.picture.editor.app.free'
GROUP BY event_date, campaign_id, campaign_name, adgroup_id, adgroup_name, keyword_id, country;
