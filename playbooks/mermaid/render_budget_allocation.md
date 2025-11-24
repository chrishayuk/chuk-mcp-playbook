# Playbook: Visualize Budget Allocation

## Description
This playbook guides you through visualizing budget allocation across departments, projects, or categories showing resource distribution, spending patterns, and fund flows. Perfect for financial planning, cost optimization, and stakeholder reporting.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Budget data by category
- Understanding of spending hierarchy
- Knowledge of cost centers

## Steps

1. **Identify budget categories**
   - List all budget line items
   - Group by department or project
   - Note fixed vs variable costs
   - Document budget constraints

2. **Map fund flow**
   - Show money allocation path
   - Document sub-allocations
   - Note reserves and contingency
   - Track spending patterns

3. **Choose diagram type**
   - Use **sankey_diagram** for fund flow
   - Use **pie_chart** for category breakdown

4. **Create visualization**
   - Show total budget allocation
   - Highlight major categories
   - Document subcategory splits
   - Note variances from plan

## MCP Tools Required

### Primary Tool: render_sankey_diagram
See [render_sankey_diagram.md](./render_sankey_diagram.md)

### Secondary Tool: render_pie_chart
See [render_pie_chart.md](./render_pie_chart.md)

## Example Usage

### Scenario: Annual Department Budget

**User Request**: "Visualize our $1M annual budget allocation across engineering, marketing, sales, and operations departments"

```json
{
  "nodes": [
    {"id": "total", "label": "Total Budget $1M"},
    {"id": "engineering", "label": "Engineering"},
    {"id": "marketing", "label": "Marketing"},
    {"id": "sales", "label": "Sales"},
    {"id": "operations", "label": "Operations"},
    {"id": "salaries", "label": "Salaries"},
    {"id": "infrastructure", "label": "Infrastructure"},
    {"id": "advertising", "label": "Advertising"},
    {"id": "events", "label": "Events"}
  ],
  "links": [
    {"source": "total", "target": "engineering", "value": 400000},
    {"source": "total", "target": "marketing", "value": 300000},
    {"source": "total", "target": "sales", "value": 200000},
    {"source": "total", "target": "operations", "value": 100000},
    {"source": "engineering", "target": "salaries", "value": 300000},
    {"source": "engineering", "target": "infrastructure", "value": 100000},
    {"source": "marketing", "target": "advertising", "value": 200000},
    {"source": "marketing", "target": "events", "value": 100000}
  ],
  "title": "Annual Budget Allocation",
  "format": "svg",
  "theme": "default"
}
```

## Best Practices

1. **Show hierarchies** - Budget rollup structures
2. **Highlight variances** - Actual vs planned
3. **Track over time** - Monthly or quarterly views
4. **Note constraints** - Budget caps and minimums
5. **Document assumptions** - Growth rates, inflation
6. **Show reserves** - Contingency and emergency funds
7. **Compare periods** - Year-over-year changes

## Related Playbooks

- [render_sankey_diagram.md](./render_sankey_diagram.md)
- [render_pie_chart.md](./render_pie_chart.md)
- [render_xy_chart.md](./render_xy_chart.md)
