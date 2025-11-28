# Scenario Playbook: Schedule a Global Meeting

## Description
This scenario demonstrates how to find the best meeting time across multiple timezones, ensuring all participants can join during reasonable business hours.

## Scenario
You need to schedule a meeting with team members in San Francisco, New York, London, and Singapore. You want to find a time that works for everyone during business hours (9 AM - 6 PM local time).

## Prerequisites
- Access to the chuk-mcp-time server
- List of participant locations/timezones
- Desired meeting duration
- Business hours constraints per location

## Steps

### 1. Identify All Participant Timezones

Collect timezone information for each location:
- San Francisco: `America/Los_Angeles` (Pacific Time)
- New York: `America/New_York` (Eastern Time)
- London: `Europe/London` (GMT/BST)
- Singapore: `Asia/Singapore` (Singapore Time)

### 2. Get Current Time for All Locations

Query each timezone to establish baseline:
```
Tool: get_time_for_timezone
- timezone_name: "America/Los_Angeles"
- mode: "fast"

Tool: get_time_for_timezone
- timezone_name: "America/New_York"
- mode: "fast"

Tool: get_time_for_timezone
- timezone_name: "Europe/London"
- mode: "fast"

Tool: get_time_for_timezone
- timezone_name: "Asia/Singapore"
- mode: "fast"
```

### 3. Calculate Time Differences

Determine UTC offsets for each location:
```
San Francisco: UTC-8 (PST) or UTC-7 (PDT)
New York:      UTC-5 (EST) or UTC-4 (EDT)
London:        UTC+0 (GMT) or UTC+1 (BST)
Singapore:     UTC+8 (SGT, no DST)
```

### 4. Find Overlapping Business Hours

Calculate when business hours overlap:

**Business Hours (Local Time):**
- San Francisco: 9 AM - 6 PM PST/PDT
- New York: 9 AM - 6 PM EST/EDT
- London: 9 AM - 6 PM GMT/BST
- Singapore: 9 AM - 6 PM SGT

**Convert to UTC:**
```
San Francisco: 17:00 - 02:00 UTC (next day)
New York:      14:00 - 23:00 UTC
London:        09:00 - 18:00 UTC
Singapore:     01:00 - 10:00 UTC
```

**Find Overlap:**
No complete overlap exists! This is common for global meetings spanning 16 time zones.

### 5. Find Best Compromise Time

When no perfect overlap exists, find the least painful time:

**Option A: Early Morning US, Evening Europe/Asia**
- UTC Time: 14:00 (2 PM UTC)
- San Francisco: 6 AM PST (before hours, but possible)
- New York: 9 AM EST ✅ (start of day)
- London: 2 PM GMT ✅ (afternoon)
- Singapore: 10 PM SGT (late, but possible)

**Option B: Late US, Morning Europe/Asia**
- UTC Time: 01:00 (1 AM UTC)
- San Francisco: 5 PM PST previous day ✅ (end of day)
- New York: 8 PM EST previous day (after hours)
- London: 1 AM GMT (not viable)
- Singapore: 9 AM SGT ✅ (start of day)

**Option C: Rotate Meeting Times**
Schedule 2 meetings to accommodate all timezones fairly:
- Meeting A: US + Europe friendly
- Meeting B: Europe + Asia friendly

### 6. Present Recommendations

**Recommended Meeting Time: 2 PM UTC (14:00 UTC)**

```
Global Meeting Time Finder
============================

Proposed Time: 2:00 PM UTC (Thursday)

Local Times:
┌─────────────────┬──────────────┬────────────────┬──────────┐
│ Location        │ Local Time   │ Business Hours │ Status   │
├─────────────────┼──────────────┼────────────────┼──────────┤
│ San Francisco   │ 6:00 AM PST  │ 9 AM - 6 PM    │ ⚠️ Early  │
│ New York        │ 9:00 AM EST  │ 9 AM - 6 PM    │ ✅ Good   │
│ London          │ 2:00 PM GMT  │ 9 AM - 6 PM    │ ✅ Good   │
│ Singapore       │ 10:00 PM SGT │ 9 AM - 6 PM    │ ⚠️ Late   │
└─────────────────┴──────────────┴────────────────┴──────────┘

Impact Summary:
- 2 locations in business hours ✅
- 1 location early morning ⚠️ (6 AM)
- 1 location late evening ⚠️ (10 PM)

Alternative: Consider rotating meeting times or splitting into 2 meetings.

Time synchronized via NTP consensus (±12.5ms accuracy)
```

## MCP Tools Required

### chuk-mcp-time

**Primary Tool**: `get_time_for_timezone`
- Called once per participant timezone
- Returns current time and offset for each location

**Example Implementation**:
```
1. get_time_for_timezone(timezone_name="America/Los_Angeles")
2. get_time_for_timezone(timezone_name="America/New_York")
3. get_time_for_timezone(timezone_name="Europe/London")
4. get_time_for_timezone(timezone_name="Asia/Singapore")

Use returned times to calculate:
- Current offset from UTC for each
- Business hours in UTC
- Overlap periods
- Best meeting time candidates
```

## Example Output

```
🌍 Global Meeting Scheduler

Team Locations:
├─ 🇺🇸 San Francisco (America/Los_Angeles) - UTC-8
├─ 🇺🇸 New York (America/New_York) - UTC-5
├─ 🇬🇧 London (Europe/London) - UTC+0
└─ 🇸🇬 Singapore (Asia/Singapore) - UTC+8

Current Time Check:
├─ San Francisco: Mon, Nov 27 2025, 5:23 PM PST
├─ New York:      Mon, Nov 27 2025, 8:23 PM EST
├─ London:        Tue, Nov 28 2025, 1:23 AM GMT
└─ Singapore:     Tue, Nov 28 2025, 9:23 AM SGT

Analysis:
Total timezone span: 16 hours
No overlapping business hours found.

Recommended Solutions:

Option 1️⃣: Single Meeting Time
📅 Tuesday, 2:00 PM UTC

Local times:
├─ San Francisco: 6:00 AM PST ⚠️  (3h before business hours)
├─ New York:      9:00 AM EST ✅  (business hours start)
├─ London:        2:00 PM GMT ✅  (mid-afternoon)
└─ Singapore:     10:00 PM SGT ⚠️  (4h after business hours)

Trade-offs:
- SF team starts early (6 AM)
- Singapore team stays late (10 PM)
- NY and London optimal

Option 2️⃣: Rotating Meeting Times
📅 Week A: 9 PM UTC (US + Europe)
📅 Week B: 2 AM UTC (Europe + Asia)

This ensures no team is always inconvenienced.

Option 3️⃣: Asynchronous Communication
Consider using recorded updates for this timezone spread.
```

## Use Cases

### 1. Weekly Team Sync
```
Scenario: Regular standup across 3-4 timezones
Approach: Find best recurring time, rotate occasionally
Tools: get_time_for_timezone for all locations
```

### 2. One-Time Important Meeting
```
Scenario: Quarterly business review with global executives
Approach: Poll for availability, find least disruptive time
Tools: get_time_for_timezone + business hours analysis
```

### 3. Emergency Response
```
Scenario: Production incident requiring global team
Approach: Immediate coordination regardless of time
Tools: get_time_for_timezone to notify and coordinate
```

### 4. Product Launch Coordination
```
Scenario: Coordinated launch across all regions
Approach: Find time that works for core stakeholders
Tools: get_time_for_timezone + UTC reference time
```

## Best Practices

### 1. Be Transparent About Impact
```
Always show who is being inconvenienced:
- "This meeting is at 6 AM for SF team"
- "Singapore team will be joining at 10 PM"
```

### 2. Rotate Meeting Times
```
Week 1: Europe-friendly (7 AM PST, 3 PM GMT, 11 PM SGT)
Week 2: Asia-friendly (5 PM PST, 1 AM GMT, 9 AM SGT)
Week 3: US-friendly (9 AM PST, 5 PM GMT, 1 AM SGT)
```

### 3. Consider Asynchronous Alternatives
```
For very wide timezone spreads (>12 hours):
- Recorded video updates
- Written summaries
- Follow-up Q&A sessions
- Regional meetings with async collaboration
```

### 4. Use UTC as Common Reference
```
Always specify meeting times in UTC:
"Meeting at 14:00 UTC (2 PM UTC)"
Then show local conversions
```

### 5. Account for Daylight Saving Time
```
Check if any locations have upcoming DST changes:
- US: 2nd Sunday in March / 1st Sunday in November
- EU: Last Sunday in March / Last Sunday in October
- Some regions don't observe DST (Asia, most of Africa)
```

## Common Timezone Challenges

### Challenge 1: No Overlap
**Solution**: Rotating times or split meetings

### Challenge 2: DST Transitions
**Solution**: Use IANA timezones (handles DST automatically)

### Challenge 3: Cultural Work Hours
**Solution**: Consider regional norms (some regions start earlier/later)

### Challenge 4: Weekend/Holiday Differences
**Solution**: Check regional holidays before scheduling

## Notes

- 16-hour timezone span (SF to Singapore) makes scheduling very difficult
- Consider if meeting is truly necessary for all participants
- Some team members can watch recordings instead
- Use accurate NTP time to ensure everyone joins at exact same moment
- Consider time zone fatigue - don't always inconvenience same locations
- Tools like World Time Buddy can visualize overlaps
- Always send calendar invites with timezone support (.ics files)

## Advanced: Business Hours Matrix

Create a matrix showing overlap:
```
        SF    NY    LON   SG
SF      ✅    ⚠️    ❌    ❌
NY      ⚠️    ✅    ✅    ❌
LON     ❌    ✅    ✅    ⚠️
SG      ❌    ❌    ⚠️    ✅

✅ = Full business hours overlap
⚠️ = Partial overlap (early/late in one location)
❌ = No overlap
```

This shows:
- NY ↔ LON has good overlap
- SF ↔ SG has no overlap
- Need compromise time or split meetings
