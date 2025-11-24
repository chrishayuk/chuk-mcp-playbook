# Playbook: Visualize Microservices Architecture

## Description
This playbook guides you through visualizing microservices architecture, including service topology, inter-service communication patterns, external dependencies, API gateways, and infrastructure components. Perfect for documenting system architecture, onboarding new team members, or planning architectural changes.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Understanding of your microservices ecosystem
- Knowledge of service dependencies and communication patterns
- List of external services and infrastructure components

## ⚠️ CRITICAL: Participant Type Warning (for Sequence Diagrams)

**If using sequence diagrams, ONLY use these participant types:**
- `"actor"` - for human users/external clients
- `"participant"` - for ALL services, databases, queues, APIs

**DO NOT USE**: `"boundary"`, `"control"`, `"entity"`, `"database"`, etc. These will cause rendering failures!

Use descriptive **labels** to distinguish roles: `{"id": "db", "label": "User Database", "type": "participant"}` ✅

## Steps

1. **Identify all services and components**
   - List all microservices in your system
   - Identify external services (databases, message queues, cache layers)
   - Note infrastructure components (load balancers, API gateways)
   - Document third-party integrations

2. **Map service relationships**
   - Document which services communicate with each other
   - Identify synchronous vs asynchronous communication
   - Note data flow directions
   - Document external dependencies

3. **Choose the appropriate diagram type**
   - Use **architecture_diagram** for detailed technical architecture
   - Use **c4_context_diagram** for high-level system context
   - Use **sequence_diagram** for specific interaction flows
   - Use **block_diagram** for simplified logical groupings

4. **Create the visualization**
   - Start with high-level C4 context for stakeholders
   - Use architecture diagram for engineering teams
   - Add sequence diagrams for critical flows
   - Document with clear labels and descriptions

5. **Review and iterate**
   - Verify all services are represented
   - Ensure communication patterns are accurate
   - Add notes for important architectural decisions

## MCP Tools Required

### Primary Tool: render_architecture_diagram
Best for detailed technical architecture with multiple service types and communication patterns.

See [render_architecture_diagram.md](./render_architecture_diagram.md) for full details.

### Primary Tool: render_c4_context_diagram
Best for high-level system context showing external actors and system boundaries.

See [render_c4_context_diagram.md](./render_c4_context_diagram.md) for full details.

### Secondary Tool: render_sequence_diagram
Useful for documenting specific interaction patterns between services.

See [render_sequence_diagram.md](./render_sequence_diagram.md) for full details.

### Secondary Tool: render_block_diagram
Useful for simplified logical groupings without technical details.

See [render_block_diagram.md](./render_block_diagram.md) for full details.

## Recommended Diagram Type

### Primary: Architecture Diagram
**When to use**: Engineering documentation, detailed service topology, deployment planning

**Strengths**:
- Shows different component types (services, databases, queues, APIs)
- Clearly represents communication patterns with labeled arrows
- Supports grouping by domain or namespace
- Includes infrastructure components

**Example structure**:
```json
{
  "components": [
    {"id": "api_gateway", "label": "API Gateway", "type": "api_gateway"},
    {"id": "auth_service", "label": "Auth Service", "type": "service"},
    {"id": "user_service", "label": "User Service", "type": "service"},
    {"id": "order_service", "label": "Order Service", "type": "service"},
    {"id": "payment_service", "label": "Payment Service", "type": "service"},
    {"id": "notification_service", "label": "Notification Service", "type": "service"},
    {"id": "user_db", "label": "User DB", "type": "database"},
    {"id": "order_db", "label": "Order DB", "type": "database"},
    {"id": "redis_cache", "label": "Redis Cache", "type": "cache"},
    {"id": "rabbitmq", "label": "RabbitMQ", "type": "message_queue"},
    {"id": "stripe_api", "label": "Stripe API", "type": "external"}
  ],
  "connections": [
    {"from": "api_gateway", "to": "auth_service", "label": "REST"},
    {"from": "api_gateway", "to": "user_service", "label": "REST"},
    {"from": "api_gateway", "to": "order_service", "label": "REST"},
    {"from": "order_service", "to": "payment_service", "label": "gRPC"},
    {"from": "payment_service", "to": "stripe_api", "label": "HTTPS"},
    {"from": "order_service", "to": "rabbitmq", "label": "publish"},
    {"from": "rabbitmq", "to": "notification_service", "label": "subscribe"}
  ]
}
```

### Primary: C4 Context Diagram
**When to use**: Executive presentations, system overview, stakeholder communication

**Strengths**:
- Shows system boundaries clearly
- Focuses on external actors and their interactions
- Abstracts away internal complexity
- Perfect for non-technical audiences

**Example structure**:
```json
{
  "elements": [
    {"id": "customer", "label": "Customer", "type": "person", "description": "Online shoppers"},
    {"id": "admin", "label": "Admin", "type": "person", "description": "System administrators"},
    {"id": "ecommerce", "label": "E-commerce Platform", "type": "system", "description": "Microservices-based platform"},
    {"id": "payment", "label": "Payment Gateway", "type": "external_system", "description": "Stripe payment processing"},
    {"id": "email", "label": "Email Service", "type": "external_system", "description": "SendGrid email delivery"}
  ],
  "relationships": [
    {"from": "customer", "to": "ecommerce", "description": "Browse and purchase products"},
    {"from": "admin", "to": "ecommerce", "description": "Manage products and orders"},
    {"from": "ecommerce", "to": "payment", "description": "Process payments"},
    {"from": "ecommerce", "to": "email", "description": "Send notifications"}
  ]
}
```

## Example Usage

### Scenario: E-commerce Microservices Platform

**User Request**: "Visualize our e-commerce microservices architecture showing all services, databases, and external integrations"

**Step 1: Create High-Level C4 Context (for stakeholders)**

```json
{
  "elements": [
    {"id": "customer", "label": "Customer", "type": "person", "description": "End users shopping online"},
    {"id": "merchant", "label": "Merchant", "type": "person", "description": "Store owners managing inventory"},
    {"id": "platform", "label": "E-commerce Platform", "type": "system", "description": "Microservices platform for online retail"},
    {"id": "stripe", "label": "Stripe", "type": "external_system", "description": "Payment processing"},
    {"id": "sendgrid", "label": "SendGrid", "type": "external_system", "description": "Email notifications"},
    {"id": "s3", "label": "AWS S3", "type": "external_system", "description": "Product image storage"}
  ],
  "relationships": [
    {"from": "customer", "to": "platform", "description": "Browse products, place orders"},
    {"from": "merchant", "to": "platform", "description": "Manage inventory and orders"},
    {"from": "platform", "to": "stripe", "description": "Process payments via API"},
    {"from": "platform", "to": "sendgrid", "description": "Send order confirmations"},
    {"from": "platform", "to": "s3", "description": "Store and retrieve images"}
  ],
  "title": "E-commerce Platform - System Context",
  "format": "svg",
  "theme": "default"
}
```

**Step 2: Create Detailed Architecture Diagram (for engineering team)**

```json
{
  "components": [
    {"id": "cdn", "label": "CloudFront CDN", "type": "infrastructure", "description": "Content delivery"},
    {"id": "alb", "label": "Application Load Balancer", "type": "load_balancer"},
    {"id": "api_gateway", "label": "API Gateway", "type": "api_gateway", "description": "Kong API Gateway"},
    {"id": "auth_svc", "label": "Auth Service", "type": "service", "description": "JWT authentication"},
    {"id": "user_svc", "label": "User Service", "type": "service", "description": "User profiles and preferences"},
    {"id": "product_svc", "label": "Product Service", "type": "service", "description": "Product catalog management"},
    {"id": "cart_svc", "label": "Cart Service", "type": "service", "description": "Shopping cart operations"},
    {"id": "order_svc", "label": "Order Service", "type": "service", "description": "Order processing"},
    {"id": "payment_svc", "label": "Payment Service", "type": "service", "description": "Payment orchestration"},
    {"id": "inventory_svc", "label": "Inventory Service", "type": "service", "description": "Stock management"},
    {"id": "notification_svc", "label": "Notification Service", "type": "service", "description": "Email/SMS notifications"},
    {"id": "user_db", "label": "User PostgreSQL", "type": "database"},
    {"id": "product_db", "label": "Product PostgreSQL", "type": "database"},
    {"id": "order_db", "label": "Order PostgreSQL", "type": "database"},
    {"id": "redis", "label": "Redis Cluster", "type": "cache", "description": "Session and cache"},
    {"id": "kafka", "label": "Apache Kafka", "type": "message_queue", "description": "Event streaming"},
    {"id": "elasticsearch", "label": "Elasticsearch", "type": "search_engine"},
    {"id": "s3", "label": "S3 Bucket", "type": "storage"},
    {"id": "stripe", "label": "Stripe API", "type": "external"}
  ],
  "connections": [
    {"from": "cdn", "to": "alb", "label": "HTTPS", "type": "sync"},
    {"from": "alb", "to": "api_gateway", "label": "HTTP/2", "type": "sync"},
    {"from": "api_gateway", "to": "auth_svc", "label": "REST", "type": "sync"},
    {"from": "api_gateway", "to": "user_svc", "label": "REST", "type": "sync"},
    {"from": "api_gateway", "to": "product_svc", "label": "REST", "type": "sync"},
    {"from": "api_gateway", "to": "cart_svc", "label": "REST", "type": "sync"},
    {"from": "api_gateway", "to": "order_svc", "label": "REST", "type": "sync"},
    {"from": "auth_svc", "to": "user_db", "label": "SQL", "type": "sync"},
    {"from": "user_svc", "to": "user_db", "label": "SQL", "type": "sync"},
    {"from": "product_svc", "to": "product_db", "label": "SQL", "type": "sync"},
    {"from": "product_svc", "to": "elasticsearch", "label": "Index", "type": "async"},
    {"from": "product_svc", "to": "s3", "label": "S3 API", "type": "sync"},
    {"from": "cart_svc", "to": "redis", "label": "Redis protocol", "type": "sync"},
    {"from": "order_svc", "to": "order_db", "label": "SQL", "type": "sync"},
    {"from": "order_svc", "to": "payment_svc", "label": "gRPC", "type": "sync"},
    {"from": "order_svc", "to": "inventory_svc", "label": "gRPC", "type": "sync"},
    {"from": "order_svc", "to": "kafka", "label": "Publish events", "type": "async"},
    {"from": "payment_svc", "to": "stripe", "label": "REST API", "type": "sync"},
    {"from": "kafka", "to": "notification_svc", "label": "Subscribe", "type": "async"},
    {"from": "kafka", "to": "inventory_svc", "label": "Subscribe", "type": "async"}
  ],
  "groups": [
    {"id": "frontend", "label": "Frontend Layer", "components": ["cdn", "alb"]},
    {"id": "gateway", "label": "Gateway Layer", "components": ["api_gateway"]},
    {"id": "core_services", "label": "Core Services", "components": ["auth_svc", "user_svc", "product_svc", "cart_svc", "order_svc"]},
    {"id": "backend_services", "label": "Backend Services", "components": ["payment_svc", "inventory_svc", "notification_svc"]},
    {"id": "data_layer", "label": "Data Layer", "components": ["user_db", "product_db", "order_db", "redis", "elasticsearch"]},
    {"id": "messaging", "label": "Messaging", "components": ["kafka"]},
    {"id": "external", "label": "External Services", "components": ["s3", "stripe"]}
  ],
  "title": "E-commerce Microservices Architecture",
  "direction": "TB",
  "format": "svg",
  "theme": "default"
}
```

**Step 3: Document Critical Interaction (optional)**

For a specific flow like order placement, create a sequence diagram:

```json
{
  "participants": [
    {"id": "client", "label": "Mobile App", "type": "actor"},
    {"id": "gateway", "label": "API Gateway", "type": "boundary"},
    {"id": "order", "label": "Order Service", "type": "control"},
    {"id": "payment", "label": "Payment Service", "type": "control"},
    {"id": "inventory", "label": "Inventory Service", "type": "control"},
    {"id": "kafka", "label": "Kafka", "type": "queue"}
  ],
  "messages": [
    {"from": "client", "to": "gateway", "message": "POST /orders", "arrow_type": "solid"},
    {"from": "gateway", "to": "order", "message": "createOrder()", "arrow_type": "solid"},
    {"from": "order", "to": "inventory", "message": "reserveStock()", "arrow_type": "solid"},
    {"from": "inventory", "to": "order", "message": "reservation confirmed", "arrow_type": "dotted"},
    {"from": "order", "to": "payment", "message": "processPayment()", "arrow_type": "solid"},
    {"from": "payment", "to": "order", "message": "payment successful", "arrow_type": "dotted"},
    {"from": "order", "to": "kafka", "message": "publish OrderCreated event", "arrow_type": "async"},
    {"from": "order", "to": "gateway", "message": "order details", "arrow_type": "dotted"},
    {"from": "gateway", "to": "client", "message": "201 Created", "arrow_type": "dotted"}
  ],
  "title": "Order Placement Flow",
  "autonumber": true,
  "format": "svg"
}
```

## Alternative Approaches

### Option 1: Block Diagram for Simplified View
Use when you need a simple logical grouping without technical details:
- Group related services into blocks
- Show high-level data flow
- Abstract away infrastructure complexity
- Good for presentations to non-technical stakeholders

### Option 2: Layered Architecture Diagram
Organize services by architectural layers:
- Presentation layer (API Gateway, Load Balancers)
- Service layer (Business logic microservices)
- Data layer (Databases, caches)
- Integration layer (Message queues, external APIs)

### Option 3: Multiple Diagrams by Domain
For large systems, create separate diagrams:
- User management domain
- Product catalog domain
- Order processing domain
- Payment processing domain
- Each with its own services and dependencies

## Best Practices

### 1. Start with Context
- Begin with a C4 context diagram for high-level overview
- Add detailed architecture diagrams for engineering teams
- Use sequence diagrams for complex interaction patterns

### 2. Group Related Services
- Use logical grouping (domains, bounded contexts)
- Show physical deployment boundaries (VPCs, clusters)
- Clearly label infrastructure components

### 3. Show Communication Patterns
- Label protocols (REST, gRPC, GraphQL)
- Distinguish sync vs async communication
- Indicate direction of data flow

### 4. Document External Dependencies
- Clearly mark third-party services
- Show which services integrate with external systems
- Note authentication mechanisms

### 5. Keep It Current
- Update diagrams when architecture changes
- Version control your diagram definitions
- Include diagram generation in documentation workflow

### 6. Use Consistent Naming
- Match service names to actual deployment names
- Use consistent abbreviations
- Include version numbers if relevant

### 7. Consider Your Audience
- Technical details for engineering teams
- High-level abstractions for management
- Security focus for security reviews
- Cost perspective for finance discussions

## Common Variations

### Variation 1: Multi-Region Architecture
Show services deployed across multiple AWS regions or availability zones:
- Use groups to represent regions
- Show cross-region replication
- Document failover patterns

### Variation 2: Service Mesh Visualization
For Istio/Linkerd environments:
- Show service mesh control plane
- Document sidecar proxies
- Visualize traffic management policies

### Variation 3: Event-Driven Architecture
Emphasize asynchronous communication:
- Highlight message brokers (Kafka, RabbitMQ)
- Show event publishers and subscribers
- Document event schemas

### Variation 4: API-First Architecture
Focus on API boundaries:
- Show API versioning strategy
- Document authentication flows
- Highlight rate limiting and throttling

### Variation 5: Serverless Microservices
For AWS Lambda / Azure Functions:
- Show function triggers
- Document event sources
- Visualize function chaining

## Related Playbooks

### Architecture & Design
- [render_architecture_diagram.md](./render_architecture_diagram.md) - Detailed technical architecture
- [render_c4_context_diagram.md](./render_c4_context_diagram.md) - System context view
- [render_block_diagram.md](./render_block_diagram.md) - Simplified block diagrams

### Interactions & Flows
- [render_sequence_diagram.md](./render_sequence_diagram.md) - Service interaction patterns
- [render_flowchart.md](./render_flowchart.md) - Process flows

### Other Scenario Playbooks
- [render_api_interaction_flow.md](./render_api_interaction_flow.md) - API communication details
- [render_cloud_infrastructure_diagram.md](./render_cloud_infrastructure_diagram.md) - Cloud infrastructure
- [render_data_pipeline.md](./render_data_pipeline.md) - Data flow visualization

## Notes

- For systems with >20 services, consider creating multiple diagrams by domain
- Include deployment information (Kubernetes, ECS, VM-based) in component descriptions
- Document service discovery mechanisms (Consul, Eureka, built-in)
- Note scalability characteristics (stateless, stateful, horizontally scalable)
- Consider creating separate diagrams for different environments (dev, staging, prod)
- Use consistent color themes across related diagrams
- Export in SVG format for inclusion in architecture documentation
- Version control diagram source definitions alongside code
