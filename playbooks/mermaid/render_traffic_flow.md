# Playbook: Visualize Traffic Flow

## Description
This playbook guides you through visualizing website traffic flows, user paths through your site, conversion funnels, and navigation patterns. Perfect for UX optimization, conversion rate improvement, and understanding user behavior.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Analytics data (Google Analytics, Mixpanel)
- Understanding of key user paths
- Knowledge of conversion goals

## Steps

1. **Identify key pages**
   - Landing pages
   - Category pages
   - Product/content pages
   - Checkout/conversion pages
   - Exit pages

2. **Map user journeys**
   - Entry points
   - Navigation paths
   - Drop-off points
   - Conversion funnels
   - Exit points

3. **Choose diagram type**
   - Use **sankey_diagram** for traffic flow volumes
   - Use **user_journey** for experience mapping
   - Use **flowchart** for funnel logic

4. **Create visualization**
   - Show traffic volumes between pages
   - Highlight conversion paths
   - Note drop-off rates
   - Document user segments

## MCP Tools Required

### Primary Tool: render_sankey_diagram
See [render_sankey_diagram.md](./render_sankey_diagram.md)

### Secondary Tool: render_user_journey
See [render_user_journey.md](./render_user_journey.md)

### Secondary Tool: render_flowchart
See [render_flowchart.md](./render_flowchart.md)

## Example Usage

### Scenario: E-commerce User Traffic Flow

**User Request**: "Show how users navigate through our e-commerce site from homepage to order confirmation, including drop-off points"

```json
{
  "nodes": [
    {"id": "home", "label": "Homepage"},
    {"id": "products", "label": "Products Page"},
    {"id": "product_detail", "label": "Product Details"},
    {"id": "cart", "label": "Cart"},
    {"id": "checkout", "label": "Checkout"},
    {"id": "confirmation", "label": "Order Confirmation"},
    {"id": "exit", "label": "Exit Site"}
  ],
  "links": [
    {"source": "home", "target": "products", "value": 1000},
    {"source": "home", "target": "exit", "value": 200},
    {"source": "products", "target": "product_detail", "value": 700},
    {"source": "products", "target": "exit", "value": 300},
    {"source": "product_detail", "target": "cart", "value": 350},
    {"source": "product_detail", "target": "exit", "value": 350},
    {"source": "cart", "target": "checkout", "value": 280},
    {"source": "cart", "target": "exit", "value": 70},
    {"source": "checkout", "target": "confirmation", "value": 210},
    {"source": "checkout", "target": "exit", "value": 70}
  ],
  "title": "E-commerce User Traffic Flow",
  "format": "svg",
  "theme": "default"
}
```

## Best Practices

1. **Show volumes** - Number of users or sessions
2. **Calculate conversion rates** - At each step
3. **Identify drop-offs** - Where users leave
4. **Segment traffic** - By source, device, cohort
5. **Track over time** - Monthly trends
6. **A/B test variations** - Compare flow changes
7. **Mobile vs desktop** - Separate analyses

## Related Playbooks

- [render_sankey_diagram.md](./render_sankey_diagram.md)
- [render_user_journey.md](./render_user_journey.md)
- [render_checkout_process.md](./render_checkout_process.md)
- [render_user_onboarding_flow.md](./render_user_onboarding_flow.md)
