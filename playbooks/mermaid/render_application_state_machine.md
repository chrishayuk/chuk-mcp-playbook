# Playbook: Visualize Application State Machine

## Description
This playbook guides you through visualizing state machines for applications, including order workflows, ticket lifecycles, document approval flows, and any process with defined states and transitions. Perfect for documenting business logic, planning state transitions, debugging workflow issues, and communicating requirements to stakeholders.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Understanding of all possible states in your workflow
- Knowledge of valid state transitions
- List of triggers and conditions for transitions

## Steps

1. **Identify all states**
   - List all possible states in the workflow
   - Identify initial state(s)
   - Note final/terminal states
   - Document transient vs stable states

2. **Map transitions**
   - Document valid state changes
   - Note transition triggers (events, actions)
   - Identify conditions for transitions
   - Map invalid/prohibited transitions

3. **Document business rules**
   - State entry actions
   - State exit actions
   - Validation rules
   - Time-based transitions

4. **Choose the appropriate diagram type**
   - Use **state_diagram** for state machines
   - Use **flowchart** for complex decision logic

5. **Create the visualization**
   - Show all states clearly
   - Label transitions with triggers
   - Document conditions
   - Include notes for business rules

## MCP Tools Required

### Primary Tool: render_state_diagram
Best for visualizing state machines with states and transitions.

See [render_state_diagram.md](./render_state_diagram.md) for full details.

### Secondary Tool: render_flowchart
Useful for documenting complex decision logic within state transitions.

See [render_flowchart.md](./render_flowchart.md) for full details.

## Recommended Diagram Type

### Primary: State Diagram
**When to use**: Workflow documentation, business logic specification, debugging state issues

**Strengths**:
- Shows states and transitions clearly
- Represents event-driven behavior
- Documents valid state changes
- Standard notation for state machines

**Example structure**:
```json
{
  "states": [
    {"id": "draft", "label": "Draft"},
    {"id": "submitted", "label": "Submitted"},
    {"id": "approved", "label": "Approved"}
  ],
  "transitions": [
    {"from": "draft", "to": "submitted", "label": "submit()"},
    {"from": "submitted", "to": "approved", "label": "approve()"}
  ]
}
```

### Secondary: Flowchart
**When to use**: Complex validation logic, multi-step decision processes

**Strengths**:
- Shows detailed decision logic
- Represents branching conditions
- Documents validation rules
- Good for implementation reference

## Example Usage

### Scenario 1: E-commerce Order State Machine

**User Request**: "Visualize the order lifecycle from creation to completion"

```json
{
  "states": [
    {"id": "start", "type": "start"},
    {"id": "pending", "label": "Pending Payment", "description": "Order created, awaiting payment"},
    {"id": "paid", "label": "Paid", "description": "Payment confirmed"},
    {"id": "processing", "label": "Processing", "description": "Order being prepared"},
    {"id": "shipped", "label": "Shipped", "description": "Order in transit"},
    {"id": "delivered", "label": "Delivered", "description": "Order received by customer"},
    {"id": "completed", "label": "Completed", "description": "Order finalized"},
    {"id": "cancelled", "label": "Cancelled", "description": "Order cancelled"},
    {"id": "refunded", "label": "Refunded", "description": "Payment refunded"},
    {"id": "end", "type": "end"}
  ],
  "transitions": [
    {"from": "start", "to": "pending", "label": "create order"},
    {"from": "pending", "to": "paid", "label": "payment success"},
    {"from": "pending", "to": "cancelled", "label": "payment timeout (30 min)"},
    {"from": "paid", "to": "processing", "label": "start fulfillment"},
    {"from": "processing", "to": "shipped", "label": "ship order"},
    {"from": "processing", "to": "cancelled", "label": "out of stock"},
    {"from": "shipped", "to": "delivered", "label": "delivery confirmed"},
    {"from": "delivered", "to": "completed", "label": "return window closed (14 days)"},
    {"from": "paid", "to": "refunded", "label": "cancel before shipping"},
    {"from": "processing", "to": "refunded", "label": "cancel during processing"},
    {"from": "delivered", "to": "refunded", "label": "return request"},
    {"from": "cancelled", "to": "end"},
    {"from": "refunded", "to": "end"},
    {"from": "completed", "to": "end"}
  ],
  "title": "E-commerce Order State Machine",
  "format": "svg",
  "theme": "default"
}
```

### Scenario 2: Support Ticket Lifecycle

**User Request**: "Show the support ticket workflow from creation to resolution"

```json
{
  "states": [
    {"id": "start", "type": "start"},
    {"id": "new", "label": "New", "description": "Ticket created"},
    {"id": "triaged", "label": "Triaged", "description": "Priority assigned"},
    {"id": "assigned", "label": "Assigned", "description": "Assigned to agent"},
    {"id": "in_progress", "label": "In Progress", "description": "Agent working on ticket"},
    {"id": "waiting_customer", "label": "Waiting on Customer", "description": "Pending customer response"},
    {"id": "waiting_internal", "label": "Waiting on Internal", "description": "Pending internal team"},
    {"id": "resolved", "label": "Resolved", "description": "Solution provided"},
    {"id": "closed", "label": "Closed", "description": "Ticket finalized"},
    {"id": "reopened", "label": "Reopened", "description": "Customer reopened"},
    {"id": "end", "type": "end"}
  ],
  "transitions": [
    {"from": "start", "to": "new", "label": "create ticket"},
    {"from": "new", "to": "triaged", "label": "triage()"},
    {"from": "triaged", "to": "assigned", "label": "assign()"},
    {"from": "assigned", "to": "in_progress", "label": "start work"},
    {"from": "in_progress", "to": "waiting_customer", "label": "request info"},
    {"from": "in_progress", "to": "waiting_internal", "label": "escalate"},
    {"from": "waiting_customer", "to": "in_progress", "label": "customer responds"},
    {"from": "waiting_customer", "to": "closed", "label": "no response (7 days)"},
    {"from": "waiting_internal", "to": "in_progress", "label": "internal responds"},
    {"from": "in_progress", "to": "resolved", "label": "provide solution"},
    {"from": "resolved", "to": "closed", "label": "customer confirms OR timeout (48h)"},
    {"from": "resolved", "to": "reopened", "label": "customer not satisfied"},
    {"from": "closed", "to": "reopened", "label": "reopen within 7 days"},
    {"from": "reopened", "to": "assigned", "label": "reassign"},
    {"from": "closed", "to": "end"}
  ],
  "title": "Support Ticket State Machine",
  "format": "svg",
  "theme": "default"
}
```

### Scenario 3: Document Approval Workflow

**User Request**: "Visualize our document approval process with multiple reviewers"

```json
{
  "states": [
    {"id": "start", "type": "start"},
    {"id": "draft", "label": "Draft", "description": "Author editing"},
    {"id": "submitted", "label": "Submitted for Review", "description": "Waiting for reviewers"},
    {"id": "under_review", "label": "Under Review", "description": "Reviewers reviewing"},
    {"id": "changes_requested", "label": "Changes Requested", "description": "Revisions needed"},
    {"id": "approved_manager", "label": "Manager Approved", "description": "Manager signed off"},
    {"id": "approved_legal", "label": "Legal Approved", "description": "Legal signed off"},
    {"id": "final_approval", "label": "Final Approval", "description": "Director review"},
    {"id": "published", "label": "Published", "description": "Document active"},
    {"id": "archived", "label": "Archived", "description": "No longer active"},
    {"id": "rejected", "label": "Rejected", "description": "Not approved"},
    {"id": "end", "type": "end"}
  ],
  "transitions": [
    {"from": "start", "to": "draft", "label": "create document"},
    {"from": "draft", "to": "submitted", "label": "submit()"},
    {"from": "draft", "to": "rejected", "label": "abandon"},
    {"from": "submitted", "to": "under_review", "label": "assign reviewers"},
    {"from": "under_review", "to": "changes_requested", "label": "request changes"},
    {"from": "under_review", "to": "approved_manager", "label": "manager approves"},
    {"from": "changes_requested", "to": "draft", "label": "return to author"},
    {"from": "approved_manager", "to": "approved_legal", "label": "legal approves"},
    {"from": "approved_legal", "to": "final_approval", "label": "route to director"},
    {"from": "final_approval", "to": "published", "label": "director approves"},
    {"from": "final_approval", "to": "changes_requested", "label": "director requests changes"},
    {"from": "published", "to": "archived", "label": "expire (2 years)"},
    {"from": "rejected", "to": "end"},
    {"from": "archived", "to": "end"}
  ],
  "title": "Document Approval State Machine",
  "format": "svg",
  "theme": "default"
}
```

### Scenario 4: User Account Lifecycle

**User Request**: "Show user account states from registration to deletion"

```json
{
  "states": [
    {"id": "start", "type": "start"},
    {"id": "unverified", "label": "Unverified", "description": "Email not confirmed"},
    {"id": "active", "label": "Active", "description": "Normal account"},
    {"id": "suspended", "label": "Suspended", "description": "Temporary suspension"},
    {"id": "locked", "label": "Locked", "description": "Too many failed logins"},
    {"id": "inactive", "label": "Inactive", "description": "No activity (90 days)"},
    {"id": "pending_deletion", "label": "Pending Deletion", "description": "Grace period (30 days)"},
    {"id": "deleted", "label": "Deleted", "description": "Account removed"},
    {"id": "banned", "label": "Banned", "description": "Policy violation"},
    {"id": "end", "type": "end"}
  ],
  "transitions": [
    {"from": "start", "to": "unverified", "label": "register"},
    {"from": "unverified", "to": "active", "label": "verify email"},
    {"from": "unverified", "to": "deleted", "label": "not verified (7 days)"},
    {"from": "active", "to": "suspended", "label": "admin suspends"},
    {"from": "active", "to": "locked", "label": "5 failed login attempts"},
    {"from": "active", "to": "inactive", "label": "no login (90 days)"},
    {"from": "active", "to": "pending_deletion", "label": "user requests deletion"},
    {"from": "active", "to": "banned", "label": "policy violation"},
    {"from": "suspended", "to": "active", "label": "suspension period ends"},
    {"from": "suspended", "to": "banned", "label": "repeated violations"},
    {"from": "locked", "to": "active", "label": "reset password"},
    {"from": "inactive", "to": "active", "label": "user logs in"},
    {"from": "inactive", "to": "deleted", "label": "admin cleanup (1 year)"},
    {"from": "pending_deletion", "to": "active", "label": "user cancels within 30 days"},
    {"from": "pending_deletion", "to": "deleted", "label": "grace period expires"},
    {"from": "deleted", "to": "end"},
    {"from": "banned", "to": "end"}
  ],
  "title": "User Account Lifecycle State Machine",
  "format": "svg",
  "theme": "default"
}
```

### Scenario 5: CI/CD Pipeline Build Status

**User Request**: "Visualize build status states in our CI/CD pipeline"

```json
{
  "states": [
    {"id": "start", "type": "start"},
    {"id": "queued", "label": "Queued", "description": "Waiting for runner"},
    {"id": "running", "label": "Running", "description": "Build in progress"},
    {"id": "testing", "label": "Testing", "description": "Running tests"},
    {"id": "success", "label": "Success", "description": "All checks passed"},
    {"id": "failed", "label": "Failed", "description": "Build or tests failed"},
    {"id": "cancelled", "label": "Cancelled", "description": "User cancelled"},
    {"id": "timeout", "label": "Timeout", "description": "Exceeded time limit"},
    {"id": "deploying", "label": "Deploying", "description": "Deploying to environment"},
    {"id": "deployed", "label": "Deployed", "description": "Successfully deployed"},
    {"id": "end", "type": "end"}
  ],
  "transitions": [
    {"from": "start", "to": "queued", "label": "push commit"},
    {"from": "queued", "to": "running", "label": "runner available"},
    {"from": "queued", "to": "cancelled", "label": "user cancels"},
    {"from": "running", "to": "testing", "label": "build success"},
    {"from": "running", "to": "failed", "label": "build failed"},
    {"from": "running", "to": "cancelled", "label": "user cancels"},
    {"from": "running", "to": "timeout", "label": "exceeds 60 min"},
    {"from": "testing", "to": "success", "label": "tests pass"},
    {"from": "testing", "to": "failed", "label": "tests fail"},
    {"from": "testing", "to": "timeout", "label": "exceeds 60 min"},
    {"from": "success", "to": "deploying", "label": "auto-deploy enabled"},
    {"from": "deploying", "to": "deployed", "label": "deployment success"},
    {"from": "deploying", "to": "failed", "label": "deployment failed"},
    {"from": "failed", "to": "end"},
    {"from": "cancelled", "to": "end"},
    {"from": "timeout", "to": "end"},
    {"from": "deployed", "to": "end"}
  ],
  "title": "CI/CD Build Status State Machine",
  "format": "svg",
  "theme": "default"
}
```

## Alternative Approaches

### Option 1: Flowchart for Decision Logic
Use flowcharts when:
- Transitions have complex conditional logic
- Multiple validation steps required
- Need to show detailed business rules
- Documenting implementation details

### Option 2: Sequence Diagram for Actor Interactions
Use sequence diagrams when:
- Showing who triggers state changes
- Documenting system interactions during transitions
- Representing time-based workflows
- Including external service calls

### Option 3: Multiple State Diagrams
For complex systems:
- Main workflow state diagram
- Error handling state diagram
- Admin intervention flows
- Subprocess state machines

## Best Practices

### 1. Identify All States
- Include both stable and transient states
- Document error states
- Note initial and final states
- Consider edge cases

### 2. Label Transitions Clearly
- Use action verbs (submit, approve, cancel)
- Include conditions [if applicable]
- Note timeouts and auto-transitions
- Document triggers

### 3. Document Time-Based Transitions
- Auto-transitions after timeout
- Scheduled state changes
- Expiration logic
- SLA-based transitions

### 4. Show Error Paths
- What happens on validation failure
- Timeout handling
- System errors
- Compensation logic

### 5. Include Business Rules
- Who can trigger transitions
- Required permissions
- Validation requirements
- Preconditions and postconditions

### 6. Note State Actions
- Entry actions (on entering state)
- Exit actions (on leaving state)
- Internal actions (while in state)
- Side effects

### 7. Keep It Focused
- One business entity per diagram
- Separate concerns (order vs payment)
- Abstract subprocesses if too complex
- Link related state machines

## Common Variations

### Variation 1: Hierarchical State Machine
States with substates:
- Parent state with child states
- Nested state transitions
- State composition
- Complex workflows

### Variation 2: Concurrent State Machine
Parallel states:
- Multiple active states simultaneously
- Independent state regions
- Synchronization points
- Fork and join

### Variation 3: Event-Driven State Machine
Focus on events:
- External events triggering transitions
- Message-driven architecture
- Event sourcing patterns
- CQRS integration

### Variation 4: Time-Based State Machine
Temporal workflows:
- Scheduled transitions
- Duration-based states
- Calendar-driven changes
- Expiration handling

### Variation 5: Multi-Entity State Orchestration
Coordinated state changes:
- Order + Payment states
- Document + Approval states
- Cart + Inventory states
- Saga patterns

## Related Playbooks

### Core Diagram Types
- [render_state_diagram.md](./render_state_diagram.md) - State machine diagrams
- [render_flowchart.md](./render_flowchart.md) - Decision logic
- [render_sequence_diagram.md](./render_sequence_diagram.md) - Actor interactions

### Related Scenarios
- [render_approval_workflow.md](./render_approval_workflow.md) - Approval processes
- [render_checkout_process.md](./render_checkout_process.md) - E-commerce flows
- [render_user_onboarding_flow.md](./render_user_onboarding_flow.md) - User journeys
- [render_deployment_pipeline.md](./render_deployment_pipeline.md) - Build states

## Notes

- State machines should be deterministic (same input → same transition)
- Document invalid transitions explicitly or implicitly
- Consider idempotency for state transitions
- Note database transaction boundaries
- Include rollback/compensation logic
- Document state persistence mechanism
- Consider event sourcing for audit trails
- Export in SVG for technical documentation
- Keep diagrams synced with actual implementation
- Use state diagram as source of truth for implementation
- Generate state machine code from diagrams when possible
- Test all possible transitions, including edge cases
