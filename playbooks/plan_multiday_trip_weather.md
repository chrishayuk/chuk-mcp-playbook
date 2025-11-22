# Playbook: Plan Multi-Day Trip Weather

## Description
This playbook provides a comprehensive weather forecast for multi-day trips (up to 16 days), helping users plan activities, pack appropriately, and identify the best days for outdoor activities. It includes daily summaries, temperature ranges, precipitation, and activity recommendations.

## Prerequisites
- Destination location name OR coordinates
- Trip duration (number of days)
- Access to the chuk-mcp-open-meteo server

## Steps

1. Obtain the destination coordinates
   - Geocode destination name to latitude/longitude if needed
   - Validate coordinates

2. Request comprehensive weather forecast
   - Call weather forecast API with appropriate forecast_days (up to 16)
   - Request both daily and hourly variables for detailed planning
   - Include temperature, precipitation, wind, and weather codes

3. Analyze daily weather patterns
   - Review temperature ranges (highs/lows) for each day
   - Identify precipitation days and amounts
   - Check wind conditions
   - Interpret weather codes for conditions

4. Identify best days for activities
   - Find days with good weather (no rain, moderate temps, light wind)
   - Highlight challenging weather days (storms, extreme temps)
   - Recommend indoor vs outdoor activity days

5. Provide packing recommendations
   - Suggest clothing based on temperature range
   - Recommend rain gear if precipitation expected
   - Advise on sun protection, layers, etc.

6. Format comprehensive trip forecast
   - Day-by-day weather summary
   - Best/worst days for outdoor activities
   - Packing checklist
   - Overall trip weather assessment

## MCP Tools Required

### chuk-mcp-open-meteo

**Tool 1**: `geocode_location` (if location name is provided)
- **Parameters**:
  - `name` (string): Destination name (e.g., "Barcelona", "Vancouver", "Rome")
  - `count` (int): Number of results (default: 5)
  - `language` (string): Language code (default: "en")
- **Returns**: Coordinates (latitude, longitude) for the location

**Tool 2**: `get_weather_forecast`
- **Parameters**:
  - `latitude` (float): Destination latitude from geocoding
  - `longitude` (float): Destination longitude from geocoding
  - `temperature_unit` (string): "celsius" or "fahrenheit" (default: "celsius")
  - `wind_speed_unit` (string): "kmh", "ms", "mph", or "kn" (default: "kmh")
  - `precipitation_unit` (string): "mm" or "inch" (default: "mm")
  - `timezone` (string): Timezone (default: "auto")
  - `forecast_days` (int): Trip duration in days (1-16, default: 7)
  - `current_weather` (bool): Set to True for current conditions
  - `daily` (string): Comma-separated daily variables:
    - `temperature_2m_max` - Daily high temperature
    - `temperature_2m_min` - Daily low temperature
    - `precipitation_sum` - Total daily precipitation
    - `rain_sum` - Total daily rainfall
    - `precipitation_hours` - Hours of precipitation
    - `wind_speed_10m_max` - Maximum wind speed
    - `sunrise` - Sunrise time
    - `sunset` - Sunset time
  - `hourly` (string): Optional hourly details for specific days:
    - `temperature_2m` - Hourly temperature
    - `precipitation` - Hourly precipitation
    - `cloud_cover` - Cloud coverage percentage
    - `wind_speed_10m` - Hourly wind speed

**Tool 3**: `interpret_weather_code` (optional, for each day's conditions)
- **Parameters**:
  - `code` (int): WMO weather code from daily forecast
- **Returns**: Human-readable description (e.g., "Partly cloudy", "Rain showers")

## Example Usage

**Input**: "I'm traveling to Barcelona for 7 days starting tomorrow. What's the weather forecast?"

**Process**:
1. Geocode "Barcelona" → lat: 41.3874, lon: 2.1686
2. Call get_weather_forecast with forecast_days=7, daily variables
3. Analyze each day's conditions
4. Identify best days for sightseeing, beach, etc.
5. Create packing list based on forecast

**Output**:
```
7-Day Weather Forecast for Barcelona (Nov 23-29, 2025):

📅 Daily Forecast:

Day 1 - Saturday, Nov 23
  ☀️ Partly cloudy
  🌡️ High: 18°C | Low: 12°C
  💧 Precipitation: 0mm (0%)
  💨 Wind: 15 km/h
  ⭐ Excellent day for outdoor activities

Day 2 - Sunday, Nov 24
  🌦️ Light rain showers
  🌡️ High: 16°C | Low: 11°C
  💧 Precipitation: 8mm (65%)
  💨 Wind: 22 km/h
  ⚠️ Indoor activities recommended, bring umbrella

Day 3 - Monday, Nov 25
  ☁️ Cloudy
  🌡️ High: 15°C | Low: 10°C
  💧 Precipitation: 2mm (15%)
  💨 Wind: 12 km/h
  ✅ Good for sightseeing, light jacket needed

Day 4 - Tuesday, Nov 26
  ☀️ Sunny
  🌡️ High: 19°C | Low: 13°C
  💧 Precipitation: 0mm (0%)
  💨 Wind: 10 km/h
  ⭐ Perfect beach/outdoor day

Day 5 - Wednesday, Nov 27
  ☀️ Sunny
  🌡️ High: 20°C | Low: 14°C
  💧 Precipitation: 0mm (0%)
  💨 Wind: 8 km/h
  ⭐ Excellent day for all activities

Day 6 - Thursday, Nov 28
  🌤️ Partly cloudy
  🌡️ High: 18°C | Low: 13°C
  💧 Precipitation: 1mm (10%)
  💨 Wind: 14 km/h
  ✅ Good for outdoor activities

Day 7 - Friday, Nov 29
  🌧️ Rain
  🌡️ High: 15°C | Low: 11°C
  💧 Precipitation: 18mm (80%)
  💨 Wind: 25 km/h
  ⚠️ Indoor day - museums, restaurants

📊 Trip Summary:
  Average High: 17°C | Average Low: 12°C
  Total Precipitation: 29mm (2 rainy days)
  Best Outdoor Days: Days 1, 4, 5 (Saturday, Tuesday, Wednesday)
  Indoor Days: Days 2, 7 (Sunday, Friday)

🎒 Packing Recommendations:
  ✅ Light jacket/sweater (cool mornings/evenings)
  ✅ Rain jacket and umbrella (2 rainy days expected)
  ✅ Comfortable walking shoes (some wet conditions)
  ✅ Sunglasses and sunscreen (sunny days)
  ✅ Layers (temperature varies 15-20°C)
  ✅ Long pants and short sleeves (mix for 15-20°C range)

💡 Activity Planning Tips:
  - Schedule outdoor sightseeing for Days 4-5 (best weather)
  - Book beach activities for Days 1, 4, or 5
  - Plan museum/indoor visits for Days 2 and 7
  - Sunrise: ~7:25 AM | Sunset: ~5:20 PM (short days)
  - 9-10 hours of daylight - plan accordingly

Overall Assessment: GOOD trip weather - 5 pleasant days, 2 rainy days
```

## Expected Response Format

```
[N]-Day Weather Forecast for [Location] ([Date Range]):

📅 Daily Forecast:

Day [N] - [Day of Week], [Date]
  [Weather Icon] [Conditions]
  🌡️ High: [TEMP]°C | Low: [TEMP]°C
  💧 Precipitation: [AMOUNT]mm ([PROBABILITY]%)
  💨 Wind: [SPEED] km/h
  [Activity Recommendation]

[Repeat for each day...]

📊 Trip Summary:
  Average High: [TEMP]°C | Average Low: [TEMP]°C
  Total Precipitation: [AMOUNT]mm ([N] rainy days)
  Best Outdoor Days: [List days]
  Indoor Days: [List days]

🎒 Packing Recommendations:
  ✅ [Item based on conditions]
  ✅ [Item based on conditions]
  ...

💡 Activity Planning Tips:
  - [Specific day recommendations]
  - [Timing considerations]
  - [Daylight hours]

Overall Assessment: [EXCELLENT/GOOD/MIXED/CHALLENGING] trip weather - [summary]
```

## Weather Quality Ratings

### Excellent Outdoor Day
- No precipitation (0mm)
- Temperature 15-25°C (comfortable)
- Wind < 15 km/h
- Clear or partly cloudy

### Good Day
- Light/no precipitation (< 5mm)
- Temperature 10-28°C
- Wind < 20 km/h
- Any sky conditions except storms

### Fair Day
- Moderate precipitation (5-15mm) or brief showers
- Temperature 5-30°C
- Wind 20-30 km/h
- Activities possible with adjustments

### Poor Day (Indoor Recommended)
- Heavy precipitation (> 15mm)
- Extreme temperatures (< 5°C or > 30°C)
- Strong wind (> 30 km/h)
- Thunderstorms

## Packing Guidelines by Temperature Range

### Cold (< 10°C)
- Heavy jacket or winter coat
- Warm layers (sweaters, thermal underwear)
- Gloves, scarf, hat
- Warm, waterproof boots

### Cool (10-15°C)
- Medium jacket or fleece
- Long pants, long sleeves
- Light sweater for layers
- Closed-toe shoes

### Mild (15-20°C)
- Light jacket or cardigan
- Mix of long pants and shorts
- T-shirts and light long sleeves
- Comfortable walking shoes

### Warm (20-25°C)
- Light clothing (shorts, t-shirts)
- One light layer for evenings
- Sandals or light shoes
- Sun hat, sunglasses

### Hot (> 25°C)
- Light, breathable clothing
- Sun protection (hat, sunscreen)
- Sunglasses
- Light shoes/sandals
- Stay hydrated

## Activity Planning by Conditions

### Precipitation-Based Activities

**Sunny/No Rain Days**:
- Beach activities
- Hiking and outdoor sports
- Photography and sightseeing
- Outdoor dining
- Parks and gardens

**Partly Cloudy/Light Rain**:
- City sightseeing (covered areas)
- Outdoor markets (bring umbrella)
- Short outdoor activities
- Mixed indoor/outdoor

**Rainy Days**:
- Museums and galleries
- Indoor attractions
- Shopping centers
- Restaurants and cafes
- Spa/wellness activities
- Theater/cinema

### Wind-Based Activities

**Light Wind (< 15 km/h)**: All activities safe
**Moderate Wind (15-25 km/h)**: Avoid beach umbrellas, light outdoor gear
**Strong Wind (25-40 km/h)**: Secure belongings, indoor activities better
**Very Strong Wind (> 40 km/h)**: Stay indoors, avoid coastal areas

## Trip Weather Assessment

### Excellent Trip Weather
- 80%+ days with good/excellent conditions
- < 2 rainy days
- Comfortable temperature range
- Light winds

### Good Trip Weather
- 60-80% days with good conditions
- 2-3 rainy days
- Acceptable temperature range
- Moderate winds

### Mixed Trip Weather
- 40-60% days with good conditions
- 3-5 rainy days
- Variable temperatures
- Some challenging weather

### Challenging Trip Weather
- < 40% good weather days
- Frequent rain or storms
- Extreme temperatures
- Strong winds common

## Error Handling

- Location not found: Ask for more specific destination
- Forecast days > 16: Inform user of 16-day maximum, suggest breaking into periods
- API error: Inform user and suggest retry
- Invalid dates: Forecast only available for future dates

## Safety Notes

- Weather forecasts become less accurate beyond 7 days
- Always check forecast again 1-2 days before specific activities
- Local microclimates may differ (mountains, coasts)
- Emergency weather can change rapidly - monitor local alerts
- Temperature "feels like" may differ from actual (wind chill, humidity)
- UV index important even on cloudy days
- Altitude affects temperature (cooler in mountains)

## Notes

- Book flexible activities when possible (weather may change)
- Most accurate forecasts are within 5-7 days
- Hourly forecasts help plan specific activity timing
- Sunrise/sunset times affect available daylight for activities
- Coastal areas often have different weather than inland
- Mountain weather is more unpredictable
- Some seasons have more reliable forecasts than others
- Consider travel insurance for weather-dependent trips
