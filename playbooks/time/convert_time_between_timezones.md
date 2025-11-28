# Playbook: Convert Time Between Timezones

## Description
This playbook converts a specific datetime from one timezone to another using IANA timezone rules. Perfect for scheduling, converting meeting times, or understanding when an event in one timezone occurs in another timezone.

## Prerequisites
- Access to the chuk-mcp-time server
- Source datetime (ISO 8601 format, naive or timezone-aware)
- Source and target IANA timezone names
- Understanding that the conversion is independent of system clock

## Steps

1. Prepare the datetime string
   - Format as ISO 8601 (e.g., "2025-12-25T15:00:00")
   - Can be naive (will be interpreted in source timezone) or timezone-aware

2. Identify source and target timezones
   - Use valid IANA timezone identifiers
   - Examples: "America/New_York", "Europe/London", "Asia/Tokyo"
   - Use list_timezones if unsure of exact name

3. Request conversion
   - Call convert_time with datetime and both timezones
   - IANA tzdata handles all DST transitions automatically

4. Parse the conversion response
   - Extract converted datetime in target timezone
   - Review UTC offset changes
   - Check explanation for DST or special cases

5. Present the conversion result

## MCP Tools Required

### chuk-mcp-time

**Tool 1**: `convert_time` (Primary tool for timezone conversion)
- **Parameters**:
  - `datetime_str` (string, required): ISO 8601 datetime string
    - Naive (e.g., "2025-12-25T15:00:00") - interpreted in from_timezone
    - Can include timezone offset (e.g., "2025-12-25T15:00:00-05:00")
  - `from_timezone` (string, required): Source IANA timezone identifier
    - Examples: "America/New_York", "Europe/London"
  - `to_timezone` (string, required): Target IANA timezone identifier
    - Examples: "Asia/Tokyo", "Australia/Sydney"
- **Returns**:
  - `from_timezone` (string): Source IANA timezone
  - `from_datetime` (string): Source datetime in ISO 8601 format
  - `from_utc_offset_seconds` (int): Source UTC offset in seconds
  - `to_timezone` (string): Target IANA timezone
  - `to_datetime` (string): Target datetime in ISO 8601 format
  - `to_utc_offset_seconds` (int): Target UTC offset in seconds
  - `offset_difference_seconds` (int): Difference between offsets
  - `explanation` (string): Human-readable explanation of the conversion

**Tool 2**: `list_timezones` (Helper - for finding valid timezone names)
- **Parameters**:
  - `country_code` (string, optional): ISO 3166 country code filter
  - `search` (string, optional): Substring search filter
- **Returns**: List of valid IANA timezone identifiers

## Example Usage

### Example 1: Simple Timezone Conversion

**Input**: "What time is 3 PM EST on December 25th in Tokyo?"

**Process**:
1. Format datetime: "2025-12-25T15:00:00"
2. Source timezone: "America/New_York" (EST/EDT)
3. Target timezone: "Asia/Tokyo"
4. Call convert_time

**Output**:
```
Timezone Conversion:

From: December 25, 2025 at 3:00 PM EST
      America/New_York (UTC-05:00)
      2025-12-25T15:00:00-05:00

To:   December 26, 2025 at 5:00 AM JST
      Asia/Tokyo (UTC+09:00)
      2025-12-26T05:00:00+09:00

Time Difference: 14 hours ahead
Offset Difference: +50400 seconds (+14 hours)

Explanation: Converting from America/New_York (UTC-05:00) to Asia/Tokyo (UTC+09:00).
Tokyo is 14 hours ahead of New York during EST.
```

### Example 2: DST-Aware Conversion

**Input**: "Convert 2:30 AM on March 10, 2025 from New York to London (DST transition day in US)"

**Process**:
1. DateTime: "2025-03-10T02:30:00"
2. From: "America/New_York"
3. To: "Europe/London"
4. Call convert_time

**Output**:
```
Timezone Conversion:

From: March 10, 2025 at 2:30 AM EDT (INVALID - during DST transition!)
      America/New_York (UTC-04:00)
      2025-03-10T02:30:00-04:00

To:   March 10, 2025 at 6:30 AM GMT
      Europe/London (UTC+00:00)
      2025-03-10T06:30:00+00:00

⚠️  Note: March 10, 2025 at 2:30 AM doesn't exist in America/New_York
(clocks spring forward from 2:00 AM to 3:00 AM). The time was adjusted forward.

Explanation: During DST transition, 2:00 AM - 3:00 AM is skipped.
Your requested time was automatically adjusted to 3:30 AM EDT.
```

### Example 3: Meeting Scheduler

**Input**: "Our meeting is at 9:00 AM Pacific Time on Nov 15. What time is that in Singapore?"

**Process**:
1. DateTime: "2025-11-15T09:00:00"
2. From: "America/Los_Angeles"
3. To: "Asia/Singapore"
4. Call convert_time

**Output**:
```
Meeting Time Conversion:

Pacific Time:   November 15, 2025 at 9:00 AM PST
                America/Los_Angeles (UTC-08:00)
                2025-11-15T09:00:00-08:00

Singapore Time: November 16, 2025 at 1:00 AM SGT
                Asia/Singapore (UTC+08:00)
                2025-11-16T01:00:00+08:00

⚠️  Note: This is 1:00 AM the NEXT DAY in Singapore (16 hours ahead)

Explanation: Singapore is 16 hours ahead of Pacific Time.
The meeting starts after midnight Singapore time.
```

## Expected Response Format

```
Timezone Conversion:

From: [DATE] at [TIME] [TZ_ABBREV]
      [FROM_TIMEZONE] (UTC[OFFSET])
      [FROM_DATETIME]

To:   [DATE] at [TIME] [TZ_ABBREV]
      [TO_TIMEZONE] (UTC[OFFSET])
      [TO_DATETIME]

Time Difference: [HOURS] hours [ahead/behind]
Offset Difference: [SECONDS] seconds

[Explanation with any DST notes or special cases]
```

## Use Cases

### 1. Scheduling International Meetings
```
Question: "We want to meet at 2 PM London time on Friday. What time is that in New York?"
Conversion: Europe/London → America/New_York
Result: Helps coordinate meeting across timezones
```

### 2. Planning Travel Itineraries
```
Question: "My flight departs Tokyo at 6 PM local time. What time is that in my home timezone?"
Conversion: Asia/Tokyo → [Home timezone]
Result: Know when to expect arrival messages, coordinate pickups
```

### 3. Event Broadcasting
```
Question: "Product launch is 10 AM PT. When does it air in each region?"
Multiple conversions: America/Los_Angeles → Multiple target timezones
Result: Marketing can promote correct local times
```

### 4. Financial Markets
```
Question: "NYSE closes at 4 PM EST. When is that in Hong Kong time?"
Conversion: America/New_York → Asia/Hong_Kong
Result: Know market hours overlap
```

### 5. Historical Event Conversion
```
Question: "The moon landing was July 20, 1969 at 20:17 UTC. What time was that in Tokyo?"
Conversion: UTC → Asia/Tokyo (historical date)
Result: IANA tzdata handles historical timezone rules
```

## Error Handling

### Invalid Timezone Names
```
Error: Timezone "EST" not found
Solution: Use IANA names like "America/New_York", not abbreviations
Tool: list_timezones(search="New York") to find correct name
```

### Invalid Datetime Format
```
Error: Cannot parse datetime "12/25/2025 3PM"
Solution: Use ISO 8601 format: "2025-12-25T15:00:00"
```

### Ambiguous Times During DST
```
Warning: Time occurs twice due to DST "fall back"
Example: 1:30 AM on Nov 3, 2025 in America/New_York happens twice
Solution: IANA tzdata uses fold algorithm to disambiguate
```

### Non-Existent Times During DST
```
Warning: Time doesn't exist due to DST "spring forward"
Example: 2:30 AM on Mar 10, 2025 in America/New_York is skipped
Solution: Time is automatically adjusted forward (2:30 AM → 3:30 AM)
```

## Common Timezone Conversion Patterns

### US to Europe
```
America/New_York    → Europe/London    (+5 hours)
America/Chicago     → Europe/Paris     (+7 hours)
America/Los_Angeles → Europe/Berlin    (+9 hours)

Note: Offset varies by DST season
```

### US to Asia
```
America/New_York    → Asia/Tokyo       (+14 hours, next day)
America/Los_Angeles → Asia/Shanghai    (+16 hours, next day)
America/Chicago     → Asia/Singapore   (+14 hours, next day)
```

### Europe to Asia
```
Europe/London       → Asia/Tokyo       (+9 hours)
Europe/Paris        → Asia/Dubai       (+3 hours)
Europe/Berlin       → Asia/Hong_Kong   (+7 hours)
```

## DST Considerations

### Spring Forward (Clocks Advance)
```
US: 2nd Sunday in March (2:00 AM → 3:00 AM)
EU: Last Sunday in March (1:00 AM → 2:00 AM)

Effect: Times between old and new time don't exist
Example: 2:30 AM on transition day is invalid
```

### Fall Back (Clocks Retreat)
```
US: 1st Sunday in November (2:00 AM → 1:00 AM)
EU: Last Sunday in October (2:00 AM → 1:00 AM)

Effect: Times in that hour occur twice
Example: 1:30 AM happens twice (once before, once after transition)
```

### Regions Without DST
```
No DST: Asia/Tokyo, Asia/Shanghai, Asia/Singapore, most of Africa
Partial: Some US states (Arizona, Hawaii), parts of Australia

Effect: Offset to these regions changes during DST in other locations
```

## Notes

- IANA tzdata handles all historical timezone changes
- Political timezone changes are included in tzdata updates
- Conversions are independent of system clock (uses tzdata rules)
- Abbreviations (EST, PST) are ambiguous - always use IANA names
- Some timezones have changed offsets multiple times (e.g., Russia)
- tzdata version shown in response indicates rule version
- Future timezone rules can change - always use latest tzdata
- For far future dates, conversion assumes current timezone rules
- Historical conversions use rules from that era (very accurate)

## Advanced: Handling DST Edge Cases

### Detecting Invalid Times
```
When user provides time during spring-forward gap:
- Tool automatically adjusts time forward
- Explanation notes the adjustment
- Application should warn user about non-existent time
```

### Detecting Ambiguous Times
```
When user provides time during fall-back overlap:
- IANA fold algorithm determines which occurrence
- First occurrence chosen by default
- Consider asking user to specify if critical
```

### Planning Around DST Transitions
```
For recurring meetings:
- Check if meeting time falls during DST transition
- Consider scheduling 30 minutes after transition window
- Use get_timezone_info tool to see upcoming transitions
```

## Related Playbooks

- **get_time_for_timezone.md**: Get current time in a timezone
- **get_timezone_dst_info.md**: See DST transition schedule
- **list_available_timezones.md**: Find valid timezone identifiers
- **schedule_global_meeting.md**: Find meeting times across timezones
