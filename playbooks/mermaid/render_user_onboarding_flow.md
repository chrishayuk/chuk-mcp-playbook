# Playbook: Visualize User Onboarding Flow

## Description
This playbook guides you through visualizing user onboarding flows from signup through activation, including account creation, email verification, profile setup, and first-time user experience. Perfect for improving conversion, identifying drop-off points, and optimizing user experience.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Understanding of onboarding steps
- Knowledge of user journey touchpoints
- List of onboarding goals and metrics

## Steps

1. **Map onboarding journey**
   - Identify all onboarding steps
   - Note user actions required
   - Document system responses
   - Mark conversion points

2. **Identify drop-off points**
   - Where users abandon
   - Complex or confusing steps
   - Technical friction
   - Value communication gaps

3. **Choose diagram type**
   - Use **user_journey** for experience mapping
   - Use **flowchart** for process flow
   - Use **sequence_diagram** for system interactions

4. **Create visualization**
   - Show complete user path
   - Highlight key moments
   - Note friction points
   - Document success metrics

## MCP Tools Required

### Primary Tool: render_user_journey
Best for showing user experience and emotional journey.

See [render_user_journey.md](./render_user_journey.md) for full details.

### Primary Tool: render_flowchart
Best for showing onboarding process steps and logic.

See [render_flowchart.md](./render_flowchart.md) for full details.

### Secondary Tool: render_sequence_diagram
Best for showing technical onboarding interactions.

See [render_sequence_diagram.md](./render_sequence_diagram.md) for full details.

## Example Usage

### Scenario: SaaS Product Onboarding

```json
{
  "title": "SaaS Product Onboarding Journey",
  "sections": [
    {
      "section": "Sign Up",
      "tasks": [
        {"task": "Visit landing page", "score": 5},
        {"task": "Click 'Start Free Trial'", "score": 5},
        {"task": "Enter email and password", "score": 4},
        {"task": "Verify email", "score": 3}
      ]
    },
    {
      "section": "Profile Setup",
      "tasks": [
        {"task": "Enter company information", "score": 4},
        {"task": "Select role and team size", "score": 5},
        {"task": "Set preferences", "score": 4}
      ]
    },
    {
      "section": "First Experience",
      "tasks": [
        {"task": "Watch welcome video", "score": 4},
        {"task": "Complete interactive tutorial", "score": 5},
        {"task": "Create first project", "score": 5},
        {"task": "Invite team members", "score": 4}
      ]
    },
    {
      "section": "Activation",
      "tasks": [
        {"task": "Complete 3 key actions", "score": 5},
        {"task": "See value delivered", "score": 5},
        {"task": "Explore advanced features", "score": 4}
      ]
    }
  ],
  "format": "svg",
  "theme": "default"
}
```

## Best Practices

1. **Minimize friction** - Reduce steps to activation
2. **Show value early** - Quick wins in first session
3. **Progressive disclosure** - Don't overwhelm initially
4. **Track metrics** - Time to activation, completion rates
5. **Personalize experience** - Tailor to user role/needs
6. **Provide guidance** - Tooltips, tutorials, videos
7. **Celebrate milestones** - Acknowledge progress

## Common Variations

- Mobile app onboarding
- B2B vs B2C onboarding
- Freemium activation flows
- Enterprise onboarding (multi-step)
- Re-onboarding for major updates

## Related Playbooks

- [render_user_journey.md](./render_user_journey.md)
- [render_flowchart.md](./render_flowchart.md)
- [render_sequence_diagram.md](./render_sequence_diagram.md)
- [render_checkout_process.md](./render_checkout_process.md)

## Notes

- A/B test onboarding variations
- Track drop-off at each step
- Optimize for mobile and desktop
- Send follow-up emails for incomplete onboarding
- Measure time-to-value
