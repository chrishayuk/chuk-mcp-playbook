# Playbook: Convert Time Across Multiple Timezones

## Description
This playbook retrieves the current time across multiple timezones simultaneously using a single NTP consensus query, ensuring all times are perfectly synchronized and consistent.

## Prerequisites
- Access to the chuk-mcp-time server
- List of IANA timezone names to query
- Internet connectivity to reach NTP servers

## Steps

1. Identify all required timezones
   - List IANA timezone names (e.g., "America/New_York", "Europe/London")
   - Prioritize timezones based on relevance

2. Choose accuracy mode
   - Fast mode for general use (4 NTP servers)
   - Accurate mode for precision requirements (7 NTP servers)

3. Query each timezone
   - Make parallel or sequential calls to get_time_for_timezone
   - All queries use the same underlying NTP consensus for consistency

4. Collect and organize results
   - Group times by region or purpose
   - Calculate offsets between timezones
   - Show relative time differences

5. Present formatted multi-timezone view

## MCP Tools Required

### chuk-mcp-time

**Tool 1**: `get_local_time` (Recommended - includes DST and offset info)
- **Parameters** (per timezone):
  - `timezone` (string, required): IANA timezone identifier
  - `mode` (string, optional): "fast" or "accurate"
  - `compensate_latency` (bool, optional): true (default)
- **Returns**: Local time with timezone metadata (offset, DST status, abbreviation)

**Tool 2**: `get_time_for_timezone` (Alternative - simpler response)
- **Parameters** (per timezone):
  - `timezone_name` (string, required): IANA timezone name
  - `mode` (string, optional): "fast" or "accurate"
  - `compensate_latency` (bool, optional): true (default)
- **Returns**: Local time and basic timezone info

**Tool 3**: `list_timezones` (Helper - find timezone IDs)
- **Parameters**:
  - `country_code` (string, optional): Filter by country
  - `search` (string, optional): Search for timezone by name
- **Returns**: List of valid IANA timezone identifiers

**Note**: Making multiple calls in quick succession uses the same NTP consensus, ensuring perfect synchronization across all timezones.

## Example Usage

**Input**: "What time is it in New York, London, Tokyo, and Sydney?"

**Process**:
1. Identify timezones:
   - America/New_York
   - Europe/London
   - Asia/Tokyo
   - Australia/Sydney
2. Call get_time_for_timezone for each
3. Format as multi-timezone display

**Output**:
```
Current Time Across Timezones:

🇺🇸 New York (America/New_York)
   Wed, Nov 27 2025, 8:23 PM EST
   UTC-05:00

🇬🇧 London (Europe/London)
   Thu, Nov 28 2025, 1:23 AM GMT
   UTC+00:00

🇯🇵 Tokyo (Asia/Tokyo)
   Thu, Nov 28 2025, 10:23 AM JST
   UTC+09:00

🇦🇺 Sydney (Australia/Sydney)
   Thu, Nov 28 2025, 12:23 PM AEDT
   UTC+11:00

Reference UTC: 2025-11-28T01:23:45.123456+00:00
Accuracy: ±12.5ms from 4 NTP sources
```

## Expected Response Format

```
Current Time Across Timezones:

[ICON] [CITY] ([TIMEZONE])
   [DAY], [DATE], [TIME] [TZ_ABBREV]
   [UTC_OFFSET]

[ICON] [CITY] ([TIMEZONE])
   [DAY], [DATE], [TIME] [TZ_ABBREV]
   [UTC_OFFSET]

...

Reference UTC: [UTC_TIME]
Accuracy: ±[ERROR]ms from [SOURCES] NTP sources
```

## Common Multi-Timezone Scenarios

### Global Business Hours
```
Americas:
- America/New_York (EST/EDT)
- America/Chicago (CST/CDT)
- America/Los_Angeles (PST/PDT)

Europe:
- Europe/London (GMT/BST)
- Europe/Paris (CET/CEST)
- Europe/Berlin (CET/CEST)

Asia/Pacific:
- Asia/Tokyo (JST)
- Asia/Singapore (SGT)
- Australia/Sydney (AEST/AEDT)
```

### Financial Markets
```
- America/New_York (NYSE, NASDAQ)
- Europe/London (LSE)
- Asia/Tokyo (TSE)
- Asia/Hong_Kong (HKEX)
- Asia/Shanghai (SSE)
```

### Tech Hubs
```
- America/Los_Angeles (Silicon Valley)
- America/New_York (NYC)
- Europe/London (London)
- Asia/Bangalore (India/Kolkata)
- Asia/Singapore (Singapore)
```

## Use Cases

### 1. Global Team Standup
```
"Show current time for all our office locations."
Query: New York, London, Bangalore, Singapore, Sydney
Present: Business hours status for each location
```

### 2. Meeting Scheduler
```
"When is 3 PM EST in other timezones?"
Get current time for all zones, calculate offset from desired time
Show: What time 3 PM EST equals in each timezone
```

### 3. Server Monitoring Dashboard
```
"Display current time for all datacenter locations."
Query: US-East, US-West, EU, Asia, Australia regions
Present: Local time for each datacenter with health status
```

### 4. Travel Planning
```
"I'm traveling from LA to Tokyo via London. What are the times?"
Query: America/Los_Angeles, Europe/London, Asia/Tokyo
Show: Current time at origin, layover, and destination
Calculate: Time differences and flight duration context
```

### 5. Release Coordination
```
"We're doing a global release at 00:00 UTC. What time is that everywhere?"
Get current time in all regions
Calculate: Countdown to release in each timezone
Show: Local time when release happens
```

## Advanced Formatting

### With Business Hours Context
```
🇺🇸 New York - 8:23 PM EST
   ⚫ Outside business hours (9 AM - 5 PM)

🇬🇧 London - 1:23 AM GMT
   ⚫ Outside business hours (9 AM - 6 PM)

🇯🇵 Tokyo - 10:23 AM JST
   🟢 Business hours (9 AM - 5 PM)

🇦🇺 Sydney - 12:23 PM AEDT
   🟢 Business hours (9 AM - 5 PM)
```

### With Time Until Business Hours
```
🇺🇸 San Francisco - 5:23 PM PST
   ⚫ After hours (10h 37m until business hours)

🇬🇧 London - 1:23 AM GMT
   ⚫ After hours (7h 37m until business hours)

🇯🇵 Tokyo - 10:23 AM JST
   🟢 Business hours (6h 37m remaining)
```

### With Relative Time Differences
```
If it's 3:00 PM in New York, it's:

New York    3:00 PM  (Baseline)
London      8:00 PM  (+5 hours)
Dubai       1:00 AM* (+10 hours)
Singapore   4:00 AM* (+13 hours)
Tokyo       5:00 AM* (+14 hours)
Sydney      7:00 AM* (+16 hours)

* Next day
```

## Timezone Groups

### By Region
```
Americas: America/New_York, America/Chicago, America/Denver, America/Los_Angeles
Europe: Europe/London, Europe/Paris, Europe/Berlin, Europe/Moscow
Asia: Asia/Dubai, Asia/Singapore, Asia/Tokyo, Asia/Shanghai
Pacific: Australia/Sydney, Pacific/Auckland
```

### By Offset from UTC
```
UTC-8: America/Los_Angeles
UTC-5: America/New_York
UTC+0: Europe/London
UTC+1: Europe/Paris
UTC+9: Asia/Tokyo
UTC+11: Australia/Sydney
```

## Notes

- All times from the same NTP query are perfectly synchronized
- Daylight saving time is handled automatically per timezone
- Use IANA timezone names, not abbreviations (EST, PST vary by location)
- Timezone abbreviations shown are for reference only
- Business hours detection requires additional logic
- Icons and formatting enhance readability
- Consider showing UTC as universal reference
- Offsets change during DST transitions
- Some regions don't observe DST (Arizona, Japan, Singapore)

## Performance Tips

- Query all timezones in parallel when possible
- Cache NTP consensus and convert to multiple timezones locally if making many queries
- Fast mode sufficient for most multi-timezone displays
- Use accurate mode for financial or legal applications

## Common Timezone Pitfalls

1. **Abbreviation Ambiguity**
   - CST = China Standard Time, Central Standard Time, or Cuba Standard Time
   - Use IANA names: Asia/Shanghai, America/Chicago, America/Havana

2. **Daylight Saving Time**
   - Not all regions observe DST
   - Transition dates vary by country
   - Some regions changed DST rules (Arizona, most of Saskatchewan)

3. **Historical Changes**
   - Timezone rules change over time
   - IANA database handles historical data
   - Use current timezone names even for historical dates

4. **Political Changes**
   - Timezone boundaries change with political decisions
   - Russia, Brazil, and others have made recent changes
   - Keep timezone database updated
