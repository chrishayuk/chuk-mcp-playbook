# Playbook: Render State Diagram

## Description
This playbook creates state diagrams showing states and transitions. State diagrams are perfect for visualizing workflows, lifecycles, finite state machines (FSM), and any system that transitions between different states based on events.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Understanding of all possible states
- Knowledge of transitions and triggering events
- Clear state machine logic

## Steps

1. Identify all states
   - List all possible states in the system
   - Include start state ([*]) and end state ([*])
   - Name states clearly and concisely

2. Map transitions
   - Document all possible transitions between states
   - Identify triggering events or conditions
   - Map from/to state pairs

3. Add optional notes
   - Document important state details
   - Add timing or condition information

4. Call the render_state_diagram tool
   - Pass states list (use "[*]" for start/end)
   - Pass transitions with from, to, and label
   - Set layout direction

5. Review the generated diagram
   - Verify all states and transitions
   - Check that the state machine logic is correct

## MCP Tools Required

### mcp-mermaid-renderer

**Tool**: `render_state_diagram`
- **Parameters**:
  - `states` (list of strings, required): List of state names. Use "[*]" for start/end states
  - `transitions` (list of dict, required): List of transitions. Each dict should have:
    - `from` or `from_state` (string): Source state
    - `to` or `to_state` (string): Target state
    - `label` (string, optional): Transition trigger/condition
  - `notes` (list of dict, optional): Optional notes. Each dict should have:
    - `state` (string): State to attach to
    - `position` (string): "left of" or "right of"
    - `text` (string): Note content
  - `title` (string, optional): Diagram title
  - `direction` (string): Layout direction - "TB", "BT", "LR", "RL" (default: "TB")
  - `format` (string): Output format - "svg" (default, recommended) or "png"
  - `theme` (string): Mermaid theme - "default", "dark", "forest", "neutral"
  - `bgcolor` (string): Background color (default: "transparent")
  - `filename` (string, optional): Suggested filename
- **Returns**: Artifact metadata with download URLs

## Example Usage

**Input**: "Create a state diagram for an order processing system"

**Process**:
1. Identify states: Pending, Processing, Shipped, Delivered, Cancelled
2. Map transitions with triggering events
3. Add start and end states

**Tool Call**:
```json
{
  "states": ["[*]", "Pending", "Processing", "Shipped", "Delivered", "Cancelled", "[*]"],
  "transitions": [
    {"from": "[*]", "to": "Pending"},
    {"from": "Pending", "to": "Processing", "label": "payment confirmed"},
    {"from": "Pending", "to": "Cancelled", "label": "payment failed"},
    {"from": "Processing", "to": "Shipped", "label": "items packed"},
    {"from": "Processing", "to": "Cancelled", "label": "out of stock"},
    {"from": "Shipped", "to": "Delivered", "label": "delivery confirmed"},
    {"from": "Delivered", "to": "[*]"},
    {"from": "Cancelled", "to": "[*]"}
  ],
  "notes": [
    {"state": "Processing", "position": "right of", "text": "Typically takes 1-2 business days"}
  ],
  "title": "Order Processing States",
  "direction": "LR",
  "format": "svg",
  "theme": "default"
}
```

**Output**:
```
State diagram rendered successfully!
- Format: SVG
- States: 7
- Transitions: 8
- Download URL: [artifact link]
```

## Expected Response Format

The tool returns an artifact object with:
- `download_url`: URL to download the rendered diagram
- `source_code`: Editable Mermaid syntax
- `format`: Output format (svg or png)
- `diagram_type`: "state"

## Common Use Cases

1. **Order Workflows**: E-commerce order states, fulfillment processes
2. **User Workflows**: Registration flows, account states, onboarding
3. **Document Lifecycle**: Draft, review, approved, published, archived
4. **Connection States**: TCP connections, WebSocket states
5. **Game States**: Menu, playing, paused, game over
6. **IoT Device States**: Idle, active, sleeping, offline
7. **Approval Workflows**: Submitted, under review, approved, rejected

## Best Practices

1. **State Names**: Use clear, descriptive names (nouns or adjectives)
   - Good: "Processing", "Approved", "Active"
   - Avoid: "Process", "Approve", "Activate" (verbs are for transitions)
2. **Transition Labels**: Use verbs or events (what triggers the transition)
   - Good: "submit", "payment confirmed", "timeout"
   - Avoid: "goes to", "moves to"
3. **Start/End States**: Always use "[*]" for initial and final states
4. **Direction**:
   - LR (left-right) for workflow-style processes
   - TB (top-bottom) for hierarchical states
5. **Notes**: Add notes for timing, conditions, or important business rules
6. **Complexity**: Keep to 6-10 states for clarity
7. **Error States**: Include error/cancelled states where applicable

## Error Handling

- **Invalid State Names**: All transition references must match defined states
- **Missing [*]**: If using start/end states, include "[*]" in states list
- **Invalid Direction**: Use only TB, BT, LR, or RL
- **Invalid Note Position**: Must be "left of" or "right of"
- **Unreachable States**: Ensure all states have transitions (or are terminal)

## Notes

- State names are case-sensitive
- "[*]" represents both start and end states (context-dependent)
- Multiple transitions from same state are allowed
- Self-loops (state to itself) are supported
- Tool accepts flexible field names: from/from_state, to/to_state, label/trigger/event
- Notes are positioned relative to states
- Direction affects layout but not logic
- For complex state machines (>10 states), consider creating hierarchical diagrams
- Recommended maximum: 8-10 states per diagram for readability
- For systems with many states, group related states into composite states
