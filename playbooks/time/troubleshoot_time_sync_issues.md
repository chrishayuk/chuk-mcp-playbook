# Scenario Playbook: Troubleshoot Time Synchronization Issues

## Description
This scenario demonstrates how to diagnose and resolve time synchronization problems that can cause SSL/TLS errors, authentication failures, log correlation issues, and distributed system problems.

## Scenario
Your application is experiencing mysterious errors. SSL certificates are failing validation, distributed transactions are out of order, and logs across multiple servers don't correlate properly. These are classic symptoms of time synchronization issues.

## Prerequisites
- Access to the chuk-mcp-time server
- System experiencing time-related issues
- Admin access to affected systems (for fixes)

## Common Symptoms of Time Sync Issues

### 1. SSL/TLS Certificate Errors
```
Error: "Certificate is not yet valid"
Error: "Certificate has expired"
Cause: System clock is ahead or behind actual time
```

### 2. Authentication Failures
```
Error: "Token expired"
Error: "Replay attack detected"
Error: "Timestamp out of acceptable range"
Cause: Clock skew between client and server
```

### 3. Distributed System Issues
```
Error: "Transaction timestamps out of order"
Error: "Cannot determine event sequence"
Error: "Replica sync conflicts"
Cause: Different clocks across cluster nodes
```

### 4. Log Correlation Problems
```
Issue: Events appear in wrong order
Issue: Cannot correlate events across services
Issue: Timeline doesn't make sense
Cause: Inconsistent clocks across services
```

### 5. Database Replication Issues
```
Error: "Replica lag negative"
Error: "Future timestamp in replication stream"
Cause: Source and replica have different times
```

## Diagnostic Steps

### Step 1: Check System Clock Status

First, verify if there's actually a time synchronization problem:

```
Tool: compare_system_clock
Parameters:
  mode: "accurate"  # Use accurate mode for thorough diagnosis

Expected: status = "ok", delta_ms < 100
Problem: status = "error" or "drift", delta_ms > 100
```

**Example Output (Problem Detected):**
```
Status: ❌ ERROR - Significant clock drift

System Time:    2025-11-28T10:28:45.123456+00:00
Trusted Time:   2025-11-28T10:23:45.123456+00:00
Delta:          +5000.0ms (system is 5 seconds ahead)
Estimated Error: ±12.5ms

Sources: 7/7 NTP servers responded
```

### Step 2: Determine Drift Direction

Analyze the delta to understand the problem:

- **Positive Delta**: System clock is ahead (fast)
  - Impacts: Certificates appear "not yet valid", future timestamps

- **Negative Delta**: System clock is behind (slow)
  - Impacts: Certificates appear "expired", stale timestamps

**Interpretation:**
```
Delta < 100ms:     Normal variation, no action needed
Delta 100-1000ms:  Clock drift, should sync
Delta > 1000ms:    Serious issue, immediate sync required
Delta > 60000ms:   Critical issue (>1 minute), investigate root cause
```

### Step 3: Check for Systemic Issues

If multiple systems are involved, check each one:

```
For each server/container:
  1. compare_system_clock(mode="accurate")
  2. Record delta_ms
  3. Note status

Create matrix:
Server A: +5000ms (ERROR)
Server B: -150ms  (DRIFT)
Server C: +25ms   (OK)
Server D: +4800ms (ERROR)
```

**Pattern Analysis:**
- All servers off by similar amount → Upstream NTP issue
- Random drift patterns → Individual system issues
- VMs all drifting → Hypervisor time sync problem
- Containers drifting → Host clock issue

### Step 4: Identify Root Cause

Common root causes by environment:

#### Virtual Machines
```
Symptom: Severe drift after suspend/resume
Cause: VM tools not configured properly
Check: VMware Tools, Hyper-V Integration, VirtualBox Guest Additions
```

#### Containers (Docker/Kubernetes)
```
Symptom: Container time doesn't match host
Cause: Containers inherit host clock
Check: Host time sync configuration
```

#### Cloud Instances
```
Symptom: Clock drift on cloud VMs
Cause: NTP not configured or firewall blocking
Check: NTP service status, security groups
```

#### Physical Servers
```
Symptom: Gradual drift over days/weeks
Cause: No NTP configured or CMOS battery failure
Check: NTP daemon status, hardware clock
```

## Resolution Steps

### Resolution 1: One-Time Sync

For immediate fix:

#### macOS
```bash
# Check current time sync status
Tool: compare_system_clock(mode="fast")

# If drift detected, sync immediately:
sudo sntp -sS time.apple.com

# Verify fix
Tool: compare_system_clock(mode="fast")
Expected: delta_ms < 100
```

#### Linux (systemd-timesyncd)
```bash
# Check status
Tool: compare_system_clock(mode="accurate")

# If drift detected:
sudo systemctl restart systemd-timesyncd
timedatectl set-ntp true

# Force immediate sync
sudo timedatectl set-ntp false
sudo timedatectl set-ntp true

# Verify
Tool: compare_system_clock(mode="fast")
```

#### Linux (chrony)
```bash
# Check drift
Tool: compare_system_clock(mode="accurate")

# Force immediate sync
sudo chronyc -a makestep

# Verify
chronyc tracking
Tool: compare_system_clock(mode="fast")
```

#### Linux (ntpd - legacy)
```bash
# Check drift
Tool: compare_system_clock(mode="accurate")

# Immediate sync (stops ntpd, syncs, restarts)
sudo systemctl stop ntp
sudo ntpdate -u time.cloudflare.com
sudo systemctl start ntp

# Verify
Tool: compare_system_clock(mode="fast")
```

#### Windows
```bash
# Check drift
Tool: compare_system_clock(mode="accurate")

# Force resync
w32tm /resync /force

# If that doesn't work, reconfigure
net stop w32time
w32tm /unregister
w32tm /register
net start w32time
w32tm /resync

# Verify
w32tm /query /status
Tool: compare_system_clock(mode="fast")
```

### Resolution 2: Permanent Fix

Enable automatic time synchronization:

#### macOS
```bash
# Enable via GUI:
System Preferences > Date & Time > Set date and time automatically

# Or via command line (requires admin):
sudo systemsetup -setusingnetworktime on
sudo systemsetup -setnetworktimeserver time.apple.com
```

#### Linux (systemd)
```bash
# Enable NTP
sudo timedatectl set-ntp true

# Verify configuration
timedatectl status

# Check sync status periodically
Tool: compare_system_clock(mode="fast")
```

#### Linux (chrony)
```bash
# Ensure chrony is installed and enabled
sudo systemctl enable chronyd
sudo systemctl start chronyd

# Configure servers in /etc/chrony/chrony.conf
server time.cloudflare.com iburst
server time.google.com iburst
server time.apple.com iburst

# Restart
sudo systemctl restart chronyd

# Verify
chronyc sources
Tool: compare_system_clock(mode="fast")
```

#### Docker Containers
```bash
# Containers inherit host time
# Fix the host clock first

# Check host
Tool: compare_system_clock(mode="accurate")

# Fix host time sync (see above)

# Restart containers if needed
docker restart <container>

# Verify container time matches host
docker exec <container> date
```

#### Kubernetes Pods
```yaml
# Pods inherit node time
# Fix node time sync (see Linux steps above)

# For critical workloads, monitor via sidecar:
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: app
    ...
  - name: time-monitor
    image: alpine
    command:
    - sh
    - -c
    - "while true; do date; sleep 60; done"
```

### Resolution 3: VM-Specific Fixes

#### VMware
```bash
# Disable VM time sync (let OS handle it)
vmware-toolbox-cmd timesync disable

# Or in .vmx file:
tools.syncTime = "FALSE"
time.synchronize.continue = "FALSE"
time.synchronize.restore = "FALSE"
time.synchronize.resume.disk = "FALSE"
time.synchronize.shrink = "FALSE"

# Configure NTP in guest OS instead
# Verify
Tool: compare_system_clock(mode="accurate")
```

#### Hyper-V
```powershell
# Disable time sync integration
Disable-VMIntegrationService -VMName "YourVM" -Name "Time Synchronization"

# Configure NTP in guest OS
# Verify
Tool: compare_system_clock(mode="accurate")
```

#### VirtualBox
```bash
# Disable host time sync
VBoxManage setextradata "YourVM" "VBoxInternal/Devices/VMMDev/0/Config/GetHostTimeDisabled" 1

# Configure NTP in guest OS
# Verify
Tool: compare_system_clock(mode="accurate")
```

## Verification Workflow

After applying fixes, verify systematically:

```
Step 1: Immediate verification
  Tool: compare_system_clock(mode="fast")
  Expected: delta_ms < 100, status = "ok"

Step 2: Wait 5 minutes, check stability
  Tool: compare_system_clock(mode="fast")
  Expected: delta_ms still < 100

Step 3: Test application
  - Verify SSL/TLS errors resolved
  - Check authentication working
  - Confirm logs correlating properly

Step 4: Monitor over 24 hours
  - Check drift hasn't returned
  - Periodically run compare_system_clock
  - Set up monitoring alerts
```

## MCP Tools Required

### chuk-mcp-time

**Primary Tool**: `compare_system_clock`
- Use at every step to verify time accuracy
- Start with accurate mode for diagnosis
- Use fast mode for ongoing verification

**Diagnostic Flow**:
```
1. Initial diagnosis:
   compare_system_clock(mode="accurate")

2. If ERROR/DRIFT detected:
   - Note delta_ms and direction
   - Apply appropriate fix for OS/environment

3. Immediate verification:
   compare_system_clock(mode="fast")
   - Should show delta_ms < 100

4. Stability check (5 min later):
   compare_system_clock(mode="fast")
   - Verify drift hasn't returned

5. Ongoing monitoring:
   compare_system_clock(mode="fast") daily
   - Alert if delta_ms > 100
```

## Example Troubleshooting Session

```
🔍 Time Synchronization Troubleshooting Session

Initial Diagnosis:
Tool: compare_system_clock(mode="accurate")

Result:
❌ ERROR - Significant clock drift detected
System Time:    2025-11-28T10:28:45.123456+00:00
Trusted Time:   2025-11-28T10:23:45.123456+00:00
Delta:          +5000.0ms (5 seconds ahead)
Sources:        7/7 NTP servers

Analysis:
- System clock is 5 seconds fast
- May cause "certificate not yet valid" errors
- Needs immediate correction

Environment Check:
- OS: Ubuntu 22.04 LTS
- Virtualization: Docker container
- Host: AWS EC2 t3.medium

Root Cause:
- Container inherits host clock
- Host NTP not configured properly

Fix Applied:
1. On EC2 host:
   sudo systemctl restart systemd-timesyncd
   sudo timedatectl set-ntp true

2. Restart container:
   docker restart app-container

Verification:
Tool: compare_system_clock(mode="fast")

Result:
✅ OK - System clock is accurate
System Time:    2025-11-28T10:23:47.456789+00:00
Trusted Time:   2025-11-28T10:23:45.123456+00:00
Delta:          +2.3ms
Sources:        4/4 NTP servers

Success! Clock now synchronized within normal tolerance.

Next Steps:
- Monitor for 24 hours to ensure stability
- Set up monitoring alert if delta > 100ms
- Document in runbook for future reference
```

## Monitoring and Prevention

### Set Up Ongoing Monitoring

```python
# Pseudo-code for monitoring script
def monitor_clock_drift():
    result = compare_system_clock(mode="fast")

    if result.status == "error":
        alert("Critical: Clock drift > 1 second", severity="critical")
    elif result.status == "drift":
        alert("Warning: Clock drift detected", severity="warning")

    log_metric("clock_drift_ms", result.delta_ms)

# Run every 5 minutes
```

### Prevention Best Practices

1. **Always Configure NTP**
   - Every server should have NTP enabled
   - Use multiple reliable NTP sources
   - Prefer regional NTP pools

2. **Monitor Proactively**
   - Check clock drift before issues occur
   - Alert on drift > 100ms
   - Track drift trends over time

3. **Document Your Configuration**
   - Record NTP servers used
   - Document VM time sync settings
   - Note any special configurations

4. **Test After Changes**
   - Verify time after system updates
   - Check after VM migrations
   - Confirm after network changes

## Notes

- Clock drift is cumulative - small drift becomes large over time
- VMs are especially prone to drift
- Containers always inherit host clock
- Some applications cache time (restart after sync)
- SSL/TLS issues often manifest before other problems
- Distributed systems are especially sensitive to clock skew
- Financial and legal applications may require sub-millisecond accuracy
- Consider hardware solutions (GPS, PTP) for critical systems requiring microsecond precision
