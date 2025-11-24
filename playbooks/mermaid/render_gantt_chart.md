# Playbook: Render Gantt Chart

## Description
This playbook creates Gantt charts for project planning with tasks, milestones, and dependencies. Gantt charts visualize project timelines, showing task durations, dependencies, and progress status over time.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Project timeline with tasks and dates
- Understanding of task dependencies
- Task statuses (done, active, pending, critical)

## Steps

1. Define project sections
   - Group related tasks into logical sections
   - Name each section clearly (Planning, Development, Launch, etc.)

2. Define tasks within sections
   - Assign unique IDs to tasks that have dependencies
   - Set task names (keep under 40 chars)
   - Define start dates and durations
   - Set task status (done, active, crit, milestone)
   - Map dependencies using task IDs

3. Configure chart settings
   - Set date format (YYYY-MM-DD recommended)
   - Define excluded days (weekends, holidays)

4. Call the render_gantt_chart tool
   - Pass title, sections, and tasks
   - Use dependencies for sequential task chains

5. Review the generated diagram
   - Verify timeline is accurate
   - Check that dependencies are correct

## MCP Tools Required

### mcp-mermaid-renderer

**Tool**: `render_gantt_chart`
- **Parameters**:
  - `title` (string, required): Chart title
  - `sections` (list of dict, required): Sections grouping related tasks. Each dict should have:
    - `name`, `title`, or `section` (string): Section name
    - `tasks` (list of dict): List of tasks with:
      - `name`, `title`, or `task` (string): Task name (keep under 40 chars)
      - `id` (string, optional): Unique task identifier (required if other tasks depend on this)
      - `status` (string, optional): "active", "done", "crit", or "milestone"
      - `start_date`, `start`, or `startDate` (string, optional): Task start date (YYYY-MM-DD)
      - `end_date`, `end`, or `endDate` (string, optional): Task end date (YYYY-MM-DD)
      - `duration` (string, optional): Task duration (e.g., "2d", "1w", "3d")
      - `dependencies` (list of strings, optional): List of task IDs this task depends on
  - `date_format` (string): Date format for input dates (default: "YYYY-MM-DD")
  - `exclude_days` (list of strings, optional): Days to exclude (e.g., ["saturday", "sunday"])
  - `format` (string): Output format - "svg" (default, recommended) or "png"
  - `theme` (string): Mermaid theme - "default", "dark", "forest", "neutral"
  - `bgcolor` (string): Background color (default: "transparent")
  - `filename` (string, optional): Suggested filename
- **Returns**: Artifact metadata with download URLs

## Example Usage

**Input**: "Create a Gantt chart for a product launch timeline"

**Process**:
1. Break project into sections: Planning, Development, Launch
2. Define tasks with durations and dependencies
3. Mark completed tasks and critical milestones

**Tool Call**:
```json
{
  "title": "Product Launch Timeline",
  "sections": [
    {
      "name": "Planning",
      "tasks": [
        {"name": "Requirements gathering", "id": "req", "status": "done", "start": "2024-01-01", "duration": "2w"},
        {"name": "Design mockups", "id": "design", "status": "done", "duration": "1w", "dependencies": ["req"]}
      ]
    },
    {
      "name": "Development",
      "tasks": [
        {"name": "Backend API", "id": "backend", "status": "active", "duration": "4w", "dependencies": ["design"]},
        {"name": "Frontend UI", "id": "frontend", "status": "active", "duration": "3w", "dependencies": ["design"]},
        {"name": "Integration testing", "id": "test", "status": "crit", "duration": "1w", "dependencies": ["backend", "frontend"]}
      ]
    },
    {
      "name": "Launch",
      "tasks": [
        {"name": "Production deployment", "status": "milestone", "duration": "1d", "dependencies": ["test"]}
      ]
    }
  ],
  "date_format": "YYYY-MM-DD",
  "exclude_days": ["saturday", "sunday"],
  "format": "svg",
  "theme": "default"
}
```

**Output**:
```
Gantt chart rendered successfully!
- Format: SVG
- Sections: 3
- Total tasks: 7
- Download URL: [artifact link]
```

## Expected Response Format

The tool returns an artifact object with:
- `download_url`: URL to download the rendered diagram
- `source_code`: Editable Mermaid syntax
- `format`: Output format (svg or png)
- `diagram_type`: "gantt"

## Common Use Cases

1. **Software Projects**: Sprint planning, release timelines, feature development
2. **Product Launches**: Marketing campaigns, launch schedules
3. **Infrastructure Projects**: Migration plans, deployment schedules
4. **Event Planning**: Conference organization, wedding planning
5. **Research Projects**: Study timelines, publication schedules
6. **Business Projects**: Quarterly initiatives, annual planning

## Best Practices

1. **Task Names**: Keep under 40 characters to avoid text overlap
2. **Dependencies**: Use task IDs and dependencies field for sequential tasks
   - Preferred: `"dependencies": ["setup"]` over explicit start dates
   - Tasks automatically start after dependencies complete
3. **Task Status**:
   - "done" - completed tasks (shown in one color)
   - "active" - in-progress tasks (shown in another color)
   - "crit" - critical path tasks (highlighted)
   - "milestone" - key milestones (shown as diamonds)
4. **Duration Format**: Use "Xd" for days, "Xw" for weeks (e.g., "2d", "3w")
5. **Excluded Days**: Add weekends or holidays to accurately calculate working days
6. **Sections**: Group related tasks (max 4-6 sections for clarity)
7. **Timeline**: Keep total project duration reasonable for visualization (3-6 months ideal)

## Error Handling

- **Missing Task IDs**: If using dependencies, ensure dependent tasks have IDs
- **Invalid Dependencies**: Referenced task IDs must exist
- **Date Format Mismatch**: Ensure dates match the specified date_format
- **Overlapping Names**: Long task names may overlap - keep names concise
- **Invalid Duration**: Use format like "2d", "1w", not "2 days"
- **Invalid Status**: Use only: "active", "done", "crit", "milestone"

## Notes

- Task IDs are only required if other tasks depend on them
- Dependencies create automatic sequencing - task starts after dependency completes
- When using dependencies, specify duration instead of start_date/end_date
- Multiple dependencies: task starts after the first dependency completes
- Excluded days are not counted in duration calculations
- Flexible field names supported: name/title/task, start/start_date, dependencies/after
- Milestones are shown as single-day events
- Critical tasks are visually highlighted on the chart
- Maximum recommended tasks: 15-20 per chart for readability
- For longer projects, consider creating multiple charts for different phases
