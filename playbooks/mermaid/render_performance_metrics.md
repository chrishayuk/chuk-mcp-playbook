# Playbook: Visualize Performance Metrics

## Description
This playbook guides you through visualizing KPIs, performance metrics, and trends over time showing system performance, business metrics, and operational data. Perfect for dashboards, monitoring, and performance reporting.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Historical metrics data
- Understanding of KPIs
- Knowledge of target/baseline values

## Steps

1. **Identify key metrics**
   - Performance indicators
   - Time series data
   - Target values
   - Historical trends

2. **Organize data**
   - Time periods (daily, weekly, monthly)
   - Multiple metrics
   - Comparison periods
   - Anomalies and events

3. **Choose diagram type**
   - Use **xy_chart** for time series
   - Use **timeline** for event markers

4. **Create visualization**
   - Show trends over time
   - Include targets/baselines
   - Highlight anomalies
   - Note significant events

## MCP Tools Required

### Primary Tool: render_xy_chart
See [render_xy_chart.md](./render_xy_chart.md)

### Secondary Tool: render_timeline
See [render_timeline.md](./render_timeline.md)

## Example Usage

### Scenario: Key Performance Metrics Dashboard

**User Request**: "Visualize our key performance metrics for H1 2024 showing revenue, active users, and conversion rate trends"

```json
{
  "x_axis": {"label": "Month", "categories": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]},
  "y_axis": {"label": "Value"},
  "series": [
    {
      "name": "Revenue ($K)",
      "data": [120, 135, 148, 162, 180, 195]
    },
    {
      "name": "Active Users (K)",
      "data": [15, 17, 19, 21, 24, 27]
    },
    {
      "name": "Conversion Rate (%)",
      "data": [3.2, 3.5, 3.8, 4.1, 4.3, 4.5]
    }
  ],
  "title": "Key Performance Metrics - H1 2024",
  "chart_type": "line",
  "format": "svg",
  "theme": "default"
}
```

## Best Practices

1. **Choose relevant metrics** - What drives business
2. **Show trends** - Not just current values
3. **Include context** - Targets, previous period
4. **Note anomalies** - Explain unusual patterns
5. **Update regularly** - Keep data current
6. **Visualize appropriately** - Line for trends, bar for comparisons
7. **Add annotations** - Mark significant events

## Related Playbooks

- [render_xy_chart.md](./render_xy_chart.md)
- [render_timeline.md](./render_timeline.md)
