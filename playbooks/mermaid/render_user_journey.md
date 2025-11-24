# Playbook: Render User Journey Diagram

## Description
This playbook creates user journey diagrams showing tasks, actors, and satisfaction scores across different stages. User journey diagrams are perfect for UX flows, customer experience mapping, and understanding user interactions with satisfaction metrics.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Understanding of user workflow stages
- Knowledge of tasks performed at each stage
- Actors involved in each task
- Satisfaction scores (1-5 scale) for each task

## Steps

1. Define journey stages/sections
   - Break the user journey into logical stages
   - Name each section clearly (Discovery, Purchase, Support, etc.)

2. Define tasks within each section
   - List tasks performed at each stage
   - Identify actors involved (User, System, Support, etc.)
   - Assign satisfaction scores (1=very dissatisfied, 5=very satisfied)

3. Call the render_user_journey tool
   - Pass title and sections
   - Include tasks with actors and scores

4. Review the generated diagram
   - Verify all journey stages are represented
   - Check that satisfaction scores reflect user experience

## MCP Tools Required

### mcp-mermaid-renderer

**Tool**: `render_user_journey`
- **Parameters**:
  - `title` (string, required): Journey title
  - `sections` (list of dict, required): Journey sections. Each dict should have:
    - `name` or `section` (string): Section name
    - `tasks` (list of dict): List of tasks with:
      - `name` or `task` (string): Task name
      - `actors` or `actor` (list or comma-separated string): List of actors
      - `score` or `satisfaction` (int): Satisfaction score 1-5
  - `format` (string): Output format - "svg" (default, recommended) or "png"
  - `theme` (string): Mermaid theme - "default", "dark", "forest", "neutral"
  - `bgcolor` (string): Background color (default: "transparent")
  - `filename` (string, optional): Suggested filename
- **Returns**: Artifact metadata with download URLs

## Example Usage

**Input**: "Create a user journey for an e-commerce shopping experience"

**Process**:
1. Identify journey stages: Discovery, Shopping, Checkout, Delivery, Support
2. Define tasks at each stage
3. Assign actors and satisfaction scores

**Tool Call**:
```json
{
  "title": "E-Commerce Shopping Journey",
  "sections": [
    {
      "name": "Discovery",
      "tasks": [
        {"name": "Browse products", "actors": ["Customer"], "score": 5},
        {"name": "Search for item", "actors": ["Customer", "Search System"], "score": 4}
      ]
    },
    {
      "name": "Shopping",
      "tasks": [
        {"name": "View product details", "actors": ["Customer"], "score": 5},
        {"name": "Add to cart", "actors": ["Customer", "Cart System"], "score": 4},
        {"name": "Apply coupon", "actors": ["Customer", "Pricing System"], "score": 3}
      ]
    },
    {
      "name": "Checkout",
      "tasks": [
        {"name": "Enter shipping info", "actors": ["Customer"], "score": 3},
        {"name": "Complete payment", "actors": ["Customer", "Payment Gateway"], "score": 4}
      ]
    },
    {
      "name": "Delivery",
      "tasks": [
        {"name": "Track shipment", "actors": ["Customer", "Logistics System"], "score": 4},
        {"name": "Receive package", "actors": ["Customer", "Delivery Driver"], "score": 5}
      ]
    },
    {
      "name": "Support",
      "tasks": [
        {"name": "Contact support", "actors": ["Customer", "Support Agent"], "score": 4},
        {"name": "Leave review", "actors": ["Customer"], "score": 5}
      ]
    }
  ],
  "format": "svg",
  "theme": "default"
}
```

**Output**:
```
User journey diagram rendered successfully!
- Format: SVG
- Sections: 5
- Total tasks: 11
- Download URL: [artifact link]
```

## Expected Response Format

The tool returns an artifact object with:
- `download_url`: URL to download the rendered diagram
- `source_code`: Editable Mermaid syntax
- `format`: Output format (svg or png)
- `diagram_type`: "journey"

## Common Use Cases

1. **E-Commerce**: Shopping experience, checkout process, returns
2. **SaaS Products**: Onboarding, feature usage, support interactions
3. **Customer Service**: Support ticket lifecycle, problem resolution
4. **Healthcare**: Patient journey, appointment booking, treatment flow
5. **Education**: Student learning journey, course enrollment, assessment
6. **Banking**: Account opening, loan application, customer service

## Best Practices

1. **Satisfaction Scores**:
   - 1: Very dissatisfied (critical issues)
   - 2: Dissatisfied (major pain points)
   - 3: Neutral (adequate but room for improvement)
   - 4: Satisfied (positive experience)
   - 5: Very satisfied (exceptional experience)
2. **Section Names**: Use short, clear stage names (2-3 words)
3. **Task Names**: Keep concise (3-6 words)
4. **Actors**: Include all relevant actors (users, systems, support staff)
   - Can be a list: ["Customer", "System"]
   - Or comma-separated string: "Customer, System"
5. **Journey Length**: 4-6 sections is ideal for readability
6. **Tasks per Section**: 2-4 tasks per section
7. **Pain Points**: Low scores (1-2) highlight areas needing improvement
8. **Delighters**: High scores (5) show what's working well

## Error Handling

- **Invalid Scores**: Scores must be 1-5
- **Missing Fields**: All tasks require name, actors, and score
- **Empty Sections**: Each section should have at least one task
- **Too Many Tasks**: More than 5 tasks per section may reduce readability

## Notes

- Satisfaction scores are visually represented in the diagram
- Actors can be specified as a list or comma-separated string
- Multiple actors per task show collaboration
- Tool accepts flexible field names: name/section/task, actors/actor, score/satisfaction
- Sections represent chronological stages in the journey
- Low scores help identify pain points for UX improvements
- High scores indicate positive experiences to maintain
- Use for both current state (as-is) and future state (to-be) journeys
- Recommended maximum: 6 sections with 3-4 tasks each
- For complex journeys, create multiple diagrams for different personas or paths
