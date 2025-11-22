# Playbook: Get Weather Forecast

## Description
This playbook retrieves a multi-day weather forecast for any location worldwide using the Open-Meteo API.

## Prerequisites
- Location information (city name OR coordinates)
- Access to the chuk-mcp-open-meteo server
- Number of forecast days desired (typically 1-7 days)

## Steps

1. Get the location coordinates
   - Convert city name to latitude/longitude if needed
   - Validate coordinates are within valid ranges

2. Determine which weather variables to request
   - Temperature (high and low)
   - Precipitation probability and amount
   - Weather code (for conditions like sunny, rainy, etc.)
   - Wind speed and direction
   - Any other relevant variables

3. Call the Open-Meteo forecast API
   - Request daily forecast data with desired variables
   - Specify the number of forecast days

4. Parse the forecast response
   - Extract daily data for each forecast day
   - Organize by date

5. Format the forecast data for readability
   - Show date, temperature range, conditions, precipitation
   - Present in a structured, easy-to-read format

6. Return the formatted forecast to the user

## MCP Tools Required

### chuk-mcp-open-meteo
- **Tool**: `get_forecast`
- **Parameters**:
  - `latitude` (float): Location latitude
  - `longitude` (float): Location longitude
  - `daily` (list): Weather variables to include, such as:
    - `temperature_2m_max` - Daily maximum temperature
    - `temperature_2m_min` - Daily minimum temperature
    - `precipitation_sum` - Total daily precipitation
    - `precipitation_probability_max` - Max precipitation probability
    - `weather_code` - Weather condition code
    - `wind_speed_10m_max` - Maximum wind speed
  - `forecast_days` (int, optional): Number of days to forecast (default: 7)

## Example Usage

**Input**: "What's the 3-day weather forecast for London?"

**Process**:
1. Geocode "London" → lat: 51.5074, lon: -0.1278
2. Call get_forecast with 3-day forecast and relevant variables
3. Parse and format the response

**Output**:
```
3-Day Weather Forecast for London:

Day 1 (2024-11-23):
- High: 12°C / Low: 7°C
- Conditions: Partly cloudy
- Precipitation: 20% chance, 0.5mm expected
- Wind: 15 km/h

Day 2 (2024-11-24):
- High: 10°C / Low: 5°C
- Conditions: Rainy
- Precipitation: 80% chance, 8mm expected
- Wind: 25 km/h

Day 3 (2024-11-25):
- High: 11°C / Low: 6°C
- Conditions: Overcast
- Precipitation: 30% chance, 1mm expected
- Wind: 18 km/h
```

## Expected Response Format

Present the forecast in a structured daily format:
```
[N]-Day Weather Forecast for [Location]:

Day X ([Date]):
- High: [TEMP] / Low: [TEMP]
- Conditions: [DESCRIPTION]
- Precipitation: [PROBABILITY]%, [AMOUNT]mm expected
- Wind: [SPEED] km/h
```

## Error Handling

- Invalid location: Request more specific location or coordinates
- API unavailable: Inform user and suggest retry
- Invalid date range: Ensure forecast days is between 1-16

## Notes

- Open-Meteo provides up to 16 days of forecast
- Weather codes need to be translated to human-readable conditions
- All temperatures are in Celsius by default (can specify Fahrenheit)
- Free API with no authentication required
