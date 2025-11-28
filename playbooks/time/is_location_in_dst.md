# Playbook: Check if Location is in Daylight Saving Time

## Description
This playbook determines whether a specific location is currently observing daylight saving time (DST), including current timezone abbreviation and when DST started or will end.

## Prerequisites
- Location name or IANA timezone identifier
- Access to the chuk-mcp-time server
- Internet connectivity to reach NTP servers

## Steps

1. Find the IANA timezone for the location
   - Use list_timezones to search by location name
   - Verify correct timezone identifier

2. Get current timezone status
   - Call get_local_time to check current DST status
   - Retrieve timezone abbreviation and UTC offset
   - Get accurate current time with NTP consensus

3. Get DST transition history and schedule
   - Call get_timezone_info for transition details
   - Find when current DST period started or standard time began
   - Determine when next transition will occur

4. Determine if location observes DST at all
   - Check if transitions array is empty (never observes DST)
   - Or check if DST is currently active

5. Format response with DST status
   - State yes/no for DST status
   - Include current timezone abbreviation
   - Show when DST started/ended
   - Indicate when next change occurs

## MCP Tools Required

### chuk-mcp-time

**Tool 1**: `list_timezones` (for finding timezone)
- **Parameters**:
  - `search` (string, optional): Location name
  - `country_code` (string, optional): ISO 3166 country code
- **Returns**:
  - `timezones` (array): Matching timezone identifiers

**Tool 2**: `get_local_time` (for current DST status)
- **Parameters**:
  - `timezone` (string, required): IANA timezone identifier
  - `mode` (string, optional): "fast" (default)
- **Returns**:
  - `is_dst` (bool): Whether DST is currently active
  - `abbreviation` (string): Current timezone abbreviation
  - `utc_offset_seconds` (int): Current UTC offset
  - `local_datetime` (string): Current local time

**Tool 3**: `get_timezone_info` (for transition details)
- **Parameters**:
  - `timezone` (string, required): IANA timezone identifier
- **Returns**:
  - `current_is_dst` (bool): Current DST status
  - `transitions` (array): Upcoming DST transitions
  - `tzdata_version` (string): IANA tzdata version

## Example Usage

**Input**: "Is Sydney in DST?"

**Process**:
1. Find timezone:
   ```
   Tool: list_timezones(search="Sydney")
   Returns: {id: "Australia/Sydney"}
   ```

2. Check current status:
   ```
   Tool: get_local_time(timezone="Australia/Sydney")
   Returns: {
     is_dst: true,
     abbreviation: "AEDT",
     utc_offset_seconds: 39600
   }
   ```

3. Get transition details:
   ```
   Tool: get_timezone_info(timezone="Australia/Sydney")
   Returns: {
     transitions: [
       {
         from_datetime: "2025-10-05T16:00:00+00:00",
         is_dst: true
       },
       {
         from_datetime: "2026-04-05T16:00:00+00:00",
         is_dst: false
       }
     ]
   }
   ```

**Output**:
```
Yes, Sydney is currently in Daylight Saving Time.

Current Status:
- Time Standard: AEDT (Australian Eastern Daylight Time)
- UTC Offset: +11:00
- DST Active: Yes
- DST Started: October 5, 2025 at 2:00 AM

DST will end on April 6, 2026 at 3:00 AM.
After that, Sydney will return to AEST (UTC+10:00).
```

## Expected Response Format

```
[Yes/No], [Location] is [currently in/not in] Daylight Saving Time.

Current Status:
- Time Standard: [ABBREV] ([Full Name])
- UTC Offset: [±HH:MM]
- DST Active: [Yes/No]
- DST [Started/Ended]: [Date] at [Time]

[If DST active:]
DST will end on [Date] at [Time].
After that, [Location] will return to [STD_ABBREV] (UTC[±HH:MM]).

[If DST not active:]
DST will start on [Date] at [Time].
During DST, [Location] will use [DST_ABBREV] (UTC[±HH:MM]).

OR (for locations without DST):

No, [Location] does not observe Daylight Saving Time.
[Location] remains on [ABBREV] (UTC[±HH:MM]) year-round.
```

## Error Handling

- Location not found: Ask for more specific location or correct spelling
- Multiple locations found: Present options and ask user to clarify
- Timezone lookup fails: Suggest using IANA timezone ID directly
- Empty transitions: Location does not observe DST

## Notes

- The `is_dst` field from get_local_time definitively answers whether DST is currently active
- Don't assume DST based on time of year - always use the tool
- Some locations never observe DST (Japan, Singapore, Phoenix, Hawaii, etc.)
- Some locations stopped observing DST (Brazil 2019, Russia 2014)
- Southern Hemisphere has DST during Northern Hemisphere's winter (opposite seasons)
- DST status can change due to political decisions - always use latest tzdata
- Empty transitions array means location never observes DST
- Some US states/territories don't observe DST (Arizona except Navajo Nation, Hawaii)
- Some Australian states don't observe DST (Queensland, Western Australia, Northern Territory)
- Always use get_local_time or get_timezone_info - don't hardcode DST schedules
