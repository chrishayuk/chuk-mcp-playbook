# Playbook: Find Timezone Identifier for a City

## Description
This playbook finds the correct IANA timezone identifier for any city worldwide, including timezone abbreviation, UTC offset, and DST information.

## Prerequisites
- City name or location
- Access to the chuk-mcp-time server

## Steps

1. Search for the city's timezone
   - Use list_timezones with city name search
   - Handle ambiguous city names (multiple cities with same name)
   - Optionally filter by country code if known

2. Verify the correct timezone identifier
   - Check country code matches expected location
   - Review comment field for additional context
   - Confirm with example city if available

3. Get current timezone details
   - Call get_local_time to get current status
   - Retrieve UTC offset and abbreviation
   - Check if DST is currently active

4. Optionally get full timezone information
   - Call get_timezone_info for DST schedule
   - Determine if timezone observes DST
   - Get upcoming transition dates if applicable

5. Format and return timezone information
   - Show IANA timezone ID
   - Include current abbreviation and offset
   - Note DST observation policy
   - Provide context about the timezone

## MCP Tools Required

### chuk-mcp-time

**Tool 1**: `list_timezones` (for finding timezone)
- **Parameters**:
  - `search` (string, optional): City name to search for
  - `country_code` (string, optional): ISO 3166 country code filter
- **Returns**:
  - `timezones` (array): Matching timezone entries
    - `id` (string): IANA timezone identifier
    - `country_code` (string): ISO 3166 country code
    - `comment` (string): Additional information about timezone
    - `example_city` (string): Example city in this timezone
  - `total_count` (int): Number of matches found
  - `tzdata_version` (string): IANA tzdata version

**Tool 2**: `get_local_time` (for current details)
- **Parameters**:
  - `timezone` (string, required): IANA timezone identifier from Tool 1
  - `mode` (string, optional): "fast" (default)
- **Returns**:
  - `timezone` (string): IANA timezone identifier
  - `utc_offset_seconds` (int): Current UTC offset
  - `is_dst` (bool): Whether DST is currently active
  - `abbreviation` (string): Current timezone abbreviation

**Tool 3**: `get_timezone_info` (optional, for DST info)
- **Parameters**:
  - `timezone` (string, required): IANA timezone identifier
- **Returns**:
  - `current_abbreviation` (string): Current timezone abbreviation
  - `transitions` (array): DST transitions (empty if no DST)

## Example Usage

**Input**: "What timezone is Phoenix in?"

**Process**:
1. Search for Phoenix:
   ```
   Tool: list_timezones(search="Phoenix")
   Returns: {
     timezones: [
       {
         id: "America/Phoenix",
         country_code: "US",
         comment: "MST - Arizona (most areas)"
       }
     ]
   }
   ```

2. Get current details:
   ```
   Tool: get_local_time(timezone="America/Phoenix")
   Returns: {
     utc_offset_seconds: -25200,
     is_dst: false,
     abbreviation: "MST"
   }
   ```

3. Check DST policy:
   ```
   Tool: get_timezone_info(timezone="America/Phoenix")
   Returns: {
     transitions: []  // Empty - no DST
   }
   ```

**Output**:
```
Phoenix is in the America/Phoenix timezone.

Details:
- IANA Timezone ID: America/Phoenix
- Abbreviation: MST (Mountain Standard Time)
- UTC Offset: -07:00 (year-round)
- DST: Not observed
- Country: United States

Note: Phoenix does not observe Daylight Saving Time,
unlike most other US locations.
```

## Expected Response Format

```
[City] is in the [IANA_TIMEZONE_ID] timezone.

Details:
- IANA Timezone ID: [TIMEZONE_ID]
- Abbreviation: [ABBREV] ([Full Name])
- UTC Offset: [±HH:MM] ([year-round/winter/summer])
- DST: [Observed/Not observed]
- Country: [COUNTRY_NAME]

[Additional notes about the timezone if relevant]
```

## Error Handling

- City not found: Ask for more specific location, try country search, or suggest alternative spelling
- Multiple cities found: Present all options with countries and ask user to clarify
- Timezone lookup fails: Suggest using coordinates or IANA timezone ID directly
- Invalid search: Provide examples of valid city names

## Notes

- Always use list_timezones to find timezone - never hardcode city-to-timezone mappings
- IANA timezone IDs follow Area/Location format (e.g., America/New_York, Europe/London)
- Many cities share the same timezone (e.g., New York, Boston, Philadelphia all use America/New_York)
- Some cities may not have their own timezone ID (e.g., Mumbai uses Asia/Kolkata)
- Timezone abbreviations (EST, PST, etc.) are ambiguous - always use IANA IDs
- The search is case-insensitive and searches id, country_code, comment, and example_city fields
- Some timezones have unusual offsets (India UTC+05:30, Newfoundland UTC-03:30)
- Timezone IDs represent geographic regions, not just cities
- Historical timezone changes are tracked in IANA tzdata
- Political boundaries can affect timezone assignments
- Always verify country_code if disambiguating between cities with same name
