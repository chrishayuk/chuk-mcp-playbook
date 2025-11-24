# Playbook: Visualize Checkout Process

## Description
This playbook guides you through visualizing e-commerce checkout flows including cart review, shipping selection, payment processing, and order confirmation. Perfect for optimizing conversion rates, reducing cart abandonment, and improving user experience.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Understanding of checkout steps
- Knowledge of payment integration
- List of validation rules and error scenarios

## Steps

1. **Map checkout steps**
   - Cart review
   - Shipping address
   - Shipping method
   - Payment information
   - Order review
   - Confirmation

2. **Identify decision points**
   - Guest vs registered checkout
   - Shipping options
   - Payment methods
   - Promo code application
   - Error handling

3. **Choose diagram type**
   - Use **flowchart** for checkout logic
   - Use **sequence_diagram** for payment processing
   - Use **state_diagram** for order status

4. **Create visualization**
   - Show complete checkout path
   - Document validation steps
   - Include error handling
   - Note payment security

## MCP Tools Required

### Primary Tool: render_flowchart
See [render_flowchart.md](./render_flowchart.md)

### Secondary Tool: render_sequence_diagram
See [render_sequence_diagram.md](./render_sequence_diagram.md)

### Secondary Tool: render_state_diagram
See [render_state_diagram.md](./render_state_diagram.md)

## Example Usage

```json
{
  "nodes": [
    {"id": "start", "label": "Cart Page", "shape": "circle"},
    {"id": "check_login", "label": "User logged in?", "shape": "diamond"},
    {"id": "guest_or_login", "label": "Continue as guest or login?", "shape": "diamond"},
    {"id": "login", "label": "Login Form", "shape": "rectangle"},
    {"id": "shipping_address", "label": "Enter Shipping Address", "shape": "rectangle"},
    {"id": "validate_address", "label": "Valid address?", "shape": "diamond"},
    {"id": "shipping_method", "label": "Select Shipping Method", "shape": "rectangle"},
    {"id": "payment_method", "label": "Enter Payment Info", "shape": "rectangle"},
    {"id": "validate_payment", "label": "Valid payment?", "shape": "diamond"},
    {"id": "review_order", "label": "Review Order", "shape": "rectangle"},
    {"id": "promo_code", "label": "Apply promo code?", "shape": "diamond"},
    {"id": "apply_promo", "label": "Apply Discount", "shape": "rectangle"},
    {"id": "process_payment", "label": "Process Payment", "shape": "rectangle"},
    {"id": "payment_success", "label": "Payment successful?", "shape": "diamond"},
    {"id": "create_order", "label": "Create Order", "shape": "rectangle"},
    {"id": "send_confirmation", "label": "Send Confirmation Email", "shape": "rectangle"},
    {"id": "show_confirmation", "label": "Show Confirmation Page", "shape": "rectangle"},
    {"id": "show_error", "label": "Show Error Message", "shape": "rectangle"},
    {"id": "end", "label": "Complete", "shape": "circle"}
  ],
  "edges": [
    {"from": "start", "to": "check_login"},
    {"from": "check_login", "to": "shipping_address", "label": "Yes"},
    {"from": "check_login", "to": "guest_or_login", "label": "No"},
    {"from": "guest_or_login", "to": "login", "label": "Login"},
    {"from": "guest_or_login", "to": "shipping_address", "label": "Guest"},
    {"from": "login", "to": "shipping_address"},
    {"from": "shipping_address", "to": "validate_address"},
    {"from": "validate_address", "to": "shipping_method", "label": "Valid"},
    {"from": "validate_address", "to": "shipping_address", "label": "Invalid"},
    {"from": "shipping_method", "to": "payment_method"},
    {"from": "payment_method", "to": "validate_payment"},
    {"from": "validate_payment", "to": "review_order", "label": "Valid"},
    {"from": "validate_payment", "to": "payment_method", "label": "Invalid"},
    {"from": "review_order", "to": "promo_code"},
    {"from": "promo_code", "to": "apply_promo", "label": "Yes"},
    {"from": "promo_code", "to": "process_payment", "label": "No"},
    {"from": "apply_promo", "to": "process_payment"},
    {"from": "process_payment", "to": "payment_success"},
    {"from": "payment_success", "to": "create_order", "label": "Success"},
    {"from": "payment_success", "to": "show_error", "label": "Failed"},
    {"from": "create_order", "to": "send_confirmation"},
    {"from": "send_confirmation", "to": "show_confirmation"},
    {"from": "show_confirmation", "to": "end"},
    {"from": "show_error", "to": "payment_method"}
  ],
  "direction": "TB",
  "title": "E-commerce Checkout Flow",
  "format": "svg",
  "theme": "default"
}
```

## Best Practices

1. **Minimize steps** - Reduce friction to purchase
2. **Show progress** - Display checkout steps completed
3. **Save progress** - Allow users to return to cart
4. **Guest checkout** - Don't force account creation
5. **Multiple payment options** - Credit card, PayPal, etc.
6. **Clear error messages** - Help users fix issues
7. **Security indicators** - Show SSL, PCI compliance
8. **Mobile optimization** - Responsive checkout forms

## Related Playbooks

- [render_flowchart.md](./render_flowchart.md)
- [render_user_onboarding_flow.md](./render_user_onboarding_flow.md)
- [render_application_state_machine.md](./render_application_state_machine.md)
- [render_api_interaction_flow.md](./render_api_interaction_flow.md)
