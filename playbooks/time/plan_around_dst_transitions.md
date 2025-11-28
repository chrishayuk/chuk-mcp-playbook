# Scenario Playbook: Plan Around DST Transitions

## Description
This scenario demonstrates how to identify, plan around, and handle Daylight Saving Time (DST) transitions to avoid scheduling conflicts, application bugs, and user confusion.

## Scenario
You're a DevOps engineer managing a global service. You need to plan deployments, schedule recurring jobs, and ensure your application handles DST transitions correctly without breaking scheduled tasks or creating duplicate/skipped events.

## Prerequisites
- Access to the chuk-mcp-time server
- List of timezones your service operates in
- Schedule of recurring events or jobs
- Understanding of DST edge cases

## Steps

### 1. Identify All Relevant Timezones

Determine which timezones your service operates in:
```
- User-facing: Where your users are located
- Infrastructure: Where your servers are hosted
- Business: Where your offices/teams are located
```

### 2. Check DST Transition Schedules

Query each timezone for upcoming DST transitions:
```
Tool: get_timezone_info
For each timezone:
  - Get current DST status
  - Get next 2 years of transitions
  - Note specific dates and times
```

### 3. Identify Risk Windows

Mark DST transition dates as high-risk periods:
```
Spring Forward (lose 1 hour):
  - 2:00 AM - 3:00 AM doesn't exist
  - Risk: Scheduled events in this window are skipped or invalid

Fall Back (gain 1 hour):
  - 1:00 AM - 2:00 AM happens twice
  - Risk: Scheduled events might run twice
```

### 4. Plan Deployment Windows

Avoid deployments during DST transitions:
```
Safe windows:
  - At least 6 hours before transition
  - At least 6 hours after transition
  - UTC-based infrastructure not affected
```

### 5. Adjust Recurring Schedules

Handle recurring events across DST transitions:
```
Options:
  1. Use UTC for all scheduling (recommended)
  2. Adjust local time schedules around transitions
  3. Skip/defer events during transition window
```

## MCP Tools Required

### chuk-mcp-time

**Tool 1**: `get_timezone_info`
- Get DST transition schedule for each timezone
- See exact dates/times of transitions
- Identify current DST status

**Tool 2**: `convert_time`
- Convert scheduled times across transitions
- Verify event times before and after DST
- Detect invalid or ambiguous times

**Tool 3**: `get_local_time`
- Get current time with DST status
- Verify timezone abbreviations
- Check current offset

**Tool 4**: `list_timezones`
- Find all timezones in a region
- Identify which timezones observe DST

## Example Scenario: Production Deployment Planning

### Situation
You need to deploy a critical update to production in March 2025. Your infrastructure spans multiple timezones.

### Step 1: Identify DST Transitions

```
Query: get_timezone_info for each timezone

Results:
America/New_York:
  - March 9, 2025 at 2:00 AM EST → 3:00 AM EDT
  - Spring forward: Lose 1 hour

Europe/London:
  - March 30, 2025 at 1:00 AM GMT → 2:00 AM BST
  - Spring forward: Lose 1 hour

Asia/Tokyo:
  - No DST transitions (Japan doesn't observe DST)
  - Safe to deploy anytime

America/Los_Angeles:
  - March 9, 2025 at 2:00 AM PST → 3:00 AM PDT
  - Spring forward: Lose 1 hour
```

### Step 2: Create Risk Window Calendar

```
HIGH RISK - DO NOT DEPLOY:

March 9, 2025 (Sunday):
  - 12:00 AM - 6:00 AM PST (America/Los_Angeles)
  - 3:00 AM - 9:00 AM EST (America/New_York)
  - Risk: DST transition at 2:00 AM in US timezones

March 30, 2025 (Sunday):
  - 10:00 PM Mar 29 - 4:00 AM Mar 30 GMT (Europe/London)
  - Risk: DST transition at 1:00 AM GMT

SAFE DEPLOYMENT WINDOWS:

Option A: Before US DST transition
  - March 8, 2025 (Saturday) before 6:00 PM PST
  - Ensures 8+ hour buffer before transition

Option B: After US DST transition
  - March 9, 2025 (Sunday) after 12:00 PM EDT
  - Ensures 9+ hour buffer after transition

Option C: Between US and EU transitions
  - March 10-29, 2025 (weekdays preferred)
  - After US transition, before EU transition

RECOMMENDED: March 11, 2025 (Tuesday) at 10:00 PM UTC
  - 2 days after US DST transition
  - 19 days before EU DST transition
  - 7:00 AM JST (Tokyo - during business hours)
  - 3:00 PM PST (SF - during business hours)
  - 6:00 PM EST (NYC - after hours)
  - 10:00 PM GMT (London - late evening)
```

### Step 3: Deployment Plan

```
Deployment Schedule:
Date: Tuesday, March 11, 2025
Time: 22:00 UTC (10:00 PM UTC)

Regional Times:
┌─────────────────┬──────────────┬─────────────┬──────────┐
│ Region          │ Local Time   │ DST Status  │ Impact   │
├─────────────────┼──────────────┼─────────────┼──────────┤
│ San Francisco   │ 3:00 PM PDT  │ DST active  │ Low      │
│ New York        │ 6:00 PM EDT  │ DST active  │ Low      │
│ London          │ 10:00 PM GMT │ No DST yet  │ Low      │
│ Tokyo           │ 7:00 AM JST  │ Never DST   │ Low      │
└─────────────────┴──────────────┴─────────────┴──────────┘

Rationale:
✅ 2+ days after US DST transition (stability confirmed)
✅ 19 days before EU DST transition (good buffer)
✅ All teams can monitor deployment
✅ No timezone in transition window
```

## Example Scenario: Recurring Job Scheduling

### Situation
You have a daily report that runs at 2:00 AM local time in America/New_York. How do you handle the DST transition?

### Problem Analysis

```
March 9, 2025 DST Transition:

Regular schedule:
  - Daily at 2:00 AM EST/EDT

What happens on March 9?
  - At 2:00 AM, clocks jump to 3:00 AM
  - 2:00 AM - 3:00 AM doesn't exist
  - Job scheduled for 2:00 AM will... ???

Possible outcomes:
  1. Job skipped entirely (2:00 AM doesn't exist)
  2. Job runs at 3:00 AM (next valid time)
  3. Job runs at 1:00 AM UTC (interpreted as UTC)
  4. Job errors out (invalid time)

November 2, 2025 DST Transition:

Regular schedule:
  - Daily at 2:00 AM EST/EDT

What happens on November 2?
  - At 2:00 AM EDT, clocks fall back to 1:00 AM EST
  - 1:00 AM - 2:00 AM happens TWICE
  - Job might run twice!

Possible outcomes:
  1. Job runs twice (once in each occurrence of 2:00 AM)
  2. Job runs once (scheduler picks first or second)
  3. Job runs with wrong data (thinks it already ran)
```

### Solution 1: Use UTC for Scheduling

```
RECOMMENDED: Schedule in UTC

Old schedule:
  - 2:00 AM America/New_York (local time)
  - Problematic: Changes meaning during DST

New schedule:
  - 7:00 AM UTC (fixed time)
  - Equivalent to 2:00 AM EST
  - Becomes 3:00 AM EDT after DST transition

Benefits:
  ✅ No ambiguity during DST transitions
  ✅ Consistent from infrastructure perspective
  ✅ No duplicate or skipped runs

Trade-offs:
  ⚠️  Local time shifts by 1 hour twice a year
  ⚠️  May need to adjust if local time is important

Implementation:
  Tool: convert_time("2025-03-09T02:00:00", "America/New_York", "UTC")
  Result: 07:00 UTC
  Schedule: Daily at 07:00 UTC
```

### Solution 2: Avoid Transition Window

```
ALTERNATIVE: Schedule outside transition window

Problematic times:
  - 2:00 AM - 3:00 AM (transition window)

Safe times:
  - 12:00 AM - 1:59 AM (before transition)
  - 3:01 AM - 11:59 PM (after transition)

New schedule:
  - 3:30 AM America/New_York
  - After DST transition window
  - Safe year-round

Benefits:
  ✅ Maintains local time meaning
  ✅ Never in transition window

Trade-offs:
  ⚠️  Runs 1.5 hours later than desired
```

### Solution 3: Explicit Handling

```
ADVANCED: Handle each transition explicitly

Spring Forward (March 9):
  - Skip job on transition day OR
  - Run at 3:00 AM instead of 2:00 AM
  - Add logging: "DST transition - adjusted schedule"

Fall Back (November 2):
  - Run job only once (use first occurrence OR second occurrence)
  - Add deduplication logic
  - Add logging: "DST transition - deduplicated run"

Implementation:
  - Use get_timezone_info to detect transition dates
  - Add special cases in scheduler
  - Monitor and alert on DST transition days
```

## Example Scenario: Meeting Series Across DST

### Situation
You have a weekly meeting at 3:00 PM EST/EDT on Thursdays with participants in New York, London, and Singapore.

### Problem

```
Normal schedule:
  New York:   3:00 PM EST/EDT
  London:     8:00 PM GMT/BST
  Singapore:  4:00 AM SGT (next day)

But DST transitions don't align:
  - US DST: March 9, 2025
  - EU DST: March 30, 2025

Between March 9-30:
  New York:   3:00 PM EDT (UTC-04:00)
  London:     7:00 PM GMT (UTC+00:00)  ← 1 hour earlier!
  Singapore:  3:00 AM SGT (UTC+08:00)  ← 1 hour earlier!

After March 30:
  New York:   3:00 PM EDT (UTC-04:00)
  London:     8:00 PM BST (UTC+01:00)  ← Back to normal
  Singapore:  3:00 AM SGT (UTC+08:00)  ← Still 1 hour earlier
```

### Solution

```
Option 1: Maintain NYC time (local time for organizer)
Schedule: 3:00 PM America/New_York every Thursday

Consequences:
  - London participants: 8 PM → 7 PM → 8 PM (changes twice)
  - Singapore participants: 4 AM → 3 AM (changes once)
  - Notify participants of time changes

Option 2: Maintain UTC time (consistent for all)
Schedule: 19:00 UTC every Thursday

Consequences:
  - NYC: 2 PM EST → 3 PM EDT (shifts for organizer)
  - London: 7 PM GMT → 8 PM BST (shifts for EU)
  - Singapore: 3 AM SGT (no change)
  - All shifts happen on their DST transition dates

Option 3: Reschedule during transition period
March 9 - March 30:
  - Temporary time: 4:00 PM EDT (New York)
  - Maintains 8 PM GMT (London) and 4 AM SGT (Singapore)

After March 30:
  - Return to 3:00 PM EDT (New York)
  - Maintains 8 PM BST (London) and 3 AM SGT (Singapore)

RECOMMENDED: Option 1 with proactive communication
- Maintain organizer's local time
- Send calendar updates before DST transitions
- Include note: "Meeting time may shift due to DST"
- Use UTC in calendar invites (handles DST automatically)
```

## Best Practices

### 1. Always Use UTC for Infrastructure
```
✅ Cron jobs in UTC
✅ Database timestamps in UTC
✅ Log timestamps in UTC
✅ API contracts in UTC

Convert to local time only for display
```

### 2. Avoid Transition Windows
```
❌ Don't schedule at 2:00 AM local time
❌ Don't deploy during DST transition day
❌ Don't run critical jobs 1-4 AM on transition days

✅ Schedule at safe times (e.g., 3:30 AM or later)
✅ Deploy on weekdays, not transition weekends
✅ Add 6-hour buffers around transitions
```

### 3. Test DST Edge Cases
```
Test scenarios:
  - Job scheduled during spring forward (non-existent time)
  - Job scheduled during fall back (duplicate time)
  - Recurring event across DST boundary
  - Time zone conversion on transition day
  - User input of invalid times (e.g., 2:30 AM on March 9)

Use get_timezone_info to find exact test dates
```

### 4. Communicate Proactively
```
Before DST transitions:
  - Notify users of schedule changes
  - Update documentation
  - Send calendar updates
  - Post timezone reminders

After DST transitions:
  - Verify all systems transitioned correctly
  - Check for duplicate or skipped events
  - Monitor error logs
```

### 5. Monitor DST Transition Days
```
Set up alerts:
  - Watch for unusual error rates on transition days
  - Monitor job success/failure rates
  - Check for duplicate event processing
  - Verify time-based queries return expected results

Review get_timezone_info output 1 week before each transition
```

## Common Pitfalls

### Pitfall 1: Assuming All Countries Have Same DST
```
❌ "It's DST, so everyone spring forward"
✅ US: March 9, EU: March 30, Australia: October 5

Solution: Check each timezone individually
```

### Pitfall 2: Using Local Time for Recurring Jobs
```
❌ Cron: "0 2 * * * /script.sh" (local time)
✅ Cron in UTC: "0 7 * * * /script.sh"

Solution: Always use UTC for infrastructure
```

### Pitfall 3: Not Handling Non-Existent Times
```
❌ Assuming 2:30 AM always exists
✅ Validate time exists or handle gracefully

Solution: Check DST transitions before scheduling
```

### Pitfall 4: Forgetting Southern Hemisphere
```
❌ "DST starts in March" (true for US, false for Australia)
✅ Australia: DST starts October, ends April

Solution: Use get_timezone_info, don't assume seasons
```

### Pitfall 5: Hardcoding Offsets
```
❌ "New York is always UTC-5"
✅ New York is UTC-5 (EST) or UTC-4 (EDT)

Solution: Use timezone names, not fixed offsets
```

## Tools for DST Planning

### Pre-Transition Checklist
```
6 weeks before:
  □ Run get_timezone_info for all relevant timezones
  □ Identify transition dates
  □ Review scheduled events during transition windows
  □ Plan deployment freeze periods

2 weeks before:
  □ Communicate schedule changes to users
  □ Update documentation
  □ Review and test DST handling code
  □ Prepare monitoring alerts

1 week before:
  □ Final review of schedules
  □ Send reminder communications
  □ Enable enhanced monitoring
  □ Prepare rollback procedures

Day of transition:
  □ Monitor systems closely
  □ Check for skipped/duplicate events
  □ Verify all jobs ran as expected
  □ Review error logs

Day after transition:
  □ Validate all systems transitioned correctly
  □ Confirm no lingering issues
  □ Document any problems encountered
  □ Update runbooks with lessons learned
```

## Notes

- 70+ countries observe DST, each with different rules
- DST rules can change due to political decisions
- IANA tzdata updated multiple times per year for rule changes
- Some regions (EU) considering eliminating DST entirely
- Always use latest tzdata version
- Test applications thoroughly around DST transitions
- UTC doesn't observe DST (always stable reference)
- Spring forward is harder to handle than fall back
- Financial systems often pause during transition windows
- Consider timezone-agnostic architectures where possible

## Related Playbooks

- **get_timezone_dst_info.md**: Get DST schedule for a timezone
- **convert_time_between_timezones.md**: Handle DST in conversions
- **schedule_global_meeting.md**: Account for DST in meeting scheduling
- **troubleshoot_time_sync_issues.md**: Fix time-related problems
