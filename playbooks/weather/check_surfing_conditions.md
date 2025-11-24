# Playbook: Check Surfing Conditions

## Description
This playbook evaluates current and forecasted surfing conditions for a specific coastal location, including wave height, swell, wind, tides, and weather to help determine if conditions are suitable for surfing.

## Prerequisites
- Coastal location name OR coordinates
- Access to the chuk-mcp-open-meteo server

## Steps

1. Obtain the location coordinates
   - Geocode coastal location name to latitude/longitude if needed
   - Validate coordinates are near coastline

2. Request marine and weather forecast data
   - Call the weather API with marine forecast parameters
   - Request wave height, wave period, swell data
   - Request wind speed and direction (crucial for surf quality)
   - Request hourly weather data for context

3. Analyze surfing conditions
   - Evaluate wave height (suitable range typically 0.5m - 3m depending on skill level)
   - Check wave period (longer periods = cleaner, more powerful waves; >8s ideal, 6-8s moderate)
   - Assess swell height and direction
   - Check wind conditions (offshore = clean, onshore = choppy)
   - Review tide data (sea level changes affect wave quality)

4. Determine optimal timing
   - Identify best time windows based on wave size, period, and wind
   - Consider tide cycles (some breaks work better at specific tides)
   - Factor in weather conditions (rain, temperature, visibility)

5. Provide surfing recommendation
   - Skill level suitability (beginner/intermediate/advanced)
   - Best time window(s) to surf
   - Wave quality assessment
   - Safety considerations (wind strength, currents, water temperature)
   - Gear recommendations (wetsuit thickness, etc.)

## MCP Tools Required

### chuk-mcp-open-meteo

**Tool 1**: `geocode_location` (if location name is provided)
- **Parameters**:
  - `name` (string): Coastal location name (e.g., "Newquay", "Bondi Beach", "Huntington Beach")
  - `count` (int): Number of results (default: 5)
  - `language` (string): Language code (default: "en")
- **Returns**: Coordinates (latitude, longitude) for the location

**Tool 2**: `get_weather_forecast`
- **Parameters**:
  - `latitude` (float): Location latitude from geocoding
  - `longitude` (float): Location longitude from geocoding
  - `temperature_unit` (string): "celsius" or "fahrenheit" (default: "celsius")
  - `wind_speed_unit` (string): "kmh", "ms", "mph", or "kn" (default: "kmh")
  - `precipitation_unit` (string): "mm" or "inch" (default: "mm")
  - `timezone` (string): Timezone (default: "auto")
  - `forecast_days` (int): Number of days to forecast (default: 1)
  - `current_weather` (bool): Set to True to get current conditions
  - `hourly` (string): Comma-separated list of marine and weather variables:
    - `wave_height` - Significant wave height (meters)
    - `wave_period` - Wave period (seconds) - key quality indicator
    - `wave_direction` - Wave direction (degrees)
    - `swell_wave_height` - Swell component height
    - `wind_wave_height` - Wind-driven wave height
    - `wind_speed_10m` - Wind speed at 10m
    - `wind_direction_10m` - Wind direction
    - `temperature_2m` - Air temperature
    - `precipitation` - Precipitation amount
    - `cloud_cover` - Cloud coverage percentage

**Tool 3**: `interpret_weather_code` (optional, for weather conditions)
- **Parameters**:
  - `code` (int): WMO weather code from current_weather
- **Returns**: Human-readable description (e.g., "Clear sky", "Rain")

## Example Usage

**Input**: "Should I go surfing in Biarritz today?"

**Process**:
1. Geocode "Biarritz" → lat: 43.4832, lon: -1.5586
2. Call get_weather_forecast requesting marine forecast variables
3. Analyze wave height, period, swell, wind, and tide data
4. Determine optimal time windows
5. Provide skill-appropriate recommendation

**Output**:
```
Surfing Conditions for Biarritz:

Current Conditions (14:00):
- Wave Height: 1.8m (moderate)
- Wave Period: 9s (good - clean, organized waves)
- Swell: 1.5m SW (favorable direction)
- Wind: 12 km/h offshore NE (clean conditions)
- Water Temp: 16°C (4/3mm wetsuit recommended)
- Air Temp: 18°C
- Conditions: Partly cloudy

Recommendation: GOOD CONDITIONS - Intermediate to Advanced
- Best Time: 14:00-18:00 (rising tide, offshore winds)
- Wave Quality: Clean, organized sets
- Skill Level: Intermediate+ (1.8m waves with 9s period = powerful)
- Gear: 4/3mm wetsuit, standard shortboard

Safety Notes:
- Offshore wind - stay aware of position
- Rising tide - currents may strengthen
- Check local break-specific hazards
```

## Expected Response Format

```
Surfing Conditions for [Location]:

Current Conditions ([TIME]):
- Wave Height: [HEIGHT]m ([size description])
- Wave Period: [PERIOD]s ([quality description])
- Swell: [SWELL_HEIGHT]m [DIRECTION] ([assessment])
- Wind: [SPEED] km/h [DIRECTION] ([onshore/offshore/cross])
- Water Temp: [TEMP]°C ([wetsuit recommendation])
- Air Temp: [TEMP]°C
- Conditions: [WEATHER_DESCRIPTION]

Recommendation: [QUALITY RATING] - [SKILL LEVEL]
- Best Time: [TIME_WINDOW] ([tide/wind/swell reasoning])
- Wave Quality: [DESCRIPTION]
- Skill Level: [BEGINNER/INTERMEDIATE/ADVANCED]
- Gear: [WETSUIT], [BOARD_TYPE]

Safety Notes:
- [WIND_CONSIDERATIONS]
- [TIDE_CONSIDERATIONS]
- [CURRENT_WARNINGS]
- [LOCAL_HAZARDS]
```

## Surfing Condition Guidelines

### Wave Height Recommendations
- **Beginner**: 0.5m - 1.2m (small, manageable waves)
- **Intermediate**: 1.0m - 2.0m (moderate waves)
- **Advanced**: 1.5m - 3.0m+ (larger, more powerful waves)

### Wave Period Quality
- **Short (< 6s)**: Choppy, wind-driven waves - lower quality
- **Medium (6-8s)**: Moderate quality, punchy waves
- **Good (8-10s)**: Clean, organized waves - good quality
- **Excellent (> 10s)**: Long-period swell - premium conditions

### Wind Assessment
- **Offshore wind** (blowing from land to sea): Cleans up waves, best for surfing
- **Onshore wind** (blowing from sea to land): Creates choppy, messy conditions
- **Cross-shore wind**: Variable quality depending on angle
- **Light wind (< 15 km/h)**: Generally favorable
- **Strong wind (> 25 km/h)**: Challenging conditions, affects wave quality

### Tide Considerations
- Different breaks work better at different tides
- Rising tide often brings in larger swells
- Falling tide can expose reefs/sandbars
- Extreme low/high tides may close out breaks

### Water Temperature & Wetsuit Guide
- **< 12°C**: 5/4mm or 6/5mm wetsuit + boots + hood + gloves
- **12-15°C**: 4/3mm wetsuit + boots (optional hood)
- **15-18°C**: 3/2mm or 4/3mm wetsuit
- **18-21°C**: 3/2mm or spring suit
- **> 21°C**: Spring suit or boardshorts

## Error Handling

- Location not found or not coastal: Ask for more specific coastal location
- API error: Inform user and suggest retry
- Invalid marine data: Report which data is unavailable
- No swell/wave data: Inform user marine forecast unavailable for this location

## Safety Notes

- Always check local surf reports and webcams before going
- Be aware of rip currents, especially on rising/falling tides
- Never surf alone in challenging conditions
- Know your skill level and stay within your limits
- Check for lifeguard presence and beach warnings
- Offshore winds can push you out to sea - stay vigilant
- Cold water requires appropriate thermal protection
- Strong tidal ranges = stronger currents

## Notes

- Marine forecast data updates every 1-3 hours
- Swell direction relative to beach orientation affects wave quality
- Local break knowledge is crucial (reefs, points, beach breaks behave differently)
- Weather conditions affect visibility and comfort but not always wave quality
- Wave period is often the most important quality indicator after wave height
- Dawn/dusk sessions may have different wind patterns than midday
