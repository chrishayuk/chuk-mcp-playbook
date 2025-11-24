# Playbook: Render Radar Chart

## Description
This playbook creates radar/spider charts comparing multiple variables across datasets. Radar charts are perfect for skill assessments, product comparisons, performance metrics, and multi-dimensional data visualization.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Multiple dimensions/axes to compare
- One or more datasets with values for each axis
- Understanding of what each axis represents

## Steps

1. Define the axes
   - List all dimensions being compared (3-8 axes ideal)
   - Name each axis clearly

2. Prepare datasets
   - Create one or more data series to compare
   - Each series needs a label
   - Provide values for all axes (same order as axes list)

3. Call the render_radar_chart tool
   - Pass axes list
   - Pass datasets with labels and values

4. Review the generated diagram
   - Verify all axes are shown
   - Check that data series are clearly distinguished

## MCP Tools Required

### mcp-mermaid-renderer

**Tool**: `render_radar_chart`
- **Parameters**:
  - `axes` (list of strings, required): Axis labels (dimensions being compared)
  - `datasets` (list of dict, required): Data series. Each dict should have:
    - `label` or `name` (string): Dataset label
    - `values` or `data` (list of numbers): Values (one per axis, in same order)
  - `title` (string, optional): Chart title
  - `format` (string): Output format - "svg" (default, recommended) or "png"
  - `theme` (string): Mermaid theme - "default", "dark", "forest", "neutral"
  - `bgcolor` (string): Background color (default: "transparent")
  - `filename` (string, optional): Suggested filename
- **Returns**: Artifact metadata with download URLs

## Example Usage

**Input**: "Create a radar chart comparing employee skills"

**Process**:
1. Define skill axes: Communication, Technical, Leadership, Creativity, Problem Solving
2. Create datasets for multiple employees
3. Assign scores (0-100) for each skill

**Tool Call**:
```json
{
  "axes": ["Communication", "Technical", "Leadership", "Creativity", "Problem Solving"],
  "datasets": [
    {
      "label": "Alice",
      "values": [90, 85, 70, 75, 88]
    },
    {
      "label": "Bob",
      "values": [75, 95, 60, 80, 90]
    },
    {
      "label": "Carol",
      "values": [85, 70, 90, 85, 75]
    }
  ],
  "title": "Employee Skills Assessment",
  "format": "svg",
  "theme": "default"
}
```

**Output**:
```
Radar chart rendered successfully!
- Format: SVG
- Axes: 5
- Data series: 3
- Download URL: [artifact link]
```

## Expected Response Format

The tool returns an artifact object with:
- `download_url`: URL to download the rendered diagram
- `source_code`: Editable Mermaid syntax
- `format`: Output format (svg or png)
- `diagram_type`: "radar"

## Common Use Cases

1. **Skills Assessment**: Employee skills, team capabilities, competency profiles
2. **Product Comparison**: Feature comparison, product specs, competitive analysis
3. **Performance Metrics**: KPIs, balanced scorecard, multi-metric tracking
4. **Quality Metrics**: Software quality (performance, security, maintainability, etc.)
5. **Customer Satisfaction**: Multi-dimensional satisfaction surveys
6. **Risk Assessment**: Risk profiles across multiple dimensions

## Best Practices

1. **Number of Axes**:
   - Ideal: 5-7 axes
   - Minimum: 3 axes
   - Maximum: 10 axes (beyond this becomes cluttered)
2. **Axis Labels**: Keep concise (1-2 words)
3. **Number of Datasets**: 2-4 datasets is ideal for comparison
4. **Scale**: Use consistent scale across all axes (e.g., 0-100)
5. **Values Order**: Values must match axes order exactly
6. **Balance**: Try to have similar number of axes for balanced appearance
7. **Interpretation**: Larger area = better overall performance

## Error Handling

- **Mismatched Lengths**: Each dataset must have same number of values as axes
- **Empty Axes**: Must provide at least 3 axes
- **Empty Datasets**: Must provide at least one dataset
- **Non-numeric Values**: All values must be numbers

## Notes

- Each dataset is automatically assigned a distinct color
- Number of values in each dataset must exactly match number of axes
- Values are plotted from center (0) to outer edge (max value)
- Tool accepts flexible field names: label/name, values/data
- Axes are arranged in a circular pattern
- Each dataset forms a polygon connecting its values
- Overlapping areas show similarities/differences
- Larger filled area indicates higher overall scores
- Chart automatically scales to fit all values
- Use same scale for all axes for meaningful comparison
- Recommended maximum:
  - 7 axes
  - 4 data series
- For more dimensions or series:
  - Create multiple focused charts
  - Group related dimensions
  - Use different chart types
- Missing values are not supported - all datasets must be complete
- Zero values are valid and plot at the center
