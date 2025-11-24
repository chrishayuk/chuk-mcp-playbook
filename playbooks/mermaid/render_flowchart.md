# Playbook: Render Flowchart Diagram

## Description
This playbook creates flowchart diagrams with structured nodes and edges, perfect for visualizing processes, workflows, decision trees, and algorithm flows. Flowcharts are ideal for showing sequential steps, decision points, and process branches.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Clear understanding of the process or workflow to visualize
- Node and edge relationships defined

## Steps

1. Define the flowchart nodes
   - Identify all process steps, decisions, and endpoints
   - Assign unique IDs to each node
   - Choose appropriate shapes for each node type
   - Write clear, concise labels

2. Define the edges (connections)
   - Map the flow between nodes
   - Add labels for decision branches (Yes/No, etc.)
   - Choose appropriate arrow styles

3. Set layout direction
   - Choose TB (top-bottom), LR (left-right), BT (bottom-top), or RL (right-left)

4. Call the render_flowchart tool
   - Pass nodes with id, label, and shape
   - Pass edges with from, to, and optional label
   - Set direction, format, and theme

5. Review the generated diagram
   - Verify all nodes and edges are correct
   - Check that the flow is logical and easy to follow

## MCP Tools Required

### mcp-mermaid-renderer

**Tool**: `render_flowchart`
- **Parameters**:
  - `nodes` (list of dict, required): List of flowchart nodes. Each node dict requires:
    - `id` (string): Unique node identifier (reserved keywords like "end", "start" are auto-renamed)
    - `label` (string): Text displayed in the node
    - `shape` (string, optional): Node shape - "circle", "diamond", "rectangle", "rounded", "stadium", "hexagon", "parallelogram", "trapezoid"
    - Common aliases: "start"/"end" → circle, "decision" → diamond, "process" → rectangle
  - `edges` (list of dict, required): List of edges connecting nodes. Each edge dict requires:
    - `from` (string): Source node ID (can also use "from_node" or "source")
    - `to` (string): Target node ID (can also use "to_node" or "target")
    - `label` (string, optional): Text on the arrow
    - `style` (string, optional): "solid" (default), "dotted", "thick"
  - `direction` (string): Layout direction - "TB" (top-bottom, default), "BT", "LR", "RL"
  - `title` (string, optional): Diagram title
  - `format` (string): Output format - "svg" (default, recommended) or "png"
  - `theme` (string): Mermaid theme - "default", "dark", "forest", "neutral"
  - `bgcolor` (string): Background color (default: "transparent")
  - `filename` (string, optional): Suggested filename
- **Returns**: Artifact metadata with download URLs for rendered diagram and source code

## Example Usage

**Input**: "Create a flowchart for an e-commerce order processing system"

**Process**:
1. Identify nodes: Start, Check Stock, Process Payment, Ship Order, Cancel Order, End
2. Define decision points and branches
3. Create edges showing the flow

**Tool Call**:
```json
{
  "nodes": [
    {"id": "start", "label": "New Order", "shape": "circle"},
    {"id": "check_stock", "label": "Check Stock", "shape": "diamond"},
    {"id": "process_payment", "label": "Process Payment", "shape": "rectangle"},
    {"id": "ship_order", "label": "Ship Order", "shape": "rectangle"},
    {"id": "cancel_order", "label": "Cancel Order", "shape": "rectangle"},
    {"id": "end", "label": "End", "shape": "circle"}
  ],
  "edges": [
    {"from": "start", "to": "check_stock"},
    {"from": "check_stock", "to": "process_payment", "label": "In Stock"},
    {"from": "check_stock", "to": "cancel_order", "label": "Out of Stock"},
    {"from": "process_payment", "to": "ship_order"},
    {"from": "ship_order", "to": "end"},
    {"from": "cancel_order", "to": "end"}
  ],
  "direction": "TB",
  "title": "Order Processing Flow",
  "format": "svg",
  "theme": "default"
}
```

**Output**:
```
Flowchart diagram rendered successfully!
- Format: SVG
- Download URL: [artifact link]
- Source code: [editable Mermaid syntax]
```

## Expected Response Format

The tool returns an artifact object with:
- `download_url`: URL to download the rendered diagram
- `source_code`: Editable Mermaid syntax
- `format`: Output format (svg or png)
- `diagram_type`: "flowchart"

## Common Use Cases

1. **Business Process Flows**: Order processing, customer onboarding, approval workflows
2. **Software Algorithms**: Decision logic, error handling, data processing pipelines
3. **Troubleshooting Guides**: Diagnostic flows, problem resolution trees
4. **User Workflows**: Login flows, checkout processes, form submissions
5. **System Processes**: Deployment pipelines, data ETL flows, backup procedures

## Best Practices

1. **Node Labels**: Keep labels concise (2-5 words). Use clear action verbs.
2. **Node Shapes**:
   - Circle for start/end points
   - Diamond for decisions (Yes/No questions)
   - Rectangle for processes/actions
   - Parallelogram for input/output operations
3. **Direction**: Use TB for most workflows, LR for timeline-style processes
4. **Decision Branches**: Always label decision edges with conditions (Yes/No, True/False)
5. **Reserved Keywords**: IDs like "end", "start", "stop" are auto-renamed (e.g., "end" → "endNode")
6. **Complexity**: For complex flows (>15 nodes), consider breaking into sub-processes
7. **Format**: Use SVG for crisp, zoomable diagrams; PNG for fixed resolution

## Error Handling

- **Duplicate Node IDs**: Ensure all node IDs are unique
- **Missing Nodes**: All edge references must match existing node IDs
- **Invalid Shape**: Use only supported shapes from the list above
- **Reserved Keywords**: IDs like "end", "start" will be auto-renamed by the tool
- **Complex Labels**: If labels are too long, nodes may overlap - keep labels concise

## Notes

- Node IDs are case-sensitive
- Reserved keywords ("end", "start", "stop") are automatically renamed to avoid conflicts
- Shape aliases are supported: "rect", "box" → "rectangle"; "rhombus" → "diamond"
- The tool accepts flexible field names: "from" or "from_node", "to" or "to_node"
- SVG format is recommended for professional presentations and documentation
- Diagrams automatically adjust layout based on node relationships
- Maximum recommended nodes: 20-25 for optimal readability
