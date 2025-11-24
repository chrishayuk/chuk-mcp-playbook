# Playbook: Check Fishing Conditions

## Description
This playbook evaluates fishing conditions by analyzing tides, ocean currents, water temperature, weather, and marine forecasts to determine optimal fishing times and locations. Fish feeding patterns are heavily influenced by tidal changes, water temperature, and weather conditions.

## Prerequisites
- Fishing location (coastal, bay, harbor) name OR coordinates
- Access to the chuk-mcp-open-meteo server

## Steps

1. Obtain the fishing location coordinates
   - Geocode fishing spot, harbor, or coastal location if needed
   - Validate coordinates are coastal/ocean location

2. Request marine forecast data
   - Call marine forecast API with tide, current, and water temperature
   - Get hourly data for fishing period (current day or multi-day)
   - Focus on tidal cycles and water conditions

3. Request weather forecast data
   - Call weather forecast API for wind, precipitation, pressure
   - Get current conditions and hourly forecast
   - Weather affects fish behavior and fishing comfort

4. Analyze fishing conditions
   - Identify tidal change periods (best feeding times)
   - Check water temperature (affects fish activity and species)
   - Evaluate ocean currents (baitfish movement)
   - Review barometric pressure (fish activity indicator)
   - Assess weather conditions (wind, rain, clouds)

5. Determine optimal fishing times
   - Peak fishing windows (tidal changes, dawn/dusk)
   - Species-appropriate conditions
   - Weather-related considerations
   - Safety conditions for boat fishing

6. Provide fishing forecast
   - Best fishing times today/upcoming days
   - Recommended techniques based on conditions
   - Target species suggestions based on conditions
   - Safety considerations
   - Gear recommendations

## MCP Tools Required

### chuk-mcp-open-meteo

**Tool 1**: `geocode_location` (if location name is provided)
- **Parameters**:
  - `name` (string): Fishing location (e.g., "Chesapeake Bay", "Montauk Point", "Florida Keys")
  - `count` (int): Number of results (default: 5)
  - `language` (string): Language code (default: "en")
- **Returns**: Coordinates (latitude, longitude) for the location

**Tool 2**: `get_marine_forecast`
- **Parameters**:
  - `latitude` (float): Fishing location latitude from geocoding
  - `longitude` (float): Longitude from geocoding
  - `timezone` (string): Timezone (default: "auto")
  - `forecast_days` (int): Fishing trip duration (default: 1, max: 16)
  - `hourly` (string): Marine variables for fishing conditions:
    - `sea_level_height_msl` - Tide height (m) - **CRITICAL FOR FISHING**
    - `ocean_current_velocity` - Current speed (m/s) - baitfish movement
    - `ocean_current_direction` - Current direction (degrees)
    - `sea_surface_temperature` - Water temp (°C) - **AFFECTS FISH ACTIVITY**
    - `wave_height` - Wave height (m) - boat fishing safety
    - `wave_period` - Wave period (s) - boat comfort

**Tool 3**: `get_weather_forecast`
- **Parameters**:
  - `latitude` (float): Fishing location latitude
  - `longitude` (float): Longitude
  - `timezone` (string): Timezone (default: "auto")
  - `forecast_days` (int): Same as marine forecast
  - `current_weather` (bool): Set to True
  - `daily` (string): Daily variables for multi-day planning:
    - `sunrise` - Sunrise time (prime fishing)
    - `sunset` - Sunset time (prime fishing)
  - `hourly` (string): Weather variables:
    - `temperature_2m` - Air temperature (°C) - comfort
    - `wind_speed_10m` - Wind speed (km/h) - casting, boat safety
    - `wind_direction_10m` - Wind direction - drift fishing
    - `precipitation` - Rain (mm)
    - `cloud_cover` - Cloud coverage (%) - fish activity
    - `pressure_msl` - Barometric pressure (hPa) - **FISH BEHAVIOR**

**Tool 4**: `interpret_weather_code` (optional, for weather conditions)
- **Parameters**:
  - `code` (int): WMO weather code from current_weather
- **Returns**: Human-readable weather description

## Example Usage

**Input**: "What are the fishing conditions in Galveston Bay today?"

**Process**:
1. Geocode "Galveston Bay" → lat: 29.4241, lon: -94.8480
2. Call get_marine_forecast for tides, currents, water temp
3. Call get_weather_forecast for wind, pressure, sunrise/sunset
4. Analyze tidal changes (best feeding = 1-2 hours before/after high/low tide)
5. Check barometric pressure trends (rising = less active, falling = more active)
6. Identify optimal fishing windows

**Output**:
```
Fishing Conditions Forecast - Galveston Bay (2025-11-23):

🎣 OVERALL ASSESSMENT: GOOD - Multiple Prime Fishing Windows

🌊 Marine Conditions:
  Water Temperature: 18°C (good for redfish, speckled trout)
  Ocean Currents: 0.4 m/s NE (moderate - baitfish active)
  Wave Height: 0.5m (calm - excellent for boat fishing)

🌅 Tidal Forecast (KEY FISHING TIMES):
  High Tide #1: 06:15 at +0.9m
  Low Tide #1: 12:30 at -0.6m
  High Tide #2: 18:45 at +1.0m
  Low Tide #2: 00:30 (tomorrow) at -0.7m

  Tidal Range: 1.5-1.7m (moderate tidal movement)

⭐ PRIME FISHING WINDOWS:
  1. 04:45-07:45 (2 hrs before → 1.5 hrs after high tide) - **BEST**
     - Rising tide bringing baitfish in
     - Dawn feeding period (sunrise 07:02)
     - Water temp: 18°C | Wind: 8 km/h NE | Pressure: 1015 hPa (stable)

  2. 11:00-14:00 (1.5 hrs before → 1.5 hrs after low tide) - **GOOD**
     - Outgoing tide concentrating fish
     - Moderate conditions
     - Water temp: 19°C | Wind: 12 km/h E | Pressure: 1014 hPa (falling slightly)

  3. 17:15-20:15 (1.5 hrs before → 1.5 hrs after high tide) - **EXCELLENT**
     - Incoming tide bringing fresh water
     - Dusk feeding period (sunset 17:48)
     - Water temp: 18°C | Wind: 10 km/h SE | Pressure: 1013 hPa (falling)

☁️ Weather Conditions:
  Conditions: Partly cloudy (60% cloud cover - good for fishing)
  Air Temperature: 16-20°C (comfortable)
  Wind: 8-14 km/h E to SE (light - excellent for casting)
  Precipitation: None (0mm)
  Barometric Pressure: 1015 → 1013 hPa (falling slowly - fish more active)

🐟 Target Species Recommendations:
  ✅ Redfish (18°C optimal temp, active on tidal changes)
  ✅ Speckled Trout (feeding during dawn/dusk, incoming tide)
  ✅ Flounder (outgoing tide, current-fed areas)
  ✅ Black Drum (cooler water, structure near channels)

🎯 Fishing Techniques by Window:
  Early Morning (04:45-07:45):
  - Live bait (shrimp, mullet) on incoming tide
  - Fish oyster reefs, grass flats as water rises
  - Topwater lures at dawn (trout feeding)

  Midday (11:00-14:00):
  - Outgoing tide - fish channel edges, drop-offs
  - Soft plastics or jigs in current
  - Target structure as bait washes out

  Evening (17:15-20:15):
  - Incoming tide - fish shallow flats, shorelines
  - Topwater or suspending baits at dusk
  - Redfish in shallows as tide floods

🛟 Safety & Comfort:
  ✅ Boat Conditions: Excellent (0.5m waves, light wind)
  ✅ Visibility: Good (no fog, partly cloudy)
  ✅ Temperature: Comfortable (16-20°C - light jacket)
  ⚠️ Sun Protection: Moderate (cloudy, but UV still present)

📋 Recommended Gear:
  - Light to medium tackle (calm conditions)
  - Live bait rig or soft plastics
  - Topwater plugs for dawn/dusk
  - Waders (if wade fishing - water 18°C)
  - Light rain jacket (backup, low precip chance)
  - Sun protection (hat, sunglasses, sunscreen)

💡 Pro Tips for Today:
  - Focus on tidal change periods - fish most active
  - Dawn and dusk windows are BEST (feeding times + tide changes)
  - Falling barometric pressure = more active feeding
  - Moderate cloud cover = fish less spooky, feed more
  - Light wind = easier casting, better boat control
  - Water temp 18°C = transitional - try multiple techniques

Overall: EXCELLENT fishing day - calm conditions, good tides, falling pressure.
Prime windows at dawn (04:45-07:45) and dusk (17:15-20:15). Tight lines!
```

## Expected Response Format

```
Fishing Conditions Forecast - [Location] ([Date]):

🎣 OVERALL ASSESSMENT: [EXCELLENT/GOOD/FAIR/POOR] - [Summary]

🌊 Marine Conditions:
  Water Temperature: [TEMP]°C ([species activity assessment])
  Ocean Currents: [SPEED] m/s [DIRECTION] ([baitfish/fishing impact])
  Wave Height: [HEIGHT]m ([boat fishing assessment])

🌅 Tidal Forecast (KEY FISHING TIMES):
  High Tide #1: [TIME] at [HEIGHT]m
  Low Tide #1: [TIME] at [HEIGHT]m
  High Tide #2: [TIME] at [HEIGHT]m
  Low Tide #2: [TIME] at [HEIGHT]m

  Tidal Range: [RANGE]m ([assessment])

⭐ PRIME FISHING WINDOWS:
  1. [TIME_RANGE] ([tidal phase]) - [RATING]
     - [Tidal conditions and reasoning]
     - [Environmental conditions]

  2. [TIME_RANGE] ([tidal phase]) - [RATING]
     - [Conditions]

  [Additional windows...]

☁️ Weather Conditions:
  Conditions: [DESCRIPTION]
  Air Temperature: [RANGE]°C ([comfort])
  Wind: [SPEED] km/h [DIRECTION] ([impact on fishing])
  Precipitation: [AMOUNT]mm
  Barometric Pressure: [PRESSURE] hPa ([trend and impact])

🐟 Target Species Recommendations:
  [Species based on water temp, season, conditions]

🎯 Fishing Techniques by Window:
  [Time-specific technique recommendations]

🛟 Safety & Comfort:
  [Conditions assessment]

📋 Recommended Gear:
  [Gear suggestions based on conditions]

💡 Pro Tips:
  [Specific tactical advice for the day]

Overall: [Summary and key recommendations]
```

## Tidal Fishing Principles

### Best Fishing Times Relative to Tides
- **1-2 hours BEFORE high tide**: Incoming water, baitfish moving in, **EXCELLENT**
- **1 hour AFTER high tide**: Peak water level, structure flooded, **GOOD**
- **1-2 hours BEFORE low tide**: Outgoing water, bait washing out, **EXCELLENT**
- **1 hour AFTER low tide**: Minimal water movement, **FAIR**
- **Mid-tide (rising or falling)**: Strongest currents, baitfish active, **GOOD to EXCELLENT**
- **Slack tide (high or low peak)**: Minimal current, less bait movement, **FAIR**

### Why Tides Matter for Fishing
- **Incoming tide**: Brings fresh water, oxygen, baitfish into feeding areas
- **Outgoing tide**: Concentrates baitfish in channels, washes food to waiting fish
- **Tidal currents**: Move baitfish, activate predatory feeding
- **Water level changes**: Access to different structure (flats, reefs, grass beds)

### Tidal Range Impact
- **Large tidal range (> 2m)**: Strong currents, dramatic water level changes, very active feeding
- **Moderate range (1-2m)**: Good current flow, predictable feeding windows
- **Small range (< 1m)**: Weak currents, less tidal influence on fishing

## Water Temperature Guidelines

### Temperature and Fish Activity
- **< 10°C**: Very cold - fish lethargic, slow metabolism, minimal feeding
- **10-15°C**: Cold - slow fishing, deep water, slow presentations
- **15-20°C**: Moderate - fish active, good feeding, wide species range
- **20-25°C**: Warm - excellent fishing, peak activity for many species
- **25-30°C**: Very warm - morning/evening feeding, deep water midday
- **> 30°C**: Hot - fish stressed, seek cooler deep water or shade

### Species by Water Temperature (General Guide)
- **Cold Water (10-15°C)**: Cod, halibut, steelhead, trout
- **Cool Water (15-20°C)**: Striped bass, redfish, flounder, black drum
- **Moderate (18-24°C)**: Speckled trout, snook, tarpon, most species active
- **Warm Water (24-28°C)**: Mahi-mahi, tuna, marlin, tropical species
- **Very Warm (> 28°C)**: Sailfish, wahoo, tropical reef fish

## Barometric Pressure and Fish Behavior

### Pressure Trends
- **Falling Pressure (< 1013 hPa, dropping)**: Fish feed actively before storm, **EXCELLENT**
- **Low Pressure (< 1009 hPa)**: Storm approaching or present, fish may stop feeding, **POOR**
- **Rising Pressure (after storm)**: Fish resume feeding as pressure stabilizes, **GOOD**
- **High Pressure (> 1020 hPa, stable)**: Fish less active, more selective, **FAIR**
- **Stable Pressure (1013-1016 hPa)**: Consistent fishing, normal patterns, **GOOD**

### Why Pressure Matters
- Fish sense pressure changes through swim bladders
- Falling pressure often triggers feeding frenzy (pre-storm stocking up)
- Rapidly rising pressure after storms can shut down feeding temporarily
- Stable pressure = predictable fish behavior

## Weather Conditions Impact

### Cloud Cover
- **Overcast (> 70%)**: Fish less spooky, feed more boldly, **EXCELLENT**
- **Partly Cloudy (30-70%)**: Good balance, comfortable fishing, **GOOD**
- **Clear Skies (< 30%)**: Fish more cautious, deeper water, early/late feeding, **FAIR**

### Wind
- **Calm (< 10 km/h)**: Easy casting, boat control, but fish may be cautious, **GOOD**
- **Light (10-20 km/h)**: Ripples on water, fish less spooky, good casting, **EXCELLENT**
- **Moderate (20-30 km/h)**: Challenging casting, rougher boat ride, **FAIR**
- **Strong (> 30 km/h)**: Difficult fishing, safety concerns, **POOR**

### Wind Direction (Shore Fishing)
- **Onshore wind**: Pushes baitfish toward shore, rougher surf, **GOOD** (if manageable)
- **Offshore wind**: Calm water, but baitfish pushed away, **FAIR**
- **Cross-shore wind**: Variable, drift fishing opportunities, **GOOD**

### Precipitation
- **Light Rain**: Fish often feed well, insects on water, low light, **GOOD to EXCELLENT**
- **Heavy Rain**: Reduced visibility, runoff, muddy water, **POOR**
- **After Rain**: Rising rivers/creeks bring food, fish active, **EXCELLENT**

## Dawn and Dusk - Prime Times

### Why Dawn/Dusk are Best
- Low light conditions - fish feed more boldly
- Baitfish more active during these periods
- Predatory fish take advantage of reduced visibility
- Temperature changes trigger feeding
- Combine with tidal change = **BEST FISHING**

### Dawn/Dusk Strategy
- Arrive early, fish through the period (not just exact sunrise/sunset)
- Topwater lures effective in low light
- Fish shallow water as predators move in
- If dawn/dusk coincides with tidal change = **PRIME TIME**

## Current and Drift Fishing

### Ocean Current Effects
- **Weak (< 0.5 m/s)**: Minimal baitfish movement, slow drift, **FAIR**
- **Moderate (0.5-1.5 m/s)**: Active baitfish, good feeding, manageable drift, **EXCELLENT**
- **Strong (> 1.5 m/s)**: Difficult boat control, very active fish but hard to target, **FAIR**

### Fishing the Current
- Current edges: Predators wait in slack water, ambush prey in current
- Upcurrent casting: Natural bait presentation
- Drift fishing: Cover more water, natural bait movement

## Multi-Day Fishing Forecast

### Planning Multi-Day Trips
- Analyze tide tables for best fishing days (multiple tidal changes during daylight)
- Check moon phase (full/new moon = stronger tides = better fishing)
- Avoid extreme weather (storms, very high winds)
- Target falling barometric pressure days
- Plan around dawn/dusk on peak tide days

### Moon Phase Impact
- **Full Moon**: Larger tidal range, night feeding (less daytime), **GOOD** tides, **FAIR** daytime
- **New Moon**: Larger tidal range, similar to full moon, **GOOD** tides
- **Quarter Moons**: Smaller tidal range, better daytime feeding, **FAIR** tides, **GOOD** daytime

## Species-Specific Conditions (Examples)

### Inshore Species
- **Redfish**: 15-25°C, shallow flats on incoming tide, oyster beds, grass
- **Speckled Trout**: 18-24°C, dawn/dusk, topwater, grass flats, channels
- **Flounder**: 15-22°C, outgoing tide, channel edges, ambush predators
- **Snook**: 22-28°C, warm water, structure, bridges, incoming tide

### Offshore Species
- **Tuna**: 18-24°C, current edges, offshore structure, dawn/dusk
- **Mahi-Mahi**: 24-28°C, warm water, floating debris, weed lines
- **Marlin**: 24-30°C, very warm, offshore, current edges

## Fishing Technique Recommendations

### Based on Tide
- **Incoming Tide**: Fish flats, shorelines, structure as water rises
- **Outgoing Tide**: Fish channels, drop-offs, points as bait washes out
- **High Slack**: Fish deep structure, slow presentations
- **Low Slack**: Fish remaining deep holes, channels

### Based on Conditions
- **Calm Water**: Topwater lures, sight fishing, finesse presentations
- **Choppy Water**: Subsurface lures, heavier weights, bold colors
- **Clear Water**: Natural colors, lighter line, finesse
- **Murky Water**: Bright colors, noise (rattles), scent

## Error Handling

- Location not coastal: Inform user that marine fishing forecast requires coastal/ocean location
- No marine data available: Some areas lack marine forecast coverage
- API error: Inform user and suggest retry
- Invalid coordinates: Request valid coastal/ocean coordinates

## Safety Notes

- Always check marine weather forecasts before fishing
- Small craft advisories apply to fishing boats
- Lightning is extremely dangerous on water - seek shelter immediately
- File a float plan if offshore fishing
- Carry required safety equipment (life jackets, flares, radio)
- Check local fishing regulations and licenses
- Be aware of tidal currents when wading
- Wear appropriate sun protection
- Stay hydrated, especially in warm weather
- Know the location of nearest boat ramp/harbor

## Notes

- Fishing is affected by many variables - no guarantee of success
- Local knowledge and experience are invaluable
- Different species have different optimal conditions
- Seasonal patterns affect fish location and behavior
- Structure (reefs, wrecks, grass beds) creates micro-environments
- Bait availability is crucial - match the hatch
- Water clarity affects lure selection and presentation
- Practice catch and release for conservation
- Respect size and bag limits
- Fish bite when they're hungry - conditions just improve odds!
