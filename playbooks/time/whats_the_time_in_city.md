# Playbook: Get Current Time for a City

## Description
This playbook retrieves the current time for any city worldwide with high accuracy using NTP consensus, including timezone information and DST status.

## Prerequisites
- City name or location
- Access to the chuk-mcp-time server
- Internet connectivity to reach NTP servers

## Steps

1. Find the correct IANA timezone for the city
   - Use list_timezones to search by city name
   - Handle ambiguous city names (e.g., multiple "Portland" cities)
   - Verify the correct timezone identifier

2. Request current time for the timezone
   - Call get_local_time with the timezone identifier
   - Use fast mode for typical queries
   - Use accurate mode if high precision is needed

3. Parse the time response
   - Extract local datetime
   - Get UTC offset and timezone abbreviation
   - Check DST status
   - Note estimated error from NTP consensus

4. Format the response for the user
   - Show local time with day/date
   - Include timezone abbreviation
   - Indicate DST status
   - Provide UTC offset

5. Return the formatted time information

## MCP Tools Required

### chuk-mcp-time

**Tool 1**: `list_timezones` (for finding timezone)
- **Parameters**:
  - `search` (string, optional): City name to search for
  - `country_code` (string, optional): ISO 3166 country code filter
- **Returns**:
  - `timezones` (array): List of matching timezone entries with id, country_code, comment
  - `total_count` (int): Number of results found

**Tool 2**: `get_local_time` (for getting current time)
- **Parameters**:
  - `timezone` (string, required): IANA timezone identifier from step 1
  - `mode` (string, optional): "fast" (default) or "accurate"
  - `compensate_latency` (bool, optional): true (default)
- **Returns**:
  - `local_datetime` (string): Local time in ISO 8601 format
  - `timezone` (string): IANA timezone identifier
  - `utc_offset_seconds` (int): UTC offset in seconds
  - `is_dst` (bool): Whether DST is currently active
  - `abbreviation` (string): Timezone abbreviation (e.g., EST, GMT, JST)
  - `source_utc` (string): Source UTC time from NTP consensus
  - `tzdata_version` (string): IANA tzdata version used
  - `estimated_error_ms` (float): Accuracy of the time

## Example Usage

**Input**: "What time is it in London?"

**Process**:
1. Search for London's timezone:
   ```
   Tool: list_timezones(search="London")
   Returns: {id: "Europe/London", country_code: "GB"}
   ```

2. Get current time:
   ```
   Tool: get_local_time(timezone="Europe/London", mode="fast")
   Returns: {
     local_datetime: "2025-11-28T01:23:45.123456+00:00",
     utc_offset_seconds: 0,
     is_dst: false,
     abbreviation: "GMT"
   }
   ```

3. Format and present

**Output**:
```
Current Time in London:
Thursday, November 28, 2025 at 1:23 AM GMT

Details:
- Timezone: Europe/London
- UTC Offset: +00:00
- DST Active: No (currently GMT, not BST)
- Accuracy: ±12.5ms from NTP consensus
```

## Expected Response Format

```
Current Time in [City]:
[Day], [Date] at [Time] [TZ_ABBREV]

Details:
- Timezone: [IANA_TIMEZONE_ID]
- UTC Offset: [±HH:MM]
- DST Active: [Yes/No] ([additional context])
- Accuracy: ±[ERROR]ms from NTP consensus
```

## Error Handling

- City not found: Ask user for more specific location or try country search
- Multiple cities with same name: Present all options and ask user to clarify
- Timezone lookup fails: Suggest using coordinates or different spelling
- NTP query fails: Report error and suggest retry

## Notes

- Always use list_timezones to find the correct IANA timezone - don't hardcode mappings
- Many cities share the same timezone (e.g., New York, Boston, Philadelphia all use America/New_York)
- Don't use timezone abbreviations (EST, PST) as they are ambiguous - use IANA IDs
- The is_dst field definitively shows current DST status
- DST rules are handled automatically by the IANA tzdata
- Timezone abbreviations shown are for user readability only
- Some timezones have unusual offsets (e.g., India is UTC+05:30, Newfoundland is UTC-03:30)
- Fast mode provides ±10-50ms accuracy, which is sufficient for displaying current time
