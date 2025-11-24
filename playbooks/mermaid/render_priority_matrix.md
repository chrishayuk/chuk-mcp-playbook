# Playbook: Visualize Priority Matrix

## Description
This playbook guides you through visualizing priority matrices for decision-making, including effort vs impact, urgency vs importance (Eisenhower Matrix), and other 2x2 prioritization frameworks. Perfect for product planning, feature prioritization, and strategic decision-making.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- List of items to prioritize (features, tasks, projects)
- Criteria for two dimensions (effort, impact, urgency, importance)
- Scoring or classification for each item

## Steps

1. **Define axes**
   - X-axis dimension (e.g., Effort, Urgency)
   - Y-axis dimension (e.g., Impact, Importance)
   - Axis ranges (low to high)
   - Quadrant labels

2. **Categorize items**
   - Score each item on both dimensions
   - Place items in appropriate quadrants
   - Group similar items
   - Note dependencies

3. **Choose diagram type**
   - Use **quadrant_chart** for 2x2 matrices

4. **Create visualization**
   - Plot all items
   - Label quadrants clearly
   - Highlight priority items
   - Add decision guidance

## MCP Tools Required

### Primary Tool: render_quadrant_chart
See [render_quadrant_chart.md](./render_quadrant_chart.md)

## Example Usage

### Scenario: Feature Prioritization (Effort vs Impact)

```json
{
  "x_axis": {"label": "Effort (Development Time)", "left_label": "Low Effort", "right_label": "High Effort"},
  "y_axis": {"label": "Business Impact", "bottom_label": "Low Impact", "top_label": "High Impact"},
  "quadrants": [
    {"label": "Quick Wins", "description": "Do First - High impact, low effort"},
    {"label": "Major Projects", "description": "Do Later - High impact, high effort"},
    {"label": "Fill-ins", "description": "Do if time - Low impact, low effort"},
    {"label": "Avoid", "description": "Don't do - Low impact, high effort"}
  ],
  "points": [
    {"label": "User profile photos", "x": 0.2, "y": 0.8},
    {"label": "Email notifications", "x": 0.3, "y": 0.7},
    {"label": "Dark mode", "x": 0.4, "y": 0.4},
    {"label": "Advanced search", "x": 0.8, "y": 0.9},
    {"label": "Social sharing", "x": 0.3, "y": 0.5},
    {"label": "Custom themes", "x": 0.9, "y": 0.3},
    {"label": "Export to PDF", "x": 0.2, "y": 0.6},
    {"label": "AI recommendations", "x": 0.9, "y": 0.9},
    {"label": "Comment reactions", "x": 0.1, "y": 0.3}
  ],
  "title": "Feature Prioritization Matrix",
  "format": "svg",
  "theme": "default"
}
```

### Scenario: Eisenhower Matrix (Urgency vs Importance)

```json
{
  "x_axis": {"label": "Urgency", "left_label": "Not Urgent", "right_label": "Urgent"},
  "y_axis": {"label": "Importance", "bottom_label": "Not Important", "top_label": "Important"},
  "quadrants": [
    {"label": "Plan", "description": "Schedule - Important but not urgent"},
    {"label": "Do", "description": "Do first - Urgent and important"},
    {"label": "Eliminate", "description": "Drop - Not urgent or important"},
    {"label": "Delegate", "description": "Delegate - Urgent but not important"}
  ],
  "points": [
    {"label": "Critical bug fix", "x": 0.9, "y": 0.9},
    {"label": "Strategic planning", "x": 0.2, "y": 0.8},
    {"label": "Production incident", "x": 0.9, "y": 0.9},
    {"label": "Code review", "x": 0.7, "y": 0.5},
    {"label": "Team meeting", "x": 0.8, "y": 0.4},
    {"label": "Learn new framework", "x": 0.3, "y": 0.7},
    {"label": "Update documentation", "x": 0.4, "y": 0.6},
    {"label": "Social media check", "x": 0.3, "y": 0.2}
  ],
  "title": "Task Prioritization - Eisenhower Matrix",
  "format": "svg",
  "theme": "default"
}
```

## Best Practices

1. **Define axes clearly** - Make criteria objective
2. **Use consistent scoring** - 1-10 scale or low/medium/high
3. **Involve stakeholders** - Get multiple perspectives
4. **Review regularly** - Priorities change over time
5. **Act on insights** - Focus on high-priority quadrant
6. **Document assumptions** - Why items are scored that way
7. **Limit items** - Too many items make matrix cluttered (max 20)

## Common Variations

- Risk vs Reward
- Cost vs Benefit
- Complexity vs Value
- Frequency vs Severity
- Confidence vs Impact

## Related Playbooks

- [render_quadrant_chart.md](./render_quadrant_chart.md)
- [render_sprint_schedule.md](./render_sprint_schedule.md)
- [render_release_roadmap.md](./render_release_roadmap.md)
