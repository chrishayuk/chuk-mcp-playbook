# Playbook: Get Sunset and Sunrise Times

## Description
This playbook retrieves sunrise and sunset times for a specific location using weather data from the Open-Meteo API.

## Prerequisites
- Location information (city name OR latitude/longitude coordinates)
- Access to the chuk-mcp-open-meteo server

## Steps

1. Determine the location coordinates
   - If you have a city name, convert it to latitude and longitude using a geocoding service
   - If you already have coordinates, proceed to step 2

2. Call the Open-Meteo weather API to get daily forecast data
   - Request the daily variables for sunrise and sunset times
   - The API returns times in ISO 8601 format

3. Extract the sunrise and sunset times from the response
   - Parse the daily forecast data
   - Find today's sunrise and sunset values

4. Format the times appropriately
   - Convert from UTC to the local timezone if needed
   - Present in a readable format (e.g., "6:45 AM", "5:30 PM")

5. Return the formatted sunrise and sunset times to the user

## MCP Tools Required

### chuk-mcp-open-meteo

**Tool 1**: `geocode_location` (if location name is provided)
- **Parameters**:
  - `name` (string): Location name (e.g., "London", "Tokyo", "Sydney")
  - `count` (int): Number of results (default: 5)
  - `language` (string): Language code (default: "en")
- **Returns**: Coordinates (latitude, longitude) for the location

**Tool 2**: `get_weather_forecast`
- **Parameters**:
  - `latitude` (float): Location latitude from geocoding
  - `longitude` (float): Location longitude from geocoding
  - `timezone` (string): Timezone (default: "auto")
  - `forecast_days` (int): Number of days to forecast (default: 1)
  - `daily` (string): Comma-separated list of daily variables:
    - `sunrise` - Sunrise time in ISO 8601 format
    - `sunset` - Sunset time in ISO 8601 format
    - `daylight_duration` - Hours of daylight (optional)
    - `sunshine_duration` - Hours of sunshine (optional)

## Example Usage

**Input**: "What time is sunset in San Francisco today?"

**Process**:
1. Geocode "San Francisco" → lat: 37.7749, lon: -122.4194
2. Call get_weather_forecast with daily="sunrise,sunset"
3. Extract today's data from the daily forecast
4. Format the times in local timezone

**Output**:
```
Sunrise: 6:52 AM
Sunset: 5:23 PM
```

## Expected Response Format

Return the times in a clear, easy-to-read format:
```
For [Location]:
- Sunrise: [TIME]
- Sunset: [TIME]
```

## Error Handling

- If location cannot be geocoded, ask the user for coordinates or a more specific location
- If the API is unavailable, inform the user and suggest trying again later
- If coordinates are invalid, request valid latitude (-90 to 90) and longitude (-180 to 180)

## Notes

- Sunrise and sunset times vary by date and location
- Times are typically returned in UTC and should be converted to local time
- The Open-Meteo API is free and doesn't require authentication
