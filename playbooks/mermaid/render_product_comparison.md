# Playbook: Visualize Product Comparison

## Description
This playbook guides you through visualizing product comparisons across multiple dimensions showing strengths, weaknesses, and differentiators. Perfect for competitive analysis, feature comparison, and product positioning.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- List of products/solutions to compare
- Comparison criteria/dimensions
- Scoring for each product on each dimension

## Steps

1. **Define comparison dimensions**
   - List evaluation criteria (price, features, performance, support)
   - Weight dimensions by importance
   - Set scoring scale (1-5 or 1-10)
   - Gather data for each product

2. **Score products**
   - Evaluate each product on each dimension
   - Use objective data when possible
   - Note assumptions and sources
   - Normalize scores

3. **Choose diagram type**
   - Use **radar_chart** for multi-dimensional comparison

4. **Create visualization**
   - Show all products on same chart
   - Highlight key differentiators
   - Note strengths and weaknesses
   - Document scoring methodology

## MCP Tools Required

### Primary Tool: render_radar_chart
See [render_radar_chart.md](./render_radar_chart.md)

### Secondary Tool: render_xy_chart
See [render_xy_chart.md](./render_xy_chart.md)

## Example Usage

```json
{
  "categories": ["Price", "Features", "Performance", "Support", "Ease of Use", "Scalability"],
  "series": [
    {
      "name": "Our Product",
      "data": [8, 9, 8, 9, 8, 9]
    },
    {
      "name": "Competitor A",
      "data": [6, 7, 9, 7, 6, 8]
    },
    {
      "name": "Competitor B",
      "data": [9, 6, 6, 5, 7, 6]
    },
    {
      "name": "Competitor C",
      "data": [5, 8, 7, 8, 9, 7]
    }
  ],
  "title": "Product Comparison Analysis",
  "format": "svg",
  "theme": "default"
}
```

## Best Practices

1. **Choose relevant dimensions** - What matters to customers
2. **Use consistent scoring** - Same scale for all products
3. **Be objective** - Use data, not opinions
4. **Show sources** - Document where scores come from
5. **Update regularly** - Products evolve
6. **Highlight differentiators** - What makes you unique
7. **Consider segments** - Different buyers value different things

## Related Playbooks

- [render_radar_chart.md](./render_radar_chart.md)
- [render_xy_chart.md](./render_xy_chart.md)
- [render_priority_matrix.md](./render_priority_matrix.md)
