# Playbook: Get Timezone DST Information

## Description
This playbook retrieves detailed timezone information including current DST status, UTC offset, abbreviation, and upcoming DST transitions for the next 2 years. Essential for planning around DST changes and understanding timezone behavior.

## Prerequisites
- Access to the chuk-mcp-time server
- Valid IANA timezone identifier
- Internet connectivity to reach NTP servers

## Steps

1. Identify the timezone to query
   - Use valid IANA timezone name (e.g., "America/New_York")
   - Use list_timezones if unsure of exact name

2. Choose accuracy mode
   - Fast mode for quick queries
   - Accurate mode for precise current time

3. Request timezone information
   - Call get_timezone_info with timezone name
   - Optionally specify accuracy mode

4. Parse the response
   - Extract current offset and DST status
   - Review timezone abbreviation
   - Examine upcoming transitions (DST changes)
   - Note tzdata version

5. Present timezone details and transition schedule

## MCP Tools Required

### chuk-mcp-time

**Tool 1**: `get_timezone_info` (Primary tool for DST information)
- **Parameters**:
  - `timezone` (string, required): IANA timezone identifier
    - Examples: "America/New_York", "Europe/London", "Australia/Sydney"
  - `mode` (string, optional): "fast" (default) or "accurate"
    - Mode affects accuracy of current time, not transition data
- **Returns**:
  - `timezone` (string): IANA timezone identifier
  - `country_code` (string, optional): ISO 3166 country code
  - `comment` (string, optional): Additional timezone information
  - `current_offset_seconds` (int): Current UTC offset in seconds
  - `current_is_dst` (bool): Whether DST is currently active
  - `current_abbreviation` (string): Current timezone abbreviation
  - `transitions` (array): List of upcoming timezone transitions
    - `from_datetime` (string): Start of offset period (ISO 8601)
    - `utc_offset_seconds` (int): UTC offset during this period
    - `is_dst` (bool): Whether DST is active
    - `abbreviation` (string): Timezone abbreviation during this period
  - `tzdata_version` (string): IANA tzdata version

**Tool 2**: `get_local_time` (Helper - for current time in timezone)
- Gets current accurate time with DST status
- Useful for confirming current state

**Tool 3**: `list_timezones` (Helper - for finding timezone names)
- Use if unsure of exact IANA timezone identifier

## Example Usage

### Example 1: Check US Eastern Time DST Schedule

**Input**: "When does daylight saving time start and end in New York?"

**Process**:
1. Timezone: "America/New_York"
2. Call get_timezone_info(timezone="America/New_York", mode="fast")
3. Parse current status and transitions

**Output**:
```
Timezone Information: America/New_York

Current Status (as of Nov 28, 2025):
  Abbreviation: EST (Eastern Standard Time)
  UTC Offset: -05:00 (-18000 seconds)
  DST Active: No
  IANA tzdata version: 2024b

Upcoming DST Transitions (Next 2 Years):

1. March 9, 2025 at 2:00 AM EST → 3:00 AM EDT
   From: 2025-03-09T07:00:00+00:00 (2:00 AM local)
   New Offset: UTC-04:00 (-14400 seconds)
   DST: Yes
   Abbreviation: EDT
   → Clocks spring forward 1 hour (2:00 AM becomes 3:00 AM)

2. November 2, 2025 at 2:00 AM EDT → 1:00 AM EST
   From: 2025-11-02T06:00:00+00:00 (2:00 AM local)
   New Offset: UTC-05:00 (-18000 seconds)
   DST: No
   Abbreviation: EST
   → Clocks fall back 1 hour (2:00 AM becomes 1:00 AM)

3. March 8, 2026 at 2:00 AM EST → 3:00 AM EDT
   From: 2026-03-08T07:00:00+00:00 (2:00 AM local)
   New Offset: UTC-04:00 (-14400 seconds)
   DST: Yes
   Abbreviation: EDT
   → Clocks spring forward 1 hour

4. November 1, 2026 at 2:00 AM EDT → 1:00 AM EST
   From: 2026-11-01T06:00:00+00:00 (2:00 AM local)
   New Offset: UTC-05:00 (-18000 seconds)
   DST: No
   Abbreviation: EST
   → Clocks fall back 1 hour

Summary:
- DST starts: 2nd Sunday in March at 2:00 AM
- DST ends: 1st Sunday in November at 2:00 AM
- Spring forward: Lose 1 hour (2:00 AM → 3:00 AM)
- Fall back: Gain 1 hour (2:00 AM → 1:00 AM)
```

### Example 2: Check European Timezone (Different DST Rules)

**Input**: "When does BST start and end in London?"

**Process**:
1. Timezone: "Europe/London"
2. Call get_timezone_info(timezone="Europe/London")

**Output**:
```
Timezone Information: Europe/London

Current Status (as of Nov 28, 2025):
  Abbreviation: GMT (Greenwich Mean Time)
  UTC Offset: +00:00 (0 seconds)
  DST Active: No
  IANA tzdata version: 2024b

Upcoming DST Transitions (Next 2 Years):

1. March 30, 2025 at 1:00 AM GMT → 2:00 AM BST
   From: 2025-03-30T01:00:00+00:00 (1:00 AM local)
   New Offset: UTC+01:00 (+3600 seconds)
   DST: Yes
   Abbreviation: BST (British Summer Time)
   → Clocks spring forward 1 hour

2. October 26, 2025 at 2:00 AM BST → 1:00 AM GMT
   From: 2025-10-26T01:00:00+00:00 (2:00 AM local)
   New Offset: UTC+00:00 (0 seconds)
   DST: No
   Abbreviation: GMT
   → Clocks fall back 1 hour

3. March 29, 2026 at 1:00 AM GMT → 2:00 AM BST
   From: 2026-03-29T01:00:00+00:00
   New Offset: UTC+01:00 (+3600 seconds)
   DST: Yes
   Abbreviation: BST
   → Clocks spring forward 1 hour

4. October 25, 2026 at 2:00 AM BST → 1:00 AM GMT
   From: 2026-10-25T01:00:00+00:00
   New Offset: UTC+00:00 (0 seconds)
   DST: No
   Abbreviation: GMT
   → Clocks fall back 1 hour

Summary:
- DST starts: Last Sunday in March at 1:00 AM
- DST ends: Last Sunday in October at 2:00 AM
- Different schedule than US (starts/ends earlier)
```

### Example 3: Timezone Without DST

**Input**: "Does Japan observe daylight saving time?"

**Process**:
1. Timezone: "Asia/Tokyo"
2. Call get_timezone_info(timezone="Asia/Tokyo")

**Output**:
```
Timezone Information: Asia/Tokyo

Current Status (as of Nov 28, 2025):
  Abbreviation: JST (Japan Standard Time)
  UTC Offset: +09:00 (+32400 seconds)
  DST Active: No
  IANA tzdata version: 2024b

Upcoming DST Transitions (Next 2 Years):
  (No transitions scheduled)

Summary:
- Japan does not observe Daylight Saving Time
- Offset remains +09:00 year-round
- No clock changes throughout the year
```

### Example 4: Arizona (US State Without DST)

**Input**: "Does Arizona change time for daylight saving?"

**Process**:
1. Timezone: "America/Phoenix"
2. Call get_timezone_info(timezone="America/Phoenix")

**Output**:
```
Timezone Information: America/Phoenix

Current Status (as of Nov 28, 2025):
  Abbreviation: MST (Mountain Standard Time)
  UTC Offset: -07:00 (-25200 seconds)
  DST Active: No (Never observes DST)
  IANA tzdata version: 2024b

Upcoming DST Transitions (Next 2 Years):
  (No transitions scheduled)

Summary:
- Arizona does not observe Daylight Saving Time
- Offset remains -07:00 (MST) year-round
- Exception: Navajo Nation uses America/Denver (observes DST)
- From March-November: Arizona is same time as Pacific Time
- From November-March: Arizona is same time as Mountain Time
```

### Example 5: Southern Hemisphere (Opposite DST Season)

**Input**: "When does daylight saving happen in Sydney?"

**Process**:
1. Timezone: "Australia/Sydney"
2. Call get_timezone_info(timezone="Australia/Sydney")

**Output**:
```
Timezone Information: Australia/Sydney

Current Status (as of Nov 28, 2025):
  Abbreviation: AEDT (Australian Eastern Daylight Time)
  UTC Offset: +11:00 (+39600 seconds)
  DST Active: Yes
  IANA tzdata version: 2024b

Upcoming DST Transitions (Next 2 Years):

1. April 6, 2025 at 3:00 AM AEDT → 2:00 AM AEST
   From: 2025-04-05T16:00:00+00:00 (3:00 AM local)
   New Offset: UTC+10:00 (+36000 seconds)
   DST: No
   Abbreviation: AEST (Australian Eastern Standard Time)
   → Clocks fall back 1 hour (end of summer DST)

2. October 5, 2025 at 2:00 AM AEST → 3:00 AM AEDT
   From: 2025-10-04T16:00:00+00:00 (2:00 AM local)
   New Offset: UTC+11:00 (+39600 seconds)
   DST: Yes
   Abbreviation: AEDT
   → Clocks spring forward 1 hour (start of summer DST)

3. April 5, 2026 at 3:00 AM AEDT → 2:00 AM AEST
   From: 2026-04-04T16:00:00+00:00
   New Offset: UTC+10:00 (+36000 seconds)
   DST: No
   Abbreviation: AEST
   → Clocks fall back 1 hour

4. October 4, 2026 at 2:00 AM AEST → 3:00 AM AEDT
   From: 2026-10-03T16:00:00+00:00
   New Offset: UTC+11:00 (+39600 seconds)
   DST: Yes
   Abbreviation: AEDT
   → Clocks spring forward 1 hour

Summary:
- DST starts: 1st Sunday in October (spring in Southern Hemisphere)
- DST ends: 1st Sunday in April (fall in Southern Hemisphere)
- Opposite season from Northern Hemisphere
- Summer is October-April in Australia
```

## Expected Response Format

```
Timezone Information: [TIMEZONE_ID]

Current Status (as of [DATE]):
  Abbreviation: [ABBREV] ([FULL_NAME])
  UTC Offset: [OFFSET_HOURS] ([OFFSET_SECONDS] seconds)
  DST Active: [Yes/No]
  IANA tzdata version: [VERSION]

Upcoming DST Transitions (Next 2 Years):

[For each transition:]
N. [DATE] at [TIME] [FROM_ABBREV] → [TIME] [TO_ABBREV]
   From: [ISO8601_UTC] ([LOCAL_TIME] local)
   New Offset: UTC[OFFSET] ([OFFSET_SECONDS] seconds)
   DST: [Yes/No]
   Abbreviation: [ABBREV]
   → [Description of change]

Summary:
[Key information about DST pattern or lack thereof]
```

## Use Cases

### 1. Planning Recurring Meetings
```
Question: "Our weekly meeting is at 9 AM. Will that time change due to DST?"
Solution: get_timezone_info → See when DST transitions occur
Action: Plan to adjust recurring meeting schedule
```

### 2. Scheduling Around DST Transitions
```
Question: "When should we avoid scheduling deployments due to time changes?"
Solution: get_timezone_info for each relevant timezone
Action: Mark DST transition dates as risky deployment windows
```

### 3. Understanding Timezone Behavior
```
Question: "Why does my app show different offsets at different times of year?"
Solution: get_timezone_info → Shows DST transitions
Explanation: Offset changes twice a year in DST-observing regions
```

### 4. Travel Planning
```
Question: "I'm traveling to London in March. Will the time difference change?"
Solution: Compare get_timezone_info for both timezones
Result: See if DST transitions affect trip
```

### 5. Application Testing
```
Question: "What dates should we test DST edge cases?"
Solution: get_timezone_info → Extract transition dates
Test: Simulate application behavior on those specific dates/times
```

## DST Transition Patterns

### United States & Canada (Most Regions)
```
Start: 2nd Sunday in March at 2:00 AM local → 3:00 AM
End: 1st Sunday in November at 2:00 AM local → 1:00 AM
Duration: ~8 months of DST
```

### European Union
```
Start: Last Sunday in March at 1:00 AM UTC (2:00 AM/3:00 AM local)
End: Last Sunday in October at 1:00 AM UTC (2:00 AM/3:00 AM local)
Duration: ~7 months of DST
Note: Under review, may be discontinued in future
```

### Australia (Most Regions)
```
Start: 1st Sunday in October at 2:00 AM local → 3:00 AM
End: 1st Sunday in April at 3:00 AM local → 2:00 AM
Duration: ~6 months of DST (Southern Hemisphere summer)
```

### Brazil
```
Historically observed DST, but discontinued in 2019
No longer observes DST
```

## Regions Without DST

Many regions never observe DST:
```
Asia: Most of Asia (China, Japan, India, etc.)
Africa: Most of Africa
Americas: Arizona (except Navajo Nation), Hawaii, most of Caribbean
Middle East: Most Gulf states
Pacific: Some Pacific islands
```

## Error Handling

### Invalid Timezone
```
Error: Timezone "America/Boston" not found
Solution: Use list_timezones(search="Boston") to find "America/New_York"
```

### Future Changes
```
Note: DST rules can change due to political decisions
Example: EU considering ending DST changes
Action: Monitor tzdata updates for rule changes
```

## Notes

- Transition dates are shown 2 years in advance
- IANA tzdata is updated multiple times per year
- Political bodies can change DST rules at any time
- Historical DST transitions also available (consult IANA tzdata directly)
- Spring forward = lose 1 hour of sleep
- Fall back = gain 1 hour of sleep
- Some timezones have unusual offsets (e.g., Newfoundland uses UTC-03:30)
- Times shown in UTC to avoid ambiguity
- Local times during transitions can be non-existent or ambiguous
- Applications should avoid scheduling critical operations during transition windows

## Related Playbooks

- **get_time_for_timezone.md**: Get current time with DST status
- **convert_time_between_timezones.md**: Handle DST in conversions
- **plan_dst_transition.md**: Plan around DST changes (scenario)
- **list_available_timezones.md**: Find correct timezone identifiers
- **schedule_global_meeting.md**: Account for DST in scheduling
