# Playbook: Compare Weather on Recurring Dates (Anniversaries, Birthdays, Annual Events)

## Description
This playbook compares weather conditions for the same date across multiple years to answer questions like "Which anniversary was warmest?" or "What was the weather like on my birthday each year?" It handles recurring date queries by fetching multi-year data and filtering to specific dates.

## Prerequisites
- Recurring date (e.g., "August 30th", "December 25th")
- Year range to compare (e.g., 2003-2025)
- Location name OR coordinates
- Access to the chuk-mcp-open-meteo server

## Steps

1. Obtain the location coordinates
   - Geocode location name to latitude/longitude if needed
   - Validate coordinates

2. Identify the recurring date and year range
   - Extract specific date (month and day)
   - Determine start year and end year
   - Calculate number of occurrences to compare

3. Fetch historical weather data for the full date range
   - Call historical weather API with start_date (first year's occurrence) and end_date (last year's occurrence)
   - **Important**: API returns ALL days between start and end dates (can be thousands of days)
   - Request daily temperature, precipitation, or other variables of interest

4. Parse and filter the returned data
   - Extract only dates matching the recurring date (e.g., all "08-30" dates)
   - Ignore all other days in the dataset
   - Create year-by-year comparison of the specific date

5. Analyze and compare across years
   - Identify warmest/coldest/wettest/driest occurrence
   - Calculate average conditions for that date
   - Identify trends or patterns over time
   - Note any exceptional years

6. Present findings
   - Year-by-year comparison table
   - Highlight superlatives (warmest, coldest, etc.)
   - Provide context and trends
   - Answer the specific user question

## MCP Tools Required

### chuk-mcp-open-meteo

**Tool 1**: `geocode_location` (if location name is provided)
- **Parameters**:
  - `name` (string): Location name (e.g., "London", "New York", "Tokyo")
  - `count` (int): Number of results (default: 5)
  - `language` (string): Language code (default: "en")
- **Returns**: Coordinates (latitude, longitude) for the location

**Tool 2**: `get_historical_weather`
- **Parameters**:
  - `latitude` (float): Location latitude from geocoding
  - `longitude` (float): Location longitude from geocoding
  - `start_date` (string): First occurrence date in YYYY-MM-DD format (e.g., "2003-08-30")
  - `end_date` (string): Last occurrence date in YYYY-MM-DD format (e.g., "2025-08-30")
  - `temperature_unit` (string): "celsius" or "fahrenheit" (default: "celsius")
  - `wind_speed_unit` (string): "kmh", "ms", "mph", or "kn" (default: "kmh")
  - `precipitation_unit` (string): "mm" or "inch" (default: "mm")
  - `timezone` (string): Timezone (default: "auto")
  - `daily` (string): Daily aggregated variables:
    - `temperature_2m_max` - Daily high temperature (for warmest/coldest queries)
    - `temperature_2m_min` - Daily low temperature
    - `precipitation_sum` - Total daily precipitation (for wettest/driest queries)
    - `rain_sum` - Total daily rainfall
    - `wind_speed_10m_max` - Maximum wind speed
- **Returns**: ALL daily data between start_date and end_date (needs filtering)

## Example Usage 1: Warmest Birthday

**Input**: "Which of my birthdays was the warmest? My birthday is July 4th and I've lived in Boston since 2000."

**Process**:
1. Geocode "Boston" → lat: 42.3601, lon: -71.0589
2. Identify recurring date: July 4 (07-04)
3. Year range: 2000-2025 (26 occurrences)
4. Call get_historical_weather:
   - start_date: "2000-07-04"
   - end_date: "2025-07-04"
   - daily: "temperature_2m_max,temperature_2m_min,precipitation_sum"
5. Parse response: Extract ~9000 days of data
6. Filter to only dates where month=07 AND day=04 (26 dates)
7. Compare temperature_2m_max for each July 4
8. Identify warmest year

**Output**:
```
Birthday Weather Comparison - Boston, MA (2000-2025):

🌡️ July 4th Temperature Trends (Daily Maximum):
  2000: 28.1°C | 2001: 29.4°C | 2002: 31.2°C | 2003: 27.8°C | 2004: 30.1°C
  2005: 28.9°C | 2006: 32.3°C | 2007: 29.2°C | 2008: 27.5°C | 2009: 30.8°C
  2010: 33.7°C | 2011: 31.5°C | 2012: 28.6°C | 2013: 32.1°C | 2014: 29.3°C
  2015: 27.2°C | 2016: 34.2°C | 2017: 30.5°C | 2018: 31.8°C | 2019: 29.7°C
  2020: 28.4°C | 2021: 30.2°C | 2022: 32.9°C | 2023: 29.1°C | 2024: 31.4°C
  2025: 28.8°C

📊 Birthday Analysis:
  Total Birthdays: 26 years (2000-2025)
  Average July 4th High: 30.1°C
  Temperature Range: 7.0°C (27.2°C to 34.2°C)

  🔥 Warmest Birthday: July 4, 2016 (34.2°C) - scorching hot!
     Conditions: Sunny, heat wave conditions, perfect for fireworks

  ❄️ Coolest Birthday: July 4, 2015 (27.2°C) - relatively mild
     Conditions: Comfortable summer day, great for outdoor activities

  Top 5 Warmest Birthdays:
    1. 2016: 34.2°C (scorcher!) 🥇
    2. 2010: 33.7°C (heat wave) 🥈
    3. 2022: 32.9°C (very hot) 🥉
    4. 2006: 32.3°C
    5. 2013: 32.1°C

  Coolest 3 Birthdays:
    1. 2015: 27.2°C (mild)
    2. 2008: 27.5°C (comfortable)
    3. 2003: 27.8°C (pleasant)

📈 Trends:
  Early Years (2000-2008): Average 29.4°C
  Middle Years (2009-2017): Average 30.6°C
  Recent Years (2018-2025): Average 30.3°C

  Moderate Warming: July 4th slightly warmer in recent decades
  High Variability: 7°C range shows summer temperatures can vary significantly

Summary: Your warmest birthday was in 2016 at 34.2°C - a true scorcher perfect for
Independence Day celebrations! Your coolest birthday was 2015 at 27.2°C, still warm
but much more comfortable. July 4th in Boston averages around 30°C.
```

## Example Usage 2: Wettest Birthday

**Input**: "Which of my birthdays in the last 10 years was the wettest? My birthday is June 15 and I live in Seattle."

**Process**:
1. Geocode "Seattle" → lat: 47.6062, lon: -122.3321
2. Identify recurring date: June 15 (06-15)
3. Year range: 2015-2025 (11 occurrences)
4. Call get_historical_weather:
   - start_date: "2015-06-15"
   - end_date: "2025-06-15"
   - daily: "precipitation_sum,temperature_2m_max"
5. Filter to only June 15 dates (11 dates)
6. Compare precipitation_sum for each June 15
7. Identify wettest birthday

**Output**:
```
Birthday Weather Comparison - Seattle (2015-2025):

💧 June 15th Precipitation Trends:
  2015: 0mm (dry)    | 2016: 2mm (light) | 2017: 0mm (dry)
  2018: 12mm (rainy) | 2019: 0mm (dry)   | 2020: 8mm (showers)
  2021: 18mm (heavy) | 2022: 1mm (trace) | 2023: 0mm (dry)
  2024: 6mm (light)  | 2025: 3mm (light)

📊 Birthday Rain Analysis:
  Total Birthdays: 11 years (2015-2025)
  Average June 15th Precipitation: 4.5mm
  Dry Birthdays (< 1mm): 4 years (36%)
  Rainy Birthdays (> 5mm): 4 years (36%)

  🌧️ Wettest Birthday: June 15, 2021 (18mm) - heavy rain all day
     Temperature: 16°C, overcast, umbrellas required

  ☀️ Driest Birthdays: 2015, 2017, 2019, 2023 (0mm) - perfectly dry
     Typical conditions: Sunny, 22-24°C, ideal outdoor weather

  Wettest 3 Birthdays:
    1. 2021: 18mm (heavy rain)
    2. 2018: 12mm (rainy)
    3. 2020: 8mm (showers)

Summary: Your wettest birthday was in 2021 with 18mm of rain. However, 4 out of 11
birthdays were completely dry - June 15 in Seattle has about 60% chance of being
dry or only light rain.
```

## Expected Response Format

```
[Event Type] Weather Comparison - [Location] ([Year Range]):

[METRIC] [Date] [Weather Variable] Trends:
  [Year]: [VALUE] | [Year]: [VALUE] | [Year]: [VALUE]
  [Continue for all years...]

📊 [Event] Analysis:
  Total [Events]: [NUMBER] years ([RANGE])
  Average [Date] [Variable]: [VALUE]
  [Variable] Range: [MIN] to [MAX]

  [SUPERLATIVE ICON] [Superlative] [Event]: [Date], [Year] ([VALUE])
     Conditions: [Description]

  [OPPOSITE ICON] [Opposite Superlative] [Event]: [Date], [Year] ([VALUE])
     Conditions: [Description]

  Top [N] [Superlative] [Events]:
    1. [Year]: [VALUE] ([Event number])
    2. [Year]: [VALUE] ([Event number])
    ...

📈 Trends:
  [Period 1]: Average [VALUE]
  [Period 2]: Average [VALUE]
  [Period 3]: Average [VALUE]

  [Trend description]

Summary: [Answer to user's question with key findings]
```

## Common Queries

### Temperature-Based
- "Which anniversary/birthday was the warmest/coldest?"
- "What was the temperature on my birthday each year?"
- "How does this year's [date] compare to previous years?"

### Precipitation-Based
- "Which [recurring date] was the wettest/driest?"
- "Does it usually rain on [specific date]?"
- "What's the rainiest [date] I've experienced?"

### Trend Analysis
- "Are my anniversaries getting warmer over time?"
- "Is [date] usually sunny in [location]?"
- "How variable is the weather on [date] each year?"

## Data Parsing Instructions

### Understanding the API Response
When you call `get_historical_weather` with start_date="2003-08-30" and end_date="2025-08-30":
- API returns approximately **8,036 days** of data (all days from 2003-08-30 through 2025-08-30)
- Response includes: `time` (date array), `temperature_2m_max` (value array), etc.
- You MUST filter this to only the 23 occurrences of August 30

### Filtering Process
1. **Parse the response**: Extract `time` array and corresponding value arrays
2. **Filter by date**: Keep only entries where date matches `MM-DD` pattern (e.g., "08-30")
3. **Verify count**: Should have one entry per year in range
4. **Create mapping**: Year → value pairs for easy comparison

### Example Parsing Logic
```
Response contains:
  time: ["2003-08-30", "2003-08-31", "2003-09-01", ..., "2025-08-29", "2025-08-30"]
  temperature_2m_max: [16.9, 18.2, 17.5, ..., 20.1, 19.6]

Filter to only "??-08-30" dates:
  2003-08-30: 16.9°C
  2004-08-30: 18.2°C
  2005-08-30: 19.1°C
  ...
  2025-08-30: 19.6°C

Result: 23 date-value pairs
```

## Comparison Strategies

### Find Superlative (Warmest, Coldest, Wettest, Driest)
- Compare filtered values to find maximum or minimum
- Note the year and exact value
- Provide context about conditions that day

### Calculate Statistics
- **Average**: Mean of all filtered values
- **Range**: Difference between max and min
- **Variance**: How much values differ year-to-year
- **Trend**: Compare early years vs. recent years

### Identify Patterns
- **Consistency**: Similar values each year vs. high variability
- **Climate Change**: Warming/cooling trends over time
- **Anomalies**: Exceptionally unusual years

## Handling Edge Cases

### Leap Year Dates (February 29)
- February 29 only occurs every 4 years
- Clearly note which years are missing (non-leap years)
- Calculate statistics based on available leap years only

### Recent/Future Dates
- Historical data only available up to ~yesterday
- If end_date includes future date, data will only go to most recent available
- Clearly indicate "data available through [date]"

### Incomplete Years
- First and last year in range may have partial data
- If querying current year, only data up to today is available
- Note "preliminary" or "partial year" for current year

## Error Handling

- Location not found: Request more specific location name
- Invalid date format: Recurring date must be valid (e.g., not "February 30")
- Date out of range: Historical data typically 1940-present
- API timeout: Large date ranges (> 30 years) may be slow - consider breaking into chunks
- Parsing errors: Verify date filtering logic catches all occurrences

## Safety Notes

- Historical weather data is observed/reanalyzed data, not predictions
- Past weather on a specific date does NOT predict future weather for that date
- A warm anniversary 10 years ago doesn't mean this year's anniversary will be warm
- Weather is chaotic - historical patterns provide context, not guarantees
- Climate change may make old historical data less representative of current conditions
- Use historical data to understand typical variability, not to forecast specific future dates

## Performance Considerations

### Large Date Ranges (> 20 years)
- Response contains thousands of days - may take 10-30 seconds
- Be patient during API call
- Consider chunking very long ranges (e.g., 1970-2025) into multiple calls

### Multiple Recurring Dates
- If user asks about multiple dates (e.g., "my birthday and anniversary"), make separate API calls
- Don't try to fetch both date ranges in one call

## Notes

- This playbook is specifically for **recurring dates** (same day each year)
- For general historical comparisons, use "Compare Historical Weather" playbook
- Filtering is ESSENTIAL - don't present all 8000+ days to the user
- Focus on answering the user's specific question (warmest? wettest? trend?)
- Provide context: why was that year different? Was there a weather pattern?
- Consider mentioning climate trends if relevant (warming over decades)
