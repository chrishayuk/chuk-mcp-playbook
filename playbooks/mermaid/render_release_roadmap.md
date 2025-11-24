# Playbook: Visualize Release Roadmap

## Description
This playbook guides you through visualizing product release roadmaps showing features, versions, release dates, and strategic initiatives over time. Perfect for product planning, stakeholder communication, and coordinating cross-team efforts.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- List of planned features and releases
- Understanding of product strategy
- Knowledge of release schedule and dependencies

## Steps

1. **Identify releases**
   - List all planned releases with versions
   - Note major vs minor releases
   - Identify feature themes
   - Mark strategic milestones

2. **Plan timeline**
   - Define release cadence
   - Note feature completion dates
   - Identify dependencies
   - Document release windows

3. **Choose diagram type**
   - Use **timeline** for high-level roadmap
   - Use **gantt_chart** for detailed release planning

4. **Create visualization**
   - Show all releases chronologically
   - Group features by theme
   - Highlight major milestones
   - Include confidence levels

## MCP Tools Required

### Primary Tool: render_timeline
Best for high-level product roadmap and release communication.

See [render_timeline.md](./render_timeline.md) for full details.

### Primary Tool: render_gantt_chart
Best for detailed release planning with dependencies.

See [render_gantt_chart.md](./render_gantt_chart.md) for full details.

### Secondary Tool: render_xy_chart
Best for showing feature trends and velocity over time.

See [render_xy_chart.md](./render_xy_chart.md) for full details.

## Example Usage

### Scenario: Product Roadmap for 2024

```json
{
  "title": "Product Roadmap 2024",
  "sections": [
    {
      "section": "Q1 2024",
      "events": [
        {"time": "January", "event": "v2.0 - Mobile App Launch"},
        {"time": "February", "event": "v2.1 - Payment Integration"},
        {"time": "March", "event": "v2.2 - Analytics Dashboard"}
      ]
    },
    {
      "section": "Q2 2024",
      "events": [
        {"time": "April", "event": "v3.0 - Multi-tenant Support"},
        {"time": "May", "event": "v3.1 - API v2 Release"},
        {"time": "June", "event": "v3.2 - Advanced Search"}
      ]
    },
    {
      "section": "Q3 2024",
      "events": [
        {"time": "July", "event": "v4.0 - AI Features"},
        {"time": "August", "event": "v4.1 - Automation Workflows"},
        {"time": "September", "event": "v4.2 - Integration Marketplace"}
      ]
    },
    {
      "section": "Q4 2024",
      "events": [
        {"time": "October", "event": "v5.0 - Enterprise Features"},
        {"time": "November", "event": "v5.1 - Compliance Suite"},
        {"time": "December", "event": "v5.2 - Year-end Performance Optimizations"}
      ]
    }
  ],
  "format": "svg",
  "theme": "default"
}
```

## Best Practices

1. **Show themes** - Group features by strategic initiatives
2. **Indicate confidence** - Use colors for committed vs planned
3. **Include dependencies** - Show what blocks what
4. **Version appropriately** - Use semantic versioning
5. **Communicate often** - Update roadmap quarterly
6. **Be flexible** - Roadmaps change based on feedback
7. **Show value** - Explain why features matter

## Common Variations

- Feature-based roadmap
- Theme-based roadmap
- Now/Next/Later roadmap
- Platform vs product roadmaps
- Multi-product portfolio roadmaps

## Related Playbooks

- [render_timeline.md](./render_timeline.md)
- [render_gantt_chart.md](./render_gantt_chart.md)
- [render_project_timeline.md](./render_project_timeline.md)
- [render_sprint_schedule.md](./render_sprint_schedule.md)

## Notes

- Avoid over-committing on distant dates
- Use "tentative" for uncertain features
- Show past releases for context
- Include customer-facing names, not internal codenames
- Export for board presentations and customer communications
