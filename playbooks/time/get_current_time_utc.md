# Playbook: Get Current UTC Time

## Description
This playbook retrieves the current UTC time with high accuracy using NTP consensus from multiple trusted time servers.

## Prerequisites
- Access to the chuk-mcp-time server
- Internet connectivity to reach NTP servers

## Steps

1. Choose accuracy mode
   - Fast mode: Queries 4 NTP servers (~40-150ms)
   - Accurate mode: Queries 7 NTP servers (~100-300ms)

2. Request current UTC time
   - Call the time API with desired mode
   - Optionally disable latency compensation if raw timestamp is needed

3. Parse the time response
   - Extract ISO 8601 formatted time
   - Get epoch milliseconds
   - Check number of sources used
   - Review estimated error margin
   - Check for any warnings

4. Validate time quality
   - Verify sufficient sources were used
   - Check estimated error is acceptable
   - Review any warnings about system clock drift

5. Return the accurate UTC time to the user

## MCP Tools Required

### chuk-mcp-time

**Tool**: `get_time_utc`
- **Parameters**:
  - `mode` (string, optional): "fast" (default) or "accurate"
    - "fast": Queries 4 NTP servers, ~40-150ms response time
    - "accurate": Queries 7 NTP servers, ~100-300ms response time
  - `compensate_latency` (bool, optional): true (default) or false
    - true: Adjusts timestamp for query duration (returned time represents "now")
    - false: Returns raw consensus timestamp from when queries started
- **Returns**:
  - `iso8601_time` (string): ISO 8601 formatted timestamp (e.g., "2025-11-28T01:23:45.123456+00:00")
  - `epoch_ms` (int): Unix epoch time in milliseconds
  - `sources_used` (int): Number of NTP servers successfully queried
  - `total_sources` (int): Total NTP servers attempted
  - `consensus_method` (string): Algorithm used (e.g., "median_with_outlier_rejection")
  - `estimated_error_ms` (float): Estimated accuracy in milliseconds
  - `source_samples` (array): Individual timestamps from each NTP server
  - `warnings` (array): Any warnings about the time query
  - `system_time` (string): Local system time for comparison
  - `system_delta_ms` (float): Difference between system clock and NTP time
  - `query_duration_ms` (float): Time taken to query NTP servers
  - `latency_compensated` (bool): Whether latency compensation was applied

## Example Usage

**Input**: "What is the current UTC time?"

**Process**:
1. Call get_time_utc with default fast mode
2. Parse and format the response
3. Present time with accuracy information

**Output**:
```
Current UTC Time:
2025-11-28T01:23:45.123456+00:00

Accuracy:
- Sources: 4/4 NTP servers
- Estimated Error: ±12.5ms
- Query Duration: 42.8ms
- Consensus Method: median with outlier rejection

Note: System clock is 4.3 seconds ahead of NTP time
```

## Expected Response Format

```
Current UTC Time:
[ISO8601_TIMESTAMP]

Accuracy:
- Sources: [USED]/[TOTAL] NTP servers
- Estimated Error: ±[ERROR]ms
- Query Duration: [DURATION]ms
- Consensus Method: [METHOD]

[Optional warnings or notes about system clock drift]
```

## Error Handling

- No NTP servers available: Check internet connectivity
- Insufficient sources: Report which servers failed
- High error margin: Suggest using accurate mode or retrying
- Large system clock drift: Warn user about system time issues

## Use Cases

### 1. Trusted Timestamps for Logging
```
Get accurate UTC time for critical log entries where system clock may be unreliable.
Use: get_time_utc(mode="fast")
```

### 2. Detecting Clock Drift
```
Compare returned system_delta_ms to detect if system clock has drifted.
If delta > 1000ms, system clock may need correction.
```

### 3. High-Precision Operations
```
For financial or trading applications requiring <20ms accuracy.
Use: get_time_utc(mode="accurate")
Verify estimated_error_ms is acceptable before using timestamp.
```

### 4. Distributed System Coordination
```
Get consensus time independent of any single system's clock.
All services can query same NTP pool for consistent time.
```

## Notes

- Default fast mode is suitable for most applications (±10-50ms accuracy)
- Accurate mode provides better precision but takes longer
- Latency compensation ensures timestamp represents "now" when response is received
- Typical accuracy is much better than system clock drift (10-50 ppm)
- NTP servers used:
  - time.cloudflare.com (Cloudflare anycast NTP)
  - time.google.com (Google public NTP)
  - time.apple.com (Apple NTP servers)
  - pool.ntp.org servers (NTP Pool Project)
- All servers are stratum 1-2 for maximum accuracy
- System delta warnings indicate your computer's clock may need adjustment

## Performance Notes

- Fast mode: ~40-150ms typical response time
- Accurate mode: ~100-300ms typical response time
- Accuracy: ±10-50ms (much better than system clock drift)
- Not suitable for microsecond precision applications
- Respect NTP pool guidelines - don't query too frequently
