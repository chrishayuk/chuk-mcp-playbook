# Playbook: Visualize Concept Map

## Description
This playbook guides you through visualizing concept maps for organizing ideas, brainstorming, knowledge structure, and hierarchical information. Perfect for planning, education, knowledge management, and creative thinking.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Central concept or topic
- Related ideas and sub-concepts
- Understanding of relationships

## Steps

1. **Identify central concept**
   - Main topic or theme
   - Core ideas
   - Key categories

2. **Map related concepts**
   - Sub-topics
   - Supporting ideas
   - Relationships
   - Hierarchies

3. **Choose diagram type**
   - Use **mindmap** for concept mapping
   - Use **flowchart** for process-oriented concepts
   - Use **block_diagram** for logical groupings

4. **Create visualization**
   - Show central concept
   - Branch out to related ideas
   - Organize hierarchically
   - Group related concepts

## MCP Tools Required

### Primary Tool: render_mindmap
See [render_mindmap.md](./render_mindmap.md)

### Secondary Tool: render_flowchart
See [render_flowchart.md](./render_flowchart.md)

### Secondary Tool: render_block_diagram
See [render_block_diagram.md](./render_block_diagram.md)

## Example Usage

```json
{
  "root": {
    "label": "Mobile App Development",
    "children": [
      {
        "label": "Frontend",
        "children": [
          {"label": "React Native"},
          {"label": "Flutter"},
          {"label": "Native (iOS/Android)"}
        ]
      },
      {
        "label": "Backend",
        "children": [
          {"label": "API Design"},
          {"label": "Database"},
          {"label": "Authentication"}
        ]
      },
      {
        "label": "DevOps",
        "children": [
          {"label": "CI/CD"},
          {"label": "App Store Deployment"},
          {"label": "Monitoring"}
        ]
      },
      {
        "label": "Design",
        "children": [
          {"label": "UX Research"},
          {"label": "UI Design"},
          {"label": "Prototyping"}
        ]
      }
    ]
  },
  "title": "Mobile App Development Concept Map",
  "format": "svg",
  "theme": "default"
}
```

## Best Practices

1. **Start with central idea** - Clear main topic
2. **Branch logically** - Organize hierarchically
3. **Keep it focused** - Don't overcomplicate
4. **Use clear labels** - Concise, descriptive
5. **Group related concepts** - Visual organization
6. **Limit depth** - 3-4 levels maximum
7. **Use colors** - Differentiate categories

## Related Playbooks

- [render_mindmap.md](./render_mindmap.md)
- [render_flowchart.md](./render_flowchart.md)
- [render_block_diagram.md](./render_block_diagram.md)
