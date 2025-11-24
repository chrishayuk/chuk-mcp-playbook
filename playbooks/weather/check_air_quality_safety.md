# Playbook: Check Air Quality & Outdoor Activity Safety

## Description
This playbook evaluates current and forecasted air quality conditions to determine if it's safe for outdoor activities like running, cycling, exercise, or general outdoor exposure. It combines air quality index (AQI), pollutant levels, and weather conditions to provide health-based recommendations.

## Prerequisites
- Location name OR coordinates
- Access to the chuk-mcp-open-meteo server

## Steps

1. Obtain the location coordinates
   - Geocode location name to latitude/longitude if needed
   - Validate coordinates

2. Request air quality data
   - Call the air quality API with comprehensive pollutant parameters
   - Request AQI (Air Quality Index) for both US and European standards
   - Get hourly data for current and upcoming hours

3. Request supplementary weather data
   - Call weather forecast for UV index, temperature, humidity
   - Get current conditions and hourly forecast
   - Weather affects both air quality and outdoor safety

4. Analyze air quality levels
   - Evaluate AQI rating (good, moderate, unhealthy, etc.)
   - Check specific pollutants (PM2.5, PM10, ozone, NO2, SO2)
   - Identify any hazardous pollutants exceeding safe thresholds
   - Consider UV index for sun exposure safety

5. Provide activity recommendations
   - Determine if outdoor activities are safe
   - Specify which groups should take precautions (sensitive, general public)
   - Recommend best time windows for outdoor activities
   - Suggest protective measures if needed

## MCP Tools Required

### chuk-mcp-open-meteo

**Tool 1**: `geocode_location` (if location name is provided)
- **Parameters**:
  - `name` (string): Location name (e.g., "Beijing", "Los Angeles", "Delhi")
  - `count` (int): Number of results (default: 5)
  - `language` (string): Language code (default: "en")
- **Returns**: Coordinates (latitude, longitude) for the location

**Tool 2**: `get_air_quality`
- **Parameters**:
  - `latitude` (float): Location latitude from geocoding
  - `longitude` (float): Location longitude from geocoding
  - `timezone` (string): Timezone (default: "auto")
  - `hourly` (string): Air quality variables (defaults to comprehensive set if omitted):
    - `pm10` - Particulate matter <10μm (µg/m³)
    - `pm2_5` - Particulate matter <2.5μm (µg/m³) - most health-critical
    - `carbon_monoxide` - CO concentration (µg/m³)
    - `nitrogen_dioxide` - NO2 concentration (µg/m³)
    - `sulphur_dioxide` - SO2 concentration (µg/m³)
    - `ozone` - O3 concentration (µg/m³)
    - `us_aqi` - US Air Quality Index (0-500 scale)
    - `european_aqi` - European Air Quality Index (0-100+ scale)
    - `dust` - Dust concentration (µg/m³)
    - `uv_index` - UV radiation index (0-11+)
  - `domains` (string): Model domain - "auto", "cams_global", "cams_europe"

**Tool 3**: `get_weather_forecast` (optional, for comprehensive outdoor safety)
- **Parameters**:
  - `latitude` (float): Location latitude
  - `longitude` (float): Location longitude
  - `timezone` (string): Timezone (default: "auto")
  - `current_weather` (bool): Set to True
  - `hourly` (string): Weather variables:
    - `temperature_2m` - Temperature for heat safety
    - `relative_humidity_2m` - Humidity levels
    - `precipitation` - Rain conditions
    - `wind_speed_10m` - Wind (affects pollutant dispersion)

## Example Usage

**Input**: "Is the air quality safe for running in Phoenix today?"

**Process**:
1. Geocode "Phoenix" → lat: 33.4484, lon: -112.0740
2. Call get_air_quality for pollutant and AQI data
3. Call get_weather_forecast for supplementary conditions
4. Analyze AQI levels and specific pollutants
5. Determine safety for vigorous outdoor activity

**Output**:
```
Air Quality & Outdoor Safety for Phoenix (2025-11-23, 14:00):

Air Quality Index: 65 (Moderate - US AQI)
Overall Assessment: SAFE with precautions for sensitive groups

Pollutant Levels:
  PM2.5: 18 µg/m³ (Moderate)
  PM10: 32 µg/m³ (Good)
  Ozone: 85 µg/m³ (Moderate)
  NO2: 22 µg/m³ (Good)

UV Index: 8 (Very High - sun protection required)

Recommendation: SAFE FOR RUNNING - Moderate Precautions
- General public: Safe for outdoor exercise
- Sensitive groups: Consider reducing prolonged/intense exertion
- Use sunscreen (UV index high)
- Stay hydrated (temperature: 28°C)

Best Time for Running:
- Early morning (6:00-9:00): AQI 45 (Good), cooler temps, lower UV
- Late evening (18:00-20:00): AQI 52 (Moderate), cooler, lower UV

Health Groups to Take Precautions:
- People with asthma or respiratory conditions
- Heart disease patients
- Children and elderly during intense activity
```

## Expected Response Format

```
Air Quality & Outdoor Safety for [Location] ([Date], [Time]):

Air Quality Index: [AQI] ([Rating] - [US/European])
Overall Assessment: [SAFE/CAUTION/UNSAFE] [description]

Pollutant Levels:
  PM2.5: [VALUE] µg/m³ ([Rating])
  PM10: [VALUE] µg/m³ ([Rating])
  Ozone: [VALUE] µg/m³ ([Rating])
  NO2: [VALUE] µg/m³ ([Rating])
  [Other pollutants if elevated]

UV Index: [VALUE] ([Rating])

Recommendation: [ACTIVITY_SAFETY] - [Precaution Level]
- General public: [guidance]
- Sensitive groups: [guidance]
- [Additional safety measures]

Best Time for [Activity]:
- [Time Window]: AQI [VALUE] ([rating]), [conditions]
- [Time Window]: AQI [VALUE] ([rating]), [conditions]

Health Groups to Take Precautions:
- [List vulnerable groups]
```

## Air Quality Index (AQI) Guidelines

### US AQI Scale (0-500)
- **0-50 (Good)**: Air quality is satisfactory, safe for all outdoor activities
- **51-100 (Moderate)**: Acceptable; unusually sensitive people should consider reducing prolonged outdoor exertion
- **101-150 (Unhealthy for Sensitive Groups)**: Sensitive groups (asthma, heart disease, children, elderly) should reduce prolonged outdoor exertion
- **151-200 (Unhealthy)**: Everyone may experience health effects; sensitive groups should avoid prolonged exertion
- **201-300 (Very Unhealthy)**: Health alert - everyone should avoid prolonged outdoor exertion
- **301-500 (Hazardous)**: Health emergency - everyone should avoid all outdoor exertion

### European AQI Scale (0-100+)
- **0-20 (Good)**: Safe for all
- **20-40 (Fair)**: Generally acceptable
- **40-60 (Moderate)**: Sensitive groups take precautions
- **60-80 (Poor)**: General public may experience effects
- **80-100 (Very Poor)**: Avoid outdoor activities
- **100+ (Extremely Poor)**: Health emergency

## Pollutant-Specific Thresholds

### PM2.5 (Fine Particulate Matter) - Most Important
- **0-12 µg/m³**: Good - safe for all
- **12-35 µg/m³**: Moderate - sensitive groups take care
- **35-55 µg/m³**: Unhealthy for sensitive groups
- **55-150 µg/m³**: Unhealthy - reduce outdoor activity
- **150+ µg/m³**: Very unhealthy - avoid outdoor activity
- **Health Impact**: Respiratory and cardiovascular issues, penetrates deep into lungs

### PM10 (Coarse Particulate Matter)
- **0-50 µg/m³**: Good
- **50-150 µg/m³**: Moderate
- **150+ µg/m³**: Unhealthy
- **Health Impact**: Respiratory irritation, exacerbates asthma

### Ozone (O3) - Worse in Hot Weather
- **0-100 µg/m³**: Good
- **100-160 µg/m³**: Moderate
- **160-240 µg/m³**: Unhealthy for sensitive groups
- **240+ µg/m³**: Unhealthy
- **Health Impact**: Lung irritation, breathing difficulty, worsens with heat and exercise

### Nitrogen Dioxide (NO2) - Traffic Pollution
- **0-100 µg/m³**: Good
- **100-200 µg/m³**: Moderate
- **200+ µg/m³**: Unhealthy
- **Health Impact**: Respiratory inflammation, reduced immunity

## Activity-Specific Recommendations

### Running/Cycling (Vigorous Exercise)
- **AQI 0-50**: Safe for all intensities
- **AQI 51-100**: Safe for most; sensitive groups reduce intensity
- **AQI 101-150**: Reduce duration and intensity; sensitive groups avoid
- **AQI 151+**: Postpone outdoor exercise

### Walking/Light Exercise
- **AQI 0-100**: Safe for all
- **AQI 101-150**: Safe for most; sensitive groups reduce duration
- **AQI 151-200**: Reduce time outdoors; sensitive groups stay inside
- **AQI 201+**: Avoid outdoor activity

### Children Playing Outdoors
- **AQI 0-100**: Safe
- **AQI 101-150**: Reduce prolonged or intense play
- **AQI 151+**: Keep children indoors

## Sensitive Groups

### Who is Considered Sensitive?
- People with asthma or chronic obstructive pulmonary disease (COPD)
- People with heart disease
- Children (developing lungs)
- Older adults (65+)
- Pregnant women
- People with diabetes

## Protective Measures

### When AQI is Moderate (51-100)
- Sensitive groups: Reduce prolonged or intense outdoor activities
- Monitor symptoms (coughing, shortness of breath)
- Consider indoor alternatives for exercise

### When AQI is Unhealthy for Sensitive Groups (101-150)
- Sensitive groups: Avoid prolonged outdoor exertion
- General public: Reduce prolonged intense activities
- Keep rescue inhalers accessible (asthma patients)
- Consider N95 masks for sensitive individuals

### When AQI is Unhealthy (151+)
- Everyone: Avoid prolonged outdoor exertion
- Keep windows closed, use air purifiers indoors
- Wear N95 masks if outdoor activity is unavoidable
- Reschedule outdoor activities

## UV Index Guidance (from Air Quality Data)

- **0-2 (Low)**: No protection needed
- **3-5 (Moderate)**: Wear sunscreen, hat
- **6-7 (High)**: Sunscreen, hat, seek shade midday
- **8-10 (Very High)**: Extra protection required
- **11+ (Extreme)**: Avoid sun exposure 10 AM - 4 PM

## Error Handling

- Location not found: Ask for more specific location
- No air quality data: Some remote areas may lack coverage
- API error: Inform user and suggest retry
- Invalid data: Report which metrics are unavailable

## Safety Notes

- Air quality can change rapidly due to wildfires, industrial events, or weather
- Check air quality before outdoor activities, especially during summer and wildfire season
- Indoor air quality is typically better than outdoor when AQI > 100
- Wind can disperse pollutants (improving AQI) or bring them from other areas
- Early morning typically has better air quality than afternoon
- Ozone levels peak in afternoon heat
- Rain can clear pollutants, improving air quality

## Notes

- Air quality data updates hourly
- Forecasts are available up to several days in advance
- Local variations exist - AQI can differ significantly within a city
- Pollen data is not included in this API (separate consideration for allergies)
- Sensitive individuals should monitor symptoms regardless of AQI
- Consider both AQI and UV index for comprehensive outdoor safety
