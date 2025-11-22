# Playbook: Get Current Weather Conditions

## Description
This playbook retrieves current weather conditions for a specific location using real-time weather data.

## Prerequisites
- Location information (city name OR coordinates)
- Access to the chuk-mcp-open-meteo server

## Steps

1. Obtain the location coordinates
   - Geocode city name to latitude/longitude if needed
   - Validate coordinates

2. Request current weather data
   - Call the weather API with current weather parameters
   - Request relevant variables like temperature, conditions, wind, etc.

3. Parse the current weather response
   - Extract temperature, "feels like" temperature
   - Get weather conditions (clear, cloudy, rain, etc.)
   - Retrieve wind speed and direction
   - Get humidity and pressure data
   - Check precipitation status

4. Format the weather data
   - Create a readable summary of current conditions
   - Include all relevant measurements with units

5. Return the formatted current weather to the user

## MCP Tools Required

### chuk-mcp-open-meteo

**Tool 1**: `geocode_location` (if location name is provided)
- **Parameters**:
  - `name` (string): Location name (e.g., "London", "Paris", "New York")
  - `count` (int): Number of results (default: 5)
  - `language` (string): Language code (default: "en")
- **Returns**: Coordinates (latitude, longitude) for the location

**Tool 2**: `get_weather_forecast`
- **Parameters**:
  - `latitude` (float): Location latitude from geocoding
  - `longitude` (float): Location longitude from geocoding
  - `temperature_unit` (string): "celsius" or "fahrenheit" (default: "celsius")
  - `wind_speed_unit` (string): "kmh", "ms", "mph", or "kn" (default: "kmh")
  - `timezone` (string): Timezone (default: "auto")
  - `current_weather` (bool): Set to True to get current conditions
  - `hourly` (string): Comma-separated list of hourly variables:
    - `temperature_2m` - Current temperature
    - `apparent_temperature` - Feels like temperature
    - `relative_humidity_2m` - Humidity percentage
    - `precipitation` - Current precipitation
    - `wind_speed_10m` - Wind speed
    - `wind_direction_10m` - Wind direction
    - `pressure_msl` - Sea level pressure
    - `cloudcover` - Cloud coverage percentage

**Tool 3**: `interpret_weather_code` (optional, for human-readable conditions)
- **Parameters**:
  - `code` (int): WMO weather code from current_weather
- **Returns**: Human-readable description (e.g., "Slight rain", "Partly cloudy")

## Example Usage

**Input**: "What's the current weather in Tokyo?"

**Process**:
1. Geocode "Tokyo" → lat: 35.6762, lon: 139.6503
2. Call get_forecast requesting current weather variables
3. Parse and format current conditions

**Output**:
```
Current Weather in Tokyo:

Temperature: 18°C (Feels like: 16°C)
Conditions: Partly cloudy
Humidity: 65%
Wind: 12 km/h from Northwest
Pressure: 1013 hPa
Precipitation: None
```

## Expected Response Format

```
Current Weather in [Location]:

Temperature: [TEMP]°C (Feels like: [APPARENT_TEMP]°C)
Conditions: [WEATHER_DESCRIPTION]
Humidity: [HUMIDITY]%
Wind: [SPEED] km/h from [DIRECTION]
Pressure: [PRESSURE] hPa
Precipitation: [AMOUNT or "None"]
```

## Error Handling

- Location not found: Ask for more specific location or coordinates
- API error: Inform user and suggest retry
- Invalid data: Report which data is unavailable

## Notes

- Current weather updates every 15 minutes
- Weather code needs to be mapped to descriptions:
  - 0: Clear sky
  - 1-3: Partly cloudy
  - 45, 48: Fog
  - 51-67: Rain (various intensities)
  - 71-86: Snow (various intensities)
  - 95-99: Thunderstorm
- Wind direction: Convert degrees to compass directions (N, NE, E, etc.)
- Apparent temperature accounts for wind chill and humidity
