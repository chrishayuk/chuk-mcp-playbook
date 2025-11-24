# Playbook: Render Timeline

## Description
This playbook creates timeline diagrams showing events across time periods. Timelines are perfect for project history, roadmaps, historical events, and visualizing sequences of events organized by time periods.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Time periods or stages defined
- Events with titles and details for each period
- Chronological organization of events

## Steps

1. Define time periods
   - Break timeline into logical periods (quarters, phases, years)
   - Name each period clearly

2. Define events within each period
   - List events that occurred in each period
   - Provide event titles
   - Add details or items for each event

3. Call the render_timeline tool
   - Pass title and sections
   - Each section has a period and events

4. Review the generated diagram
   - Verify chronological order
   - Check that all events are represented

## MCP Tools Required

### mcp-mermaid-renderer

**Tool**: `render_timeline`
- **Parameters**:
  - `title` (string, required): Timeline title
  - `sections` (list of dict, required): Time period sections. Each dict should have:
    - `period`, `quarter`, `stage`, `name`, `section`, or `label` (string): Time period label
    - `events` (list of dict): List of events with:
      - `title` or `name` (string): Event title
      - `details`, `items`, or `description` (list or string): Event details (can be list or single string)
  - `format` (string): Output format - "svg" (default, recommended) or "png"
  - `theme` (string): Mermaid theme - "default", "dark", "forest", "neutral"
  - `bgcolor` (string): Background color (default: "transparent")
  - `filename` (string, optional): Suggested filename
- **Returns**: Artifact metadata with download URLs

## Example Usage

**Input**: "Create a timeline for product development roadmap"

**Process**:
1. Define quarters: Q1 2024, Q2 2024, Q3 2024, Q4 2024
2. List major features/events in each quarter
3. Add details for each event

**Tool Call**:
```json
{
  "title": "Product Development Roadmap 2024",
  "sections": [
    {
      "period": "Q1 2024",
      "events": [
        {
          "title": "User Authentication",
          "details": ["OAuth integration", "2FA support", "Social login"]
        },
        {
          "title": "Core Features",
          "details": ["Dashboard redesign", "Real-time notifications"]
        }
      ]
    },
    {
      "period": "Q2 2024",
      "events": [
        {
          "title": "Advanced Analytics",
          "details": ["Custom reports", "Data export", "Visualization tools"]
        },
        {
          "title": "Mobile App",
          "details": "iOS and Android beta release"
        }
      ]
    },
    {
      "period": "Q3 2024",
      "events": [
        {
          "title": "Integrations",
          "details": ["Slack integration", "API v2 release", "Webhooks"]
        }
      ]
    },
    {
      "period": "Q4 2024",
      "events": [
        {
          "title": "Enterprise Features",
          "details": ["SSO", "Advanced permissions", "Audit logs"]
        },
        {
          "title": "Performance",
          "details": "Infrastructure scaling and optimization"
        }
      ]
    }
  ],
  "format": "svg",
  "theme": "default"
}
```

**Output**:
```
Timeline rendered successfully!
- Format: SVG
- Periods: 4
- Total events: 8
- Download URL: [artifact link]
```

## Expected Response Format

The tool returns an artifact object with:
- `download_url`: URL to download the rendered diagram
- `source_code`: Editable Mermaid syntax
- `format`: Output format (svg or png)
- `diagram_type`: "timeline"

## Common Use Cases

1. **Product Roadmaps**: Feature releases, sprint planning, version milestones
2. **Project Timelines**: Project phases, deliverables, milestones
3. **Company History**: Company milestones, achievements, growth stages
4. **Historical Events**: Historical sequences, event chronology
5. **Release Planning**: Software releases, deployment schedules
6. **Personal Development**: Career progression, learning journey

## Best Practices

1. **Period Names**:
   - Use consistent format (Q1 2024, Q2 2024)
   - Or descriptive phases (Planning, Development, Launch)
2. **Event Titles**: Keep concise (2-5 words)
3. **Details Format**:
   - Can be a list: ["Item 1", "Item 2", "Item 3"]
   - Or single string: "Description text"
4. **Number of Periods**: 4-8 periods is ideal
5. **Events per Period**: 1-4 events per period
6. **Chronological Order**: Ensure sections are in time order
7. **Consistent Granularity**: Use same time scale throughout (all quarters, all months, all years)

## Error Handling

- **Missing Period**: All sections need a period label
- **Empty Events**: Each section should have at least one event
- **Missing Event Title**: All events need titles
- **Missing Details**: All events need details (at least one)

## Notes

- Sections represent time periods and should be in chronological order
- Events within a section can be in any order (all happen in that period)
- Details can be a single string or list of strings
- Single string is automatically converted to a list with one item
- Tool accepts flexible field names:
  - Period: period/quarter/stage/name/section/label
  - Event: title/name
  - Details: details/items/description
- Timeline flows left to right (or top to bottom depending on theme)
- Each period is visually separated
- Events are grouped under their respective periods
- For very long timelines (>10 periods), consider breaking into multiple diagrams
- Use for planning (future events) or history (past events)
- Recommended maximum: 8 periods with 3 events each
