# Playbook: List Available Timezones

## Description
This playbook helps you discover valid IANA timezone identifiers, prevent timezone hallucination errors, and find the correct timezone name for any location worldwide.

## Prerequisites
- Access to the chuk-mcp-time server
- Optional: Country code (ISO 3166) for filtering
- Optional: Search term for finding specific timezones

## Steps

1. Determine search criteria
   - Country-based search (e.g., all US timezones)
   - Name-based search (e.g., find "New York")
   - List all timezones (no filters)

2. Call list_timezones with appropriate filters
   - Use country_code for country-specific results
   - Use search for substring matching
   - Combine filters if needed

3. Parse the timezone list
   - Extract IANA timezone IDs
   - Review country codes
   - Check comments for disambiguation
   - Note example cities

4. Present formatted list to user

## MCP Tools Required

### chuk-mcp-time

**Tool**: `list_timezones`
- **Parameters**:
  - `country_code` (string, optional): ISO 3166 country code filter
    - Examples: "US", "GB", "FR", "CA", "AU", "JP"
    - Returns only timezones for that country
  - `search` (string, optional): Substring search filter (case-insensitive)
    - Searches in timezone ID, country code, comment, and example city
    - Examples: "New York", "London", "Pacific", "GMT"
- **Returns**:
  - `timezones` (array): List of timezone information entries
    - `id` (string): IANA timezone identifier (e.g., "America/New_York")
    - `country_code` (string, optional): ISO 3166 country code
    - `comment` (string, optional): Additional information
    - `example_city` (string, optional): Example city in this timezone
  - `total_count` (int): Number of timezones returned
  - `tzdata_version` (string): IANA tzdata database version

## Example Usage

### Example 1: Find US Timezones

**Input**: "What are all the timezones in the United States?"

**Process**:
1. Call list_timezones with country_code="US"
2. Parse and format results

**Output**:
```
US Timezones (Total: 24):

America/New_York
  Country: US
  Region: Eastern Time (most areas)
  Example: New York City

America/Chicago
  Country: US
  Region: Central Time (most areas)
  Example: Chicago

America/Denver
  Country: US
  Region: Mountain Time (most areas)
  Example: Denver

America/Los_Angeles
  Country: US
  Region: Pacific Time
  Example: Los Angeles

America/Anchorage
  Country: US
  Region: Alaska Time
  Example: Anchorage

America/Phoenix
  Country: US
  Region: Mountain Standard Time - Arizona (no DST)
  Example: Phoenix

Pacific/Honolulu
  Country: US
  Region: Hawaii Standard Time
  Example: Honolulu

... (and 17 more)

IANA tzdata version: 2024b
```

### Example 2: Search for Specific City

**Input**: "What's the timezone identifier for Tokyo?"

**Process**:
1. Call list_timezones with search="Tokyo"
2. Return matching results

**Output**:
```
Search Results for "Tokyo" (1 match):

Asia/Tokyo
  Country: JP
  Region: Japan Standard Time
  Example: Tokyo

This is the correct IANA timezone ID for Tokyo, Japan.

IANA tzdata version: 2024b
```

### Example 3: Find All London Timezones

**Input**: "Show me timezone options for London"

**Process**:
1. Call list_timezones with search="London"
2. Display all matches

**Output**:
```
Search Results for "London" (1 match):

Europe/London
  Country: GB
  Region: British Time (GMT/BST)
  Example: London

Note: This timezone uses GMT in winter and BST (British Summer Time) in summer.

IANA tzdata version: 2024b
```

### Example 4: List All Canadian Timezones

**Input**: "What timezones does Canada have?"

**Process**:
1. Call list_timezones with country_code="CA"
2. Format results by region

**Output**:
```
Canadian Timezones (Total: 23):

By Region:

Newfoundland Time:
  America/St_Johns (UTC-03:30, observes DST)

Atlantic Time:
  America/Halifax
  America/Glace_Bay
  America/Moncton
  America/Goose_Bay

Eastern Time:
  America/Toronto
  America/Nipigon
  America/Thunder_Bay
  America/Iqaluit
  America/Pangnirtung

Central Time:
  America/Winnipeg
  America/Rainy_River
  America/Rankin_Inlet

Mountain Time:
  America/Edmonton
  America/Cambridge_Bay
  America/Yellowknife
  America/Inuvik

Pacific Time:
  America/Vancouver
  America/Dawson_Creek
  America/Fort_Nelson
  America/Whitehorse
  America/Dawson

Note: Some regions do not observe Daylight Saving Time.

IANA tzdata version: 2024b
```

### Example 5: Discover Pacific Timezones

**Input**: "Show me all Pacific Ocean timezones"

**Process**:
1. Call list_timezones with search="Pacific"
2. Group by region

**Output**:
```
Pacific Timezones (Total: 45+):

North America:
  America/Los_Angeles (Pacific Time - US West Coast)
  America/Vancouver (Pacific Time - Canada)

Pacific Islands:
  Pacific/Auckland (New Zealand)
  Pacific/Fiji (Fiji)
  Pacific/Honolulu (Hawaii)
  Pacific/Tahiti (French Polynesia)
  Pacific/Guam (Guam)
  Pacific/Samoa (American Samoa)
  Pacific/Tongatapu (Tonga)
  Pacific/Port_Moresby (Papua New Guinea)
  ... (and many more)

Use country code for specific Pacific nations:
- NZ (New Zealand): Pacific/Auckland, Pacific/Chatham
- FJ (Fiji): Pacific/Fiji
- TO (Tonga): Pacific/Tongatapu

IANA tzdata version: 2024b
```

## Expected Response Format

```
[Search Description] ([Total Count] matches):

[TIMEZONE_ID_1]
  Country: [COUNTRY_CODE]
  Region: [COMMENT]
  Example: [EXAMPLE_CITY]

[TIMEZONE_ID_2]
  Country: [COUNTRY_CODE]
  Region: [COMMENT]
  Example: [EXAMPLE_CITY]

...

IANA tzdata version: [VERSION]
```

## Use Cases

### 1. Validating User Input
```
User says: "Set my timezone to EST"
Problem: "EST" is not a valid IANA timezone
Solution: list_timezones(search="Eastern") → Shows "America/New_York"
```

### 2. Building Timezone Picker UI
```
Need: Dropdown of all timezones for user selection
Solution: list_timezones() → Get all ~600 timezone IDs
Group by region for better UX
```

### 3. Discovering Regional Timezones
```
Question: "What timezone is Sydney in?"
Solution: list_timezones(search="Sydney") → "Australia/Sydney"
```

### 4. Finding Country-Specific Timezones
```
Question: "List all timezones for Australia"
Solution: list_timezones(country_code="AU") → 10+ Australian timezones
```

### 5. Preventing Hallucinated Timezones
```
LLM might hallucinate: "America/Boston" (doesn't exist)
Solution: list_timezones(search="Boston") → Shows "America/New_York"
Correct timezone: America/New_York (Boston is in Eastern Time)
```

## Common Timezone Lookups

### Major Cities
```
New York      → America/New_York
Los Angeles   → America/Los_Angeles
London        → Europe/London
Paris         → Europe/Paris
Berlin        → Europe/Berlin
Tokyo         → Asia/Tokyo
Shanghai      → Asia/Shanghai
Hong Kong     → Asia/Hong_Kong
Singapore     → Asia/Singapore
Dubai         → Asia/Dubai
Sydney        → Australia/Sydney
Mumbai        → Asia/Kolkata
São Paulo     → America/Sao_Paulo
Mexico City   → America/Mexico_City
Toronto       → America/Toronto
```

### Common Pitfalls
```
❌ "EST" → Not a timezone (abbreviation)
✅ "America/New_York" → Correct

❌ "PST" → Not a timezone (abbreviation)
✅ "America/Los_Angeles" → Correct

❌ "GMT" → Not a specific timezone
✅ "Europe/London" → Correct (uses GMT/BST)

❌ "America/Boston" → Doesn't exist
✅ "America/New_York" → Correct (Boston uses this)

❌ "Asia/Beijing" → Doesn't exist
✅ "Asia/Shanghai" → Correct (China Standard Time)
```

## Country Code Reference

Common ISO 3166-1 alpha-2 country codes:

```
US - United States     GB - United Kingdom
CA - Canada            FR - France
AU - Australia         DE - Germany
JP - Japan             IT - Italy
CN - China             ES - Spain
IN - India             BR - Brazil
MX - Mexico            RU - Russia
KR - South Korea       ZA - South Africa
SG - Singapore         NZ - New Zealand
AE - UAE               CH - Switzerland
```

## Filtering Strategies

### By Country
```
list_timezones(country_code="US")
→ Returns only US timezones
→ Useful for country-specific apps
```

### By City Name
```
list_timezones(search="Singapore")
→ Searches all fields for "Singapore"
→ Finds Asia/Singapore
```

### By Region
```
list_timezones(search="Pacific")
→ Returns all Pacific/* timezones
→ Also America/Los_Angeles (Pacific Time)
```

### Combined Search
```
list_timezones(country_code="AU", search="Sydney")
→ Australian timezones containing "Sydney"
→ Most specific search
```

## Error Handling

### No Results Found
```
Search: list_timezones(search="Atlantis")
Result: 0 matches
Action: Suggest broader search or nearby cities
```

### Ambiguous Search
```
Search: list_timezones(search="Central")
Result: Many matches (Central Time, Central America, Central Europe, etc.)
Action: Add country code or more specific search
```

### Invalid Country Code
```
Search: list_timezones(country_code="XX")
Result: 0 matches
Action: Provide valid ISO 3166 country code
```

## Notes

- IANA timezone database contains ~600 timezone IDs
- Many cities share the same timezone (e.g., NYC and Boston use America/New_York)
- Country codes follow ISO 3166-1 alpha-2 standard
- Some countries have dozens of timezones (Russia has 11, US has 24+)
- Search is case-insensitive
- Timezone IDs use Area/Location format (e.g., America/New_York)
- Comments often include additional regional information
- Example cities help users identify the correct timezone
- tzdata version indicates which timezone rules are in effect
- IANA updates tzdata multiple times per year for political changes

## Timezone Database Structure

IANA timezone IDs follow patterns:

```
Area/Location format:
  America/New_York    (continent/city)
  Europe/London       (continent/city)
  Asia/Tokyo          (continent/city)
  Pacific/Auckland    (ocean/island)

Some use Area/Region/Location:
  America/Argentina/Buenos_Aires
  America/Indiana/Indianapolis
  America/Kentucky/Louisville

Special zones:
  UTC                 (Coordinated Universal Time)
  Etc/GMT+5           (Fixed offset, note reversed sign!)
```

## Related Playbooks

- **get_time_for_timezone.md**: Get current time for a timezone
- **convert_time_between_timezones.md**: Convert between timezones
- **get_timezone_dst_info.md**: See DST schedule for a timezone
- **schedule_global_meeting.md**: Find meeting times across timezones
