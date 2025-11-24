# Playbook: Visualize Market Share Breakdown

## Description
This playbook guides you through visualizing market share distribution across competitors, products, or segments showing percentages, trends, and competitive positioning. Perfect for competitive analysis, market research, and strategic planning.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Market share data by competitor or segment
- Understanding of market size
- Historical data for trends

## Steps

1. **Gather market data**
   - List all competitors/segments
   - Collect market share percentages
   - Note market size
   - Document data sources

2. **Organize data**
   - Calculate percentages
   - Group small players
   - Note trends
   - Identify changes

3. **Choose diagram type**
   - Use **pie_chart** for current market share
   - Use **xy_chart** for trends over time

4. **Create visualization**
   - Show all major players
   - Highlight your position
   - Note trends
   - Document market dynamics

## MCP Tools Required

### Primary Tool: render_pie_chart
See [render_pie_chart.md](./render_pie_chart.md)

### Secondary Tool: render_xy_chart
See [render_xy_chart.md](./render_xy_chart.md)

## Example Usage

```json
{
  "title": "Cloud Provider Market Share 2024",
  "data": [
    {"label": "AWS", "value": 32},
    {"label": "Azure", "value": 23},
    {"label": "Google Cloud", "value": 11},
    {"label": "Alibaba Cloud", "value": 6},
    {"label": "IBM Cloud", "value": 4},
    {"label": "Oracle Cloud", "value": 3},
    {"label": "Others", "value": 21}
  ],
  "format": "svg",
  "theme": "default"
}
```

## Best Practices

1. **Use recent data** - Current market position
2. **Show all major players** - Complete picture
3. **Group small players** - "Others" category
4. **Note data source** - Credibility
5. **Show trends** - How market is changing
6. **Compare periods** - Year-over-year growth
7. **Add context** - Market size, growth rate

## Related Playbooks

- [render_pie_chart.md](./render_pie_chart.md)
- [render_xy_chart.md](./render_xy_chart.md)
- [render_product_comparison.md](./render_product_comparison.md)
