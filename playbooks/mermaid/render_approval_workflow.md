# Playbook: Visualize Approval Workflow

## Description
This playbook guides you through visualizing approval workflows including multi-level approvals, conditional routing, escalation paths, and timeout handling. Perfect for documenting business processes, compliance requirements, and decision chains.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Understanding of approval chain and hierarchy
- Knowledge of approval conditions and rules
- List of approvers and escalation paths

## Steps

1. **Identify approval stages**
   - List all approval levels
   - Note required approvers
   - Identify conditional approvals
   - Document escalation paths

2. **Map decision logic**
   - Document approval criteria
   - Note rejection paths
   - Identify parallel vs sequential approvals
   - Map timeout handling

3. **Choose diagram type**
   - Use **flowchart** for complex decision logic
   - Use **sequence_diagram** for approval interactions
   - Use **state_diagram** for status changes

4. **Create visualization**
   - Show all approval stages
   - Document decision points
   - Include escalation paths
   - Note timeouts and SLAs

## MCP Tools Required

### Primary Tool: render_flowchart
Best for showing approval decision logic and routing.

See [render_flowchart.md](./render_flowchart.md) for full details.

### Secondary Tool: render_sequence_diagram
Best for showing approval interactions between actors.

See [render_sequence_diagram.md](./render_sequence_diagram.md) for full details.

### Secondary Tool: render_state_diagram
Best for showing document/request status transitions.

See [render_state_diagram.md](./render_state_diagram.md) for full details.

## Example Usage

### Scenario: Purchase Order Approval Workflow

```json
{
  "nodes": [
    {"id": "start", "label": "Submit PO", "shape": "circle"},
    {"id": "check_amount", "label": "Amount < $1000?", "shape": "diamond"},
    {"id": "manager_review", "label": "Manager Review", "shape": "rectangle"},
    {"id": "manager_decision", "label": "Manager Approves?", "shape": "diamond"},
    {"id": "director_review", "label": "Director Review", "shape": "rectangle"},
    {"id": "director_decision", "label": "Director Approves?", "shape": "diamond"},
    {"id": "cfo_review", "label": "CFO Review (>$10k)", "shape": "rectangle"},
    {"id": "cfo_decision", "label": "CFO Approves?", "shape": "diamond"},
    {"id": "finance_process", "label": "Finance Processes", "shape": "rectangle"},
    {"id": "rejected", "label": "Send Rejection Notice", "shape": "rectangle"},
    {"id": "revise", "label": "Revise and Resubmit?", "shape": "diamond"},
    {"id": "approved", "label": "PO Approved", "shape": "circle"},
    {"id": "cancelled", "label": "PO Cancelled", "shape": "circle"}
  ],
  "edges": [
    {"from": "start", "to": "check_amount"},
    {"from": "check_amount", "to": "manager_review", "label": "No"},
    {"from": "check_amount", "to": "finance_process", "label": "Yes (auto-approve)"},
    {"from": "manager_review", "to": "manager_decision"},
    {"from": "manager_decision", "to": "director_review", "label": "Yes, >$10k"},
    {"from": "manager_decision", "to": "finance_process", "label": "Yes, <$10k"},
    {"from": "manager_decision", "to": "rejected", "label": "No"},
    {"from": "director_review", "to": "director_decision"},
    {"from": "director_decision", "to": "cfo_review", "label": "Yes, >$50k"},
    {"from": "director_decision", "to": "finance_process", "label": "Yes, <$50k"},
    {"from": "director_decision", "to": "rejected", "label": "No"},
    {"from": "cfo_review", "to": "cfo_decision"},
    {"from": "cfo_decision", "to": "finance_process", "label": "Yes"},
    {"from": "cfo_decision", "to": "rejected", "label": "No"},
    {"from": "finance_process", "to": "approved"},
    {"from": "rejected", "to": "revise"},
    {"from": "revise", "to": "start", "label": "Yes"},
    {"from": "revise", "to": "cancelled", "label": "No"}
  ],
  "direction": "TB",
  "title": "Purchase Order Approval Workflow",
  "format": "svg",
  "theme": "default"
}
```

## Best Practices

1. **Show all paths** - Include approval and rejection flows
2. **Document thresholds** - Note amount limits, criteria
3. **Include timeouts** - Show SLA and escalation timing
4. **Note authorities** - Document who can approve what
5. **Show escalation** - Map what happens on delays
6. **Track metrics** - Monitor approval times
7. **Document exceptions** - Show emergency override paths

## Common Variations

- Document approval workflows
- Expense approval chains
- Code review processes
- Contract approval workflows
- Leave request approvals

## Related Playbooks

- [render_flowchart.md](./render_flowchart.md)
- [render_sequence_diagram.md](./render_sequence_diagram.md)
- [render_state_diagram.md](./render_state_diagram.md)
- [render_application_state_machine.md](./render_application_state_machine.md)

## Notes

- Include compliance requirements (SOX, audit trails)
- Document delegation rules
- Show parallel vs sequential approvals
- Note notification mechanisms
- Export for process documentation and training
