# Playbook: Visualize Class Hierarchy

## Description
This playbook guides you through visualizing object-oriented class hierarchies, including inheritance relationships, interfaces, composition, aggregation, and method signatures. Perfect for documenting software architecture, planning refactoring, understanding codebases, and communicating design patterns to team members.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Understanding of your class structure
- Knowledge of inheritance and composition relationships
- List of classes, interfaces, and their members

## Steps

1. **Identify classes and interfaces**
   - List all classes in the hierarchy
   - Identify abstract classes
   - Note interfaces
   - Document enums and data classes

2. **Map relationships**
   - Inheritance (is-a)
   - Interface implementation
   - Composition (has-a)
   - Aggregation
   - Dependencies

3. **Document class members**
   - Important fields/properties
   - Key methods
   - Access modifiers
   - Static members

4. **Choose the appropriate diagram type**
   - Use **class_diagram** for OOP hierarchies

5. **Create the visualization**
   - Show inheritance chains
   - Document relationships
   - Include important members
   - Add notes for design patterns

## MCP Tools Required

### Primary Tool: render_class_diagram
Best for visualizing object-oriented class structures and relationships.

See [render_class_diagram.md](./render_class_diagram.md) for full details.

## Recommended Diagram Type

### Primary: Class Diagram
**When to use**: Code documentation, architecture planning, design review

**Strengths**:
- Shows class structure clearly
- Represents OOP relationships
- Documents methods and properties
- Standard UML notation

## Example Usage

### Scenario 1: E-commerce Domain Model

**User Request**: "Visualize our e-commerce domain model with products, orders, and users"

```json
{
  "classes": [
    {
      "name": "User",
      "type": "class",
      "attributes": [
        "+ id: UUID",
        "+ email: string",
        "+ name: string",
        "- passwordHash: string",
        "+ createdAt: DateTime"
      ],
      "methods": [
        "+ register(email, password): User",
        "+ login(email, password): Token",
        "+ updateProfile(data): void",
        "- hashPassword(password): string"
      ]
    },
    {
      "name": "Customer",
      "type": "class",
      "attributes": [
        "+ shippingAddresses: Address[]",
        "+ paymentMethods: PaymentMethod[]",
        "+ orderHistory: Order[]"
      ],
      "methods": [
        "+ placeOrder(cart: Cart): Order",
        "+ addAddress(address: Address): void",
        "+ getOrders(status: string): Order[]"
      ]
    },
    {
      "name": "Admin",
      "type": "class",
      "attributes": [
        "+ permissions: Permission[]",
        "+ role: AdminRole"
      ],
      "methods": [
        "+ manageProducts(): void",
        "+ viewAllOrders(): Order[]",
        "+ generateReports(): Report"
      ]
    },
    {
      "name": "Product",
      "type": "class",
      "attributes": [
        "+ id: UUID",
        "+ sku: string",
        "+ name: string",
        "+ description: string",
        "+ price: Money",
        "+ inventory: number"
      ],
      "methods": [
        "+ updatePrice(price: Money): void",
        "+ addInventory(quantity: number): void",
        "+ isInStock(): boolean"
      ]
    },
    {
      "name": "Order",
      "type": "class",
      "attributes": [
        "+ id: UUID",
        "+ customer: Customer",
        "+ items: OrderItem[]",
        "+ status: OrderStatus",
        "+ total: Money",
        "+ createdAt: DateTime"
      ],
      "methods": [
        "+ addItem(product: Product, quantity: number): void",
        "+ calculateTotal(): Money",
        "+ processPayment(method: PaymentMethod): void",
        "+ ship(): void"
      ]
    },
    {
      "name": "OrderItem",
      "type": "class",
      "attributes": [
        "+ product: Product",
        "+ quantity: number",
        "+ unitPrice: Money",
        "+ subtotal: Money"
      ],
      "methods": [
        "+ calculateSubtotal(): Money"
      ]
    },
    {
      "name": "Address",
      "type": "class",
      "attributes": [
        "+ street: string",
        "+ city: string",
        "+ state: string",
        "+ postalCode: string",
        "+ country: string"
      ],
      "methods": [
        "+ format(): string",
        "+ validate(): boolean"
      ]
    },
    {
      "name": "PaymentMethod",
      "type": "interface",
      "methods": [
        "+ charge(amount: Money): Transaction",
        "+ refund(transaction: Transaction): void",
        "+ validate(): boolean"
      ]
    },
    {
      "name": "CreditCard",
      "type": "class",
      "attributes": [
        "- cardNumber: string",
        "- expiryDate: string",
        "- cvv: string"
      ],
      "methods": [
        "+ charge(amount: Money): Transaction",
        "+ refund(transaction: Transaction): void",
        "+ validate(): boolean"
      ]
    },
    {
      "name": "PayPal",
      "type": "class",
      "attributes": [
        "+ email: string",
        "+ accountId: string"
      ],
      "methods": [
        "+ charge(amount: Money): Transaction",
        "+ refund(transaction: Transaction): void",
        "+ validate(): boolean"
      ]
    }
  ],
  "relationships": [
    {"from": "Customer", "to": "User", "type": "inheritance"},
    {"from": "Admin", "to": "User", "type": "inheritance"},
    {"from": "Customer", "to": "Order", "type": "association", "label": "places", "multiplicity": "1..*"},
    {"from": "Order", "to": "OrderItem", "type": "composition", "label": "contains", "multiplicity": "1..*"},
    {"from": "OrderItem", "to": "Product", "type": "association", "label": "references"},
    {"from": "Customer", "to": "Address", "type": "aggregation", "label": "has", "multiplicity": "0..*"},
    {"from": "CreditCard", "to": "PaymentMethod", "type": "implements"},
    {"from": "PayPal", "to": "PaymentMethod", "type": "implements"},
    {"from": "Order", "to": "PaymentMethod", "type": "dependency", "label": "uses"}
  ],
  "title": "E-commerce Domain Model",
  "format": "svg",
  "theme": "default"
}
```

### Scenario 2: Design Pattern - Strategy Pattern

**User Request**: "Show the Strategy pattern implementation for payment processing"

```json
{
  "classes": [
    {
      "name": "PaymentProcessor",
      "type": "class",
      "attributes": [
        "- strategy: PaymentStrategy"
      ],
      "methods": [
        "+ __init__(strategy: PaymentStrategy)",
        "+ setStrategy(strategy: PaymentStrategy): void",
        "+ processPayment(amount: float): bool"
      ]
    },
    {
      "name": "PaymentStrategy",
      "type": "interface",
      "methods": [
        "+ pay(amount: float): bool",
        "+ refund(transactionId: string): bool"
      ]
    },
    {
      "name": "CreditCardStrategy",
      "type": "class",
      "attributes": [
        "- cardNumber: string",
        "- cvv: string",
        "- gateway: PaymentGateway"
      ],
      "methods": [
        "+ pay(amount: float): bool",
        "+ refund(transactionId: string): bool",
        "- validateCard(): bool"
      ]
    },
    {
      "name": "PayPalStrategy",
      "type": "class",
      "attributes": [
        "- email: string",
        "- apiClient: PayPalAPI"
      ],
      "methods": [
        "+ pay(amount: float): bool",
        "+ refund(transactionId: string): bool"
      ]
    },
    {
      "name": "CryptoStrategy",
      "type": "class",
      "attributes": [
        "- walletAddress: string",
        "- blockchain: BlockchainAPI"
      ],
      "methods": [
        "+ pay(amount: float): bool",
        "+ refund(transactionId: string): bool",
        "- confirmTransaction(): bool"
      ]
    }
  ],
  "relationships": [
    {"from": "PaymentProcessor", "to": "PaymentStrategy", "type": "association", "label": "uses"},
    {"from": "CreditCardStrategy", "to": "PaymentStrategy", "type": "implements"},
    {"from": "PayPalStrategy", "to": "PaymentStrategy", "type": "implements"},
    {"from": "CryptoStrategy", "to": "PaymentStrategy", "type": "implements"}
  ],
  "title": "Strategy Pattern - Payment Processing",
  "format": "svg",
  "theme": "default"
}
```

### Scenario 3: REST API Controllers (MVC Pattern)

**User Request**: "Document our REST API controller hierarchy"

```json
{
  "classes": [
    {
      "name": "BaseController",
      "type": "abstract",
      "attributes": [
        "# logger: Logger",
        "# db: Database"
      ],
      "methods": [
        "+ handleError(error: Error): Response",
        "+ validateRequest(req: Request): bool",
        "# authenticate(req: Request): User"
      ]
    },
    {
      "name": "UserController",
      "type": "class",
      "methods": [
        "+ GET /users: User[]",
        "+ GET /users/:id: User",
        "+ POST /users: User",
        "+ PUT /users/:id: User",
        "+ DELETE /users/:id: void"
      ]
    },
    {
      "name": "ProductController",
      "type": "class",
      "methods": [
        "+ GET /products: Product[]",
        "+ GET /products/:id: Product",
        "+ POST /products: Product",
        "+ PUT /products/:id: Product",
        "+ DELETE /products/:id: void",
        "+ GET /products/:id/inventory: number"
      ]
    },
    {
      "name": "OrderController",
      "type": "class",
      "methods": [
        "+ GET /orders: Order[]",
        "+ GET /orders/:id: Order",
        "+ POST /orders: Order",
        "+ PUT /orders/:id/status: Order",
        "+ POST /orders/:id/cancel: void"
      ]
    },
    {
      "name": "AuthController",
      "type": "class",
      "attributes": [
        "- jwtSecret: string",
        "- tokenExpiry: number"
      ],
      "methods": [
        "+ POST /auth/register: Token",
        "+ POST /auth/login: Token",
        "+ POST /auth/refresh: Token",
        "+ POST /auth/logout: void",
        "- generateToken(user: User): string"
      ]
    }
  ],
  "relationships": [
    {"from": "UserController", "to": "BaseController", "type": "inheritance"},
    {"from": "ProductController", "to": "BaseController", "type": "inheritance"},
    {"from": "OrderController", "to": "BaseController", "type": "inheritance"},
    {"from": "AuthController", "to": "BaseController", "type": "inheritance"}
  ],
  "title": "REST API Controller Hierarchy",
  "format": "svg",
  "theme": "default"
}
```

## Alternative Approaches

### Option 1: Multiple Diagrams by Layer
Create separate diagrams for:
- Domain model layer
- Service layer
- Controller/API layer
- Data access layer

### Option 2: Focus on Design Patterns
Highlight specific patterns:
- Factory pattern
- Observer pattern
- Decorator pattern
- Singleton pattern

### Option 3: Simplified Overview
High-level view:
- Show only class names
- Hide methods and properties
- Focus on relationships
- Good for presentations

## Best Practices

### 1. Show Key Members Only
- Include important public methods
- Show critical properties
- Hide trivial getters/setters (unless relevant)
- Note design pattern roles

### 2. Use Access Modifiers
- + public
- - private
- # protected
- ~ package/internal

### 3. Document Relationships Clearly
- Inheritance (solid line, closed arrow)
- Implementation (dashed line, closed arrow)
- Association (solid line, open arrow)
- Composition (solid line, filled diamond)
- Aggregation (solid line, hollow diamond)
- Dependency (dashed line, open arrow)

### 4. Show Multiplicity
- 1 (exactly one)
- 0..1 (zero or one)
- * or 0..* (zero or more)
- 1..* (one or more)
- n..m (specific range)

### 5. Use Abstract Classes and Interfaces
- Mark abstract classes clearly
- Show interfaces distinctly
- Document abstract methods
- Note template methods

### 6. Group Related Classes
- By package/module
- By layer (domain, service, controller)
- By feature area
- By design pattern

### 7. Keep It Focused
- One subsystem per diagram
- Maximum 10-15 classes
- Abstract unnecessary details
- Link to related diagrams

## Common Variations

### Variation 1: Database ORM Models
For Django/SQLAlchemy/JPA:
- Show model classes
- Document field types
- Note foreign keys
- Include model methods

### Variation 2: React Component Hierarchy
For frontend components:
- Show component relationships
- Document props and state
- Note lifecycle methods
- Show composition

### Variation 3: Microservices Internal Structure
Per-service class hierarchy:
- Domain models
- Service classes
- Repository pattern
- DTO/VO objects

### Variation 4: Plugin Architecture
Extensible systems:
- Plugin interface
- Core classes
- Extension points
- Plugin implementations

### Variation 5: Testing Class Structure
Test organization:
- Test base classes
- Test fixtures
- Mocks and stubs
- Helper utilities

## Related Playbooks

### Core Diagram Types
- [render_class_diagram.md](./render_class_diagram.md) - Class diagram creation

### Related Scenarios
- [render_database_schema_visualization.md](./render_database_schema_visualization.md) - Database models
- [render_microservices_architecture.md](./render_microservices_architecture.md) - Service structure
- [render_api_interaction_flow.md](./render_api_interaction_flow.md) - API design

## Notes

- Keep diagrams focused on one aspect or layer
- Use consistent naming conventions
- Document design patterns in notes
- Include type information when relevant
- Show generic types (List<T>, Map<K,V>)
- Note SOLID principles violations or adherence
- Export in SVG for code documentation
- Generate diagrams from code when possible (javadoc, pydoc)
- Keep diagrams synced with codebase
- Use as design tool before implementation
- Include in architecture decision records (ADRs)
- Document breaking changes when refactoring
