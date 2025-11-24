# Playbook: Render Architecture Diagram

## Description
This playbook creates architecture diagrams showing services, groups, and connections. Architecture diagrams are perfect for cloud architecture, system design, infrastructure diagrams, and visualizing distributed systems with grouped components.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Understanding of system services/components
- Clear identification of architectural layers or groups
- Knowledge of service connections and communication

## Steps

1. Define services
   - List all services/components
   - Assign unique IDs
   - Choose appropriate icons (cloud, database, server, etc.)
   - Optionally assign to groups

2. Define groups (optional)
   - Create logical groupings (tiers, layers, zones)
   - Assign services to groups

3. Define connections
   - Map connections between services
   - Add labels for protocols or descriptions
   - Specify directions if needed

4. Call the render_architecture_diagram tool
   - Pass services with id, label, icon, and group
   - Pass edges with from/to service IDs
   - Pass groups if using tier/layer organization

5. Review the generated diagram
   - Verify all services and connections
   - Check that groupings are logical

## MCP Tools Required

### mcp-mermaid-renderer

**Tool**: `render_architecture_diagram`
- **Parameters**:
  - `services` (list of dict, required): Services/components. Each dict MUST have:
    - `id` (string, REQUIRED): Unique service identifier
    - `label` or `name` (string, REQUIRED): Display name
    - `icon` (string, optional): "cloud", "database", "disk", "internet", "server" (default: "server")
    - `group` (string, optional): Parent group ID
  - `edges` (list of dict, required): Connections between services. Each dict MUST have:
    - `from_service`, `from`, or `source` (string, REQUIRED): Source service ID
    - `to_service`, `to`, or `target` (string, REQUIRED): Target service ID
    - `from_direction` (string, optional): Exit direction - "L", "R", "T", "B"
    - `to_direction` (string, optional): Entry direction - "L", "R", "T", "B"
    - `arrow` (boolean, optional): Show arrow (default: true)
    - `label` (string, optional): Connection description
  - `groups` (list of dict, optional): Group containers. Each dict MUST have:
    - `id` (string, REQUIRED): Unique group identifier
    - `label` or `name` (string, REQUIRED): Display name
    - `icon` (string, optional): Icon type (default: "cloud")
    - `members` or `services` (list, optional): List of service IDs in this group
  - `title` (string, optional): Diagram title
  - `format` (string): Output format - "svg" (default, recommended) or "png"
  - `theme` (string): Mermaid theme - "default", "dark", "forest", "neutral"
  - `bgcolor` (string): Background color (default: "transparent")
  - `filename` (string, optional): Suggested filename
- **Returns**: Artifact metadata with download URLs

## Example Usage

**Input**: "Create an architecture diagram for a three-tier web application"

**Process**:
1. Define services: Web servers, app servers, database
2. Group by tier: public, application, data
3. Map connections

**Tool Call**:
```json
{
  "services": [
    {"id": "lb", "label": "Load Balancer", "icon": "internet", "group": "public"},
    {"id": "web1", "label": "Web Server 1", "icon": "server", "group": "public"},
    {"id": "web2", "label": "Web Server 2", "icon": "server", "group": "public"},
    {"id": "app1", "label": "App Server 1", "icon": "server", "group": "app"},
    {"id": "app2", "label": "App Server 2", "icon": "server", "group": "app"},
    {"id": "db", "label": "PostgreSQL", "icon": "database", "group": "data"},
    {"id": "cache", "label": "Redis", "icon": "database", "group": "data"}
  ],
  "edges": [
    {"from": "lb", "to": "web1", "label": "HTTPS"},
    {"from": "lb", "to": "web2", "label": "HTTPS"},
    {"from": "web1", "to": "app1", "label": "HTTP"},
    {"from": "web1", "to": "app2", "label": "HTTP"},
    {"from": "web2", "to": "app1", "label": "HTTP"},
    {"from": "web2", "to": "app2", "label": "HTTP"},
    {"from": "app1", "to": "db", "label": "SQL"},
    {"from": "app2", "to": "db", "label": "SQL"},
    {"from": "app1", "to": "cache", "label": "GET/SET"},
    {"from": "app2", "to": "cache", "label": "GET/SET"}
  ],
  "groups": [
    {"id": "public", "label": "Public Tier", "icon": "internet"},
    {"id": "app", "label": "Application Tier", "icon": "server"},
    {"id": "data", "label": "Data Tier", "icon": "database"}
  ],
  "title": "Three-Tier Web Application",
  "format": "svg",
  "theme": "default"
}
```

**Output**:
```
Architecture diagram rendered successfully!
- Format: SVG
- Services: 7
- Groups: 3
- Connections: 10
- Download URL: [artifact link]
```

## Expected Response Format

The tool returns an artifact object with:
- `download_url`: URL to download the rendered diagram
- `source_code`: Editable Mermaid syntax
- `format`: Output format (svg or png)
- `diagram_type`: "architecture"

## Common Use Cases

1. **Cloud Architecture**: AWS/Azure/GCP infrastructure, multi-tier applications
2. **Microservices**: Service mesh, API gateway, microservice communication
3. **Network Architecture**: DMZ, internal zones, security layers
4. **Data Architecture**: Data pipelines, ETL, data lakes
5. **Container Orchestration**: Kubernetes clusters, Docker architecture
6. **Hybrid Cloud**: On-premise and cloud integration

## Best Practices

1. **Service IDs**: Use short, lowercase identifiers (e.g., "web", "db", "api")
2. **Service Labels**: Clear, descriptive names (2-4 words)
3. **Icons**:
   - "server": Application servers, compute instances
   - "database": Databases, data stores
   - "cloud": Cloud services, grouped resources
   - "internet": Public-facing components, load balancers
   - "disk": Storage, file systems
4. **Groups**: Organize by tier (public/app/data), zone (dmz/internal), or layer
5. **Edge Labels**: Include protocol or communication type (HTTP, SQL, gRPC)
6. **Directions**: Use from_direction/to_direction for specific routing needs
7. **IMPORTANT**: Edges must reference actual service IDs
   - Edges with undefined service IDs are automatically skipped
   - Verify all edge references exist in services list
8. **Complexity**: Keep to 10-15 services for clarity

## Error Handling

- **Missing Required Fields**: All services need id and label/name
- **Invalid Service References**: Edge from/to must reference existing service IDs
- **Undefined Services in Edges**: Edges with undefined services are automatically skipped with warning
- **Invalid Icons**: Use only supported icon types
- **Missing Group ID**: Groups must have unique IDs
- **Validation Errors**: Tool provides detailed error messages for invalid inputs

## Notes

- Service IDs are case-sensitive
- Services can be assigned to groups via:
  1. Service's `group` field (direct assignment)
  2. Group's `members` field (list of service IDs)
- Tool accepts flexible field names:
  - Services: id/alias, label/name
  - Edges: from/from_service/source, to/to_service/target
  - Groups: label/name, members/services
- Edges with undefined service IDs are skipped (not an error)
- Groups provide visual organization (tiers, layers, zones)
- Directions (L/R/T/B) control edge routing
- Arrows are shown by default (set arrow=false to hide)
- Tool validates all required fields and provides helpful error messages
- Recommended maximum: 15 services, 3-4 groups
- For large architectures:
  - Create multiple focused diagrams
  - Use groups to organize complexity
  - Consider hierarchical diagrams
