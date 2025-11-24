# Playbook: Visualize Skill Assessment

## Description
This playbook guides you through visualizing team or individual skill assessments across multiple competency areas showing proficiency levels, gaps, and strengths. Perfect for performance reviews, training planning, and hiring decisions.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- List of skills/competencies to assess
- Assessment criteria (1-5 or 1-10 scale)
- Evaluation data for individuals or teams

## Steps

1. **Define competencies**
   - List relevant skills
   - Define proficiency levels
   - Set assessment criteria
   - Note required levels

2. **Assess skills**
   - Evaluate current proficiency
   - Identify gaps
   - Note strengths
   - Compare to requirements

3. **Choose diagram type**
   - Use **radar_chart** for multi-skill assessment

4. **Create visualization**
   - Show all competencies
   - Compare individuals or teams
   - Highlight gaps
   - Note development areas

## MCP Tools Required

### Primary Tool: render_radar_chart
See [render_radar_chart.md](./render_radar_chart.md)

### Secondary Tool: render_pie_chart
See [render_pie_chart.md](./render_pie_chart.md)

## Example Usage

```json
{
  "categories": ["Frontend", "Backend", "DevOps", "Testing", "Security", "Architecture"],
  "series": [
    {
      "name": "Team Average",
      "data": [7, 6, 5, 6, 4, 5]
    },
    {
      "name": "Required Level",
      "data": [8, 8, 7, 7, 7, 6]
    },
    {
      "name": "Senior Dev",
      "data": [9, 7, 6, 8, 5, 7]
    },
    {
      "name": "Junior Dev",
      "data": [6, 5, 3, 5, 3, 3]
    }
  ],
  "title": "Team Skill Assessment",
  "format": "svg",
  "theme": "default"
}
```

## Best Practices

1. **Use objective criteria** - Clear proficiency definitions
2. **Get multiple perspectives** - Self, peer, manager assessments
3. **Update regularly** - Skills change over time
4. **Identify gaps** - What needs development
5. **Plan training** - Address skill gaps
6. **Celebrate strengths** - Recognize expertise
7. **Compare to requirements** - Role-specific needs

## Related Playbooks

- [render_radar_chart.md](./render_radar_chart.md)
- [render_product_comparison.md](./render_product_comparison.md)
