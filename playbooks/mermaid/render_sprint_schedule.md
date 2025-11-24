# Playbook: Visualize Sprint Schedule

## Description
This playbook guides you through visualizing Agile sprint schedules, including user stories, tasks, sprint goals, capacity, and team velocity. Perfect for sprint planning, tracking progress, managing workload, and communicating sprint commitments.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- List of user stories and tasks for the sprint
- Understanding of team capacity and velocity
- Knowledge of story points and priorities

## Steps

1. **Identify sprint tasks**
   - List all user stories
   - Break down into tasks
   - Estimate story points
   - Assign owners

2. **Plan sprint timeline**
   - Define sprint duration (typically 2 weeks)
   - Note sprint ceremonies (standup, review, retro)
   - Identify dependencies
   - Mark blockers

3. **Choose diagram type**
   - Use **gantt_chart** for detailed sprint task tracking
   - Use **quadrant_chart** for prioritization

4. **Create visualization**
   - Show all stories and tasks
   - Track daily progress
   - Highlight blocked items
   - Monitor burndown

## MCP Tools Required

### Primary Tool: render_gantt_chart
Best for detailed sprint task scheduling and progress tracking.

See [render_gantt_chart.md](./render_gantt_chart.md) for full details.

### Secondary Tool: render_quadrant_chart
Best for story prioritization (effort vs value).

See [render_quadrant_chart.md](./render_quadrant_chart.md) for full details.

## Example Usage

### Scenario: Two-Week Sprint Schedule

**User Request**: "Visualize our Sprint 23 schedule showing user stories, story points, and sprint ceremonies"

```json
{
  "title": "Sprint 23 - User Profile Enhancements",
  "dateFormat": "YYYY-MM-DD",
  "sections": [
    {
      "name": "High Priority (13 points)",
      "tasks": [
        {"id": "user-123", "name": "[5pts] User profile photo upload", "start": "2024-01-08", "duration": "3d", "assignee": "Alice"},
        {"id": "user-124", "name": "[3pts] Edit profile information", "start": "2024-01-08", "duration": "2d", "assignee": "Bob"},
        {"id": "user-125", "name": "[5pts] Profile privacy settings", "start": "2024-01-11", "duration": "3d", "dependencies": ["user-124"], "assignee": "Alice"}
      ]
    },
    {
      "name": "Medium Priority (8 points)",
      "tasks": [
        {"id": "user-126", "name": "[3pts] Profile completion widget", "start": "2024-01-10", "duration": "2d", "assignee": "Carol"},
        {"id": "user-127", "name": "[5pts] Social media links", "start": "2024-01-12", "duration": "3d", "dependencies": ["user-126"], "assignee": "Carol"}
      ]
    },
    {
      "name": "Sprint Ceremonies",
      "tasks": [
        {"id": "planning", "name": "Sprint Planning", "start": "2024-01-08", "duration": "2h", "milestone": true},
        {"id": "review", "name": "Sprint Review", "start": "2024-01-19", "duration": "1h", "milestone": true},
        {"id": "retro", "name": "Sprint Retrospective", "start": "2024-01-19", "duration": "1h", "milestone": true}
      ]
    }
  ],
  "format": "svg",
  "theme": "default"
}
```

## Best Practices

1. **Estimate accurately** - Use story points or hours
2. **Account for capacity** - Consider PTO, meetings, and overhead
3. **Limit WIP** - Don't overcommit the team
4. **Track daily** - Update progress in daily standup
5. **Identify blockers** - Flag impediments immediately
6. **Balance workload** - Distribute work evenly across team
7. **Include ceremonies** - Show sprint events on timeline

## Common Variations

- Kanban board view
- Burndown chart tracking
- Team capacity planning
- Cross-team dependencies
- Release train schedules

## Related Playbooks

- [render_gantt_chart.md](./render_gantt_chart.md)
- [render_quadrant_chart.md](./render_quadrant_chart.md)
- [render_project_timeline.md](./render_project_timeline.md)
- [render_release_roadmap.md](./render_release_roadmap.md)

## Notes

- Update daily with actual progress
- Track velocity for future planning
- Document reasons for scope changes
- Celebrate completed stories
- Use for retrospective discussions
