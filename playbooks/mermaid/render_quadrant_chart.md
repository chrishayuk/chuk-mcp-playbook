# Playbook: Render Quadrant Chart

## Description
This playbook creates 2x2 quadrant charts for analyzing items across two dimensions. Quadrant charts are perfect for BCG matrix, prioritization frameworks, product positioning, and risk assessment.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Two dimensions to compare (e.g., impact vs effort, growth vs market share)
- Items to plot with X and Y coordinates
- Optional quadrant labels

## Steps

1. Define the two axes
   - Choose X-axis dimension (e.g., Market Share, Effort, Cost)
   - Choose Y-axis dimension (e.g., Growth Rate, Impact, Value)
   - Create clear axis labels

2. Plot items
   - Assign X and Y coordinates to each item (0-1 scale or 0-100)
   - Position items based on their values on both dimensions
   - Remember: High X = right, High Y = top

3. Label quadrants (optional)
   - Name each of the four quadrants
   - Keep labels simple and concise

4. Call the render_quadrant_chart tool
   - Pass title, axis labels, and points
   - Coordinates auto-normalize (0-100 → 0-1)

5. Review the generated diagram
   - Verify item positioning is correct
   - Check that quadrant divisions make sense

## MCP Tools Required

### mcp-mermaid-renderer

**Tool**: `render_quadrant_chart`
- **Parameters**:
  - `title` (string, required): Chart title
  - `x_axis_label` (string, required): X-axis label (horizontal)
  - `y_axis_label` (string, required): Y-axis label (vertical)
  - `points` (list of dict, required): Points to plot. Each dict should have:
    - `x` or `X` (float): X coordinate (0-1 scale, or 0-100 auto-normalized)
    - `y` or `Y` (float): Y coordinate (0-1 scale, or 0-100 auto-normalized)
    - `label` or `name` (string): Point label
  - `quadrant1_label` (string, optional): Top-right quadrant label (keep simple)
  - `quadrant2_label` (string, optional): Top-left quadrant label
  - `quadrant3_label` (string, optional): Bottom-left quadrant label
  - `quadrant4_label` (string, optional): Bottom-right quadrant label
  - `format` (string): Output format - "svg" (default, recommended) or "png"
  - `theme` (string): Mermaid theme - "default", "dark", "forest", "neutral"
  - `bgcolor` (string): Background color (default: "transparent")
  - `filename` (string, optional): Suggested filename
- **Returns**: Artifact metadata with download URLs

## Example Usage

**Input**: "Create a BCG matrix for product portfolio analysis"

**Process**:
1. Use Market Share (X-axis) and Growth Rate (Y-axis)
2. Plot products with their coordinates
3. Label quadrants: Stars, Question Marks, Cash Cows, Dogs

**Tool Call**:
```json
{
  "title": "Product Portfolio - BCG Matrix",
  "x_axis_label": "Market Share",
  "y_axis_label": "Growth Rate",
  "points": [
    {"x": 0.8, "y": 0.85, "label": "Product A"},
    {"x": 0.25, "y": 0.9, "label": "Product B"},
    {"x": 0.75, "y": 0.2, "label": "Product C"},
    {"x": 0.3, "y": 0.25, "label": "Product D"}
  ],
  "quadrant1_label": "Stars",
  "quadrant2_label": "Question Marks",
  "quadrant3_label": "Dogs",
  "quadrant4_label": "Cash Cows",
  "format": "svg",
  "theme": "default"
}
```

**Output**:
```
Quadrant chart rendered successfully!
- Format: SVG
- Points plotted: 4
- Quadrants labeled: Yes
- Download URL: [artifact link]
```

## Expected Response Format

The tool returns an artifact object with:
- `download_url`: URL to download the rendered diagram
- `source_code`: Editable Mermaid syntax
- `format`: Output format (svg or png)
- `diagram_type`: "quadrant"

## Common Use Cases

1. **BCG Matrix**: Product portfolio analysis (Stars, Cash Cows, Question Marks, Dogs)
2. **Prioritization**: Effort vs Impact, Cost vs Value, Urgency vs Importance
3. **Product Positioning**: Feature analysis, competitive positioning
4. **Risk Assessment**: Likelihood vs Impact, Probability vs Severity
5. **Decision Making**: Feasibility vs Desirability
6. **Resource Allocation**: ROI vs Investment, Performance vs Potential

## Best Practices

1. **Coordinate Scale**:
   - Use 0-1 scale for precision
   - Or use 0-100 (auto-normalized to 0-1)
   - High X = right side, High Y = top
   - Low X = left side, Low Y = bottom
2. **Axis Labels**:
   - Keep concise (2-4 words)
   - Use "Low to High" if needed (e.g., "Market Share (Low to High)")
3. **Quadrant Labels**:
   - Keep very simple (1-2 words)
   - Avoid parentheses (auto-removed)
   - Good: "Stars", "Cash Cows"
   - Avoid: "Stars (High Growth, High Share)"
4. **Number of Points**: 5-15 points is ideal for readability
5. **Point Labels**: Keep short to avoid overlap
6. **Quadrant Interpretation**:
   - Quadrant 1 (top-right): High X, High Y
   - Quadrant 2 (top-left): Low X, High Y
   - Quadrant 3 (bottom-left): Low X, Low Y
   - Quadrant 4 (bottom-right): High X, Low Y

## Error Handling

- **Invalid Coordinates**: X and Y must be numeric
- **Out of Range**: Coordinates > 100 may cause issues (use 0-100 or 0-1)
- **Missing Fields**: All points need x, y, and label
- **Too Many Points**: More than 20 points becomes cluttered

## Notes

- Coordinates are automatically normalized:
  - 0-1: used as-is
  - 1-100: divided by 100
  - Example: x=75 becomes x=0.75
- The chart divides at 0.5 (50%) on both axes
- High values are positioned towards top-right
- Low values are positioned towards bottom-left
- Tool accepts flexible field names: x/X, y/Y, label/name
- Quadrant numbering follows standard: 1=top-right, 2=top-left, 3=bottom-left, 4=bottom-right
- Parentheses in quadrant labels are automatically removed
- For prioritization, common approach: X=Effort (low=left, high=right), Y=Impact (low=bottom, high=top)
- This creates: High Impact/Low Effort (top-left) as "Quick Wins"
- Maximum recommended points: 15-20 for clarity
