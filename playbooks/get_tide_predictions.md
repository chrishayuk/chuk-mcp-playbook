# Playbook: Get Tide Predictions

## Description
This playbook retrieves tide predictions (high tide and low tide times and heights) for a specific coastal location using marine forecast data. Tides follow a predictable cycle of approximately two high tides and two low tides per day.

## Prerequisites
- Coastal location name OR coordinates
- Access to the chuk-mcp-open-meteo server

## Steps

1. Obtain the coastal location coordinates
   - Geocode coastal location name to latitude/longitude if needed
   - Validate coordinates are near a coastline or ocean

2. Request marine forecast with tide data
   - Call the marine forecast API with sea level height parameter
   - Request hourly data for accurate tide timing
   - Get forecast for desired number of days

3. Analyze sea level height data
   - Identify peaks in sea_level_height_msl (high tides)
   - Identify troughs in sea_level_height_msl (low tides)
   - Extract times and heights for each tide event

4. Format tide predictions
   - List high and low tides chronologically
   - Include time (local timezone) and height (meters)
   - Indicate tidal range (difference between high and low)

5. Return formatted tide predictions to user

## MCP Tools Required

### chuk-mcp-open-meteo

**Tool 1**: `geocode_location` (if location name is provided)
- **Parameters**:
  - `name` (string): Coastal location name (e.g., "Portsmouth", "Boston Harbor", "Sydney")
  - `count` (int): Number of results (default: 5)
  - `language` (string): Language code (default: "en")
- **Returns**: Coordinates (latitude, longitude) for the location

**Tool 2**: `get_marine_forecast`
- **Parameters**:
  - `latitude` (float): Location latitude from geocoding
  - `longitude` (float): Location longitude from geocoding
  - `timezone` (string): Timezone (default: "auto")
  - `forecast_days` (int): Number of days to forecast (default: 1, max: 16)
  - `hourly` (string): Must include `sea_level_height_msl` for tide data
    - `sea_level_height_msl` - Sea level height in meters relative to mean sea level
    - Positive values = higher than average (high tide approaching/present)
    - Negative values = lower than average (low tide approaching/present)

## Example Usage

**Input**: "What time is high tide today in Dover?"

**Process**:
1. Geocode "Dover" → lat: 51.1295, lon: 1.3089
2. Call get_marine_forecast with hourly="sea_level_height_msl"
3. Analyze hourly sea level data to find peaks (high tides) and troughs (low tides)
4. Extract times and heights
5. Format and present results

**Output**:
```
Tide Predictions for Dover (2025-11-23):

High Tides:
  05:30 - +1.52m above mean sea level
  17:45 - +1.38m above mean sea level

Low Tides:
  00:15 - -2.05m below mean sea level
  12:20 - -2.15m below mean sea level

Tidal Range: ~3.6m (moderate)

Next High Tide: 05:30 (in 6 hours)
```

## Expected Response Format

```
Tide Predictions for [Location] ([Date]):

High Tides:
  [TIME] - [HEIGHT]m above mean sea level
  [TIME] - [HEIGHT]m above mean sea level

Low Tides:
  [TIME] - [HEIGHT]m below mean sea level
  [TIME] - [HEIGHT]m below mean sea level

Tidal Range: ~[RANGE]m ([small/moderate/large])

Next High Tide: [TIME] ([relative time])
Next Low Tide: [TIME] ([relative time])
```

## Tidal Range Guidelines

### Range Classification
- **Small (< 2m)**: Minimal tidal variation, safer for harbor navigation
- **Moderate (2-4m)**: Standard tidal range for most locations
- **Large (4-6m)**: Significant tidal variation, strong currents possible
- **Very Large (> 6m)**: Extreme tidal range (e.g., Bay of Fundy), very strong currents

### Current Strength
- Tidal currents are strongest during mid-tide (halfway between high and low)
- Slack water (weakest currents) occurs at high tide and low tide peaks
- Large tidal ranges = stronger currents = more dangerous for swimming

### Timing Patterns
- Tides typically occur every ~6 hours 12 minutes (semi-diurnal pattern)
- Two high tides and two low tides per day in most locations
- Times shift approximately 50 minutes later each day
- Some locations have diurnal (one high/low per day) or mixed patterns

## Use Cases

### Harbor Navigation
- Plan entry/exit during high tide to avoid grounding
- Deeper draft vessels need high tide clearance
- Check local harbor depth charts against tide predictions

### Fishing
- Fish are most active during tidal changes (rising or falling)
- Best fishing often 1-2 hours before and after high/low tide
- Incoming tide brings baitfish, outgoing exposes feeding areas

### Beach Activities
- Low tide exposes more beach area, tide pools, sandbars
- High tide brings deeper water for swimming
- Avoid getting trapped by incoming tide on rocks/sandbars

### Surfing
- Different breaks work better at different tides
- Rising tide often brings larger swells
- Some reefs only break at specific tide heights

### Swimming Safety
- Avoid swimming during mid-tide (strongest currents)
- Safer to swim near high or low slack water
- Be aware of rip currents stronger during tidal changes

## Error Handling

- Location not coastal: Inform user that tide data requires ocean/coastal coordinates
- No marine data available: Some inland seas may not have tide data
- API error: Inform user and suggest retry
- Invalid coordinates: Request valid latitude/longitude near coastline

## Safety Notes

- Tidal predictions are based on astronomical calculations (moon/sun position)
- Weather conditions (storms, wind, pressure) can affect actual tide heights
- Always check local tide tables and harbor/beach warnings
- Never turn your back on the ocean - rogue waves can occur at any tide
- Tidal currents can be dangerous - strongest during mid-tide
- Plan activities with tide timing in mind - getting cut off by rising tide is dangerous
- Some areas have rapids or whirlpools during strong tidal flows

## Notes

- Tidal cycle is driven by moon's gravitational pull (primary) and sun (secondary)
- Spring tides (larger range) occur during full and new moons
- Neap tides (smaller range) occur during quarter moons
- Local geography greatly affects tidal range and timing
- Bays and estuaries can amplify tidal range
- Some enclosed seas (Mediterranean, Baltic) have minimal tides
- Tidal predictions become less accurate further in advance (best within 7 days)
