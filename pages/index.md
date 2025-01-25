---
title: Wolf Creek Pass Snowfall
hide_title: true
---

<br>

<Image 
    url="https://raw.githubusercontent.com/davidsrrose/snow-stake/refs/heads/main/media/wolf_creek_logo.png"
    description="Sample placeholder image"
    height=100
    align="center"
/>

<br>
<br>

### Cumulative snowfall since 2015
```season_cum
SELECT 
    YEAR(Date) AS Year,
    SUM(Snowfall) AS total_snowfall,
    SUM(SUM(Snowfall)) OVER (ORDER BY YEAR(Date) ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_snowfall
FROM 
    snowfall_data.daily_snowfall_data
GROUP BY 
    YEAR(Date)
ORDER BY 
    Year;
```
<LineChart 
    data={season_cum}
    x="Year"
    y="cumulative_snowfall"
    yAxisTitle="Cumulative Inches"
/>

<br>

### Historical Season Snowfall
```yoy
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
    data={yoy}
    x=Year
    y=total_snowfall 
    yAxisTitle="Inches"
/>

<br>
<br>

### EV Gas Station Map
```ev_map
select State, count(*) AS ev_station_count from ev_stations.us_alt_fuel_stations
where State not in ('CA')
group by State order by ev_station_count desc
```

<USMap data={ev_map} state=State abbreviations=true value=ev_station_count/>

<br>


### Cumulative snowfall since 2015
```season_cum
SELECT 
    YEAR(Date) AS Year,
    SUM(Snowfall) AS total_snowfall,
    SUM(SUM(Snowfall)) OVER (ORDER BY YEAR(Date) ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_snowfall
FROM 
    snowfall_data.daily_snowfall_data
GROUP BY 
    YEAR(Date)
ORDER BY 
    Year;
```
<LineChart 
    data={season_cum}
    x="Year"
    y="cumulative_snowfall"
    yAxisTitle="Cumulative Inches"
/>

<br>

### Historical Season Snowfall
```yoy
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
    data={yoy}
    x=Year
    y=total_snowfall 
    yAxisTitle="Inches"
/>

<br>
<br>

### EV Gas Station Map
```ev_map
select State, count(*) AS ev_station_count from ev_stations.us_alt_fuel_stations
where State not in ('CA')
group by State order by ev_station_count desc
```

<USMap data={ev_map} state=State abbreviations=true value=ev_station_count/>



