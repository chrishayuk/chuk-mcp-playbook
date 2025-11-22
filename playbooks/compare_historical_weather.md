# Playbook: Compare Historical Weather

## Description
This playbook retrieves and compares historical weather data with current forecasts to identify patterns, trends, and anomalies. Useful for understanding climate trends, comparing conditions to past events, or analyzing seasonal patterns.

## Prerequisites
- Location name OR coordinates
- Historical date or date range to compare
- Access to the chuk-mcp-open-meteo server

## Steps

1. Obtain the location coordinates
   - Geocode location name to latitude/longitude if needed
   - Validate coordinates

2. Request historical weather data
   - Call historical weather API with start and end dates
   - Request relevant variables (temperature, precipitation, wind)
   - Get daily or hourly data based on analysis needs

3. Request current forecast data (optional)
   - Call weather forecast API for comparison period
   - Request same variables as historical query
   - Enables direct comparison of historical vs. current

4. Analyze and compare data
   - Compare temperature ranges (historical vs. current/typical)
   - Identify precipitation patterns or anomalies
   - Calculate averages, extremes, trends
   - Look for climate patterns or changes

5. Present findings
   - Highlight key differences or similarities
   - Provide context (warmer/cooler than usual, wetter/drier)
   - Show trends if analyzing multiple years
   - Answer specific user questions about historical weather

## MCP Tools Required

### chuk-mcp-open-meteo

**Tool 1**: `geocode_location` (if location name is provided)
- **Parameters**:
  - `name` (string): Location name (e.g., "Chicago", "Melbourne", "Berlin")
  - `count` (int): Number of results (default: 5)
  - `language` (string): Language code (default: "en")
- **Returns**: Coordinates (latitude, longitude) for the location

**Tool 2**: `get_historical_weather`
- **Parameters**:
  - `latitude` (float): Location latitude from geocoding
  - `longitude` (float): Location longitude from geocoding
  - `start_date` (string): Start date in YYYY-MM-DD format
  - `end_date` (string): End date in YYYY-MM-DD format
  - `temperature_unit` (string): "celsius" or "fahrenheit" (default: "celsius")
  - `wind_speed_unit` (string): "kmh", "ms", "mph", or "kn" (default: "kmh")
  - `precipitation_unit` (string): "mm" or "inch" (default: "mm")
  - `timezone` (string): Timezone (default: "auto")
  - `hourly` (string): Hourly variables (optional for detailed analysis):
    - `temperature_2m` - Hourly temperature
    - `relative_humidity_2m` - Humidity
    - `precipitation` - Precipitation
    - `wind_speed_10m` - Wind speed
    - `pressure_msl` - Sea level pressure
    - `cloud_cover` - Cloud coverage
  - `daily` (string): Daily aggregated variables (recommended):
    - `temperature_2m_max` - Daily high temperature
    - `temperature_2m_min` - Daily low temperature
    - `precipitation_sum` - Total daily precipitation
    - `rain_sum` - Total daily rainfall
    - `wind_speed_10m_max` - Maximum wind speed

**Tool 3**: `get_weather_forecast` (optional, for current comparison)
- **Parameters**:
  - `latitude` (float): Location latitude
  - `longitude` (float): Location longitude
  - `temperature_unit` (string): Same as historical query
  - `wind_speed_unit` (string): Same as historical query
  - `precipitation_unit` (string): Same as historical query
  - `timezone` (string): Timezone (default: "auto")
  - `forecast_days` (int): Number of days for comparison
  - `daily` (string): Same variables as historical query for comparison

## Example Usage

**Input**: "What was the weather like on my wedding day 5 years ago in Seattle?"

**Process**:
1. Geocode "Seattle" → lat: 47.6062, lon: -122.3321
2. Calculate date: 5 years ago from today (2020-11-23)
3. Call get_historical_weather for 2020-11-23
4. Extract and format weather data for that day
5. Optionally compare with current forecast

**Output**:
```
Historical Weather for Seattle - November 23, 2020:

🌡️ Temperature:
  High: 12°C (54°F)
  Low: 7°C (45°F)
  Average: 10°C (50°F)

💧 Precipitation:
  Total: 8mm (moderate rain)
  Hours of rain: 6 hours

💨 Wind:
  Max speed: 22 km/h
  Direction: SW (from ocean)

☁️ Conditions:
  Cloud cover: 85% (mostly cloudy)
  Overall: Rainy, typical Seattle fall weather

📊 Comparison to Current Forecast (Nov 23, 2025):
  Temperature: Current 6°C vs. 2020: 10°C (4°C cooler now)
  Precipitation: Current 12mm vs. 2020: 8mm (wetter now)
  Conditions: Similar - rainy, cloudy, typical Pacific Northwest

Summary: Your wedding day 5 years ago was mild and rainy with temperatures around 10°C.
Light jacket and umbrella weather - typical for Seattle in late November!
```

## Example Usage 2: Climate Trend Analysis

**Input**: "How has summer weather in Phoenix changed over the last 10 years?"

**Process**:
1. Geocode "Phoenix" → lat: 33.4484, lon: -112.0740
2. Query historical data for June-August for years 2015-2024
3. Calculate average temperatures, precipitation for each summer
4. Identify trends and anomalies
5. Compare with current year forecast

**Output**:
```
Summer Weather Trends - Phoenix (2015-2024):

📈 Temperature Trends (June-August Average):
  2015: 36.2°C | 2016: 36.8°C | 2017: 37.1°C | 2018: 36.5°C | 2019: 37.4°C
  2020: 37.8°C | 2021: 37.2°C | 2022: 38.1°C | 2023: 38.5°C | 2024: 38.9°C

  10-Year Average: 37.5°C
  Trend: +2.7°C increase over 10 years (warming trend)
  Hottest Summer: 2024 (38.9°C average)
  Coolest Summer: 2015 (36.2°C average)

💧 Precipitation Trends (June-August Total):
  Average: 42mm per summer (monsoon season)
  Wettest: 2018 (68mm) | Driest: 2020 (18mm)
  Trend: High variability, no clear trend

🔥 Extreme Heat Days (> 40°C):
  2015: 12 days | 2020: 18 days | 2024: 27 days
  Trend: Increasing frequency of extreme heat

Summary: Phoenix summers have warmed significantly over the past decade (+2.7°C),
with increasing frequency of extreme heat days. Monsoon precipitation remains
highly variable with no clear trend.
```

## Expected Response Format

### Single Day/Event Query
```
Historical Weather for [Location] - [Date]:

🌡️ Temperature:
  High: [TEMP]°C
  Low: [TEMP]°C
  Average: [TEMP]°C

💧 Precipitation:
  Total: [AMOUNT]mm
  Hours of precipitation: [HOURS]

💨 Wind:
  Max speed: [SPEED] km/h
  Direction: [DIRECTION]

☁️ Conditions:
  [Description of overall conditions]

📊 Comparison to [Current/Typical]:
  [Comparative analysis]

Summary: [Narrative description of the historical weather]
```

### Trend Analysis Query
```
[Period] Weather Trends - [Location] ([Year Range]):

📈 Temperature Trends:
  [Year-by-year data]
  [Period] Average: [TEMP]°C
  Trend: [Description of trend]
  Hottest [Period]: [Year] ([TEMP]°C)
  Coolest [Period]: [Year] ([TEMP]°C)

💧 Precipitation Trends:
  [Year-by-year or summary data]
  Trend: [Description]

[Other Metrics]:
  [Relevant analysis]

Summary: [Overall findings and trends]
```

## Common Use Cases

### 1. Event Memory Recall
"What was the weather like on [specific past date]?"
- Weddings, birthdays, graduations
- Historical events
- Personal milestones
- **Note**: For recurring date queries like "Which anniversary was warmest?", use the "Compare Recurring Date Weather" playbook instead

### 2. Climate Trend Analysis
"How has the climate changed over [time period]?"
- Temperature trends
- Precipitation patterns
- Extreme weather frequency

### 3. Seasonal Comparisons
"How does this winter compare to last winter?"
- Year-over-year comparisons
- Seasonal pattern analysis
- Anomaly identification

### 4. Trip Planning Historical Context
"What was the weather like in Rome last April?"
- Research weather for trip planning
- Compare to current forecast
- Understand typical conditions

### 5. Agricultural/Business Planning
"How much rain did we get last growing season?"
- Precipitation totals
- Growing degree days
- Frost dates

## Analysis Guidelines

### Temperature Analysis
- **Daily Range**: Difference between high and low
- **Averages**: Mean temperature over period
- **Extremes**: Record highs/lows
- **Trends**: Warming or cooling patterns
- **Anomalies**: Unusual heat or cold spells

### Precipitation Analysis
- **Total Accumulation**: Sum over period
- **Frequency**: Number of rainy days
- **Intensity**: Heavy vs. light precipitation events
- **Dry Spells**: Consecutive days without rain
- **Comparison**: Above or below average

### Wind Analysis
- **Average Speed**: Mean wind speed
- **Peak Gusts**: Maximum recorded
- **Prevailing Direction**: Most common wind direction
- **Calm Days**: Days with light winds

### Pattern Recognition
- **Seasonal Cycles**: Expected patterns by season
- **Climate Variability**: Natural fluctuations
- **Long-term Trends**: Multi-year changes
- **Anomalies**: Unusual events or conditions

## Data Availability

### Historical Record Length
- Most locations: 1940-present (varies by location)
- Some locations: 1900-present
- Quality and availability varies by region
- More recent data typically more complete

### Data Resolution
- **Hourly**: Available for detailed analysis
- **Daily**: Aggregated from hourly (high, low, sum, max)
- **Monthly/Yearly**: Can be calculated from daily

### Geographic Coverage
- Global coverage for most land areas
- Ocean coverage limited to certain regions
- Remote areas may have gaps or interpolated data

## Comparison Strategies

### Year-over-Year
Compare same period in different years
- "This November vs. last November"
- Identify annual variations

### Period Averages
Compare to multi-year average
- "This summer vs. 10-year summer average"
- Understand if conditions are typical or anomalous

### Extreme Events
Compare to historical extremes
- "Hottest day ever vs. today"
- Put current conditions in historical context

### Trend Analysis
Analyze multi-year patterns
- "Temperature increase over 30 years"
- Identify climate change signals

## Error Handling

- Location not found: Ask for more specific location
- Date out of range: Historical data typically 1940-present (varies by location)
- API error: Inform user and suggest retry
- Invalid date format: Request YYYY-MM-DD format
- Future dates: Historical API only supports past dates

## Safety Notes

- Historical data is observed/reanalyzed data, not predictions
- Weather patterns from the past don't guarantee future conditions
- Climate change may make historical comparisons less predictive
- Use historical data for context, not for forecasting
- Local microclimates may differ from historical records
- Extreme events are rare - historical data may not capture all extremes

## Notes

- Historical weather data is based on weather models reanalysis and station observations
- Data quality varies by location and time period
- More recent history (last 20 years) generally more accurate
- Very old data (before 1950) may be less reliable in some locations
- Hourly data provides more detail but larger data volumes
- Daily aggregates are sufficient for most comparisons
- Consider multiple years for reliable climate averages (typically 30-year periods)
- Urban areas may show heat island effects not captured in older data
- Coastal and mountain areas can have significant local variations
