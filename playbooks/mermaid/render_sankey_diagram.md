# Playbook: Render Sankey Diagram

## Description
This playbook creates Sankey diagrams showing flow quantities between nodes. Sankey diagrams are perfect for energy flow, budget allocation, process flows, and any data showing flow or transfer between sources and targets.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Understanding of flow relationships
- Quantifiable flows between sources and targets
- Clear node names

## Steps

1. Identify all nodes
   - List all source nodes (where flows originate)
   - List all target nodes (where flows end)
   - List intermediate nodes (if any)

2. Define flows
   - Map each flow from source to target
   - Assign quantity/value to each flow
   - Ensure node names are consistent

3. Call the render_sankey_diagram tool
   - Pass links with source, target, and value

4. Review the generated diagram
   - Verify all flows are represented
   - Check that flow widths reflect values

## MCP Tools Required

### mcp-mermaid-renderer

**Tool**: `render_sankey_diagram`
- **Parameters**:
  - `links` (list of dict, required): Flow links. Each dict should have:
    - `source` or `from` (string): Source node name
    - `target` or `to` (string): Target node name
    - `value`, `amount`, or `quantity` (number): Flow value
  - `title` (string, optional): Diagram title
  - `format` (string): Output format - "svg" (default, recommended) or "png"
  - `theme` (string): Mermaid theme - "default", "dark", "forest", "neutral"
  - `bgcolor` (string): Background color (default: "transparent")
  - `filename` (string, optional): Suggested filename
- **Returns**: Artifact metadata with download URLs

## Example Usage

**Input**: "Create a Sankey diagram showing website traffic flow"

**Process**:
1. Identify sources: Organic, Paid Ads, Social Media
2. Identify targets: Home, Products, Checkout, Exit
3. Map flows with visitor counts

**Tool Call**:
```json
{
  "links": [
    {"source": "Organic", "target": "Home", "value": 5000},
    {"source": "Organic", "target": "Products", "value": 2000},
    {"source": "Paid Ads", "target": "Home", "value": 3000},
    {"source": "Paid Ads", "target": "Products", "value": 2000},
    {"source": "Social Media", "target": "Home", "value": 1500},
    {"source": "Home", "target": "Products", "value": 4000},
    {"source": "Home", "target": "Exit", "value": 5500},
    {"source": "Products", "target": "Checkout", "value": 3000},
    {"source": "Products", "target": "Exit", "value": 5000},
    {"source": "Checkout", "target": "Exit", "value": 3000}
  ],
  "title": "Website Traffic Flow",
  "format": "svg",
  "theme": "default"
}
```

**Output**:
```
Sankey diagram rendered successfully!
- Format: SVG
- Nodes: 7
- Flows: 10
- Download URL: [artifact link]
```

## Expected Response Format

The tool returns an artifact object with:
- `download_url`: URL to download the rendered diagram
- `source_code`: Editable Mermaid syntax
- `format`: Output format (svg or png)
- `diagram_type`: "sankey"

## Common Use Cases

1. **Energy Flow**: Power generation to consumption, energy distribution
2. **Budget Allocation**: Budget sources to spending categories
3. **Website Analytics**: Traffic sources to pages to conversions
4. **Supply Chain**: Raw materials to products to customers
5. **Money Flow**: Revenue sources to expenses to profit
6. **Process Flows**: Material flow through manufacturing processes
7. **Data Flow**: Data sources through processing to outputs

## Best Practices

1. **Node Names**:
   - Keep concise (1-3 words)
   - Use consistent naming (no duplicates with different spellings)
2. **Flow Values**:
   - Use actual quantities, not percentages
   - Ensure values are proportional and meaningful
   - All values should be positive
3. **Flow Conservation**: Total inflows to a node should match total outflows (unless it's a source or sink)
4. **Complexity**: Keep to 8-15 nodes for clarity
5. **Link Count**: 10-20 links is optimal
6. **Grouping**: Group small flows into "Others" if needed
7. **Direction**: Flows generally go left-to-right

## Error Handling

- **Missing Fields**: All links need source, target, and value
- **Invalid Values**: Values must be positive numbers
- **Empty Links**: Must provide at least one link
- **Node Names**: Source and target names are case-sensitive

## Notes

- Nodes are automatically created from link sources and targets
- No need to explicitly define nodes - they're inferred from links
- Link width is proportional to the flow value
- Flows are shown left-to-right by default
- A node can be both a source and a target (intermediate node)
- Tool accepts flexible field names: source/from, target/to, value/amount/quantity
- Total inflow to a node determines its size on the left
- Total outflow from a node determines its size on the right
- For flow conservation: Σ(inflows) = Σ(outflows) for intermediate nodes
- Sankey diagrams are great for showing:
  - Where things come from
  - Where things go
  - Relative quantities of flows
- Recommended maximum: 15 nodes, 25 links
- For complex systems, create multiple focused diagrams
- Colors are automatically assigned to flows
