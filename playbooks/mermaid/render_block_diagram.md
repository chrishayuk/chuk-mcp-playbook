# Playbook: Render Block Diagram

## Description
This playbook creates block diagrams with customizable blocks and connections. Block diagrams are perfect for system architecture, component layouts, hardware design, and any system that can be represented as interconnected blocks.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Understanding of system components
- Clear identification of blocks and their connections
- Optional: layout preferences (columns)

## Steps

1. Define all blocks
   - List all components/modules
   - Assign unique IDs (will be auto-sanitized)
   - Set labels for each block
   - Optionally set width, height, and shape

2. Define connections
   - Map connections between blocks
   - Add labels to connections if needed

3. Call the render_block_diagram tool
   - Pass blocks with id, label, and optional dimensions/shape
   - Pass edges with from/to block IDs

4. Review the generated diagram
   - Verify all blocks and connections are shown
   - Check that layout is clear

## MCP Tools Required

### mcp-mermaid-renderer

**Tool**: `render_block_diagram`
- **Parameters**:
  - `blocks` (list of dict, required): Blocks. Each dict should have:
    - `id` (string): Block ID (auto-sanitized to CamelCase)
    - `label`, `name`, or `text` (string): Block label
    - `width` (int, optional): Block width (1-10)
    - `height` (int, optional): Block height (1-10)
    - `shape` (string, optional): "square", "round", "circle", "diamond", "hexagon"
  - `edges` (list of dict, required): Connections between blocks. Each dict should have:
    - `from_block`, `from`, or `source` (string): Source block ID
    - `to_block`, `to`, or `target` (string): Target block ID
    - `label` (string, optional): Edge label
  - `title` (string, optional): Diagram title
  - `columns` (int, optional): Number of columns in layout
  - `format` (string): Output format - "svg" (default, recommended) or "png"
  - `theme` (string): Mermaid theme - "default", "dark", "forest", "neutral"
  - `bgcolor` (string): Background color (default: "transparent")
  - `filename` (string, optional): Suggested filename
- **Returns**: Artifact metadata with download URLs

## Example Usage

**Input**: "Create a block diagram for a web application architecture"

**Process**:
1. Identify blocks: Load Balancer, Web Server, App Server, Database, Cache
2. Define connections showing data flow
3. Set shapes for different component types

**Tool Call**:
```json
{
  "blocks": [
    {"id": "lb", "label": "Load Balancer", "shape": "hexagon"},
    {"id": "web1", "label": "Web Server 1", "width": 2},
    {"id": "web2", "label": "Web Server 2", "width": 2},
    {"id": "app", "label": "App Server", "width": 3, "height": 2},
    {"id": "db", "label": "Database", "shape": "round"},
    {"id": "cache", "label": "Redis Cache", "shape": "diamond"}
  ],
  "edges": [
    {"from": "lb", "to": "web1", "label": "HTTP"},
    {"from": "lb", "to": "web2", "label": "HTTP"},
    {"from": "web1", "to": "app"},
    {"from": "web2", "to": "app"},
    {"from": "app", "to": "db", "label": "SQL"},
    {"from": "app", "to": "cache", "label": "GET/SET"}
  ],
  "title": "Web Application Architecture",
  "columns": 3,
  "format": "svg",
  "theme": "default"
}
```

**Output**:
```
Block diagram rendered successfully!
- Format: SVG
- Blocks: 6
- Connections: 6
- Download URL: [artifact link]
```

## Expected Response Format

The tool returns an artifact object with:
- `download_url`: URL to download the rendered diagram
- `source_code`: Editable Mermaid syntax
- `format`: Output format (svg or png)
- `diagram_type`: "block"

## Common Use Cases

1. **System Architecture**: Application components, microservices, system topology
2. **Network Diagrams**: Network components, routers, switches, servers
3. **Hardware Design**: Electronic components, circuit blocks
4. **Data Flow**: Data processing pipelines, ETL workflows
5. **Module Structure**: Software modules, library dependencies
6. **Infrastructure**: Cloud resources, deployment architecture

## Best Practices

1. **Block IDs**:
   - Use simple, descriptive IDs (e.g., "web", "db", "cache")
   - IDs are auto-sanitized to CamelCase
   - Keep IDs short and meaningful
2. **Block Labels**: Clear, concise names (2-4 words)
3. **Block Sizes**:
   - Width/height: 1-10 scale
   - Use larger sizes for more important or complex components
   - Default size is adequate for most cases
4. **Shapes**:
   - Square: Default, general components
   - Round: Databases, storage
   - Circle: Start/end points, users
   - Diamond: Decision points, cache
   - Hexagon: Gateway, boundary components
5. **Layout**: Use `columns` parameter to control grid layout
6. **Edge Labels**: Add labels to clarify connection types (HTTP, SQL, etc.)
7. **Complexity**: Keep to 8-12 blocks for clarity

## Error Handling

- **Missing IDs**: All blocks must have unique IDs
- **Invalid References**: Edge from/to must reference existing block IDs
- **Invalid Dimensions**: Width/height must be 1-10
- **Invalid Shape**: Use only supported shapes
- **Duplicate IDs**: Each block must have a unique ID

## Notes

- Block IDs are automatically sanitized to be Mermaid-safe (CamelCase, no special chars)
- Original IDs are mapped to sanitized versions for edges
- Tool accepts flexible field names:
  - Blocks: label/name/text
  - Edges: from/from_block/source, to/to_block/target
- Blocks are arranged in a grid layout
- Columns parameter controls grid width (default: auto)
- Block dimensions (width/height) affect visual size, not logical spacing
- Edges show directional connections between blocks
- Edge labels are optional but helpful for clarity
- Multiple edges between same blocks are supported
- Self-loops (block to itself) are supported
- Recommended maximum: 12-15 blocks for readability
- For larger systems, create multiple focused diagrams or use hierarchical blocks
- Colors are automatically assigned based on theme
