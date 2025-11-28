# Playbook: Check System Clock Drift

## Description
This playbook compares your system clock against trusted NTP sources to detect clock drift, skew, or synchronization issues. Essential for troubleshooting time-sensitive applications.

## Prerequisites
- Access to the chuk-mcp-time server
- Internet connectivity to reach NTP servers
- System experiencing potential time issues

## Steps

1. Choose accuracy mode for comparison
   - Fast mode: Quick check with 4 NTP servers
   - Accurate mode: Thorough check with 7 NTP servers

2. Run system clock comparison
   - Call the compare API with desired mode
   - Let it query NTP servers and compare to system time

3. Parse the comparison results
   - Extract system time and trusted NTP time
   - Calculate time delta (difference)
   - Check estimated error margin
   - Determine status (ok, drift, error)

4. Interpret the status
   - OK: Delta < 100ms (system clock is accurate)
   - Drift: Delta 100-1000ms (clock drifting, may need attention)
   - Error: Delta > 1000ms (significant issue, needs correction)

5. Report findings and recommendations

## MCP Tools Required

### chuk-mcp-time

**Tool**: `compare_system_clock`
- **Parameters**:
  - `mode` (string, optional): "fast" (default) or "accurate"
    - "fast": Queries 4 NTP servers for quick check
    - "accurate": Queries 7 NTP servers for thorough validation
- **Returns**:
  - `system_time` (string): Current system clock time
  - `trusted_time` (string): NTP consensus time
  - `delta_ms` (float): Difference in milliseconds (positive = system ahead)
  - `estimated_error_ms` (float): Accuracy margin of NTP consensus
  - `status` (string): "ok", "drift", or "error"
  - `sources_used` (int): Number of NTP servers used
  - `total_sources` (int): Total NTP servers attempted

## Example Usage

**Input**: "Is my system clock accurate?"

**Process**:
1. Call compare_system_clock with fast mode
2. Parse the response
3. Interpret status and delta

**Output (OK status):**
```
System Clock Health Check:

Status: ✅ OK - System clock is accurate

System Time:    2025-11-28T10:23:49.456789+00:00
Trusted Time:   2025-11-28T10:23:45.123456+00:00
Delta:          +2.4ms (system is 2.4ms ahead)
Estimated Error: ±12.5ms

Sources: 4/4 NTP servers responded
Conclusion: Your system clock is well synchronized.
```

**Output (Drift status):**
```
System Clock Health Check:

Status: ⚠️  DRIFT - Clock is drifting

System Time:    2025-11-28T10:23:45.123456+00:00
Trusted Time:   2025-11-28T10:23:44.500000+00:00
Delta:          +623.5ms (system is 623.5ms ahead)
Estimated Error: ±15.2ms

Sources: 4/4 NTP servers responded
Recommendation: Your clock is drifting. Consider enabling NTP synchronization.
```

**Output (Error status):**
```
System Clock Health Check:

Status: ❌ ERROR - Significant clock drift detected

System Time:    2025-11-28T10:23:49.456789+00:00
Trusted Time:   2025-11-28T10:23:45.123456+00:00
Delta:          +4333.3ms (system is 4.3 seconds ahead)
Estimated Error: ±12.5ms

Sources: 4/4 NTP servers responded
Recommendation: Your system clock has significant drift. Please synchronize your clock immediately.

To fix on macOS/Linux:
  sudo ntpdate -u time.cloudflare.com

To fix on Windows:
  w32tm /resync
```

## Expected Response Format

```
System Clock Health Check:

Status: [STATUS_ICON] [STATUS_MESSAGE]

System Time:    [SYSTEM_TIME]
Trusted Time:   [NTP_TIME]
Delta:          [DELTA]ms ([DIRECTION])
Estimated Error: ±[ERROR]ms

Sources: [USED]/[TOTAL] NTP servers responded
[Recommendation or conclusion]
```

## Status Interpretation

### ✅ OK (delta < 100ms)
- System clock is accurate
- No action required
- Normal clock drift variation

### ⚠️ DRIFT (delta 100-1000ms)
- Clock is drifting beyond normal range
- May cause issues with time-sensitive applications
- Consider enabling NTP synchronization
- Monitor for further drift

### ❌ ERROR (delta > 1000ms)
- Significant clock synchronization issue
- Will cause problems with:
  - SSL/TLS certificate validation
  - Distributed systems
  - Time-based authentication
  - Log correlation
- Immediate action required

## Common Causes of Clock Drift

1. **Virtual Machines**
   - VMs can experience severe time drift
   - Enable VM guest tools time synchronization
   - Configure NTP in the guest OS

2. **Hibernation/Sleep**
   - Clock may drift when system resumes
   - System usually resynchronizes automatically
   - May take a few minutes

3. **No NTP Configuration**
   - System clock naturally drifts (10-50 ppm)
   - Enable NTP daemon (ntpd, chrony, or systemd-timesyncd)

4. **Bad Hardware Clock**
   - CMOS battery failure
   - Defective motherboard clock
   - May require hardware replacement

5. **Timezone Issues**
   - Wrong timezone configuration
   - Daylight saving time not applied
   - Check system timezone settings

## Fixing Clock Drift

### macOS
```bash
# One-time sync
sudo sntp -sS time.apple.com

# Enable automatic time sync in System Preferences
# System Preferences > Date & Time > Set date and time automatically
```

### Linux (systemd)
```bash
# Check status
timedatectl status

# Enable NTP
sudo timedatectl set-ntp true

# One-time sync
sudo ntpdate -u time.cloudflare.com
```

### Linux (chrony)
```bash
# Force sync
sudo chronyc -a makestep

# Check sources
chronyc sources
```

### Windows
```bash
# Resync clock
w32tm /resync

# Check status
w32tm /query /status

# Configure NTP server
w32tm /config /manualpeerlist:"time.cloudflare.com" /syncfromflags:manual /update
```

## Use Cases

### 1. Troubleshooting SSL/TLS Errors
```
"Why am I getting certificate validation errors?"
Clock drift can cause certificates to appear expired or not yet valid.
Run: compare_system_clock() to check for time issues.
```

### 2. Distributed System Debugging
```
"Events in my logs are out of order across servers."
Clock skew between servers causes log correlation issues.
Run: compare_system_clock(mode="accurate") on each server.
```

### 3. Monitoring Server Health
```
"Regular health check for production servers."
Add to monitoring to detect clock drift before it causes issues.
Run: compare_system_clock() periodically.
```

### 4. Development Environment Setup
```
"Setting up new dev machine or VM."
Verify clock is properly synchronized before development.
Run: compare_system_clock() to validate.
```

### 5. After System Resume
```
"Laptop was in sleep mode for several days."
Check if clock synchronized properly after resume.
Run: compare_system_clock() to verify.
```

## Notes

- Run accurate mode for critical systems or detailed diagnostics
- Fast mode sufficient for quick health checks
- Positive delta means system clock is ahead
- Negative delta means system clock is behind
- VMs and containers often have worse clock accuracy
- Docker containers inherit host clock issues
- Cloud instances (AWS, GCP, Azure) usually have NTP configured
- Check NTP configuration if consistently seeing drift status
- Some applications require <1ms accuracy (trading, telecom) - may need GPS or PTP
