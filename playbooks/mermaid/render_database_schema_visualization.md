# Playbook: Visualize Database Schema

## Description
This playbook guides you through visualizing database schemas, including tables, columns, relationships, foreign keys, indexes, and constraints. Perfect for database documentation, understanding data models, planning schema migrations, and onboarding developers to your data architecture.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Understanding of your database schema
- Knowledge of table relationships and foreign keys
- List of entities and their attributes

## Steps

1. **Identify all entities (tables)**
   - List all database tables
   - Note key business entities
   - Identify lookup/reference tables
   - Document junction tables for many-to-many relationships

2. **Map table relationships**
   - Identify primary keys
   - Document foreign key relationships
   - Note relationship cardinality (one-to-one, one-to-many, many-to-many)
   - Map cascading delete/update rules

3. **Document table structure**
   - List important columns for each table
   - Note data types
   - Identify nullable vs required fields
   - Document unique constraints and indexes

4. **Choose the appropriate diagram type**
   - Use **er_diagram** for relational database schemas
   - Use **class_diagram** for ORM models (JPA, Django, ActiveRecord)

5. **Create the visualization**
   - Start with core entities
   - Add relationships with cardinality
   - Include important attributes
   - Document constraints and indexes in notes

## MCP Tools Required

### Primary Tool: render_er_diagram
Best for visualizing relational database schemas with tables and foreign key relationships.

See [render_er_diagram.md](./render_er_diagram.md) for full details.

### Secondary Tool: render_class_diagram
Useful for documenting ORM models and object-relational mapping.

See [render_class_diagram.md](./render_class_diagram.md) for full details.

## Recommended Diagram Type

### Primary: ER Diagram
**When to use**: Database documentation, schema planning, migration design

**Strengths**:
- Shows tables and their columns clearly
- Represents relationships with cardinality
- Documents primary and foreign keys
- Standard notation for database design

**Example structure**:
```json
{
  "entities": [
    {
      "name": "users",
      "attributes": [
        {"name": "id", "type": "INT", "key": "PK"},
        {"name": "email", "type": "VARCHAR(255)", "key": "UK"},
        {"name": "created_at", "type": "TIMESTAMP"}
      ]
    },
    {
      "name": "orders",
      "attributes": [
        {"name": "id", "type": "INT", "key": "PK"},
        {"name": "user_id", "type": "INT", "key": "FK"},
        {"name": "total", "type": "DECIMAL(10,2)"}
      ]
    }
  ],
  "relationships": [
    {
      "from": "users",
      "to": "orders",
      "type": "one_to_many",
      "label": "places"
    }
  ]
}
```

### Secondary: Class Diagram
**When to use**: ORM model documentation, object-oriented database design

**Strengths**:
- Shows inheritance hierarchies
- Documents model methods
- Represents OOP concepts
- Good for application-level data models

## Example Usage

### Scenario 1: E-commerce Database Schema

**User Request**: "Visualize our e-commerce database schema showing users, products, orders, and reviews"

```json
{
  "entities": [
    {
      "name": "users",
      "attributes": [
        {"name": "id", "type": "BIGINT", "key": "PK"},
        {"name": "email", "type": "VARCHAR(255)", "key": "UK"},
        {"name": "password_hash", "type": "VARCHAR(255)"},
        {"name": "first_name", "type": "VARCHAR(100)"},
        {"name": "last_name", "type": "VARCHAR(100)"},
        {"name": "phone", "type": "VARCHAR(20)"},
        {"name": "created_at", "type": "TIMESTAMP"},
        {"name": "updated_at", "type": "TIMESTAMP"}
      ]
    },
    {
      "name": "addresses",
      "attributes": [
        {"name": "id", "type": "BIGINT", "key": "PK"},
        {"name": "user_id", "type": "BIGINT", "key": "FK"},
        {"name": "street", "type": "VARCHAR(255)"},
        {"name": "city", "type": "VARCHAR(100)"},
        {"name": "state", "type": "VARCHAR(50)"},
        {"name": "postal_code", "type": "VARCHAR(20)"},
        {"name": "country", "type": "VARCHAR(50)"},
        {"name": "is_default", "type": "BOOLEAN"}
      ]
    },
    {
      "name": "categories",
      "attributes": [
        {"name": "id", "type": "INT", "key": "PK"},
        {"name": "name", "type": "VARCHAR(100)", "key": "UK"},
        {"name": "slug", "type": "VARCHAR(100)", "key": "UK"},
        {"name": "parent_id", "type": "INT", "key": "FK"}
      ]
    },
    {
      "name": "products",
      "attributes": [
        {"name": "id", "type": "BIGINT", "key": "PK"},
        {"name": "category_id", "type": "INT", "key": "FK"},
        {"name": "sku", "type": "VARCHAR(50)", "key": "UK"},
        {"name": "name", "type": "VARCHAR(255)"},
        {"name": "description", "type": "TEXT"},
        {"name": "price", "type": "DECIMAL(10,2)"},
        {"name": "stock_quantity", "type": "INT"},
        {"name": "created_at", "type": "TIMESTAMP"},
        {"name": "updated_at", "type": "TIMESTAMP"}
      ]
    },
    {
      "name": "orders",
      "attributes": [
        {"name": "id", "type": "BIGINT", "key": "PK"},
        {"name": "user_id", "type": "BIGINT", "key": "FK"},
        {"name": "shipping_address_id", "type": "BIGINT", "key": "FK"},
        {"name": "order_number", "type": "VARCHAR(50)", "key": "UK"},
        {"name": "status", "type": "ENUM", "comment": "pending, paid, shipped, delivered, cancelled"},
        {"name": "subtotal", "type": "DECIMAL(10,2)"},
        {"name": "tax", "type": "DECIMAL(10,2)"},
        {"name": "shipping", "type": "DECIMAL(10,2)"},
        {"name": "total", "type": "DECIMAL(10,2)"},
        {"name": "created_at", "type": "TIMESTAMP"},
        {"name": "updated_at", "type": "TIMESTAMP"}
      ]
    },
    {
      "name": "order_items",
      "attributes": [
        {"name": "id", "type": "BIGINT", "key": "PK"},
        {"name": "order_id", "type": "BIGINT", "key": "FK"},
        {"name": "product_id", "type": "BIGINT", "key": "FK"},
        {"name": "quantity", "type": "INT"},
        {"name": "unit_price", "type": "DECIMAL(10,2)"},
        {"name": "subtotal", "type": "DECIMAL(10,2)"}
      ]
    },
    {
      "name": "reviews",
      "attributes": [
        {"name": "id", "type": "BIGINT", "key": "PK"},
        {"name": "product_id", "type": "BIGINT", "key": "FK"},
        {"name": "user_id", "type": "BIGINT", "key": "FK"},
        {"name": "rating", "type": "INT", "comment": "1-5 stars"},
        {"name": "title", "type": "VARCHAR(255)"},
        {"name": "comment", "type": "TEXT"},
        {"name": "created_at", "type": "TIMESTAMP"}
      ]
    },
    {
      "name": "payments",
      "attributes": [
        {"name": "id", "type": "BIGINT", "key": "PK"},
        {"name": "order_id", "type": "BIGINT", "key": "FK"},
        {"name": "payment_method", "type": "ENUM", "comment": "card, paypal, bank_transfer"},
        {"name": "amount", "type": "DECIMAL(10,2)"},
        {"name": "status", "type": "ENUM", "comment": "pending, completed, failed, refunded"},
        {"name": "transaction_id", "type": "VARCHAR(255)"},
        {"name": "created_at", "type": "TIMESTAMP"}
      ]
    }
  ],
  "relationships": [
    {
      "from": "users",
      "to": "addresses",
      "type": "one_to_many",
      "label": "has"
    },
    {
      "from": "users",
      "to": "orders",
      "type": "one_to_many",
      "label": "places"
    },
    {
      "from": "users",
      "to": "reviews",
      "type": "one_to_many",
      "label": "writes"
    },
    {
      "from": "categories",
      "to": "categories",
      "type": "one_to_many",
      "label": "parent/child"
    },
    {
      "from": "categories",
      "to": "products",
      "type": "one_to_many",
      "label": "contains"
    },
    {
      "from": "products",
      "to": "order_items",
      "type": "one_to_many",
      "label": "ordered in"
    },
    {
      "from": "products",
      "to": "reviews",
      "type": "one_to_many",
      "label": "has"
    },
    {
      "from": "orders",
      "to": "order_items",
      "type": "one_to_many",
      "label": "contains"
    },
    {
      "from": "orders",
      "to": "payments",
      "type": "one_to_many",
      "label": "paid by"
    },
    {
      "from": "addresses",
      "to": "orders",
      "type": "one_to_many",
      "label": "ships to"
    }
  ],
  "title": "E-commerce Database Schema",
  "format": "svg",
  "theme": "default"
}
```

### Scenario 2: Multi-Tenant SaaS Database

**User Request**: "Show our multi-tenant database schema with organization and team hierarchy"

```json
{
  "entities": [
    {
      "name": "organizations",
      "attributes": [
        {"name": "id", "type": "UUID", "key": "PK"},
        {"name": "name", "type": "VARCHAR(255)"},
        {"name": "subdomain", "type": "VARCHAR(100)", "key": "UK"},
        {"name": "plan", "type": "ENUM", "comment": "free, starter, pro, enterprise"},
        {"name": "created_at", "type": "TIMESTAMP"}
      ]
    },
    {
      "name": "teams",
      "attributes": [
        {"name": "id", "type": "UUID", "key": "PK"},
        {"name": "organization_id", "type": "UUID", "key": "FK"},
        {"name": "name", "type": "VARCHAR(255)"},
        {"name": "created_at", "type": "TIMESTAMP"}
      ]
    },
    {
      "name": "users",
      "attributes": [
        {"name": "id", "type": "UUID", "key": "PK"},
        {"name": "email", "type": "VARCHAR(255)", "key": "UK"},
        {"name": "name", "type": "VARCHAR(255)"},
        {"name": "created_at", "type": "TIMESTAMP"}
      ]
    },
    {
      "name": "organization_users",
      "attributes": [
        {"name": "id", "type": "UUID", "key": "PK"},
        {"name": "organization_id", "type": "UUID", "key": "FK"},
        {"name": "user_id", "type": "UUID", "key": "FK"},
        {"name": "role", "type": "ENUM", "comment": "owner, admin, member"},
        {"name": "joined_at", "type": "TIMESTAMP"}
      ]
    },
    {
      "name": "team_members",
      "attributes": [
        {"name": "id", "type": "UUID", "key": "PK"},
        {"name": "team_id", "type": "UUID", "key": "FK"},
        {"name": "user_id", "type": "UUID", "key": "FK"},
        {"name": "role", "type": "ENUM", "comment": "lead, member"},
        {"name": "joined_at", "type": "TIMESTAMP"}
      ]
    },
    {
      "name": "projects",
      "attributes": [
        {"name": "id", "type": "UUID", "key": "PK"},
        {"name": "team_id", "type": "UUID", "key": "FK"},
        {"name": "name", "type": "VARCHAR(255)"},
        {"name": "status", "type": "ENUM", "comment": "active, archived"},
        {"name": "created_at", "type": "TIMESTAMP"}
      ]
    },
    {
      "name": "tasks",
      "attributes": [
        {"name": "id", "type": "UUID", "key": "PK"},
        {"name": "project_id", "type": "UUID", "key": "FK"},
        {"name": "assigned_to", "type": "UUID", "key": "FK"},
        {"name": "title", "type": "VARCHAR(255)"},
        {"name": "status", "type": "ENUM", "comment": "todo, in_progress, done"},
        {"name": "priority", "type": "ENUM", "comment": "low, medium, high"},
        {"name": "due_date", "type": "DATE"},
        {"name": "created_at", "type": "TIMESTAMP"}
      ]
    }
  ],
  "relationships": [
    {
      "from": "organizations",
      "to": "teams",
      "type": "one_to_many",
      "label": "has"
    },
    {
      "from": "organizations",
      "to": "organization_users",
      "type": "one_to_many",
      "label": "has members"
    },
    {
      "from": "users",
      "to": "organization_users",
      "type": "one_to_many",
      "label": "member of"
    },
    {
      "from": "users",
      "to": "team_members",
      "type": "one_to_many",
      "label": "member of"
    },
    {
      "from": "teams",
      "to": "team_members",
      "type": "one_to_many",
      "label": "has members"
    },
    {
      "from": "teams",
      "to": "projects",
      "type": "one_to_many",
      "label": "owns"
    },
    {
      "from": "projects",
      "to": "tasks",
      "type": "one_to_many",
      "label": "contains"
    },
    {
      "from": "users",
      "to": "tasks",
      "type": "one_to_many",
      "label": "assigned"
    }
  ],
  "title": "Multi-Tenant SaaS Database Schema",
  "format": "svg",
  "theme": "default"
}
```

### Scenario 3: Content Management System (CMS)

**User Request**: "Visualize our CMS database with posts, pages, media, and taxonomies"

```json
{
  "entities": [
    {
      "name": "authors",
      "attributes": [
        {"name": "id", "type": "INT", "key": "PK"},
        {"name": "username", "type": "VARCHAR(50)", "key": "UK"},
        {"name": "email", "type": "VARCHAR(255)", "key": "UK"},
        {"name": "bio", "type": "TEXT"}
      ]
    },
    {
      "name": "posts",
      "attributes": [
        {"name": "id", "type": "INT", "key": "PK"},
        {"name": "author_id", "type": "INT", "key": "FK"},
        {"name": "title", "type": "VARCHAR(255)"},
        {"name": "slug", "type": "VARCHAR(255)", "key": "UK"},
        {"name": "content", "type": "LONGTEXT"},
        {"name": "excerpt", "type": "TEXT"},
        {"name": "status", "type": "ENUM", "comment": "draft, published, archived"},
        {"name": "published_at", "type": "TIMESTAMP"},
        {"name": "created_at", "type": "TIMESTAMP"}
      ]
    },
    {
      "name": "pages",
      "attributes": [
        {"name": "id", "type": "INT", "key": "PK"},
        {"name": "parent_id", "type": "INT", "key": "FK"},
        {"name": "title", "type": "VARCHAR(255)"},
        {"name": "slug", "type": "VARCHAR(255)", "key": "UK"},
        {"name": "content", "type": "LONGTEXT"},
        {"name": "template", "type": "VARCHAR(100)"},
        {"name": "status", "type": "ENUM", "comment": "draft, published"}
      ]
    },
    {
      "name": "categories",
      "attributes": [
        {"name": "id", "type": "INT", "key": "PK"},
        {"name": "name", "type": "VARCHAR(100)", "key": "UK"},
        {"name": "slug", "type": "VARCHAR(100)", "key": "UK"},
        {"name": "description", "type": "TEXT"}
      ]
    },
    {
      "name": "tags",
      "attributes": [
        {"name": "id", "type": "INT", "key": "PK"},
        {"name": "name", "type": "VARCHAR(50)", "key": "UK"},
        {"name": "slug", "type": "VARCHAR(50)", "key": "UK"}
      ]
    },
    {
      "name": "post_categories",
      "attributes": [
        {"name": "post_id", "type": "INT", "key": "FK"},
        {"name": "category_id", "type": "INT", "key": "FK"}
      ]
    },
    {
      "name": "post_tags",
      "attributes": [
        {"name": "post_id", "type": "INT", "key": "FK"},
        {"name": "tag_id", "type": "INT", "key": "FK"}
      ]
    },
    {
      "name": "media",
      "attributes": [
        {"name": "id", "type": "INT", "key": "PK"},
        {"name": "author_id", "type": "INT", "key": "FK"},
        {"name": "filename", "type": "VARCHAR(255)"},
        {"name": "file_path", "type": "VARCHAR(500)"},
        {"name": "mime_type", "type": "VARCHAR(100)"},
        {"name": "file_size", "type": "BIGINT"},
        {"name": "alt_text", "type": "VARCHAR(255)"},
        {"name": "uploaded_at", "type": "TIMESTAMP"}
      ]
    },
    {
      "name": "comments",
      "attributes": [
        {"name": "id", "type": "INT", "key": "PK"},
        {"name": "post_id", "type": "INT", "key": "FK"},
        {"name": "parent_id", "type": "INT", "key": "FK"},
        {"name": "author_name", "type": "VARCHAR(100)"},
        {"name": "author_email", "type": "VARCHAR(255)"},
        {"name": "content", "type": "TEXT"},
        {"name": "status", "type": "ENUM", "comment": "pending, approved, spam"},
        {"name": "created_at", "type": "TIMESTAMP"}
      ]
    }
  ],
  "relationships": [
    {
      "from": "authors",
      "to": "posts",
      "type": "one_to_many",
      "label": "writes"
    },
    {
      "from": "authors",
      "to": "media",
      "type": "one_to_many",
      "label": "uploads"
    },
    {
      "from": "pages",
      "to": "pages",
      "type": "one_to_many",
      "label": "parent/child"
    },
    {
      "from": "posts",
      "to": "post_categories",
      "type": "one_to_many",
      "label": "belongs to"
    },
    {
      "from": "categories",
      "to": "post_categories",
      "type": "one_to_many",
      "label": "contains"
    },
    {
      "from": "posts",
      "to": "post_tags",
      "type": "one_to_many",
      "label": "tagged with"
    },
    {
      "from": "tags",
      "to": "post_tags",
      "type": "one_to_many",
      "label": "applied to"
    },
    {
      "from": "posts",
      "to": "comments",
      "type": "one_to_many",
      "label": "has"
    },
    {
      "from": "comments",
      "to": "comments",
      "type": "one_to_many",
      "label": "replies to"
    }
  ],
  "title": "Content Management System Database Schema",
  "format": "svg",
  "theme": "default"
}
```

## Alternative Approaches

### Option 1: Class Diagram for ORM Models
Use class diagrams when:
- Documenting Django models, JPA entities, or ActiveRecord models
- Showing model inheritance hierarchies
- Representing model methods and business logic
- Visualizing object-oriented database design

### Option 2: Multiple Diagrams by Domain
For large databases:
- User management domain (users, roles, permissions)
- Content domain (posts, pages, media)
- Commerce domain (products, orders, payments)
- Analytics domain (events, sessions, metrics)

### Option 3: Simplified High-Level View
Create abstracted views:
- Show only major entities
- Omit detailed columns
- Focus on relationship patterns
- Good for presentations

## Best Practices

### 1. Focus on Important Columns
- Always include primary keys
- Show foreign keys
- Include unique constraints
- Document important business fields
- Omit system fields (created_by, updated_by) unless relevant

### 2. Use Clear Naming Conventions
- Use singular or plural consistently (user vs users)
- Follow database naming conventions (snake_case, camelCase)
- Use descriptive table names
- Avoid abbreviations unless standard

### 3. Document Cardinality
- Show one-to-one, one-to-many, many-to-many relationships
- Note optional vs required relationships
- Document junction tables for many-to-many

### 4. Include Data Types
- Show column data types (INT, VARCHAR, TIMESTAMP)
- Note length constraints (VARCHAR(255))
- Document precision for decimals (DECIMAL(10,2))

### 5. Mark Key Constraints
- PK for primary keys
- FK for foreign keys
- UK for unique keys
- Add notes for composite keys

### 6. Group Related Tables
- Organize by domain or module
- Use colors or layout to show groupings
- Separate core vs auxiliary tables

### 7. Document Enums and Constraints
- Show enum values in comments
- Note check constraints
- Document default values

## Common Variations

### Variation 1: Temporal Database Schema
For audit trails and history:
- Show version/history tables
- Document temporal foreign keys
- Note valid_from/valid_to columns

### Variation 2: Sharded Database Schema
For horizontally partitioned data:
- Show shard key columns
- Document partitioning strategy
- Note cross-shard relationships

### Variation 3: Materialized Views
Show derived data structures:
- Document source tables
- Show refresh strategy
- Note indexed columns

### Variation 4: Database Migration Schema
Show before/after states:
- Original schema
- Target schema after migration
- Highlight changes

### Variation 5: NoSQL Document Schema
For MongoDB/DocumentDB:
- Show document structure
- Note embedded vs referenced documents
- Document indexes

## Related Playbooks

### Core Diagram Types
- [render_er_diagram.md](./render_er_diagram.md) - Database entity-relationship diagrams
- [render_class_diagram.md](./render_class_diagram.md) - ORM model class diagrams

### Architecture Playbooks
- [render_microservices_architecture.md](./render_microservices_architecture.md) - System architecture
- [render_data_pipeline.md](./render_data_pipeline.md) - Data flow and ETL

### Related Scenarios
- [render_class_hierarchy.md](./render_class_hierarchy.md) - OOP inheritance

## Notes

- For databases with >15 tables, consider creating multiple domain-specific diagrams
- Include indexes in notes or descriptions (especially for performance-critical queries)
- Document cascading delete/update rules in relationship labels or notes
- Note any soft-delete patterns (deleted_at columns)
- For large schemas, create both detailed and high-level overview diagrams
- Consider showing sample data or data volume estimates in notes
- Export in SVG format for database documentation
- Keep diagrams synced with actual database schema (consider automation)
- Use database schema export tools to generate initial entity lists
- Document any database-specific features (PostgreSQL arrays, JSON columns, etc.)
