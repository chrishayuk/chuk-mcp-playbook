# Playbook: Get Current Time via Telehack

## Description
This playbook retrieves the current date and time by connecting to telehack.com via telnet and executing the `date` command. This is an experimental approach to getting time information using a telnet-based service.

## Prerequisites
- Access to the telnet MCP server (chuk-mcp-telnet-client)
- Network connectivity to telehack.com (port 23)

## Steps

1. Connect to telehack.com
   - Establish telnet connection to telehack.com on port 23
   - Wait for connection to establish

2. Execute the date command
   - Send the "date" command to the telnet session
   - Wait for response from the server

3. Parse the response
   - Extract the date and time information from the telnet output
   - Handle any connection banners or extra output
   - Identify the actual date/time string in the response

4. Format the time information
   - Convert the telehack date format to a readable format
   - Include timezone information if available
   - Present in a clear, user-friendly format

5. Close the telnet session
   - Properly terminate the telnet connection
   - Clean up the session

## MCP Tools Required

### telnet (chuk-mcp-telnet-client)

**Tool 1**: `telnet_client`
- **Parameters**:
  - `host` (string): "telehack.com"
  - `port` (int): 23 (standard telnet port)
  - `commands` (list): ["date"] - Command to get current time
  - `session_id` (string, optional): For session management
  - `close_session` (bool, optional): Whether to close after execution
- **Returns**: Telnet session output including the date/time response

**Tool 2**: `close_telnet_session` (if session management needed)
- **Parameters**:
  - `session_id` (string): Session identifier from telnet_client
- **Returns**: Confirmation of session closure

## Example Usage

**Input**: "What is the current time?"

**Process**:
1. Call `telnet_client(host="telehack.com", port=23, commands=["date"])`
2. Parse the response to extract date/time
3. Format and present to user

**Output**:
```
Current Time (via Telehack):

Date: Sunday, November 24, 2025
Time: 14:23:45 UTC

Note: Time retrieved from telehack.com telnet service
```

## Expected Response Format

```
Current Time (via Telehack):

Date: [DAY], [MONTH] [DATE], [YEAR]
Time: [HH:MM:SS] [TIMEZONE]

Note: Time retrieved from telehack.com telnet service
```

## Error Handling

- Connection failed: Inform user that telehack.com is unreachable
- Timeout: Suggest retry or inform about service availability
- Invalid response: Report that date command did not return expected format
- Parse error: Show raw output and explain parsing failed

## Notes

- Telehack.com is a retro computing simulation and may have variable response times
- The `date` command on telehack returns the current date/time
- Response may include ANSI escape codes or terminal formatting
- This is an experimental approach - in production, use dedicated time APIs
- Connection banner and other output should be filtered out to find the actual date/time
- Telehack typically returns time in UTC
- Session management can be used for multiple commands, but single command is sufficient for time

## Parsing Tips

- Look for lines containing recognizable date patterns (day names, month names)
- Filter out connection banners (usually first few lines)
- Date format from telehack typically includes: day of week, month, date, time, year
- May need to strip ANSI codes or terminal control characters
- The actual date line usually contains multiple space-separated components

## Alternative Approaches

If telehack is unavailable or unreliable:
- Use system time (if available via other MCP tools)
- Use weather API's timestamp data
- Use dedicated time/NTP services
- Note: This playbook is primarily for demonstration of creative tool usage
