# Playbook: Get DST Transition Dates for a Location

## Description
This playbook retrieves the specific dates and times when clocks change for daylight saving time (DST) in any location worldwide, including spring forward and fall back transitions.

## Prerequisites
- Location name or IANA timezone identifier
- Access to the chuk-mcp-time server

## Steps

1. Find the IANA timezone for the location
   - Use list_timezones to search by location name
   - Verify correct timezone identifier

2. Request DST transition information
   - Call get_timezone_info with the timezone identifier
   - Retrieve transitions for next 2 years

3. Parse the transition schedule
   - Extract transition datetimes
   - Identify spring forward vs fall back transitions
   - Note new UTC offsets and abbreviations after each transition
   - Determine if location observes DST at all

4. Format transition information
   - Show dates in user-friendly format
   - Explain what happens during each transition
   - Include time changes and offset changes
   - Note the DST pattern/rule if applicable

5. Return the DST schedule to the user

## MCP Tools Required

### chuk-mcp-time

**Tool 1**: `list_timezones` (for finding timezone)
- **Parameters**:
  - `search` (string, optional): Location name
  - `country_code` (string, optional): ISO 3166 country code
- **Returns**:
  - `timezones` (array): Matching timezone identifiers

**Tool 2**: `get_timezone_info` (for DST transitions)
- **Parameters**:
  - `timezone` (string, required): IANA timezone identifier
  - `mode` (string, optional): "fast" (default) or "accurate"
- **Returns**:
  - `timezone` (string): IANA timezone identifier
  - `current_is_dst` (bool): Whether DST is currently active
  - `current_abbreviation` (string): Current timezone abbreviation
  - `current_offset_seconds` (int): Current UTC offset
  - `transitions` (array): List of upcoming DST transitions
    - `from_datetime` (string): When transition occurs (ISO 8601 UTC)
    - `utc_offset_seconds` (int): New offset after transition
    - `is_dst` (bool): Whether DST is active after transition
    - `abbreviation` (string): New timezone abbreviation
  - `tzdata_version` (string): IANA tzdata version

## Example Usage

**Input**: "When do the clocks go forward in New York?"

**Process**:
1. Find timezone:
   ```
   Tool: list_timezones(search="New York")
   Returns: {id: "America/New_York"}
   ```

2. Get DST transitions:
   ```
   Tool: get_timezone_info(timezone="America/New_York")
   Returns: {
     current_is_dst: false,
     current_abbreviation: "EST",
     transitions: [
       {
         from_datetime: "2026-03-08T07:00:00+00:00",
         utc_offset_seconds: -14400,
         is_dst: true,
         abbreviation: "EDT"
       },
       {
         from_datetime: "2026-11-01T06:00:00+00:00",
         utc_offset_seconds: -18000,
         is_dst: false,
         abbreviation: "EST"
       }
     ]
   }
   ```

**Output**:
```
New York (America/New_York) DST Schedule:

Spring Forward (Start of DST):
  Date: Sunday, March 8, 2026
  Time: 2:00 AM EST → 3:00 AM EDT
  Change: Clocks move forward 1 hour
  Effect: You lose 1 hour (2:00-3:00 AM doesn't exist)
  New offset: UTC-04:00

Fall Back (End of DST):
  Date: Sunday, November 1, 2026
  Time: 2:00 AM EDT → 1:00 AM EST
  Change: Clocks move back 1 hour
  Effect: You gain 1 hour (1:00-2:00 AM happens twice)
  New offset: UTC-05:00

Pattern: US observes DST from 2nd Sunday in March to 1st Sunday in November
```

## Expected Response Format

```
[Location] ([Timezone]) DST Schedule:

Spring Forward (Start of DST):
  Date: [Day], [Date]
  Time: [Time] [From_TZ] → [Time] [To_TZ]
  Change: Clocks move forward [N] hour(s)
  Effect: [Description of what happens]
  New offset: UTC[±HH:MM]

Fall Back (End of DST):
  Date: [Day], [Date]
  Time: [Time] [From_TZ] → [Time] [To_TZ]
  Change: Clocks move back [N] hour(s)
  Effect: [Description of what happens]
  New offset: UTC[±HH:MM]

Pattern: [Description of DST rule if applicable]

OR (for locations without DST):

[Location] does not observe Daylight Saving Time.
Clocks remain at [TZ_ABBREV] (UTC[±HH:MM]) year-round.
```

## Error Handling

- Location not found: Ask for more specific location or correct spelling
- Ambiguous location: Present all matching timezones and ask user to clarify
- Timezone lookup fails: Suggest using country code or IANA timezone ID directly
- Empty transitions array: Location does not observe DST

## Notes

- Always use get_timezone_info to retrieve actual transition dates - don't hardcode DST rules
- DST rules vary by country and can change due to political decisions
- Some locations never observe DST (Japan, most of China, Arizona, Hawaii, etc.)
- Some locations used to observe DST but stopped (Brazil 2019, Russia 2014)
- Transitions array is empty for locations that don't observe DST
- Northern and Southern Hemispheres have opposite DST seasons
- US: 2nd Sunday in March / 1st Sunday in November
- EU: Last Sunday in March / Last Sunday in October
- Australia: 1st Sunday in October / 1st Sunday in April
- Times shown in UTC to avoid ambiguity - convert to local time for user display
- Spring forward means times in the gap don't exist (e.g., 2:30 AM on transition day)
- Fall back means times in the overlap happen twice
- IANA tzdata is updated regularly when governments change DST rules
- Some regions have unusual DST patterns (e.g., Morocco, Chile have unique rules)
