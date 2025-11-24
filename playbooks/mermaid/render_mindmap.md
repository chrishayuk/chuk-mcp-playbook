# Playbook: Render Mindmap

## Description
This playbook creates mindmaps showing hierarchical relationships and ideas. Mindmaps are perfect for brainstorming, concept mapping, knowledge organization, and visualizing hierarchical information radiating from a central concept.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Central topic or concept
- Related ideas and subtopics organized hierarchically
- Understanding of relationships between concepts

## Steps

1. Define the root concept
   - Choose the central topic
   - Make it clear and concise

2. Define child nodes
   - List main branches from the root
   - Add sub-branches for each main idea
   - Organize hierarchically (parent-child relationships)
   - Optionally choose shapes for emphasis

3. Call the render_mindmap tool
   - Pass root text
   - Pass children as strings or dicts with nested structure

4. Review the generated diagram
   - Verify all ideas are captured
   - Check that hierarchy is logical

## MCP Tools Required

### mcp-mermaid-renderer

**Tool**: `render_mindmap`
- **Parameters**:
  - `root` (string, required): Root node text (central concept)
  - `children` (list, required): Child nodes. Can be strings or dicts with:
    - `text`, `label`, or `name` (string): Node text
    - `shape` (string, optional): "square", "rounded", "circle", "bang", "cloud", "hexagon"
    - `children` or `nodes` (list, optional): Nested child nodes (recursive)
  - `format` (string): Output format - "svg" (default, recommended) or "png"
  - `theme` (string): Mermaid theme - "default", "dark", "forest", "neutral"
  - `bgcolor` (string): Background color (default: "transparent")
  - `filename` (string, optional): Suggested filename
- **Returns**: Artifact metadata with download URLs

## Example Usage

**Input**: "Create a mindmap for project planning concepts"

**Process**:
1. Choose root: "Project Planning"
2. Define main branches: Scope, Schedule, Resources, Risks
3. Add sub-branches for each category

**Tool Call**:
```json
{
  "root": "Project Planning",
  "children": [
    {
      "text": "Scope",
      "children": [
        "Requirements",
        "Deliverables",
        {"text": "Constraints", "shape": "hexagon"}
      ]
    },
    {
      "text": "Schedule",
      "children": [
        "Timeline",
        "Milestones",
        "Dependencies"
      ]
    },
    {
      "text": "Resources",
      "children": [
        "Team",
        "Budget",
        "Tools"
      ]
    },
    {
      "text": "Risks",
      "shape": "bang",
      "children": [
        "Technical",
        "Schedule",
        "Budget"
      ]
    }
  ],
  "format": "svg",
  "theme": "default"
}
```

**Output**:
```
Mindmap rendered successfully!
- Format: SVG
- Root: Project Planning
- Main branches: 4
- Download URL: [artifact link]
```

## Expected Response Format

The tool returns an artifact object with:
- `download_url`: URL to download the rendered diagram
- `source_code`: Editable Mermaid syntax
- `format`: Output format (svg or png)
- `diagram_type`: "mindmap"

## Common Use Cases

1. **Brainstorming**: Idea generation, creative thinking, problem solving
2. **Knowledge Organization**: Learning topics, study notes, concept mapping
3. **Project Planning**: Breaking down projects, WBS (Work Breakdown Structure)
4. **Content Planning**: Blog topics, course outlines, book structures
5. **Decision Making**: Options analysis, pros/cons, decision trees
6. **Meeting Notes**: Organizing discussion points, action items

## Best Practices

1. **Root Node**: Use a clear, concise central concept (2-4 words)
2. **Hierarchy**:
   - Keep 2-4 main branches from root
   - Limit depth to 3-4 levels
   - Each branch should represent a major category
3. **Node Text**: Keep short (1-4 words per node)
4. **Shapes**: Use shapes to emphasize important nodes
   - Circle: Core concepts
   - Bang (!): Warnings, risks, important items
   - Cloud: Ideas, possibilities
   - Square: Concrete items, deliverables
   - Hexagon: Processes, actions
5. **Balance**: Try to balance branches (similar complexity)
6. **Simplicity**: Start simple, add detail as needed
7. **Children Format**:
   - Strings for simple nodes: "Requirements"
   - Dicts for nodes with shape or children: {"text": "Risks", "shape": "bang"}

## Error Handling

- **Empty Root**: Root text is required
- **Empty Children**: Must provide at least one child node
- **Invalid Shape**: Use only supported shapes
- **Deep Nesting**: Very deep hierarchies (>5 levels) may be hard to read
- **Too Many Branches**: More than 8 main branches becomes cluttered

## Notes

- Children can be simple strings or structured dicts
- Nested children create hierarchical structure
- Shapes are optional and used for visual emphasis
- Tool accepts flexible field names: text/label/name, children/nodes
- Mindmap layout is automatically optimized
- Branches radiate from the central root node
- Different shapes help distinguish node types or importance
- For simple nodes without shape or children, use strings
- For nodes with shape or nested children, use dicts
- Recommended maximum:
  - 4-6 main branches
  - 3-4 levels deep
  - 20-30 total nodes
- For large topic maps, create multiple focused mindmaps
- Colors are automatically assigned to branches
