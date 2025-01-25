---
title: Wolf Creek Pass Snowfall
hide_title: true
---

<Image 
    url="https://raw.githubusercontent.com/davidsrrose/snow-stake/refs/heads/main/media/wolf_creek_logo.png"
    description="Sample placeholder image"
    height=80
    align="left"
/>

### Season Total Snowfall
```snow_data
SELECT 
    YEAR(Date) AS Year,
    SUM(Snowfall) AS total_snowfall
FROM 
    snowfall_data.daily_snowfall_data
GROUP BY 
    YEAR(Date)
ORDER BY 
    Year;


```
<LineChart 
    data={snow_data}
    x=Year
    y=total_snowfall 
    yAxisTitle="Inches"
/>

### EV Gas Station Map
```ev_map
select State, count(*) AS ev_station_count from ev_stations.us_alt_fuel_stations
where State not in ('CA')
group by State order by ev_station_count desc
```

<USMap data={ev_map} state=State abbreviations=true value=ev_station_count/>

