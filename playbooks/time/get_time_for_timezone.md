# Playbook: Get Time for Specific Timezone

## Description
This playbook retrieves the current time for any timezone worldwide with high accuracy using NTP consensus, then converts it to the requested timezone.

## Prerequisites
- Access to the chuk-mcp-time server
- Valid IANA timezone name (e.g., "America/New_York", "Europe/London", "Asia/Tokyo")
- Internet connectivity to reach NTP servers

## Steps

1. Identify the target timezone
   - Use IANA timezone database names
   - Common examples: America/New_York, Europe/London, Asia/Tokyo, Australia/Sydney

2. Choose accuracy mode
   - Fast mode: Queries 4 NTP servers (~40-150ms)
   - Accurate mode: Queries 7 NTP servers (~100-300ms)

3. Request time for timezone
   - Call the time API with timezone name and mode
   - Optionally disable latency compensation if needed

4. Parse the timezone response
   - Extract local time in requested timezone
   - Get UTC time for reference
   - Check timezone offset
   - Review accuracy information

5. Return formatted time for the timezone

## MCP Tools Required

### chuk-mcp-time

**Tool 1**: `get_local_time` (Recommended - includes timezone metadata)
- **Parameters**:
  - `timezone` (string, required): IANA timezone identifier
    - Examples: "America/New_York", "Europe/London", "Asia/Tokyo"
  - `mode` (string, optional): "fast" (default) or "accurate"
  - `compensate_latency` (bool, optional): true (default) or false
- **Returns**:
  - `local_datetime` (string): Local time in ISO 8601 format with timezone
  - `timezone` (string): IANA timezone identifier
  - `utc_offset_seconds` (int): UTC offset in seconds
  - `is_dst` (bool): Whether daylight saving time is active
  - `abbreviation` (string): Timezone abbreviation (e.g., EST, BST)
  - `source_utc` (string): Source UTC time from consensus
  - `tzdata_version` (string): IANA tzdata version
  - `estimated_error_ms` (float): Estimated error from UTC consensus

**Tool 2**: `get_time_for_timezone` (Alternative - simpler response)
- **Parameters**:
  - `timezone_name` (string, required): IANA timezone name
  - `mode` (string, optional): "fast" (default) or "accurate"
  - `compensate_latency` (bool, optional): true (default) or false
- **Returns**:
  - All fields from `get_time_utc` plus:
  - `timezone` (string): The requested timezone name
  - `local_time` (string): ISO 8601 time in the requested timezone

**Tool 3**: `list_timezones` (Helper - for finding valid timezone names)
- **Parameters**:
  - `country_code` (string, optional): ISO 3166 country code (e.g., "US", "GB")
  - `search` (string, optional): Substring search filter (case-insensitive)
- **Returns**: List of valid IANA timezone identifiers with metadata

## Example Usage

**Input**: "What time is it in Tokyo right now?"

**Process**:
1. Identify timezone: "Asia/Tokyo"
2. Call get_local_time with fast mode
3. Parse and format the response

**Output (using get_local_time)**:
```
Current Time in Tokyo (Asia/Tokyo):
2025-11-28T10:23:45.123456+09:00

Timezone Information:
- Abbreviation: JST (Japan Standard Time)
- UTC Offset: +09:00 (+32400 seconds)
- DST Active: No
- IANA tzdata version: 2024b

UTC Reference:
2025-11-28T01:23:45.123456+00:00

Accuracy:
- Sources: 4/4 NTP servers
- Estimated Error: ±12.5ms
```

**Output (using get_time_for_timezone - simpler)**:
```
Current Time in Tokyo (Asia/Tokyo):
2025-11-28T10:23:45.123456+09:00

UTC Reference:
2025-11-28T01:23:45.123456+00:00

Accuracy:
- Sources: 4/4 NTP servers
- Estimated Error: ±12.5ms
```

## Expected Response Format

```
Current Time in [CITY] ([TIMEZONE]):
[LOCAL_TIME]

UTC Reference:
[UTC_TIME]

Accuracy:
- Sources: [USED]/[TOTAL] NTP servers
- Estimated Error: ±[ERROR]ms
- Timezone Offset: [OFFSET]
```

## Common Timezones

### Americas
- `America/New_York` - Eastern Time (ET)
- `America/Chicago` - Central Time (CT)
- `America/Denver` - Mountain Time (MT)
- `America/Los_Angeles` - Pacific Time (PT)
- `America/Toronto` - Eastern Time (Canada)
- `America/Sao_Paulo` - Brasília Time

### Europe
- `Europe/London` - Greenwich Mean Time (GMT) / British Summer Time (BST)
- `Europe/Paris` - Central European Time (CET)
- `Europe/Berlin` - Central European Time (CET)
- `Europe/Moscow` - Moscow Standard Time (MSK)
- `Europe/Istanbul` - Turkey Time (TRT)

### Asia/Pacific
- `Asia/Tokyo` - Japan Standard Time (JST)
- `Asia/Shanghai` - China Standard Time (CST)
- `Asia/Hong_Kong` - Hong Kong Time (HKT)
- `Asia/Singapore` - Singapore Time (SGT)
- `Asia/Dubai` - Gulf Standard Time (GST)
- `Australia/Sydney` - Australian Eastern Time (AET)
- `Pacific/Auckland` - New Zealand Time (NZST/NZDT)

## Error Handling

- Invalid timezone name: Provide common timezone examples
- No NTP servers available: Check internet connectivity
- High error margin: Suggest using accurate mode
- Daylight saving time: Timezone conversion handles this automatically

## Use Cases

### 1. Global Team Coordination
```
"What time is it in London and New York?"
Get times for multiple timezones to coordinate meetings.
```

### 2. Server Time Display
```
Display current time for different datacenter locations.
Use fast mode for real-time updates.
```

### 3. Scheduling Across Timezones
```
Convert a specific time to multiple timezones for global scheduling.
Use accurate mode for precision.
```

### 4. Travel Planning
```
"What time will it be in Paris when it's 3 PM here?"
Compare local time to destination timezone.
```

## Notes

- Timezone conversion accounts for daylight saving time automatically
- IANA timezone database is used for accuracy
- Offset shown in format like +09:00 or -05:00
- Some timezones have different names for DST periods
- All times are based on NTP consensus for accuracy
- Fast mode suitable for most applications
- Accurate mode recommended for time-critical operations

## Timezone Name Tips

- Use full IANA names, not abbreviations (use "America/New_York" not "EST")
- City-based names are more reliable than abbreviation-based
- Many cities have the same timezone (e.g., "Asia/Tokyo" = "Asia/Seoul")
- Some regions have multiple timezones (use specific city)
- Daylight saving rules are handled automatically
