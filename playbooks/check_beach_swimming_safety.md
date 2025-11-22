# Playbook: Check Beach Swimming Safety

## Description
This playbook evaluates beach and ocean swimming conditions to determine if it's safe for recreational swimming. It combines wave height, ocean currents, water temperature, tides, weather, and air quality to provide comprehensive swimming safety guidance.

## Prerequisites
- Beach or coastal location name OR coordinates
- Access to the chuk-mcp-open-meteo server

## Steps

1. Obtain the beach location coordinates
   - Geocode beach or coastal location name if needed
   - Validate coordinates are coastal/ocean location

2. Request marine conditions data
   - Call marine forecast API with wave, current, and tide parameters
   - Get current conditions and hourly forecast
   - Focus on swimming safety metrics

3. Request weather and environmental data
   - Call weather forecast API for temperature, wind, UV index
   - Optionally call air quality API for beach air quality
   - Get current and upcoming hours

4. Analyze swimming safety conditions
   - Evaluate wave height (safe range < 1m for swimming)
   - Check ocean current velocity (dangerous if > 1 m/s)
   - Assess water temperature (hypothermia risk)
   - Review tidal currents (strongest at mid-tide)
   - Check weather conditions (lightning, storms)
   - Evaluate UV index for sun safety

5. Provide swimming safety recommendation
   - Safe/Caution/Unsafe rating
   - Specific hazards to avoid
   - Best times for swimming
   - Safety precautions and equipment
   - Beach conditions summary

## MCP Tools Required

### chuk-mcp-open-meteo

**Tool 1**: `geocode_location` (if location name is provided)
- **Parameters**:
  - `name` (string): Beach or coastal location (e.g., "Bondi Beach", "Venice Beach", "Miami Beach")
  - `count` (int): Number of results (default: 5)
  - `language` (string): Language code (default: "en")
- **Returns**: Coordinates (latitude, longitude) for the location

**Tool 2**: `get_marine_forecast`
- **Parameters**:
  - `latitude` (float): Beach latitude from geocoding
  - `longitude` (float): Beach longitude from geocoding
  - `timezone` (string): Timezone (default: "auto")
  - `forecast_days` (int): Forecast duration (default: 1)
  - `hourly` (string): Marine variables for swimming safety:
    - `wave_height` - Significant wave height (m) - PRIMARY SAFETY METRIC
    - `wave_period` - Wave period (s)
    - `ocean_current_velocity` - Current speed (m/s) - RIP CURRENT INDICATOR
    - `ocean_current_direction` - Current direction (degrees)
    - `sea_level_height_msl` - Tide height (m) - for tidal current assessment
    - `sea_surface_temperature` - Water temperature (°C) - HYPOTHERMIA RISK

**Tool 3**: `get_weather_forecast`
- **Parameters**:
  - `latitude` (float): Beach latitude
  - `longitude` (float): Beach longitude
  - `timezone` (string): Timezone (default: "auto")
  - `current_weather` (bool): Set to True
  - `hourly` (string): Weather variables:
    - `temperature_2m` - Air temperature (°C)
    - `wind_speed_10m` - Wind speed (affects waves)
    - `wind_direction_10m` - Wind direction
    - `precipitation` - Rain
    - `cloud_cover` - Sun exposure
    - `visibility` - Visibility (fog hazard)

**Tool 4**: `get_air_quality` (optional, for beach air quality)
- **Parameters**:
  - `latitude` (float): Beach latitude
  - `longitude` (float): Beach longitude
  - `hourly` (string): Air quality variables:
    - `uv_index` - UV radiation (sun safety)
    - `us_aqi` - Air quality index

**Tool 5**: `interpret_weather_code` (optional, for weather conditions)
- **Parameters**:
  - `code` (int): WMO weather code from current_weather
- **Returns**: Human-readable weather description and severity

## Example Usage

**Input**: "Is it safe to swim at Waikiki Beach today?"

**Process**:
1. Geocode "Waikiki Beach" → lat: 21.2793, lon: -157.8293
2. Call get_marine_forecast for waves, currents, water temp, tides
3. Call get_weather_forecast for air temp, wind, weather
4. Optionally get air quality for UV index
5. Analyze all conditions against swimming safety thresholds
6. Provide comprehensive safety recommendation

**Output**:
```
Beach Swimming Safety - Waikiki Beach (2025-11-23, 14:00):

🏊 OVERALL ASSESSMENT: SAFE - Excellent Swimming Conditions

🌊 Ocean Conditions:
  Wave Height: 0.6m (small, safe for swimming)
  Wave Period: 10s (gentle, long-period swells)
  Ocean Currents: 0.2 m/s E (weak, minimal rip current risk)
  Water Temperature: 24°C (comfortable, no wetsuit needed)

🌅 Tide Status:
  Current Tide: Falling (0.3m above MSL)
  High Tide: 11:30 at +0.5m (passed)
  Low Tide: 17:45 at -0.3m (approaching)
  Tidal Currents: Moderate (mid-tide phase - increasing current)

🌤️ Weather Conditions:
  Air Temperature: 27°C (warm and pleasant)
  Wind: 12 km/h NE (light trade winds)
  Conditions: Sunny
  Visibility: Excellent (> 10km)

☀️ Sun Safety:
  UV Index: 10 (Very High - sun protection essential)
  Cloud Cover: 20% (mostly sunny)

✅ SAFE FOR SWIMMING - All Conditions Favorable:
  ✅ Waves: Small and gentle (< 1m)
  ✅ Currents: Weak (< 0.5 m/s)
  ✅ Water Temp: Comfortable (24°C)
  ✅ Weather: Clear, no storms
  ✅ Visibility: Excellent

⏰ Best Swimming Times Today:
  Now - 16:00: Excellent conditions
  16:00-18:00: Good (low tide, possible stronger currents)

⚠️ Safety Reminders:
  🌊 Rip Current Safety: If caught, swim parallel to shore, don't panic
  ☀️ Sun Protection: Use SPF 50+ sunscreen, reapply every 2 hours (UV index 10)
  🏖️ Hydration: Drink water regularly in 27°C heat
  👀 Supervision: Never swim alone, stay within designated swimming areas
  🌊 Tidal Awareness: Currents increasing toward low tide (17:45)

👥 Suitable For:
  ✅ All skill levels (children, adults, elderly with supervision)
  ✅ Beginner swimmers (conditions are gentle)
  ✅ Families with children

🏊 Swimming Conditions Summary:
  Water Entry: Easy and safe
  Wave Action: Gentle rolling waves, good for body surfing
  Current Risk: Low (stay in designated areas)
  Underwater Visibility: Good (clear water)
  Beach Conditions: Sandy bottom, gradual depth

Overall: EXCELLENT swimming day - small waves, warm water, beautiful weather!
Don't forget strong sun protection (UV index very high).
```

## Expected Response Format

```
Beach Swimming Safety - [Location] ([Date], [Time]):

🏊 OVERALL ASSESSMENT: [SAFE/CAUTION/UNSAFE] - [Condition Summary]

🌊 Ocean Conditions:
  Wave Height: [HEIGHT]m ([description and safety assessment])
  Wave Period: [PERIOD]s ([description])
  Ocean Currents: [SPEED] m/s [DIRECTION] ([rip current risk])
  Water Temperature: [TEMP]°C ([comfort/safety assessment])

🌅 Tide Status:
  Current Tide: [Rising/Falling] ([HEIGHT]m relative to MSL)
  High Tide: [TIME] at [HEIGHT]m
  Low Tide: [TIME] at [HEIGHT]m
  Tidal Currents: [Strength assessment]

🌤️ Weather Conditions:
  Air Temperature: [TEMP]°C ([comfort level])
  Wind: [SPEED] km/h [DIRECTION] ([assessment])
  Conditions: [DESCRIPTION]
  Visibility: [DISTANCE] km

☀️ Sun Safety:
  UV Index: [VALUE] ([rating and recommendation])
  Cloud Cover: [PERCENT]%

[SAFE/CAUTION/UNSAFE] FOR SWIMMING - Conditions Summary:
  [✅/⚠️/❌] Waves: [Assessment]
  [✅/⚠️/❌] Currents: [Assessment]
  [✅/⚠️/❌] Water Temp: [Assessment]
  [✅/⚠️/❌] Weather: [Assessment]
  [✅/⚠️/❌] Visibility: [Assessment]

⏰ Best Swimming Times:
  [TIME_RANGE]: [Conditions]

⚠️ Safety Reminders:
  [Specific safety guidance based on conditions]

👥 Suitable For:
  [Skill levels and groups]

🏊 Swimming Conditions Summary:
  [Specific beach/water conditions]

Overall: [Summary assessment and key recommendations]
```

## Swimming Safety Thresholds

### Wave Height - PRIMARY SAFETY METRIC
- **< 0.5m**: Calm - safe for all swimmers including children
- **0.5-1m**: Small - safe for most swimmers, some body surfing
- **1-1.5m**: Moderate - challenging for weak swimmers, caution for children
- **1.5-2m**: Rough - experienced swimmers only, NOT safe for children
- **> 2m**: Dangerous - swimming NOT recommended, strong undertow risk

### Ocean Current Velocity - RIP CURRENT RISK
- **< 0.5 m/s**: Weak - minimal drift, safe for most swimmers
- **0.5-1 m/s**: Moderate - noticeable drift, stay alert, swim near lifeguards
- **1-2 m/s**: Strong - RIP CURRENT DANGER, experienced swimmers only
- **> 2 m/s**: Very Strong - UNSAFE, rip currents very dangerous, DO NOT SWIM

### Water Temperature - HYPOTHERMIA RISK
- **> 24°C**: Warm - comfortable swimming, no wetsuit needed
- **20-24°C**: Comfortable - pleasant for most, long swims safe
- **15-20°C**: Cool - wetsuit recommended for extended swimming
- **10-15°C**: Cold - wetsuit required, limit exposure time
- **< 10°C**: Very Cold - DANGEROUS, hypothermia risk within minutes

### Tidal Current Strength
- **High or Low Tide (slack water)**: Weakest currents, safest for swimming
- **Mid-Tide (between high and low)**: Strongest currents, highest rip current risk
- **Large Tidal Range**: Stronger currents, greater caution needed

## Rip Current Safety

### What is a Rip Current?
- Narrow, powerful channel of water flowing from shore to sea
- Can pull swimmers away from beach quickly
- Most common cause of beach rescues
- Not undertow - flows along surface

### How to Identify Rip Currents
- Darker water channel between breaking waves
- Fewer breaking waves in rip area
- Foam, seaweed, debris moving seaward
- Choppy, turbulent water surface

### If Caught in a Rip Current
1. **DON'T PANIC** - rips won't pull you underwater
2. **DON'T SWIM AGAINST IT** - you'll exhaust yourself
3. **SWIM PARALLEL** to shore until out of current
4. **THEN swim to shore** at an angle
5. **FLOAT/TREAD WATER** if too tired - rip will dissipate offshore
6. **SIGNAL FOR HELP** - wave arms, shout to lifeguards

### When Rip Currents are Strongest
- Mid-tide (halfway between high and low)
- After storms or with large swells
- Strong onshore winds
- Near structures (piers, jetties, groins)
- Gaps in sandbars or reefs

## Weather Hazards for Swimming

### Thunderstorms - MOST DANGEROUS
- **Lightning**: Can strike water and swimmers (often fatal)
- **Action**: Exit water immediately if thunder heard or lightning seen
- **Rule**: 30/30 rule - seek shelter if < 30 seconds between lightning/thunder, wait 30 min after last thunder

### Strong Winds
- **Onshore wind**: Creates larger waves, rougher conditions
- **Offshore wind**: Can push swimmers and floats away from shore (very dangerous)
- **Action**: Avoid swimming in winds > 25 km/h

### Fog
- **Low visibility**: Disorientation, difficulty finding shore
- **Boat traffic**: Swimmers not visible to boats
- **Action**: Stay close to shore, avoid swimming if visibility < 100m

### Heavy Rain
- **Runoff**: Pollution, bacteria from storm drains
- **Visibility**: Difficult to see hazards or other swimmers
- **Action**: Wait 24-72 hours after heavy rain before swimming (water quality)

## UV Index and Sun Safety

### UV Index Scale
- **0-2 (Low)**: Minimal protection needed
- **3-5 (Moderate)**: Wear sunscreen, hat
- **6-7 (High)**: Sunscreen SPF 30+, hat, sunglasses, seek shade
- **8-10 (Very High)**: SPF 50+, protective clothing, limit midday sun
- **11+ (Extreme)**: Maximum protection, avoid sun 10 AM - 4 PM

### Sun Safety for Swimming
- Apply waterproof sunscreen 15-30 min before swimming
- Reapply every 2 hours and after swimming
- Water reflects UV - increases exposure
- Cloudy days still have UV radiation
- Children especially vulnerable - use SPF 50+

## Water Temperature Guidelines

### Comfort and Safety by Temperature
- **> 26°C**: Very warm - extended swimming safe, dehydration risk
- **24-26°C**: Warm - ideal swimming temperature
- **21-24°C**: Comfortable - most people swim comfortably
- **18-21°C**: Cool - tolerable for active swimming, wetsuit for extended
- **15-18°C**: Cold - wetsuit recommended, limit time to 30-60 min
- **12-15°C**: Very Cold - wetsuit essential, 15-30 min max
- **< 12°C**: Dangerous - hypothermia risk, experienced cold-water swimmers only

### Hypothermia Warning Signs
- Shivering (mild hypothermia)
- Confusion, slurred speech
- Loss of coordination
- Drowsiness, exhaustion
- **Action**: Exit water immediately, warm gradually, seek medical help

## Tidal Considerations for Swimming

### Best Tides for Swimming
- **High Tide**: Deeper water at shore, easier entry, fewer exposed rocks
- **Low Tide**: More beach area, tide pools to explore, but may expose hazards
- **Slack Water**: Around high and low tide - weakest currents, safest swimming

### Tidal Hazards
- **Rising Tide**: Can cut off access to beach or isolated areas
- **Falling Tide**: Can expose swimmers to rocks, reefs, stronger currents
- **Spring Tides**: Larger tidal range (full/new moon) - stronger currents
- **Neap Tides**: Smaller range (quarter moon) - weaker currents

## Supervision and Safety Rules

### Never Swim Alone
- Always swim with a buddy
- Tell someone on shore your swimming plans
- Stay within sight of beach/lifeguards

### Swim Near Lifeguards
- Swim only in designated swimming areas
- Obey lifeguard warnings and flags
- Red flag = dangerous, DO NOT SWIM
- Yellow flag = caution
- Green flag = safe conditions

### Know Your Limits
- Don't overestimate your swimming ability
- Avoid alcohol before/during swimming
- Rest periodically
- Exit water if feeling tired or cold

### Children Safety
- Constant adult supervision required
- Young children should wear Coast Guard-approved flotation devices
- Keep within arm's reach in water
- Swimming lessons recommended for all children

## Error Handling

- Location not coastal: Inform user that swimming safety requires beach/ocean location
- No marine data available: Some areas lack marine forecast coverage
- API error: Inform user and suggest retry
- Invalid coordinates: Request valid beach/coastal location

## Safety Notes

- **ALWAYS check local beach warnings, flags, and lifeguard guidance**
- This playbook provides general guidance - local conditions vary
- Beaches with lifeguards are statistically much safer
- Check local water quality reports (bacteria, pollution)
- Marine life hazards vary by location (jellyfish, sharks, stingrays)
- Beach features create hazards: piers, jetties, rocks, reefs
- Never dive into unknown water - check depth first
- Respect ocean wildlife - don't touch or harass
- Rip currents kill more people than sharks, lightning, hurricanes combined
- Most drownings occur on unguarded beaches
- If in doubt, stay out - the ocean will be there tomorrow

## Notes

- Ocean conditions can change rapidly - check frequently
- Early morning often has calmest conditions
- Afternoon sea breezes typically increase wave action
- Weekends and holidays have more crowded beaches
- Some beaches have seasonal swimming restrictions
- Jellyfish, stingrays more common in certain seasons
- Water quality worse after heavy rain (24-72 hour wait recommended)
- Red tide or algae blooms can cause beach closures
- Respect posted beach closures - there for safety
- Consider swimming ability before entering challenging conditions
