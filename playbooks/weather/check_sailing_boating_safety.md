# Playbook: Check Sailing & Boating Safety Conditions

## Description
This playbook evaluates marine and weather conditions to determine if it's safe for sailing, boating, or other water vessel activities. It combines wave conditions, wind, visibility, tides, and weather forecasts to provide comprehensive maritime safety guidance.

## Prerequisites
- Departure location or sailing area (coastal/ocean coordinates)
- Access to the chuk-mcp-open-meteo server

## Steps

1. Obtain the location coordinates
   - Geocode harbor/marina/coastal location name if needed
   - Validate coordinates are over water or near coastline

2. Request marine forecast data
   - Call marine forecast API with wave, current, and tide parameters
   - Get hourly data for departure window and duration
   - Request forecast for trip duration

3. Request weather forecast data
   - Call weather forecast API with wind, visibility, and precipitation
   - Get current conditions and hourly forecast
   - Check for storms or adverse weather

4. Analyze maritime safety conditions
   - Evaluate wave height and period (vessel stability)
   - Check wind speed and direction (sail trim, motor power needed)
   - Review ocean currents (navigation, fuel consumption)
   - Assess tides for harbor entry/exit depth clearance
   - Check visibility (navigation safety)
   - Identify weather hazards (storms, fog, lightning)

5. Determine vessel-appropriate safety rating
   - Small craft advisory conditions (< 7m vessels)
   - Recreational boating suitability
   - Experience level requirements
   - Optimal departure windows

6. Provide comprehensive maritime briefing
   - Go/No-go recommendation
   - Best departure and return times
   - Hazards to monitor
   - Safety equipment recommendations
   - Navigation considerations

## MCP Tools Required

### chuk-mcp-open-meteo

**Tool 1**: `geocode_location` (if location name is provided)
- **Parameters**:
  - `name` (string): Harbor, marina, or coastal location (e.g., "Newport Harbor", "San Diego Bay", "Key West")
  - `count` (int): Number of results (default: 5)
  - `language` (string): Language code (default: "en")
- **Returns**: Coordinates (latitude, longitude) for the location

**Tool 2**: `get_marine_forecast`
- **Parameters**:
  - `latitude` (float): Location latitude from geocoding
  - `longitude` (float): Location longitude from geocoding
  - `timezone` (string): Timezone (default: "auto")
  - `forecast_days` (int): Trip duration in days (default: 1, max: 16)
  - `hourly` (string): Comma-separated marine variables:
    - `wave_height` - Significant wave height (m) - primary safety metric
    - `wave_period` - Wave period (s) - affects vessel motion
    - `wave_direction` - Wave direction (degrees)
    - `swell_wave_height` - Swell component (m)
    - `wind_wave_height` - Wind-driven waves (m)
    - `ocean_current_velocity` - Current speed (m/s)
    - `ocean_current_direction` - Current direction (degrees)
    - `sea_level_height_msl` - Tide height (m) for harbor clearance
    - `sea_surface_temperature` - Water temperature (°C)

**Tool 3**: `get_weather_forecast`
- **Parameters**:
  - `latitude` (float): Location latitude
  - `longitude` (float): Location longitude
  - `timezone` (string): Timezone (default: "auto")
  - `forecast_days` (int): Same as marine forecast
  - `current_weather` (bool): Set to True
  - `hourly` (string): Weather variables:
    - `wind_speed_10m` - Wind speed (km/h) - critical for sailing
    - `wind_direction_10m` - Wind direction (degrees)
    - `visibility` - Visibility distance (m)
    - `precipitation` - Rain/precipitation (mm)
    - `cloud_cover` - Cloud coverage (%)
    - `temperature_2m` - Air temperature (°C)

**Tool 4**: `interpret_weather_code` (optional, for weather conditions)
- **Parameters**:
  - `code` (int): WMO weather code from current_weather
- **Returns**: Human-readable description and severity

## Example Usage

**Input**: "Is it safe to sail from Newport Harbor today?"

**Process**:
1. Geocode "Newport Harbor" → lat: 33.6064, lon: -117.9289
2. Call get_marine_forecast for wave, current, tide data
3. Call get_weather_forecast for wind, visibility, precipitation
4. Analyze all conditions against small craft advisory thresholds
5. Provide go/no-go recommendation with timing

**Output**:
```
Sailing & Boating Safety Brief - Newport Harbor (2025-11-23):

⚓ OVERALL ASSESSMENT: SAFE - Good Conditions for Recreational Sailing

🌊 Marine Conditions (Current - 10:00):
  Wave Height: 0.8m (calm - comfortable for all vessels)
  Wave Period: 8s (moderate - smooth motion)
  Swell: 0.6m from SW (gentle)
  Ocean Currents: 0.3 m/s NW (weak - minimal navigation impact)
  Sea Surface Temp: 18°C (wetsuit recommended if capsizing risk)

🌀 Wind Conditions:
  Wind Speed: 12 km/h (light breeze - ideal for sailing)
  Wind Direction: NW (offshore from coast)
  Gusts: 18 km/h (steady, no strong gusts)

🌅 Tide Information:
  Current Tide: Rising (0.4m above MSL)
  High Tide: 14:30 at +1.2m (safe harbor depth)
  Low Tide: 20:15 at -0.8m (check draft clearance for return)
  Recommendation: Safe departure now, return before low tide if draft > 1.5m

☁️ Weather Conditions:
  Conditions: Partly cloudy
  Visibility: 10+ km (excellent)
  Precipitation: None (0mm)
  Temperature: 19°C (comfortable, light jacket)

✅ SAFE FOR SAILING - Conditions Summary:
  ✅ Waves: Calm (< 1m)
  ✅ Wind: Light and steady (ideal sailing conditions)
  ✅ Visibility: Excellent (> 5km)
  ✅ Weather: No precipitation or storms
  ✅ Currents: Weak (easy navigation)
  ✅ Tides: Safe harbor clearance

⏰ Recommended Sailing Window:
  Best Time: 10:00-17:00
  - Light, steady winds (10-15 km/h)
  - Calm seas (0.6-1.0m waves)
  - Good visibility throughout
  - High tide at 14:30 (optimal harbor depth)

⚠️ Conditions to Monitor:
  - Wind expected to increase to 20 km/h by 18:00 (still safe)
  - Return before 20:15 low tide if draft > 1.5m
  - Sea breeze may shift to onshore (SW) afternoon

👥 Skill Level: Suitable for all experience levels
🚤 Vessel Types: All recreational vessels - sailboats, motorboats, kayaks

🛟 Safety Equipment Required:
  ✅ Life jackets (PFDs) for all aboard
  ✅ VHF radio (monitor weather updates)
  ✅ Visual distress signals
  ✅ Navigation lights (if returning after sunset ~17:30)
  ✅ Anchor and proper ground tackle

💡 Navigation Tips:
  - Offshore wind (NW) - stay aware of position relative to shore
  - Weak currents - minimal drift compensation needed
  - Excellent visibility - good for navigation
  - Check harbor depth chart against low tide time for return

Overall: EXCELLENT day for sailing - light winds, calm seas, clear conditions
```

## Expected Response Format

```
Sailing & Boating Safety Brief - [Location] ([Date]):

⚓ OVERALL ASSESSMENT: [SAFE/CAUTION/UNSAFE] - [Condition Summary]

🌊 Marine Conditions (Current - [TIME]):
  Wave Height: [HEIGHT]m ([description])
  Wave Period: [PERIOD]s ([description])
  Swell: [HEIGHT]m from [DIRECTION] ([assessment])
  Ocean Currents: [SPEED] m/s [DIRECTION] ([impact])
  Sea Surface Temp: [TEMP]°C ([recommendation])

🌀 Wind Conditions:
  Wind Speed: [SPEED] km/h ([description])
  Wind Direction: [DIRECTION] ([onshore/offshore])
  Gusts: [SPEED] km/h ([assessment])

🌅 Tide Information:
  Current Tide: [Rising/Falling] ([HEIGHT]m relative to MSL)
  High Tide: [TIME] at [HEIGHT]m
  Low Tide: [TIME] at [HEIGHT]m
  Recommendation: [Depth clearance guidance]

☁️ Weather Conditions:
  Conditions: [DESCRIPTION]
  Visibility: [DISTANCE] km ([rating])
  Precipitation: [AMOUNT]mm
  Temperature: [TEMP]°C ([comfort level])

[SAFE/CAUTION/UNSAFE] FOR SAILING - Conditions Summary:
  [✅/⚠️/❌] Waves: [Assessment]
  [✅/⚠️/❌] Wind: [Assessment]
  [✅/⚠️/❌] Visibility: [Assessment]
  [✅/⚠️/❌] Weather: [Assessment]
  [✅/⚠️/❌] Currents: [Assessment]
  [✅/⚠️/❌] Tides: [Assessment]

⏰ Recommended Sailing Window:
  Best Time: [TIME_RANGE]
  - [Condition notes]

⚠️ Conditions to Monitor:
  - [Hazard or changing condition]

👥 Skill Level: [Required experience]
🚤 Vessel Types: [Suitable vessel types]

🛟 Safety Equipment Required:
  [List required equipment]

💡 Navigation Tips:
  - [Specific navigation guidance]

Overall: [Summary assessment]
```

## Small Craft Advisory Thresholds

### Safe Conditions (All Vessels)
- **Wave Height**: < 1.5m
- **Wind Speed**: < 20 km/h
- **Visibility**: > 5 km
- **Ocean Currents**: < 1 m/s
- **Weather**: No thunderstorms, fog, or heavy precipitation

### Caution (Experienced Sailors, Larger Vessels)
- **Wave Height**: 1.5-2.5m
- **Wind Speed**: 20-33 km/h (small craft advisory threshold)
- **Visibility**: 2-5 km
- **Ocean Currents**: 1-2 m/s
- **Weather**: Light rain, moderate winds

### Unsafe (Small Craft Advisory - vessels < 7m)
- **Wave Height**: 2.5-4m
- **Wind Speed**: 33-47 km/h (gale warning threshold ~55 km/h)
- **Visibility**: < 2 km
- **Ocean Currents**: > 2 m/s (very strong)
- **Weather**: Thunderstorms, heavy rain, or fog

### Dangerous (All Vessels Stay in Harbor)
- **Wave Height**: > 4m
- **Wind Speed**: > 47 km/h (gale force)
- **Visibility**: < 1 km
- **Ocean Currents**: > 3 m/s
- **Weather**: Storms, lightning, severe weather warnings

## Wave Conditions Assessment

### Wave Height Impact by Vessel
- **< 0.5m**: Flat - ideal for all vessels including kayaks
- **0.5-1m**: Slight - comfortable for all recreational vessels
- **1-1.5m**: Moderate - may be choppy for small craft
- **1.5-2.5m**: Rough - challenging for vessels < 5m, experienced sailors
- **2.5-4m**: Very rough - large vessels only, small craft advisory
- **> 4m**: High seas - dangerous, stay in harbor

### Wave Period Consideration
- **< 5s**: Choppy, uncomfortable motion (wind waves)
- **5-8s**: Moderate motion, can be bumpy
- **8-12s**: Comfortable long-period swells
- **> 12s**: Very smooth, gentle rise and fall

## Wind Conditions for Sailing

### Beaufort Scale for Sailors
- **0-6 km/h**: Calm - motoring or drifting
- **6-11 km/h**: Light air - minimal sailing
- **12-19 km/h**: Light breeze - ideal sailing conditions
- **20-28 km/h**: Moderate breeze - good sailing, reef in gusts
- **29-38 km/h**: Fresh breeze - reefing recommended
- **39-49 km/h**: Strong breeze - experienced sailors, double-reefed
- **50-61 km/h**: Near gale - small craft advisory, harbor recommended
- **> 62 km/h**: Gale - dangerous, stay in harbor

### Wind Direction Considerations
- **Offshore wind** (blowing from land): Can push vessels away from safety
- **Onshore wind** (blowing toward land): Easier to return, but lee shore hazard
- **Cross-shore wind**: Variable sailing angles
- Always monitor wind forecasts - can change rapidly

## Ocean Current Impact

### Current Speed Effects
- **< 0.5 m/s**: Negligible navigation impact
- **0.5-1 m/s**: Noticeable drift, minor course correction needed
- **1-2 m/s**: Significant drift, substantial course correction, fuel consideration
- **2-3 m/s**: Strong currents, difficult navigation, high fuel consumption
- **> 3 m/s**: Very strong, dangerous for small vessels

### Navigation with Currents
- Account for set (direction) and drift (speed)
- Current with wind: faster passage, but harder return
- Current against wind: choppy seas, uncomfortable motion
- Harbor entrances: strong currents during tidal changes

## Tidal Considerations for Boating

### Harbor Entry/Exit Safety
- Check chart datum and vessel draft against tide height
- Low tide: Ensure adequate depth clearance (draft + 1m safety margin)
- High tide: Check bridge clearance for sailboat masts
- Tidal currents strongest at mid-tide (halfway between high/low)
- Slack water (weakest current) at high and low tide peaks

### Planning Around Tides
- Departure: Outgoing tide helps exit harbor
- Return: Incoming tide helps harbor entry
- Grounding risk highest at low tide in shallow areas
- Anchorage depth changes significantly with tides

## Visibility Requirements

### Minimum Safe Visibility
- **> 5 km**: Excellent - safe navigation
- **2-5 km**: Good - safe with proper navigation equipment
- **1-2 km**: Poor - experienced navigators only, radar recommended
- **< 1 km**: Fog - unsafe without radar/GPS, risk of collision

### Reduced Visibility Causes
- Fog (especially when warm air over cold water)
- Heavy rain or precipitation
- Spray from high seas
- Nighttime (requires navigation lights and proper equipment)

## Weather Hazards

### Thunderstorms
- Lightning strike risk (fatal on water)
- Sudden wind shifts and gusts
- Heavy rain reducing visibility
- **Action**: Monitor radar, seek harbor before storms arrive

### Fog
- Severely reduced visibility
- Risk of collision
- Disorientation
- **Action**: Use radar, GPS, sound signals; proceed slowly or wait

### Heavy Rain
- Reduced visibility
- Increased wave action
- Crew discomfort
- **Action**: Don appropriate foul weather gear, reduce speed

## Safety Equipment Checklist

### Required Equipment (All Vessels)
- ✅ Life jackets (USCG/approved PFDs) for every person
- ✅ Throwable flotation device
- ✅ Visual distress signals (flares, flag, light)
- ✅ Sound producing device (horn, whistle)
- ✅ Fire extinguisher (if engine/fuel aboard)
- ✅ Navigation lights (if operating sunset to sunrise)

### Recommended Equipment
- ✅ VHF marine radio (monitor Channel 16)
- ✅ GPS/chartplotter
- ✅ Compass
- ✅ Anchor and rode (appropriate for depth and vessel)
- ✅ First aid kit
- ✅ Bilge pump
- ✅ Tool kit and spare parts
- ✅ Foul weather gear
- ✅ Drinking water
- ✅ EPIRB or PLB (offshore sailing)

## Error Handling

- Location not coastal/marine: Inform that marine data requires ocean coordinates
- No marine data available: Some areas lack marine forecast coverage
- API error: Inform user and suggest retry
- Invalid coordinates: Request valid lat/lon over water

## Safety Notes

- **ALWAYS check official marine forecasts** before departure (NOAA, local coast guard)
- Weather can change rapidly at sea - monitor continuously
- Small craft advisories are serious warnings - respect them
- If in doubt, stay in harbor - the sea will be there tomorrow
- File a float plan with someone on shore
- Check NOTAM (Notices to Mariners) for hazards, restrictions
- Know your vessel's capabilities and your own skill limits
- Ensure communication equipment is working (VHF radio, cell phone)
- Check fuel - account for currents and potential headwinds on return
- Hypothermia risk even in moderate water temperatures
- Always wear a PFD (life jacket) - most boating deaths are drownings

## Notes

- Marine forecasts update every 3-6 hours - refresh before departure
- Offshore conditions often differ from nearshore
- Headlands and points can have rougher conditions
- Harbor entrances can be dangerous in certain wind/tide combinations
- Sea state can be worse than forecast if wind opposes current
- Afternoon sea breezes are common on coasts (onshore wind develops)
- Night sailing requires additional skills and equipment
- Moonless nights are very dark on water - navigation lights essential
- Cold water (< 15°C) requires immersion suit or wetsuit if capsizing risk exists
