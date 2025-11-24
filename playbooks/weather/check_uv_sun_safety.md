# Playbook: Check UV Index & Sun Safety

## Description
This playbook retrieves UV index forecasts and provides sun safety recommendations for outdoor activities. UV radiation from the sun can cause skin damage, sunburn, and increase skin cancer risk. The UV index helps determine appropriate sun protection measures.

## Prerequisites
- Location name OR coordinates
- Access to the chuk-mcp-open-meteo server

## Steps

1. Obtain the location coordinates
   - Geocode location name to latitude/longitude if needed
   - Validate coordinates

2. Request UV index and weather data
   - Call air quality API to get UV index forecast
   - Call weather forecast API for cloud cover, temperature
   - Get hourly data for current day and upcoming days

3. Analyze UV exposure risk
   - Identify peak UV hours (typically 10 AM - 4 PM)
   - Check cloud cover (reduces but doesn't eliminate UV)
   - Determine UV index rating (low, moderate, high, very high, extreme)
   - Consider duration of outdoor exposure

4. Provide sun safety recommendations
   - SPF sunscreen level needed
   - Protective clothing requirements
   - Shade recommendations
   - Best/worst times for outdoor activities
   - Special considerations for children, fair skin

5. Create hourly UV forecast
   - Show UV index throughout the day
   - Highlight peak exposure times
   - Recommend outdoor activity timing
   - Provide protection measures by hour

## MCP Tools Required

### chuk-mcp-open-meteo

**Tool 1**: `geocode_location` (if location name is provided)
- **Parameters**:
  - `name` (string): Location name (e.g., "Miami", "Phoenix", "Brisbane")
  - `count` (int): Number of results (default: 5)
  - `language` (string): Language code (default: "en")
- **Returns**: Coordinates (latitude, longitude) for the location

**Tool 2**: `get_air_quality`
- **Parameters**:
  - `latitude` (float): Location latitude from geocoding
  - `longitude` (float): Location longitude from geocoding
  - `timezone` (string): Timezone (default: "auto")
  - `hourly` (string): Must include `uv_index`:
    - `uv_index` - UV radiation index (0-11+ scale) - **PRIMARY METRIC**

**Tool 3**: `get_weather_forecast` (supplementary for context)
- **Parameters**:
  - `latitude` (float): Location latitude
  - `longitude` (float): Location longitude
  - `timezone` (string): Timezone (default: "auto")
  - `forecast_days` (int): Number of days (default: 1)
  - `hourly` (string): Weather variables affecting UV exposure:
    - `cloud_cover` - Cloud coverage (%) - reduces UV but doesn't block it
    - `temperature_2m` - Air temperature (°C) - heat safety
    - `precipitation` - Rain (mm) - outdoor activity planning
  - `daily` (string): Daily planning variables:
    - `sunrise` - Sunrise time
    - `sunset` - Sunset time
    - `temperature_2m_max` - Daily high temperature

## Example Usage

**Input**: "Should I wear sunscreen in Seattle today?"

**Process**:
1. Geocode "Seattle" → lat: 47.6062, lon: -122.3321
2. Call get_air_quality to get UV index forecast
3. Call get_weather_forecast for cloud cover and temperature
4. Analyze UV index levels throughout day
5. Provide sunscreen recommendation and sun safety guidance

**Output**:
```
UV Index & Sun Safety Forecast - Seattle (2025-11-23):

☀️ OVERALL UV RISK: LOW to MODERATE - Sunscreen Recommended

📊 Hourly UV Index Forecast:

06:00-08:00: UV 0 (None - sunrise 07:29)
08:00-09:00: UV 0.5 (Low)
09:00-10:00: UV 1.2 (Low)
10:00-11:00: UV 1.8 (Low)
11:00-12:00: UV 2.3 (Low) ← Increasing
12:00-13:00: UV 2.5 (Low) ← Peak UV
13:00-14:00: UV 2.4 (Low)
14:00-15:00: UV 1.9 (Low)
15:00-16:00: UV 1.3 (Low)
16:00-17:00: UV 0.6 (Low)
17:00-18:00: UV 0 (None - sunset 16:34)

Peak UV Time: 12:00-13:00 (UV index 2.5)

☁️ Environmental Conditions:
  Cloud Cover: 65% (mostly cloudy - reduces UV by ~50%)
  Temperature: 12°C high (cool and comfortable)
  Conditions: Partly cloudy
  Note: Clouds reduce UV but don't eliminate it - protection still needed

🧴 Sun Protection Recommendations:

YES - Wear Sunscreen (SPF 15+ recommended)
- UV index 2.5 = Low risk, but protection still beneficial
- Apply 30 minutes before going outside
- Reapply every 2 hours if outdoors continuously

Additional Protection:
  ✅ Sunglasses with UV protection (protects eyes even on cloudy days)
  ✅ Hat optional (low UV, but good practice)
  ⚠️ Shade not critical (low UV levels)
  ⚠️ Long sleeves optional (for comfort/warmth more than sun protection)

👶 Special Considerations:
  - Children: Use SPF 30+ on exposed skin (children's skin more sensitive)
  - Fair skin: SPF 30+ recommended even with low UV
  - Sensitive skin: Use broad-spectrum sunscreen

⏰ Best Times for Outdoor Activities:
  All Day: UV levels are low throughout the day
  - Safe for extended outdoor activities without excessive sun concern
  - Focus more on staying warm (12°C) than sun protection

💡 Sun Safety Tips:
  ✅ Even cloudy days have UV radiation (65% cloud cover today)
  ✅ UV reflects off water, snow, sand - extra exposure near these
  ✅ Sunscreen takes 15-30 min to absorb - apply before going out
  ✅ Don't forget lips (SPF lip balm), ears, neck, hands
  ✅ UVA rays penetrate clouds - broad-spectrum sunscreen important

Overall: LOW UV day - minimal sun risk, but basic protection (SPF 15-30) still recommended
for extended outdoor exposure. Greater concern is staying warm at 12°C!
```

## Example Usage 2: High UV Location

**Input**: "What's the UV index in Phoenix today?"

**Output**:
```
UV Index & Sun Safety Forecast - Phoenix (2025-11-23):

☀️ OVERALL UV RISK: VERY HIGH to EXTREME - Maximum Protection Required

📊 Hourly UV Index Forecast:

06:00-08:00: UV 0 (None - sunrise 06:52)
08:00-09:00: UV 2.1 (Low)
09:00-10:00: UV 4.5 (Moderate) ← Sunscreen critical
10:00-11:00: UV 6.8 (High) ⚠️
11:00-12:00: UV 8.5 (Very High) ⚠️⚠️
12:00-13:00: UV 9.2 (Very High) ⚠️⚠️ ← Peak
13:00-14:00: UV 9.0 (Very High) ⚠️⚠️
14:00-15:00: UV 8.1 (Very High) ⚠️⚠️
15:00-16:00: UV 6.3 (High) ⚠️
16:00-17:00: UV 3.8 (Moderate)
17:00-18:00: UV 1.2 (Low)
18:00-19:00: UV 0 (None - sunset 17:23)

Peak UV Time: 12:00-14:00 (UV index 9+) - AVOID DIRECT SUN

☁️ Environmental Conditions:
  Cloud Cover: 10% (clear skies - no UV reduction)
  Temperature: 28°C high (hot - dehydration risk)
  Conditions: Sunny
  Altitude: 340m (higher altitude = slightly more UV)

🧴 Sun Protection Recommendations - MAXIMUM PROTECTION REQUIRED:

CRITICAL - Wear SPF 50+ Broad-Spectrum Sunscreen
- Apply generously 30 minutes before sun exposure
- Reapply every 2 hours (more often if sweating)
- Use water-resistant formula if swimming/sweating
- Apply 1 oz (shot glass full) for full body coverage

Essential Protection:
  ⚠️⚠️ Wide-brimmed hat (3+ inch brim) - REQUIRED
  ⚠️⚠️ UV-blocking sunglasses (99-100% UVA/UVB) - REQUIRED
  ⚠️⚠️ Seek shade 10 AM - 4 PM - STRONGLY RECOMMENDED
  ⚠️⚠️ Long sleeves, long pants (UV-protective clothing ideal) - RECOMMENDED
  ⚠️⚠️ Avoid direct sun during peak hours (12-2 PM) - CRITICAL

👶 Special Considerations:
  - Children: Keep in shade, full coverage clothing, SPF 50+, reapply hourly
  - Babies < 6 months: Keep out of direct sun entirely
  - Fair skin: Minimize sun exposure, maximum protection essential
  - Sensitive skin/medications: Consult doctor (some meds increase UV sensitivity)

⏰ Recommended Outdoor Activity Timing:

❌ AVOID: 10:00-16:00 (UV 6-9+ Very High/Extreme)
  - Peak danger hours for sun damage
  - If must be outside: full protection, frequent shade breaks

✅ SAFER: 06:00-09:00 or 17:00-19:00 (UV 0-4 Low/Moderate)
  - Early morning: UV rising but manageable with SPF 30+
  - Evening: UV declining, cooler temperatures
  - Still use sunscreen even during these hours

🌡️ Heat Safety (Combined with UV):
  - Temperature 28°C + full sun = heat stress risk
  - Drink water every 15-20 minutes outdoors
  - Watch for heat exhaustion symptoms (dizziness, nausea, headache)
  - Take breaks in air conditioning or shade

💡 Sun Safety Tips:
  ⚠️ UV damage is cumulative - today's exposure adds to lifetime risk
  ⚠️ Sunburn can occur in as little as 15 minutes at UV 9+
  ⚠️ No such thing as "healthy tan" - tanning = skin damage
  ⚠️ Reflective surfaces (water, sand, concrete) increase exposure by 25-50%
  ⚠️ UV penetrates light clothing - use UPF-rated fabrics or SPF underneath

⚕️ Skin Cancer Prevention:
  - Phoenix has high skin cancer rates due to intense year-round UV
  - Regular skin checks recommended
  - See dermatologist for suspicious moles/spots

Overall: EXTREME UV day - serious sun protection absolutely essential.
Avoid midday sun (10 AM-4 PM), use SPF 50+, wear protective clothing and hat.
This is NOT a day to be casual about sun safety!
```

## Expected Response Format

```
UV Index & Sun Safety Forecast - [Location] ([Date]):

☀️ OVERALL UV RISK: [LOW/MODERATE/HIGH/VERY HIGH/EXTREME] - [Protection Summary]

📊 Hourly UV Index Forecast:

[HH:00-HH:00]: UV [VALUE] ([Rating]) [Warning symbols if high]
[Continue for daylight hours...]

Peak UV Time: [TIME_RANGE] (UV index [VALUE])

☁️ Environmental Conditions:
  Cloud Cover: [PERCENT]% ([impact on UV])
  Temperature: [TEMP]°C ([comfort/heat safety])
  Conditions: [DESCRIPTION]
  [Additional factors]

🧴 Sun Protection Recommendations:

[SPF Level and Application Instructions]

[Protection Level]: Protection:
  [Protection items with priority indicators]

👶 Special Considerations:
  [Vulnerable group guidance]

⏰ Best Times for Outdoor Activities:
  [Time-based recommendations]

💡 Sun Safety Tips:
  [Specific tips for the conditions]

Overall: [Summary and key recommendations]
```

## UV Index Scale and Guidelines

### UV Index Ratings (WHO Standard)

**0-2: Low**
- Minimal sun protection needed for most people
- Sunglasses recommended on bright days
- SPF 15+ if outside > 1 hour
- Safe for extended outdoor activities

**3-5: Moderate**
- Protection required
- SPF 30+ sunscreen
- Hat and sunglasses
- Seek shade during midday (11 AM - 3 PM)
- T-shirt recommended for extended exposure

**6-7: High**
- Protection essential
- SPF 30-50 sunscreen, reapply every 2 hours
- Wide-brimmed hat mandatory
- UV-blocking sunglasses
- Seek shade 10 AM - 4 PM
- Protective clothing recommended

**8-10: Very High**
- Extra protection required
- SPF 50+ sunscreen, reapply hourly if sweating
- Wide-brimmed hat essential
- Sunglasses with UV protection
- Minimize sun exposure 10 AM - 4 PM
- Long sleeves, long pants or UV protective clothing
- Shade essential during peak hours

**11+: Extreme**
- Maximum protection critical
- SPF 50+ sunscreen, reapply every 1-2 hours
- Avoid sun exposure 10 AM - 4 PM if possible
- Full protective clothing required
- Wide-brimmed hat, UV sunglasses mandatory
- Stay in shade whenever possible
- Seek indoor activities during peak UV

## Sunscreen Guidelines

### SPF (Sun Protection Factor) Selection
- **SPF 15**: Blocks ~93% UVB (low to moderate UV)
- **SPF 30**: Blocks ~97% UVB (moderate to high UV) - MINIMUM recommended
- **SPF 50**: Blocks ~98% UVB (high to very high UV)
- **SPF 100**: Blocks ~99% UVB (extreme UV or very fair skin)

### Proper Sunscreen Application
- Apply 15-30 minutes before sun exposure
- Use 1 ounce (30ml / shot glass full) for full body
- Don't forget: ears, lips, feet, hands, neck, scalp (if thinning hair)
- Reapply every 2 hours (more often if swimming or sweating)
- Water-resistant ≠ waterproof - still reapply after swimming
- Broad-spectrum (protects against UVA and UVB)

### Sunscreen Expiration
- Check expiration date - expired sunscreen loses effectiveness
- Typically 2-3 years shelf life
- Discard if separated, changed color, or smells off

## Protective Clothing

### UPF (Ultraviolet Protection Factor) Ratings
- **UPF 15-24**: Good protection (blocks 93-96% UV)
- **UPF 25-39**: Very good protection (blocks 96-97.5% UV)
- **UPF 40-50+**: Excellent protection (blocks 97.5-98%+ UV)

### Clothing Sun Protection
- Dark colors block more UV than light colors
- Tightly woven fabrics better than loose weaves
- Dry clothing more protective than wet
- Long sleeves/pants cover more skin
- Wide-brimmed hat (3+ inch brim all around) protects face, ears, neck
- Ordinary t-shirt ≈ UPF 5-8 (not sufficient for high UV)

## UV and Cloud Cover

### How Clouds Affect UV
- **Clear sky (0-25% clouds)**: Full UV exposure
- **Partly cloudy (25-75%)**: 50-85% UV penetration
- **Overcast (75-100%)**: Still 30-50% UV penetration
- **Thick storm clouds**: Can block 80%+ UV

### Important Notes
- Never skip sunscreen on cloudy days
- UVA rays (aging/cancer) penetrate clouds easily
- Up to 80% of UV reaches skin on cloudy days
- Hazy days can have high UV (pollution doesn't block UV)

## Special UV Exposure Factors

### Altitude
- UV increases ~10-12% per 1,000m elevation gain
- Mountains have higher UV than sea level
- Ski resorts at high altitude = very high UV exposure

### Reflective Surfaces
- **Snow**: Reflects up to 80% UV (doubles exposure)
- **Sand**: Reflects up to 25% UV
- **Water**: Reflects up to 30% UV
- **Concrete/pavement**: Reflects 10-15% UV
- **Grass/soil**: Reflects 2-3% UV

### Latitude
- Closer to equator = higher UV year-round
- UV strongest at solar noon (when sun highest in sky)
- Summer has higher UV than winter (except near equator)

### Time of Year
- Summer solstice (late June) = highest UV in Northern Hemisphere
- Winter solstice (late December) = lowest UV in Northern Hemisphere
- UV highest when sun's angle is highest in sky

## Vulnerable Groups

### Children and Babies
- Children's skin more susceptible to UV damage
- Babies < 6 months: Keep out of direct sun, use shade/clothing (not sunscreen)
- Children 6 months+: SPF 50+ broad-spectrum, reapply often
- One bad sunburn in childhood doubles melanoma risk
- Establish sun safety habits early

### Fair Skin (Skin Types I-II)
- Burns easily, rarely tans
- Higher skin cancer risk
- Needs maximum protection at all UV levels
- SPF 50+ even in moderate UV
- Consider UV-protective clothing

### Medications Increasing UV Sensitivity
- Some antibiotics (doxycycline, tetracycline)
- Some acne medications (isotretinoin)
- Some blood pressure medications
- Some antidepressants
- Check medication labels for photosensitivity warnings

### History of Skin Cancer
- Extra vigilance required
- Maximum protection at all UV levels
- Regular dermatology check-ups
- Avoid sun during peak hours

## UV and Eye Safety

### UV Damage to Eyes
- UV exposure contributes to cataracts
- Can cause photokeratitis ("snow blindness")
- Increases risk of macular degeneration
- Damages cornea and conjunctiva

### Sunglasses Protection
- Look for "UV400" or "100% UVA/UVB protection"
- Wraparound style blocks side UV
- Larger lenses = better coverage
- Polarized reduces glare but doesn't affect UV protection
- Children need sunglasses too

## Vitamin D Balance

### UV and Vitamin D Production
- UVB rays needed for vitamin D synthesis in skin
- 10-30 minutes midday sun exposure 2-3x/week often sufficient
- Fair skin produces vitamin D faster than dark skin
- Sunscreen blocks vitamin D production

### Balancing UV Risk and Vitamin D
- Brief sun exposure (15 min) on arms/legs without sunscreen
- Dietary vitamin D (supplements, fortified foods)
- Don't sunbathe for vitamin D - risk outweighs benefit
- Consult doctor about vitamin D supplementation

## Multi-Day UV Forecast

### Planning Outdoor Activities
- Check UV forecast for event planning
- Schedule outdoor events early morning or late afternoon
- Provide shade structures for outdoor gatherings
- Inform participants to bring sun protection
- Consider rescheduling if extreme UV + high heat

### UV Patterns
- UV typically peaks 11 AM - 2 PM (solar noon ± 1 hour)
- UV lowest early morning and late afternoon
- Summer UV much higher than winter (at mid-latitudes)
- Spring UV can be surprisingly high (longer days)

## Error Handling

- Location not found: Ask for more specific location
- No UV data available: Some high-latitude areas have minimal UV in winter
- API error: Inform user and suggest retry
- Invalid coordinates: Request valid latitude/longitude

## Safety Notes

- UV damage is cumulative over lifetime - every exposure counts
- There is no safe UV tan - tanning = DNA damage
- Indoor tanning beds are NOT safer (emit mostly UVA, cause cancer)
- Window glass blocks UVB but not UVA (car/office still has UV exposure)
- UV strongest at high altitude, near equator, during summer
- Medications can increase photosensitivity - check with doctor/pharmacist
- Self-exams for skin cancer: Check moles for changes (ABCDEs)
- See dermatologist annually if high risk (fair skin, history, many moles)

## Notes

- UV index is global standard (developed by WHO)
- Forecast UV index - actual may vary with clouds/weather
- UV radiation invisible - can't feel it burning until damage done
- Cloudy ≠ safe from UV
- Shade reduces but doesn't eliminate UV exposure
- Water, snow, sand reflect UV - extra protection needed
- Most skin damage occurs before age 18 - protect children
- Skin cancer is highly preventable with sun protection
- Sunscreen complements but doesn't replace shade/clothing
- "Base tan" doesn't protect - it IS skin damage
