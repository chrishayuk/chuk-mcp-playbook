# Playbook: Render XY Chart

## Description
This playbook creates line or bar charts with X/Y axes. XY charts are perfect for trends, comparisons, time series data, and visualizing numeric data across categories.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- X-axis categories (labels)
- Y-axis data values
- One or more data series to plot

## Steps

1. Define the axes
   - Choose X-axis label (e.g., "Month", "Quarter", "Category")
   - Choose Y-axis label (e.g., "Sales", "Users", "Revenue")
   - List X-axis categories

2. Prepare datasets
   - Create one or more data series
   - Each series needs a label and values
   - Values must match the number of X categories

3. Choose chart type
   - Line chart for trends over time
   - Bar chart for comparisons

4. Call the render_xy_chart tool
   - Pass axis labels, categories, and datasets
   - Set chart type (line or bar)

5. Review the generated diagram
   - Verify data is plotted correctly
   - Check that legend is clear

## MCP Tools Required

### mcp-mermaid-renderer

**Tool**: `render_xy_chart`
- **Parameters**:
  - `x_axis_label` (string, required): X-axis label
  - `y_axis_label` (string, required): Y-axis label
  - `x_categories` (list of strings, required): X-axis categories/labels
  - `datasets` (list of dict, required): Data series. Each dict should have:
    - `label` or `name` (string): Series label
    - `data` or `values` (list of numbers): Y values (one per X category)
  - `title` (string, optional): Chart title
  - `chart_type` (string): "line" or "bar" (default: "line")
  - `format` (string): Output format - "svg" (default, recommended) or "png"
  - `theme` (string): Mermaid theme - "default", "dark", "forest", "neutral"
  - `bgcolor` (string): Background color (default: "transparent")
  - `filename` (string, optional): Suggested filename
- **Returns**: Artifact metadata with download URLs

## Example Usage

**Input**: "Create a line chart showing monthly sales for three products"

**Process**:
1. X-axis: Months (Jan-Jun)
2. Y-axis: Sales ($)
3. Three data series: Product A, B, C

**Tool Call**:
```json
{
  "x_axis_label": "Month",
  "y_axis_label": "Sales ($1000s)",
  "x_categories": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
  "datasets": [
    {
      "label": "Product A",
      "data": [45, 52, 48, 61, 58, 65]
    },
    {
      "label": "Product B",
      "data": [32, 38, 35, 42, 45, 48]
    },
    {
      "label": "Product C",
      "data": [18, 22, 28, 31, 35, 42]
    }
  ],
  "title": "Monthly Product Sales",
  "chart_type": "line",
  "format": "svg",
  "theme": "default"
}
```

**Output**:
```
XY chart rendered successfully!
- Format: SVG
- Type: line
- Data series: 3
- Data points: 18
- Download URL: [artifact link]
```

## Expected Response Format

The tool returns an artifact object with:
- `download_url`: URL to download the rendered diagram
- `source_code`: Editable Mermaid syntax
- `format`: Output format (svg or png)
- `diagram_type`: "xy"

## Common Use Cases

1. **Sales Data**: Revenue trends, product comparisons, regional performance
2. **Web Analytics**: Traffic trends, user growth, conversion rates
3. **Project Metrics**: Velocity, burn-down, story points
4. **Financial Data**: Stock prices, budget vs actual, expense tracking
5. **Performance Metrics**: Response times, error rates, throughput
6. **Scientific Data**: Experimental results, measurements over time

## Best Practices

1. **Chart Type Selection**:
   - Line charts: Trends over time, continuous data
   - Bar charts: Comparisons across categories, discrete data
2. **X-Axis Categories**: Keep labels short (1-3 words)
3. **Y-Axis Label**: Include units (e.g., "Sales ($)", "Users (thousands)")
4. **Number of Series**: 2-5 series is ideal for readability
5. **Data Points**: 5-15 points per series is optimal
6. **Data Length**: All series must have same number of values as X categories
7. **Scale**: Consider normalizing data if series have very different ranges
8. **Colors**: Automatically assigned to distinguish series

## Error Handling

- **Mismatched Data Length**: Each dataset must have same number of values as X categories
- **Empty Categories**: X categories list cannot be empty
- **Empty Datasets**: Must provide at least one dataset
- **Invalid Chart Type**: Must be "line" or "bar"
- **Non-numeric Data**: Y values must be numbers

## Notes

- Number of data values must exactly match number of X categories
- Each dataset is automatically assigned a distinct color
- Line charts connect data points with lines
- Bar charts show values as vertical bars
- Multiple datasets are shown with different colors in legend
- Tool accepts flexible field names: label/name, data/values
- For time series, use consistent time intervals in X categories
- Y-axis scale automatically adjusts to fit data range
- Recommended maximum:
  - 5 data series
  - 15 data points per series
- For more series or points, consider:
  - Breaking into multiple charts
  - Aggregating data
  - Using a different visualization type
- Missing data points are not supported - all series must be complete
