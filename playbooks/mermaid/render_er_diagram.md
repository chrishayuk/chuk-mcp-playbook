# Playbook: Render ER Diagram

## Description
This playbook creates Entity-Relationship (ER) diagrams for database schema design. ER diagrams visualize database entities, their attributes, and relationships, making them essential for database design and documentation.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Understanding of database schema structure
- Knowledge of entities, attributes, and relationships
- Clear identification of primary keys, foreign keys, and cardinality

## Steps

1. Define all entities (tables)
   - List all database tables
   - Define attributes with data types
   - Mark primary keys (PK), foreign keys (FK), and unique keys (UK)

2. Define relationships
   - Map relationships between entities
   - Specify cardinality (one-to-one, one-to-many, many-to-many)
   - Mark identifying vs non-identifying relationships

3. Call the render_er_diagram tool
   - Pass entities with attributes and keys
   - Pass relationships with cardinality

4. Review the generated diagram
   - Verify all entities and relationships
   - Check that keys are properly marked

## MCP Tools Required

### mcp-mermaid-renderer

**Tool**: `render_er_diagram`
- **Parameters**:
  - `entities` (list of dict, required): Entities with name and attributes. Each dict should have:
    - `name`, `entity`, or `table` (string): Entity/table name
    - `attributes` (list): Attributes as strings (e.g., "customer_id PK", "name varchar", "email string UK") or dicts with {name, type, key}
      - Key values: "PK" (primary key), "FK" (foreign key), "UK" (unique key)
  - `relationships` (list of dict, required): Relationships between entities. Each dict should have:
    - `from_entity`, `from`, or `source` (string): Source entity name
    - `to_entity`, `to`, or `target` (string): Target entity name
    - `from_cardinality` (string): "zero-or-one", "exactly-one", "zero-or-more", "one-or-more"
    - `to_cardinality` (string): "zero-or-one", "exactly-one", "zero-or-more", "one-or-more"
    - `label` (string, optional): Relationship description
    - `identifying` (boolean, optional): true for identifying relationships (default: false)
  - `title` (string, optional): Diagram title
  - `format` (string): Output format - "svg" (default, recommended) or "png"
  - `theme` (string): Mermaid theme - "default", "dark", "forest", "neutral"
  - `bgcolor` (string): Background color (default: "transparent")
  - `filename` (string, optional): Suggested filename
- **Returns**: Artifact metadata with download URLs

## Example Usage

**Input**: "Create an ER diagram for an e-commerce database"

**Process**:
1. Define entities: users, orders, order_items, products
2. Define attributes with keys (PK, FK, UK)
3. Map relationships with cardinality

**Tool Call**:
```json
{
  "entities": [
    {
      "name": "users",
      "attributes": [
        "id uuid PK",
        "email varchar UK",
        "name varchar",
        "created_at timestamp"
      ]
    },
    {
      "name": "orders",
      "attributes": [
        "id uuid PK",
        "user_id uuid FK",
        "total decimal",
        "status varchar",
        "created_at timestamp"
      ]
    },
    {
      "name": "order_items",
      "attributes": [
        "id uuid PK",
        "order_id uuid FK",
        "product_id uuid FK",
        "quantity int",
        "price decimal"
      ]
    },
    {
      "name": "products",
      "attributes": [
        "id uuid PK",
        "name varchar",
        "price decimal",
        "stock int"
      ]
    }
  ],
  "relationships": [
    {
      "from_entity": "users",
      "to_entity": "orders",
      "from_cardinality": "exactly-one",
      "to_cardinality": "zero-or-more",
      "label": "places"
    },
    {
      "from_entity": "orders",
      "to_entity": "order_items",
      "from_cardinality": "exactly-one",
      "to_cardinality": "one-or-more",
      "label": "contains",
      "identifying": true
    },
    {
      "from_entity": "products",
      "to_entity": "order_items",
      "from_cardinality": "exactly-one",
      "to_cardinality": "zero-or-more",
      "label": "included in"
    }
  ],
  "title": "E-Commerce Database Schema",
  "format": "svg",
  "theme": "default"
}
```

**Output**:
```
ER diagram rendered successfully!
- Format: SVG
- Entities: 4
- Relationships: 3
- Download URL: [artifact link]
```

## Expected Response Format

The tool returns an artifact object with:
- `download_url`: URL to download the rendered diagram
- `source_code`: Editable Mermaid syntax
- `format`: Output format (svg or png)
- `diagram_type`: "er"

## Common Use Cases

1. **Database Design**: New schema design, schema documentation
2. **Data Modeling**: Conceptual and logical data models
3. **Schema Migration**: Planning database changes and refactoring
4. **API Design**: Backend data structure planning
5. **Documentation**: Technical documentation for developers
6. **Database Review**: Understanding existing database structure

## Best Practices

1. **Attribute Format**:
   - String format: "field_name data_type KEY" (e.g., "id uuid PK")
   - Dict format: {"name": "id", "type": "uuid", "key": "PK"}
2. **Key Types**:
   - PK: Primary key (uniquely identifies record)
   - FK: Foreign key (references another table)
   - UK: Unique key (must be unique but not primary)
3. **Cardinality**:
   - "exactly-one": Must have exactly one (1)
   - "zero-or-one": Optional, at most one (0..1)
   - "one-or-more": At least one, possibly many (1..*)
   - "zero-or-more": Optional, possibly many (0..*)
4. **Identifying Relationships**: Set identifying=true when child entity depends on parent
5. **Naming**: Use consistent naming conventions (snake_case for database entities)
6. **Complexity**: Keep to 6-10 entities per diagram for clarity
7. **Data Types**: Use standard database types (varchar, int, uuid, decimal, timestamp)

## Error Handling

- **Invalid Cardinality**: Use only the four supported cardinality values
- **Missing Entity Names**: All entities must have names
- **Unknown Entities**: Relationship references must match defined entity names
- **Invalid Keys**: Use only PK, FK, or UK for key types
- **Malformed Attributes**: String format should be "name type" or "name type KEY"

## Notes

- Entity names are case-sensitive (typically lowercase with underscores)
- Attributes can be strings or dicts - string format is more concise
- String attribute format: "field_name data_type [KEY]"
- Tool supports flexible field names: name/entity/table, from/from_entity, to/to_entity
- Identifying relationships are visually distinguished in the diagram
- Foreign keys should reference primary keys in related entities
- For many-to-many relationships, create a junction/bridge table with FKs to both entities
- Recommended maximum: 10-12 entities per diagram for readability
- For large schemas, create multiple diagrams focusing on different modules/domains
- Cardinality shorthand notation supported: "1-to-many", "many-to-many", etc.
