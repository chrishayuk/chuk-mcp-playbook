# Playbook: Visualize Project Timeline

## Description
This playbook guides you through visualizing project timelines with tasks, milestones, dependencies, and resource allocation. Perfect for project planning, tracking progress, communicating schedules to stakeholders, and managing dependencies.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- List of project tasks and their durations
- Understanding of task dependencies
- Knowledge of milestones and deadlines

## Steps

1. **Identify all tasks**
   - List all project tasks
   - Note task durations
   - Identify dependencies
   - Mark milestones

2. **Organize timeline**
   - Group tasks by phase or workstream
   - Note start and end dates
   - Identify critical path
   - Document resource assignments

3. **Choose diagram type**
   - Use **gantt_chart** for detailed project schedules
   - Use **timeline** for high-level milestones

4. **Create visualization**
   - Show all tasks with durations
   - Mark dependencies
   - Highlight critical path
   - Include milestones

## MCP Tools Required

### Primary Tool: render_gantt_chart
Best for detailed project schedules with tasks, dependencies, and progress tracking.

See [render_gantt_chart.md](./render_gantt_chart.md) for full details.

### Secondary Tool: render_timeline
Best for high-level milestone visualization and roadmap communication.

See [render_timeline.md](./render_timeline.md) for full details.

## Recommended Diagram Type

### Primary: Gantt Chart
**When to use**: Detailed project planning, task tracking, resource management

**Strengths**:
- Shows task durations clearly
- Represents dependencies
- Tracks progress
- Identifies critical path

## Example Usage

### Scenario: Software Development Project

**User Request**: "Create a timeline for our Q1 2024 software development project showing all phases from requirements to launch"

```json
{
  "title": "Software Development Project - Q1 2024",
  "dateFormat": "YYYY-MM-DD",
  "sections": [
    {
      "name": "Planning Phase",
      "tasks": [
        {"id": "req", "name": "Requirements Gathering", "start": "2024-01-02", "duration": "2w"},
        {"id": "design", "name": "Technical Design", "start": "2024-01-16", "duration": "2w", "dependencies": ["req"]},
        {"id": "arch_review", "name": "Architecture Review", "start": "2024-01-30", "duration": "3d", "dependencies": ["design"], "milestone": true}
      ]
    },
    {
      "name": "Development Phase",
      "tasks": [
        {"id": "setup", "name": "Environment Setup", "start": "2024-02-02", "duration": "1w", "dependencies": ["arch_review"]},
        {"id": "backend", "name": "Backend Development", "start": "2024-02-09", "duration": "6w", "dependencies": ["setup"]},
        {"id": "frontend", "name": "Frontend Development", "start": "2024-02-09", "duration": "6w", "dependencies": ["setup"]},
        {"id": "api_integration", "name": "API Integration", "start": "2024-03-22", "duration": "2w", "dependencies": ["backend", "frontend"]}
      ]
    },
    {
      "name": "Testing Phase",
      "tasks": [
        {"id": "unit_tests", "name": "Unit Testing", "start": "2024-04-05", "duration": "1w", "dependencies": ["api_integration"]},
        {"id": "integration_tests", "name": "Integration Testing", "start": "2024-04-12", "duration": "2w", "dependencies": ["unit_tests"]},
        {"id": "uat", "name": "User Acceptance Testing", "start": "2024-04-26", "duration": "2w", "dependencies": ["integration_tests"]},
        {"id": "launch", "name": "Production Launch", "start": "2024-05-10", "duration": "1d", "dependencies": ["uat"], "milestone": true}
      ]
    }
  ],
  "format": "svg",
  "theme": "default"
}
```

## Best Practices

1. **Break down large tasks** - Keep tasks to 1-2 week durations
2. **Identify dependencies** - Show which tasks block others
3. **Mark milestones** - Highlight key decision points
4. **Show critical path** - Identify tasks that affect end date
5. **Track progress** - Update completion percentages regularly
6. **Include buffer time** - Add contingency for risks
7. **Group related tasks** - Use sections for phases or teams

## Common Variations

- Sprint planning timelines
- Release roadmaps
- Migration project schedules
- Event planning timelines
- Construction/build schedules

## Related Playbooks

- [render_gantt_chart.md](./render_gantt_chart.md)
- [render_timeline.md](./render_timeline.md)
- [render_sprint_schedule.md](./render_sprint_schedule.md)
- [render_release_roadmap.md](./render_release_roadmap.md)

## Notes

- Update Gantt charts as project progresses
- Use colors to indicate task status (not started, in progress, completed, delayed)
- Export in SVG for project documentation
- Share with stakeholders for progress updates
- Integrate with project management tools (Jira, Asana)
