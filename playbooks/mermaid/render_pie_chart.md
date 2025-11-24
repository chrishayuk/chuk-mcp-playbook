# Playbook: Render Pie Chart

## Description
This playbook creates pie charts showing proportional data distribution. Pie charts are perfect for showing percentages, market share, budget allocation, and any data where parts make up a whole.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Data that represents parts of a whole
- Clear labels for each segment
- Numeric values for each segment

## Steps

1. Prepare your data
   - Collect all categories and their values
   - Ensure data represents parts of a whole
   - Create label-value pairs

2. Call the render_pie_chart tool
   - Pass data as a dictionary of label-value pairs
   - Set title and display options

3. Review the generated diagram
   - Verify all segments are shown correctly
   - Check that proportions are accurate

## MCP Tools Required

### mcp-mermaid-renderer

**Tool**: `render_pie_chart`
- **Parameters**:
  - `data` (dict, required): Label to value mapping (e.g., {"Product A": 45, "Product B": 30, "Product C": 25})
  - `title` (string, optional): Chart title
  - `show_data` (boolean): Show numeric values in the chart (default: false)
  - `format` (string): Output format - "svg" (default, recommended) or "png"
  - `theme` (string): Mermaid theme - "default", "dark", "forest", "neutral"
  - `bgcolor` (string): Background color (default: "transparent")
  - `filename` (string, optional): Suggested filename
- **Returns**: Artifact metadata with download URLs

## Example Usage

**Input**: "Create a pie chart showing market share distribution"

**Process**:
1. Collect market share data for each company
2. Create label-value pairs
3. Generate chart with values displayed

**Tool Call**:
```json
{
  "data": {
    "Company A": 35,
    "Company B": 28,
    "Company C": 20,
    "Company D": 12,
    "Others": 5
  },
  "title": "Market Share by Company",
  "show_data": true,
  "format": "svg",
  "theme": "default"
}
```

**Output**:
```
Pie chart rendered successfully!
- Format: SVG
- Segments: 5
- Total value: 100
- Download URL: [artifact link]
```

## Expected Response Format

The tool returns an artifact object with:
- `download_url`: URL to download the rendered diagram
- `source_code`: Editable Mermaid syntax
- `format`: Output format (svg or png)
- `diagram_type`: "pie"

## Common Use Cases

1. **Business Analytics**: Market share, revenue distribution, customer segments
2. **Budget Planning**: Budget allocation, expense breakdown, resource distribution
3. **Survey Results**: Poll results, preference distribution, demographic breakdowns
4. **Project Management**: Time allocation, resource usage, task distribution
5. **Web Analytics**: Traffic sources, browser usage, device types
6. **Sales Data**: Product sales mix, regional sales, category performance

## Best Practices

1. **Number of Segments**:
   - Ideal: 3-6 segments
   - Maximum: 8 segments (beyond this, consider grouping into "Others")
2. **Labels**: Use clear, concise labels (2-4 words)
3. **Values**: Can be absolute numbers or percentages
4. **Show Data**: Enable show_data=true to display values on segments
5. **Data Total**: Values don't need to sum to 100 (proportions are calculated automatically)
6. **Small Segments**: Group very small segments (<5%) into "Others" category
7. **Colors**: Tool automatically assigns distinct colors to segments
8. **Ordering**: Consider ordering segments by size (largest to smallest)

## Error Handling

- **Empty Data**: Must provide at least one label-value pair
- **Invalid Values**: Values must be numeric (integers or decimals)
- **Negative Values**: Values should be positive
- **Too Many Segments**: More than 10 segments becomes hard to read

## Notes

- Data is provided as a simple dictionary/object of label-value pairs
- Values are automatically converted to percentages for display
- Values don't need to sum to 100 - proportions are calculated
- Labels appear in the legend
- Show_data displays the actual values on the chart segments
- Tool automatically assigns colors from a palette
- Each segment's size is proportional to its value relative to the total
- For comparisons over time, consider using a bar chart or line chart instead
- For showing parts of multiple wholes, consider using multiple pie charts or a stacked bar chart
- Pie charts work best when showing how a whole is divided into parts
- Avoid using pie charts for data that doesn't represent parts of a whole
