# Playbook: Render Class Diagram

## Description
This playbook creates UML class diagrams showing classes, attributes, methods, and relationships. Class diagrams are essential for visualizing object-oriented design, code architecture, and domain models.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Understanding of the class structure and relationships
- Knowledge of attributes, methods, and visibility modifiers
- Clear domain model or code architecture

## Steps

1. Define all classes
   - List class names
   - Define attributes with types and visibility
   - Define methods with parameters and return types
   - Add annotations for interfaces, abstract classes, enums

2. Define relationships
   - Map inheritance, composition, aggregation
   - Document associations between classes
   - Add cardinality where relevant

3. Call the render_class_diagram tool
   - Pass classes with attributes and methods
   - Pass relationships with types and cardinality

4. Review the generated diagram
   - Verify all classes and relationships are correct
   - Check that the model accurately represents the design

## MCP Tools Required

### mcp-mermaid-renderer

**Tool**: `render_class_diagram`
- **Parameters**:
  - `classes` (list of dict, required): List of class definitions. Each dict should have:
    - `name` (string): Class name
    - `attributes` (list, optional): Attributes as strings (e.g., "id: UUID", "+name: String", "-password: String") or dicts with {name, type, visibility}
      - Prefix: +/- for public/private, # for protected, ~ for package
    - `methods` (list, optional): Methods as strings (e.g., "login(): boolean", "save(data): void") or dicts with {name, parameters, return_type, visibility}
    - `annotation` (string, optional): Class stereotype like "Interface", "Abstract", "Enum"
  - `relationships` (list of dict, optional): List of relationships. Each dict should have:
    - `from_class`, `from`, or `source` (string): Source class name
    - `to_class`, `to`, or `target` (string): Target class name
    - `type` (string): Relationship type - "inheritance", "composition", "aggregation", "association", "dependency", "realization"
    - `label` (string, optional): Relationship description
    - `cardinality` (string, optional): Cardinality like "1", "0..*", "1..*"
  - `title` (string, optional): Diagram title
  - `format` (string): Output format - "svg" (default, recommended) or "png"
  - `theme` (string): Mermaid theme - "default", "dark", "forest", "neutral"
  - `bgcolor` (string): Background color (default: "transparent")
  - `filename` (string, optional): Suggested filename
- **Returns**: Artifact metadata with download URLs

## Example Usage

**Input**: "Create a class diagram for an e-commerce domain model"

**Process**:
1. Define classes: User, Order, OrderStatus
2. Define attributes and methods with visibility
3. Map relationships (User places Orders, Order has OrderStatus)

**Tool Call**:
```json
{
  "classes": [
    {
      "name": "User",
      "attributes": ["-id: UUID", "-email: String", "+name: String"],
      "methods": ["+login(email, password): boolean", "+logout(): void"]
    },
    {
      "name": "Order",
      "attributes": ["-id: UUID", "-total: Decimal", "+status: OrderStatus"],
      "methods": ["+addItem(item): void", "-calculateTotal(): Decimal"]
    },
    {
      "name": "OrderStatus",
      "annotation": "Enum"
    }
  ],
  "relationships": [
    {"from": "User", "to": "Order", "type": "association", "label": "places", "cardinality": "1..*"},
    {"from": "Order", "to": "OrderStatus", "type": "dependency"}
  ],
  "title": "E-Commerce Domain Model",
  "format": "svg",
  "theme": "default"
}
```

**Output**:
```
Class diagram rendered successfully!
- Format: SVG
- Classes: 3
- Relationships: 2
- Download URL: [artifact link]
```

## Expected Response Format

The tool returns an artifact object with:
- `download_url`: URL to download the rendered diagram
- `source_code`: Editable Mermaid syntax
- `format`: Output format (svg or png)
- `diagram_type`: "class"

## Common Use Cases

1. **Software Design**: Object-oriented design, API models, data structures
2. **Domain Modeling**: Business entities, domain-driven design
3. **Database Design**: ORM models, entity relationships
4. **Code Documentation**: Visualizing existing code structure
5. **Architecture Review**: System component relationships
6. **API Design**: Request/response models, DTOs

## Best Practices

1. **Visibility Modifiers**:
   - `+` public - accessible from anywhere
   - `-` private - accessible only within class
   - `#` protected - accessible to subclasses
   - `~` package - accessible within package
2. **Attribute Format**: "name: type" or with visibility "+name: type"
3. **Method Format**: "methodName(params): returnType"
4. **Relationship Types**:
   - Inheritance: "is-a" relationship (subclass extends superclass)
   - Composition: "has-a" with strong ownership (part dies with whole)
   - Aggregation: "has-a" with weak ownership (part exists independently)
   - Association: General relationship between classes
   - Dependency: One class uses another
   - Realization: Class implements interface
5. **Cardinality**: Use standard notation - "1", "0..1", "0..*", "1..*", "*"
6. **Annotations**: Use for interfaces, abstract classes, enums, stereotypes
7. **Complexity**: Keep to 5-8 classes per diagram for clarity

## Error Handling

- **Invalid Visibility**: Use only +, -, #, ~ prefixes
- **Missing Class Names**: All classes must have names
- **Invalid Relationships**: Relationship types must match supported types
- **Unknown Classes**: Relationship references must match defined class names
- **Malformed Attributes**: Use "name: type" format
- **Malformed Methods**: Use "name(params): returnType" format

## Notes

- Class names are case-sensitive
- Attributes and methods can be specified as strings or structured dicts
- String format is more concise: "+email: String" instead of {"name": "email", "type": "String", "visibility": "public"}
- Tool automatically parses visibility prefixes in string format
- Parameters in methods are comma-separated: "method(param1, param2): void"
- Flexible field names: from/from_class/source, to/to_class/target
- Relationships are rendered with appropriate arrow types automatically
- Maximum recommended classes: 10-12 for readability
- For large systems, create multiple diagrams focusing on different subsystems
