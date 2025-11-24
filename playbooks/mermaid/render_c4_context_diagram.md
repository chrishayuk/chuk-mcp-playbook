# Playbook: Render C4 Context Diagram

## Description
This playbook creates C4 context diagrams showing system architecture at the highest level. C4 context diagrams visualize how software systems interact with users and external systems, providing a bird's-eye view of the system landscape.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Understanding of the system architecture
- Identification of all people, systems, and their relationships

## Steps

1. Identify people/actors
   - List all user types and personas
   - Assign unique IDs and descriptive labels
   - Keep descriptions concise (under 80 chars)

2. Identify systems
   - List internal and external systems
   - Mark external/third-party systems
   - Keep descriptions brief

3. Map relationships
   - Document how people use systems
   - Document how systems interact
   - Use very short labels (2-4 words)
   - Specify technology/protocol where relevant

4. Call the render_c4_context_diagram tool
   - Pass title, people, systems, and relationships
   - Keep all descriptions concise for best layout

5. Review the generated diagram
   - Verify all components and relationships are shown
   - Check that the system boundaries are clear

## MCP Tools Required

### mcp-mermaid-renderer

**Tool**: `render_c4_context_diagram`
- **Parameters**:
  - `title` (string, required): Diagram title
  - `systems` (list of dict, required): List of systems. Each dict should have:
    - `id` or `alias` (string): Short identifier (no spaces)
    - `name` or `label` (string): Display name
    - `description` (string, optional): Brief description (auto-truncated to 80 chars)
    - `external` (boolean, optional): true for external/third-party systems (default: false)
  - `relationships` (list of dict, required): List of relationships. Each dict should have:
    - `from` or `source` (string): Source element id
    - `to` or `target` (string): Target element id
    - `label` or `description` (string): Brief label (auto-truncated to 50 chars)
    - `technology` (string, optional): Protocol like "HTTPS", "REST", "SQL"
  - `people` (list of dict, optional): List of people/actors. Each dict should have:
    - `id` or `alias` (string): Short identifier (no spaces)
    - `name` or `label` (string): Display name
    - `description` (string, optional): Brief description (auto-truncated to 80 chars)
  - `format` (string): Output format - "svg" (default, recommended) or "png"
  - `theme` (string): Mermaid theme - "default", "dark", "forest", "neutral"
  - `bgcolor` (string): Background color (default: "transparent")
  - `filename` (string, optional): Suggested filename
- **Returns**: Artifact metadata with download URLs

## Example Usage

**Input**: "Create a C4 context diagram for an e-commerce platform"

**Process**:
1. Identify actors: Customer, Admin
2. Identify systems: E-Commerce Platform (internal), Payment Gateway (external), Email Service (external)
3. Map relationships between actors and systems

**Tool Call**:
```json
{
  "title": "E-Commerce System Context",
  "people": [
    {"id": "customer", "name": "Customer", "description": "Online shopper"},
    {"id": "admin", "name": "Admin", "description": "Store administrator"}
  ],
  "systems": [
    {"id": "shop", "name": "E-Commerce Platform", "description": "Main shopping system"},
    {"id": "payment", "name": "Payment Gateway", "description": "Stripe payment processing", "external": true},
    {"id": "email", "name": "Email Service", "description": "SendGrid email delivery", "external": true}
  ],
  "relationships": [
    {"from": "customer", "to": "shop", "label": "Browse and purchase", "technology": "HTTPS"},
    {"from": "admin", "to": "shop", "label": "Manages", "technology": "HTTPS"},
    {"from": "shop", "to": "payment", "label": "Process payments", "technology": "REST API"},
    {"from": "shop", "to": "email", "label": "Send notifications", "technology": "SMTP"}
  ],
  "format": "svg",
  "theme": "default"
}
```

**Output**:
```
C4 context diagram rendered successfully!
- Format: SVG
- People: 2
- Systems: 3
- Relationships: 4
- Download URL: [artifact link]
```

## Expected Response Format

The tool returns an artifact object with:
- `download_url`: URL to download the rendered diagram
- `source_code`: Editable Mermaid syntax
- `format`: Output format (svg or png)
- `diagram_type`: "c4_context"

## Common Use Cases

1. **Enterprise Architecture**: Organization-wide system landscape, integration overview
2. **Product Documentation**: High-level system overview for stakeholders
3. **Project Planning**: Understanding system boundaries and dependencies
4. **Vendor Management**: Identifying external systems and integrations
5. **Security Review**: Understanding system perimeter and external touchpoints
6. **Onboarding**: Introducing new team members to system architecture

## Best Practices

1. **Descriptions**: Keep very concise (under 80 chars). Avoid verbose text.
   - Good: "Payment processing"
   - Bad: "This system handles all payment processing including credit cards, PayPal, and Apple Pay with fraud detection"
2. **Relationship Labels**: Use 2-4 words maximum
   - Good: "Uses", "Manages", "Sends emails"
   - Bad: "Accesses the platform to view accounts and manage transactions"
3. **External Systems**: Always mark third-party systems as external=true
4. **Technology Labels**: Keep short - "HTTPS", "REST", "SQL", "SMTP"
5. **System IDs**: Use short, lowercase identifiers without spaces
6. **Focus**: Show only the most important relationships, avoid clutter
7. **Level**: This is the highest level - don't include implementation details

## Error Handling

- **Long Descriptions**: Automatically truncated to 80 chars for systems/people
- **Long Labels**: Automatically truncated to 50 chars for relationships
- **Missing Required Fields**: Ensure all systems/people have id and name
- **Invalid References**: All relationship from/to must reference existing ids
- **Complex Diagrams**: For layouts with many elements, consider splitting or using render_mermaid_diagram for manual control

## Notes

- C4 stands for Context, Containers, Components, Code - this is the Context level
- IDs are case-sensitive and should not contain spaces
- External systems are visually distinguished in the diagram
- The tool automatically handles layout optimization
- Descriptions and labels are automatically truncated for best visual layout
- For complex architectures (>10 systems), consider creating multiple focused diagrams
- Tool accepts flexible field names: id/alias, name/label, from/source, to/target
- Recommended maximum: 6-8 systems for clarity
