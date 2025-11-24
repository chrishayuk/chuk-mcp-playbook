# Playbook: Visualize API Interaction Flow

## Description
This playbook guides you through visualizing API request/response flows, including authentication, authorization, error handling, retry logic, and data transformations. Perfect for API documentation, debugging integration issues, understanding system behavior, and onboarding developers to your API ecosystem.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Understanding of the API endpoints and their interactions
- Knowledge of authentication mechanisms
- List of request/response patterns and error scenarios

## ⚠️ CRITICAL: Participant Type Warning

**When using sequence diagrams, ONLY use these participant types:**
- `"actor"` - for human users
- `"participant"` - for ALL systems, services, APIs, databases

**DO NOT USE**: `"boundary"`, `"control"`, `"entity"`, `"database"`, `"queue"`, etc. These will cause rendering failures!

Use descriptive **labels** to distinguish roles: `{"id": "db", "label": "User Database", "type": "participant"}` ✅

Examples in this playbook show various types for illustration, but **you must change them to "actor" or "participant" when using the tool**.

## Steps

1. **Identify all participants**
   - List client applications (web, mobile, third-party)
   - Identify backend services and APIs
   - Note authentication/authorization services
   - Document databases and external services
   - **Remember: Use only "actor" or "participant" types with descriptive labels**

2. **Map the API flow**
   - Document the sequence of API calls
   - Note request methods (GET, POST, PUT, DELETE)
   - Identify authentication steps (token exchange, validation)
   - Map response codes and payloads

3. **Document error scenarios**
   - Note validation errors (400 responses)
   - Document authentication failures (401/403)
   - Show retry logic for transient failures
   - Include timeout handling

4. **Choose the appropriate diagram type**
   - Use **sequence_diagram** for detailed API interactions
   - Use **flowchart** for decision logic and branching
   - Use **state_diagram** for status transitions

5. **Create the visualization**
   - Use sequence diagrams for primary flow
   - Add flowcharts for complex decision trees
   - Document with clear labels and HTTP status codes

## MCP Tools Required

### Primary Tool: render_sequence_diagram
Best for showing chronological API request/response flows between participants.

See [render_sequence_diagram.md](./render_sequence_diagram.md) for full details.

### Secondary Tool: render_flowchart
Useful for documenting API logic, validation rules, and error handling branches.

See [render_flowchart.md](./render_flowchart.md) for full details.

### Secondary Tool: render_state_diagram
Useful for showing resource state transitions through API operations.

See [render_state_diagram.md](./render_state_diagram.md) for full details.

## Recommended Diagram Type

### Primary: Sequence Diagram
**When to use**: API documentation, integration guides, debugging, team onboarding

**Strengths**:
- Shows chronological order of API calls
- Clearly represents request/response patterns
- Supports activation boxes for processing time
- Can include notes for important details

**Example structure**:
```json
{
  "participants": [
    {"id": "client", "label": "Client App", "type": "actor"},
    {"id": "gateway", "label": "API Gateway", "type": "boundary"},
    {"id": "auth", "label": "Auth Service", "type": "control"},
    {"id": "api", "label": "Resource API", "type": "control"},
    {"id": "db", "label": "Database", "type": "database"}
  ],
  "messages": [
    {"from": "client", "to": "gateway", "message": "POST /api/v1/resource", "arrow_type": "solid"},
    {"from": "gateway", "to": "auth", "message": "validateToken()", "arrow_type": "solid"},
    {"from": "auth", "to": "gateway", "message": "token valid", "arrow_type": "dotted"}
  ]
}
```

### Secondary: Flowchart
**When to use**: Complex validation logic, error handling branches, decision trees

**Strengths**:
- Shows decision points clearly
- Documents branching logic
- Good for error handling flows
- Useful for request validation steps

## Example Usage

### Scenario 1: OAuth 2.0 Authentication Flow

**User Request**: "Visualize the OAuth 2.0 authorization code flow for our API"

```json
{
  "participants": [
    {"id": "user", "label": "User", "type": "actor"},
    {"id": "client", "label": "Client App", "type": "boundary"},
    {"id": "auth_server", "label": "Authorization Server", "type": "control"},
    {"id": "resource_server", "label": "Resource API", "type": "control"},
    {"id": "db", "label": "User Database", "type": "database"}
  ],
  "messages": [
    {"from": "user", "to": "client", "message": "Click 'Login'", "arrow_type": "solid"},
    {"from": "client", "to": "auth_server", "message": "GET /authorize?client_id=xxx&redirect_uri=yyy", "arrow_type": "solid"},
    {"from": "auth_server", "to": "user", "message": "Login page", "arrow_type": "dotted"},
    {"from": "user", "to": "auth_server", "message": "POST /login (credentials)", "arrow_type": "solid"},
    {"from": "auth_server", "to": "db", "message": "Validate credentials", "arrow_type": "solid", "activate": true},
    {"from": "db", "to": "auth_server", "message": "User valid", "arrow_type": "dotted"},
    {"from": "auth_server", "to": "client", "message": "302 Redirect with auth code", "arrow_type": "dotted"},
    {"from": "client", "to": "auth_server", "message": "POST /token (code + client_secret)", "arrow_type": "solid"},
    {"from": "auth_server", "to": "client", "message": "200 OK (access_token + refresh_token)", "arrow_type": "dotted"},
    {"from": "client", "to": "resource_server", "message": "GET /api/user (Bearer token)", "arrow_type": "solid"},
    {"from": "resource_server", "to": "auth_server", "message": "Validate token", "arrow_type": "solid"},
    {"from": "auth_server", "to": "resource_server", "message": "Token valid", "arrow_type": "dotted"},
    {"from": "resource_server", "to": "client", "message": "200 OK (user data)", "arrow_type": "dotted"},
    {"from": "client", "to": "user", "message": "Display dashboard", "arrow_type": "dotted"}
  ],
  "notes": [
    {"position": "right of", "participants": ["auth_server"], "text": "Authorization code expires in 10 minutes"},
    {"position": "right of", "participants": ["client"], "text": "Access token expires in 1 hour\nRefresh token expires in 30 days"}
  ],
  "title": "OAuth 2.0 Authorization Code Flow",
  "autonumber": true,
  "format": "svg",
  "theme": "default"
}
```

### Scenario 2: REST API CRUD Operations with Error Handling

**User Request**: "Show the API flow for creating a new order, including validation and error cases"

```json
{
  "participants": [
    {"id": "client", "label": "Mobile App", "type": "actor"},
    {"id": "lb", "label": "Load Balancer", "type": "boundary"},
    {"id": "api", "label": "Order API", "type": "control"},
    {"id": "validator", "label": "Validation Service", "type": "control"},
    {"id": "inventory", "label": "Inventory Service", "type": "control"},
    {"id": "payment", "label": "Payment Gateway", "type": "control"},
    {"id": "db", "label": "Order Database", "type": "database"},
    {"id": "cache", "label": "Redis Cache", "type": "database"}
  ],
  "messages": [
    {"from": "client", "to": "lb", "message": "POST /api/v1/orders (order data)", "arrow_type": "solid"},
    {"from": "lb", "to": "api", "message": "Forward request", "arrow_type": "solid"},
    {"from": "api", "to": "cache", "message": "Check user session", "arrow_type": "solid"},
    {"from": "cache", "to": "api", "message": "Session valid", "arrow_type": "dotted"},
    {"from": "api", "to": "validator", "message": "validateOrderData()", "arrow_type": "solid", "activate": true},
    {"from": "validator", "to": "api", "message": "Validation passed", "arrow_type": "dotted"},
    {"from": "api", "to": "inventory", "message": "checkStockAvailability()", "arrow_type": "solid"},
    {"from": "inventory", "to": "api", "message": "Stock available", "arrow_type": "dotted"},
    {"from": "api", "to": "payment", "message": "authorizePayment()", "arrow_type": "solid"},
    {"from": "payment", "to": "api", "message": "Payment authorized", "arrow_type": "dotted"},
    {"from": "api", "to": "db", "message": "INSERT order", "arrow_type": "solid"},
    {"from": "db", "to": "api", "message": "Order created", "arrow_type": "dotted"},
    {"from": "api", "to": "inventory", "message": "reserveStock()", "arrow_type": "async"},
    {"from": "api", "to": "lb", "message": "201 Created (order_id)", "arrow_type": "dotted"},
    {"from": "lb", "to": "client", "message": "201 Created", "arrow_type": "dotted"}
  ],
  "notes": [
    {"position": "over", "participants": ["validator"], "text": "Validates:\n- Required fields\n- Data types\n- Business rules"},
    {"position": "right of", "participants": ["payment"], "text": "Payment authorization\nhold expires in 7 days"}
  ],
  "title": "Create Order API Flow - Success Case",
  "autonumber": true,
  "format": "svg",
  "theme": "default"
}
```

### Scenario 3: API Error Handling Flow

**User Request**: "Show what happens when payment fails during order creation"

```json
{
  "participants": [
    {"id": "client", "label": "Mobile App", "type": "actor"},
    {"id": "api", "label": "Order API", "type": "control"},
    {"id": "payment", "label": "Payment Gateway", "type": "control"},
    {"id": "external", "label": "Stripe API", "type": "boundary"}
  ],
  "messages": [
    {"from": "client", "to": "api", "message": "POST /api/v1/orders", "arrow_type": "solid"},
    {"from": "api", "to": "payment", "message": "authorizePayment()", "arrow_type": "solid", "activate": true},
    {"from": "payment", "to": "external", "message": "POST /v1/payment_intents", "arrow_type": "solid"},
    {"from": "external", "to": "payment", "message": "402 Payment Required (insufficient funds)", "arrow_type": "dotted"},
    {"from": "payment", "to": "api", "message": "PaymentFailedException", "arrow_type": "dotted"},
    {"from": "api", "to": "client", "message": "402 Payment Required (error details)", "arrow_type": "dotted"}
  ],
  "notes": [
    {"position": "right of", "participants": ["payment"], "text": "Error details include:\n- Error code\n- User-friendly message\n- Retry recommendation"}
  ],
  "title": "Create Order API Flow - Payment Failure",
  "autonumber": true,
  "format": "svg",
  "theme": "default"
}
```

### Scenario 4: API Request Validation Logic (Flowchart)

**User Request**: "Document the validation logic for order creation requests"

```json
{
  "nodes": [
    {"id": "start", "label": "Receive POST /orders", "shape": "circle"},
    {"id": "check_auth", "label": "Valid Bearer token?", "shape": "diamond"},
    {"id": "check_body", "label": "Request body present?", "shape": "diamond"},
    {"id": "check_required", "label": "All required fields?", "shape": "diamond"},
    {"id": "check_quantity", "label": "Quantity > 0?", "shape": "diamond"},
    {"id": "check_price", "label": "Valid price format?", "shape": "diamond"},
    {"id": "check_address", "label": "Valid shipping address?", "shape": "diamond"},
    {"id": "process", "label": "Process order", "shape": "rectangle"},
    {"id": "return_201", "label": "Return 201 Created", "shape": "rectangle"},
    {"id": "return_401", "label": "Return 401 Unauthorized", "shape": "rectangle"},
    {"id": "return_400_no_body", "label": "Return 400 (Missing body)", "shape": "rectangle"},
    {"id": "return_400_fields", "label": "Return 400 (Missing fields)", "shape": "rectangle"},
    {"id": "return_400_quantity", "label": "Return 400 (Invalid quantity)", "shape": "rectangle"},
    {"id": "return_400_price", "label": "Return 400 (Invalid price)", "shape": "rectangle"},
    {"id": "return_400_address", "label": "Return 400 (Invalid address)", "shape": "rectangle"},
    {"id": "end", "label": "End", "shape": "circle"}
  ],
  "edges": [
    {"from": "start", "to": "check_auth"},
    {"from": "check_auth", "to": "check_body", "label": "Yes"},
    {"from": "check_auth", "to": "return_401", "label": "No"},
    {"from": "check_body", "to": "check_required", "label": "Yes"},
    {"from": "check_body", "to": "return_400_no_body", "label": "No"},
    {"from": "check_required", "to": "check_quantity", "label": "Yes"},
    {"from": "check_required", "to": "return_400_fields", "label": "No"},
    {"from": "check_quantity", "to": "check_price", "label": "Yes"},
    {"from": "check_quantity", "to": "return_400_quantity", "label": "No"},
    {"from": "check_price", "to": "check_address", "label": "Yes"},
    {"from": "check_price", "to": "return_400_price", "label": "No"},
    {"from": "check_address", "to": "process", "label": "Yes"},
    {"from": "check_address", "to": "return_400_address", "label": "No"},
    {"from": "process", "to": "return_201"},
    {"from": "return_201", "to": "end"},
    {"from": "return_401", "to": "end"},
    {"from": "return_400_no_body", "to": "end"},
    {"from": "return_400_fields", "to": "end"},
    {"from": "return_400_quantity", "to": "end"},
    {"from": "return_400_price", "to": "end"},
    {"from": "return_400_address", "to": "end"}
  ],
  "direction": "TB",
  "title": "Order Creation Request Validation Flow",
  "format": "svg",
  "theme": "default"
}
```

### Scenario 5: GraphQL API Query Flow

**User Request**: "Show how a GraphQL query flows through our system"

```json
{
  "participants": [
    {"id": "client", "label": "React App", "type": "actor"},
    {"id": "apollo", "label": "Apollo Gateway", "type": "boundary"},
    {"id": "user_graph", "label": "User GraphQL Service", "type": "control"},
    {"id": "order_graph", "label": "Order GraphQL Service", "type": "control"},
    {"id": "user_db", "label": "User DB", "type": "database"},
    {"id": "order_db", "label": "Order DB", "type": "database"}
  ],
  "messages": [
    {"from": "client", "to": "apollo", "message": "POST /graphql (query with user and orders)", "arrow_type": "solid"},
    {"from": "apollo", "to": "user_graph", "message": "Resolve user fields", "arrow_type": "solid", "activate": true},
    {"from": "user_graph", "to": "user_db", "message": "SELECT user WHERE id=123", "arrow_type": "solid"},
    {"from": "user_db", "to": "user_graph", "message": "User data", "arrow_type": "dotted"},
    {"from": "user_graph", "to": "apollo", "message": "User result", "arrow_type": "dotted"},
    {"from": "apollo", "to": "order_graph", "message": "Resolve orders for user_id=123", "arrow_type": "solid", "activate": true},
    {"from": "order_graph", "to": "order_db", "message": "SELECT orders WHERE user_id=123", "arrow_type": "solid"},
    {"from": "order_db", "to": "order_graph", "message": "Order list", "arrow_type": "dotted"},
    {"from": "order_graph", "to": "apollo", "message": "Orders result", "arrow_type": "dotted"},
    {"from": "apollo", "to": "client", "message": "200 OK (merged data)", "arrow_type": "dotted"}
  ],
  "notes": [
    {"position": "right of", "participants": ["apollo"], "text": "Apollo Gateway\nstitches results\nfrom multiple services"}
  ],
  "title": "GraphQL Federated Query Flow",
  "autonumber": true,
  "format": "svg",
  "theme": "default"
}
```

## Alternative Approaches

### Option 1: Flowchart for Decision Logic
Use flowcharts when:
- Documenting complex validation rules
- Showing branching error handling
- Illustrating retry logic with backoff
- Mapping request routing decisions

### Option 2: State Diagram for Resource Status
Use state diagrams for:
- Order status transitions (pending → paid → shipped)
- Document approval workflows
- User account states (active → suspended → deleted)
- Resource lifecycle management

### Option 3: Multiple Diagrams per Endpoint
For complex APIs:
- Happy path sequence diagram
- Error handling flowchart
- Authentication flow separately
- Rate limiting logic

## Best Practices

### 1. Use HTTP Status Codes
- Always include status codes in response messages (200, 201, 400, 401, 404, 500)
- Use standard HTTP methods (GET, POST, PUT, PATCH, DELETE)
- Note content types (application/json, multipart/form-data)

### 2. Show Authentication Clearly
- Document token exchange patterns
- Show where JWT/OAuth tokens are validated
- Note token expiration times in notes
- Include refresh token flows

### 3. Document Error Scenarios
- Create separate diagrams for error cases
- Show retry logic and backoff strategies
- Document timeout behavior
- Include circuit breaker patterns

### 4. Use Activation Boxes
- Enable activation in sequence diagrams to show processing time
- Helps visualize synchronous vs asynchronous calls
- Shows which service is actively processing

### 5. Add Descriptive Notes
- Document rate limits
- Note timeout values
- Explain business rules
- Clarify security requirements

### 6. Keep It Focused
- One diagram per API endpoint or flow
- Separate happy path from error scenarios
- Break complex flows into multiple diagrams

### 7. Version Your API Diagrams
- Include API version in title (/api/v1, /api/v2)
- Update diagrams when APIs change
- Archive old versions for reference

## Common Variations

### Variation 1: Webhook Integration
Show outbound API calls:
- Event triggers webhook
- Your system calls external API
- Handle webhook retries
- Document signature verification

### Variation 2: Polling vs WebSocket
Compare different interaction patterns:
- Traditional REST polling
- Server-sent events (SSE)
- WebSocket bi-directional communication
- Long polling techniques

### Variation 3: API Gateway Patterns
Document gateway responsibilities:
- Request routing
- Rate limiting enforcement
- Authentication/authorization
- Response caching

### Variation 4: Microservices API Composition
Show API aggregation:
- Backend for frontend (BFF) pattern
- API composition layer
- Multiple service calls aggregated
- Parallel vs sequential calls

### Variation 5: Async API Patterns
Document asynchronous interactions:
- Message queue based APIs
- Job submission and status checking
- Callback URLs for completion
- Event-driven API notifications

## Related Playbooks

### Core Diagram Types
- [render_sequence_diagram.md](./render_sequence_diagram.md) - API interaction flows
- [render_flowchart.md](./render_flowchart.md) - Validation and decision logic
- [render_state_diagram.md](./render_state_diagram.md) - Resource state transitions

### Architecture Playbooks
- [render_microservices_architecture.md](./render_microservices_architecture.md) - Overall system architecture
- [render_deployment_pipeline.md](./render_deployment_pipeline.md) - CI/CD for APIs

### Process Playbooks
- [render_approval_workflow.md](./render_approval_workflow.md) - Approval processes
- [render_checkout_process.md](./render_checkout_process.md) - E-commerce flows

## Notes

- Always test your API flows before documenting them
- Include both successful and error scenarios
- Document rate limits and throttling behavior
- Note any authentication requirements (API keys, OAuth, JWT)
- Include examples of actual request/response payloads in notes
- Use autonumbering for complex flows to track message order
- Export in SVG format for API documentation
- Keep diagrams up to date with API changes
- Consider automating diagram generation from OpenAPI/Swagger specs
