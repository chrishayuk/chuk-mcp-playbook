# Playbook: Render Sequence Diagram

## Description
This playbook creates sequence diagrams showing interactions between participants over time. Sequence diagrams are ideal for visualizing API flows, system interactions, message passing, and communication protocols between components.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Understanding of the interaction flow between components
- Clear identification of participants and message exchanges

## Steps

1. Identify all participants
   - List all actors, systems, services, or components
   - **Choose safe participant types: ONLY "actor" (for humans) or "participant" (for all systems)**
   - Use descriptive labels to distinguish roles (e.g., "Auth Service", "User Database", "Payment API")
   - Assign unique IDs and display labels

2. Map the message flow
   - Document each message exchange in chronological order
   - Identify request/response patterns
   - Note any activations or lifecycle events

3. Add optional notes
   - Document important details, timeouts, or business rules
   - Position notes relative to participants

4. Call the render_sequence_diagram tool
   - Pass participants with id, label, and type
   - Pass messages with from, to, message text, and arrow type
   - Include notes if needed
   - Enable autonumber if desired

5. Review the generated diagram
   - Verify message order is correct
   - Check that all interactions are clear

## MCP Tools Required

### mcp-mermaid-renderer

**Tool**: `render_sequence_diagram`
- **Parameters**:
  - `participants` (list of dict, required): List of participants. Each dict should have:
    - `id` or `name` (string): Unique identifier
    - `label` (string, optional): Display name (defaults to id/name)
    - `type` (string, optional): Participant type - **"participant" (default, recommended)** or **"actor"** (for human users)

    **⚠️ IMPORTANT**: While other types like "boundary", "control", "entity", "database" are part of the Mermaid spec, they are **NOT supported** by mermaid.ink renderer and will cause failures. **Use only "participant" or "actor"** for reliable rendering. Distinguish roles through meaningful labels instead.
  - `messages` (list of dict, required): List of messages exchanged. Each dict should have:
    - `from` or `from_participant` (string): Source participant ID
    - `to` or `to_participant` (string): Target participant ID
    - `message`, `text`, or `label` (string): Message text
    - `arrow_type` (string, optional): Arrow style - "solid" (default), "dotted", "solid_open", "dotted_open", "solid_cross", "dotted_cross", "async", "async_open"
    - `activate` (boolean, optional): Set to true to activate the target participant
  - `notes` (list of dict, optional): List of notes. Each note should have:
    - `position` (string): "right of", "left of", or "over"
    - `participants` (list of strings): Participant IDs
    - `text` (string): Note content
  - `title` (string, optional): Diagram title
  - `autonumber` (boolean): Automatically number messages (default: false)
  - `format` (string): Output format - "svg" (default, recommended) or "png"
  - `theme` (string): Mermaid theme - "default", "dark", "forest", "neutral"
  - `bgcolor` (string): Background color (default: "transparent")
  - `filename` (string, optional): Suggested filename
- **Returns**: Artifact metadata with download URLs

## Example Usage

**Input**: "Create a sequence diagram for a user login API flow"

**Process**:
1. Identify participants: Client App, API Gateway, Auth Service, Database
2. Map the login flow messages
3. Add note about token expiration

**Tool Call**:
```json
{
  "participants": [
    {"id": "client", "label": "Client App", "type": "actor"},
    {"id": "api", "label": "API Gateway", "type": "participant"},
    {"id": "auth", "label": "Auth Service", "type": "participant"},
    {"id": "db", "label": "Database", "type": "participant"}
  ],
  "messages": [
    {"from": "client", "to": "api", "message": "POST /login", "arrow_type": "solid"},
    {"from": "api", "to": "auth", "message": "validateCredentials()", "arrow_type": "solid"},
    {"from": "auth", "to": "db", "message": "SELECT user", "arrow_type": "solid"},
    {"from": "db", "to": "auth", "message": "user data", "arrow_type": "dotted"},
    {"from": "auth", "to": "api", "message": "JWT token", "arrow_type": "dotted"},
    {"from": "api", "to": "client", "message": "200 OK + token", "arrow_type": "dotted"}
  ],
  "notes": [
    {"position": "right of", "participants": ["auth"], "text": "Token expires in 24h"}
  ],
  "title": "User Login Flow",
  "autonumber": true,
  "format": "svg",
  "theme": "default"
}
```

**Output**:
```
Sequence diagram rendered successfully!
- Format: SVG
- Participants: 4
- Messages: 6
- Download URL: [artifact link]
```

## Expected Response Format

The tool returns an artifact object with:
- `download_url`: URL to download the rendered diagram
- `source_code`: Editable Mermaid syntax
- `format`: Output format (svg or png)
- `diagram_type`: "sequence"

## Common Use Cases

1. **API Interactions**: REST API calls, microservice communication, webhook flows
2. **Authentication Flows**: Login, OAuth, SSO, token refresh
3. **Payment Processing**: Payment gateway integration, transaction flows
4. **Database Operations**: CRUD operations, transaction management
5. **Message Queue Flows**: Pub/sub patterns, event-driven architecture
6. **Error Handling**: Exception flows, retry logic, fallback mechanisms

## Best Practices

1. **Participant Types** (⚠️ CRITICAL):
   - **ONLY USE**: "actor" (for human users) or "participant" (for all systems/services)
   - **DO NOT USE**: "boundary", "control", "entity", "database", "collections", "queue" - these will cause rendering failures
   - Distinguish different roles through meaningful **labels** instead (e.g., "API Gateway", "Auth Service", "User Database")
   - Example: `{"id": "db", "label": "User Database", "type": "participant"}` ✅
   - NOT: `{"id": "db", "label": "User Database", "type": "database"}` ❌

2. **Message Labels** (⚠️ CRITICAL for mermaid.ink):
   - **AVOID special characters that cause rendering failures:**
     - ❌ Single quotes `'` - use plain text instead: "Add to cart" not "'Add to cart'"
     - ❌ Curly braces `{}` - use parentheses instead: "(productId)" not "{productId}"
     - ❌ Angle brackets `<>` - use parentheses or plain text
     - ❌ Pipe symbols `|` - use commas or "and"
     - ❌ Arrows like `->` or `=>` in text - spell out "to" or use spaces
   - **SAFE characters to use:**
     - ✅ Parentheses `()` for parameters: "POST /cart/add (productId, qty)"
     - ✅ Forward slashes `/` for URLs: "GET /api/users"
     - ✅ Colons `:` for labels: "Status: 200 OK"
     - ✅ Hyphens `-` and underscores `_`
     - ✅ Commas `,` for lists
   - **Keep concise**: API endpoints, method names, HTTP status codes
   - **Example - Good**: `"POST /cart/add (productId, qty, userId)"` ✅
   - **Example - Bad**: `"POST /cart/add {productId, qty, userId}"` ❌

3. **Arrow Types**:
   - Solid arrows for synchronous calls
   - Dotted arrows for responses/returns
   - Async arrows for fire-and-forget messages

4. **Autonumbering**: Enable for complex flows with many messages

5. **Activation**: Use activate=true to show when a participant is processing

6. **Notes**: Add notes for important timing, security, or business logic details

7. **Organization**: Keep flows left-to-right (client → server → database)

## Error Handling

### Common Errors

1. **"mermaid.ink rendering failed" - MOST COMMON**

   **Cause A: Unsupported participant types**
   - Using "boundary", "control", "entity", "database", etc.
   - **Solution**: Change ALL participant types to either "actor" or "participant"
   - **Example**: Change `{"type": "database"}` to `{"type": "participant", "label": "User Database"}`

   **Cause B: Special characters in message labels** (Very Common!)
   - Single quotes `'`, curly braces `{}`, angle brackets `<>`, pipes `|`, arrows `->`
   - **Solution**: Remove or replace problem characters:
     - Replace `'Add to cart'` with `Add to cart` (no quotes)
     - Replace `{productId}` with `(productId)` (parentheses instead)
     - Replace `GET /product/{id}` with `GET /product/ID` or `GET product by id`
     - Avoid `->` and `=>` - spell out relationships instead
   - **Fallback**: If `render_sequence_diagram` keeps failing, use `render_mermaid_diagram` with raw Mermaid code (see Fallback Strategy below)

2. **Unknown Participant**
   - All message references must match defined participant IDs (case-sensitive)
   - Check spelling and ensure participants are defined before being referenced

3. **Invalid Arrow Type**
   - Use only supported arrow types: "solid", "dotted", "solid_open", "dotted_open", "solid_cross", "dotted_cross", "async", "async_open"

4. **Invalid Note Position**
   - Must be "right of", "left of", or "over"

5. **Empty Messages**
   - All messages must have text content in the "message", "text", or "label" field

6. **Field Name Variations**
   - Tool accepts flexible field names (from/from_participant, message/text/label)
   - If one doesn't work, try the alternative

## Fallback Strategy: Using render_mermaid_diagram

If `render_sequence_diagram` keeps failing after fixing participant types and message labels, use the **`render_mermaid_diagram`** tool as a fallback. This tool accepts raw Mermaid code and often succeeds when the structured tool fails.

### How to use the fallback:

**Tool**: `render_mermaid_diagram`
- **Parameters**:
  - `code` (string): Raw Mermaid diagram code
  - `format` (string): "svg" or "png"
  - `theme` (string): "default", "dark", "forest", "neutral"
  - `filename` (string, optional): Output filename

**Example fallback usage:**
```json
{
  "code": "sequenceDiagram\n    title Add to Cart Flow\n    autonumber\n    actor Customer\n    participant App as Web App\n    participant API as API Gateway\n    participant Cart as Cart Service\n    participant DB as Cart Database\n\n    Customer->>App: Click Add to cart\n    App->>API: POST /cart/add (productId, qty)\n    API->>Cart: addItem(productId, qty)\n    Cart->>DB: upsertCartItem\n    DB-->>Cart: OK\n    Cart-->>API: 201 Created\n    API-->>App: 200 OK\n    App-->>Customer: Show success\n\n    Note over Cart,DB: Price validated",
  "format": "svg",
  "theme": "default",
  "filename": "add_to_cart.svg"
}
```

### Tips for raw Mermaid code:
- Use simple participant names (no special `actor` or `participant` keywords with `as` if having issues)
- Keep message labels clean and simple
- Use standard Mermaid arrow syntax: `-->` for dotted, `->` for solid, `->>` for with arrowhead
- Test your Mermaid code at mermaid.live first if needed
- Use `\n` for line breaks in JSON strings

## Notes

- Participant IDs are case-sensitive
- Messages appear in the order they are defined in the list
- Autonumbering starts at 1 and increments for each message
- Activation boxes show when a participant is actively processing
- Notes can span multiple participants using "over" position
- The tool supports flexible field naming for better compatibility
- For complex interactions, consider breaking into multiple diagrams
- Maximum recommended messages: 15-20 for optimal readability
