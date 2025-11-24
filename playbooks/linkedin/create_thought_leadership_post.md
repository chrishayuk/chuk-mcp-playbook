# Playbook: Create Thought Leadership Post

## Description
This playbook creates an authoritative thought leadership post that positions you as an industry expert. Thought leadership posts share insights, frameworks, predictions, or controversial perspectives that challenge conventional thinking. These posts build your professional brand and attract opportunities.

## Prerequisites
- Access to the chuk-mcp-linkedin server
- Expert knowledge or unique perspective on a topic
- Understanding of your target audience
- Original insight or framework to share

## Steps

1. Create a new draft with thought_leader theme
   - Initialize draft with compelling name
   - Apply "thought_leader" theme for authority positioning
   - Set post type to "text"

2. Add a bold or provocative hook
   - Use "bold" hook type for strong statements
   - Challenge conventional wisdom
   - Make a prediction or share contrarian view
   - Keep < 210 characters

3. Add structured body content
   - Share your framework or methodology
   - Use numbered list or clear structure
   - Include specific, actionable insights
   - Back up claims with experience or examples

4. Add supporting components
   - Timeline for processes or evolution
   - Key takeaway to emphasize main point
   - Checklist for actionable steps
   - Quote if relevant to add credibility

5. Add separator for visual breaks
   - Use visual separators to break up sections
   - Improve readability and scannability

6. Add strong CTA and hashtags
   - Direct or curiosity CTA to spark discussion
   - Invite debate or different perspectives
   - Use 3-5 industry-relevant hashtags
   - Compose and preview

## MCP Tools Required

### chuk-mcp-linkedin

**Tool 1**: `linkedin_create`
- **Parameters**:
  - `name` (string): Draft name (e.g., "Leadership Framework", "Industry Prediction 2025")
  - `post_type` (string): "text"
- **Returns**: Draft ID

**Tool 2**: `linkedin_apply_theme`
- **Parameters**:
  - `theme_name` (string): "thought_leader"
    - Professional, authoritative tone
    - Clear, structured formatting
    - Emphasis on insights and frameworks
- **Returns**: Theme applied confirmation

**Tool 3**: `linkedin_add_hook`
- **Parameters**:
  - `hook_type` (string): "bold" or "question"
    - `bold`: Strong statement or prediction
    - `question`: Thought-provoking question
  - `text` (string): Hook text (< 210 chars)
- **Returns**: Updated draft with hook

**Tool 4**: `linkedin_add_body`
- **Parameters**:
  - `content` (string): Main thought leadership content
  - `structure` (string): "listicle" or "problem_solution"
    - Use numbered lists for frameworks
    - Use problem-solution for insights
- **Returns**: Updated draft with body

**Tool 5**: `linkedin_add_numbered_list`
- **Parameters**:
  - `title` (string): List title (e.g., "My Framework:", "Key Principles:")
  - `items` (list): List of points
  - `style` (string): "numbered", "arrow", or "checkmark"
- **Returns**: Updated draft with formatted list
- **Use for**: Frameworks, principles, steps, lessons

**Tool 6**: `linkedin_add_timeline`
- **Parameters**:
  - `title` (string): Timeline title
  - `events` (list): List of time-ordered events
    - Each item: {"time": "Year/Stage", "event": "What happened"}
  - `style` (string): "vertical" or "horizontal"
- **Returns**: Updated draft with timeline
- **Use for**: Evolution, journey, process steps, historical context

**Tool 7**: `linkedin_add_key_takeaway`
- **Parameters**:
  - `takeaway` (string): Main insight or lesson
  - `highlight` (bool): Add visual emphasis (default: true)
- **Returns**: Updated draft with highlighted takeaway
- **Use for**: Emphasizing core message, TLDR, main lesson

**Tool 8**: `linkedin_add_checklist`
- **Parameters**:
  - `title` (string): Checklist title
  - `items` (list): List of actionable items
  - `checked` (list): Optional list of pre-checked items
- **Returns**: Updated draft with checklist
- **Use for**: Action items, implementation steps, best practices

**Tool 9**: `linkedin_add_quote`
- **Parameters**:
  - `quote` (string): Quote text
  - `author` (string): Quote attribution (optional)
  - `context` (string): Additional context (optional)
- **Returns**: Updated draft with formatted quote
- **Use for**: Supporting your point, adding credibility, inspiration

**Tool 10**: `linkedin_add_separator`
- **Parameters**:
  - `style` (string): "line", "dots", or "stars"
  - `length` (int): Separator length in characters
- **Returns**: Updated draft with visual separator
- **Use for**: Breaking sections, improving readability

**Tool 11**: `linkedin_add_tip_box`
- **Parameters**:
  - `message` (string): Tip or note content
  - `icon` (string): Emoji icon (default: "💡")
- **Returns**: Updated draft with highlighted tip box
- **Use for**: Pro tips, warnings, important notes

**Tool 12**: `linkedin_add_cta`
- **Parameters**:
  - `cta_type` (string): "direct", "curiosity", or "soft"
  - `text` (string): CTA text
- **Returns**: Updated draft with CTA

**Tool 13**: `linkedin_add_hashtags`
- **Parameters**:
  - `tags` (list): 3-5 relevant hashtags
- **Returns**: Updated draft with hashtags

**Tool 14**: `linkedin_compose_post`
- **Parameters**:
  - `spacing` (string): "spacious" (recommended for thought leadership)
- **Returns**: Composed post text

**Tool 15**: `linkedin_preview_url`
- **Parameters**: Optional draft_id
- **Returns**: Shareable preview URL

## Example Usage

**Input**: "Create a thought leadership post about why most product roadmaps fail"

**Process**:
1. Create draft: "Product Roadmap Framework"
2. Apply theme: "thought_leader"
3. Add hook: "Most product roadmaps are glorified wish lists. Here's why yours is probably failing..."
4. Add body: "After reviewing 100+ product roadmaps at Series A-C startups, I've identified the pattern. The problem isn't your features—it's your framework."
5. Add numbered list: "The 4-Part Roadmap Framework" with clear principles
6. Add timeline: Evolution from reactive to strategic roadmapping
7. Add key takeaway: "A roadmap isn't a promise—it's a hypothesis."
8. Add tip box: "Pro tip: Review your roadmap monthly, not quarterly"
9. Add separator for visual break
10. Add CTA: "What's your biggest roadmap challenge?"
11. Add hashtags: ["ProductManagement", "Leadership", "Strategy"]
12. Compose and preview

**Output**:
```
Most product roadmaps are glorified wish lists. Here's why yours is probably failing...

After reviewing 100+ product roadmaps at Series A-C startups, I've identified the pattern.

The problem isn't your features—it's your framework.

━━━━━━━━━━━━━━━━━━━━

The 4-Part Roadmap Framework:

1. Problem Space (not feature requests)
   → Define customer pain points first

2. Outcome Metrics (not output)
   → Measure impact, not delivery

3. Strategic Bets (not everything)
   → Say no to 80% of requests

4. Learning Loops (not fixed plans)
   → Iterate based on data

━━━━━━━━━━━━━━━━━━━━

Evolution Timeline:

2020: Reactive roadmap (customer requests drive everything)
2022: Feature-based roadmap (shipping as success metric)
2024: Outcome-based roadmap (impact as success metric)
2025: Strategic roadmap (bets on business objectives)

━━━━━━━━━━━━━━━━━━━━

💡 KEY TAKEAWAY:
A roadmap isn't a promise—it's a hypothesis.

💡 Pro tip: Review your roadmap monthly, not quarterly. Markets change fast.

What's your biggest roadmap challenge?

#ProductManagement #Leadership #Strategy
```

## Expected Response Format

```
[BOLD HOOK - Provocative statement or prediction]

[CONTEXT - Why this matters]

[SEPARATOR]

[FRAMEWORK/INSIGHTS - Numbered list or structure]

[SEPARATOR]

[SUPPORTING COMPONENT - Timeline, checklist, or quote]

[SEPARATOR]

[KEY TAKEAWAY - Main lesson]

[TIP BOX - Actionable advice]

[CTA - Invite discussion]

[Hashtags]
```

## Thought Leadership Themes

### Thought Leader (Default)
- Authority and expertise positioning
- Professional, insightful tone
- Clear frameworks and methodologies
- Best for: Industry insights, predictions, frameworks

### Contrarian Voice (Alternative)
- Challenge status quo
- Provocative, debate-sparking tone
- Question conventional wisdom
- Best for: Hot takes, controversial opinions

**To use Contrarian:**
```
linkedin_apply_theme(theme_name="contrarian_voice")
```

### Coach Mentor (Alternative)
- Guiding, supportive tone
- Teaching and mentorship focus
- Actionable advice emphasis
- Best for: Lessons learned, career advice

**To use Coach:**
```
linkedin_apply_theme(theme_name="coach_mentor")
```

## Hook Strategies for Thought Leadership

### Bold Statement Hook
- **Format**: "Most [common practice] is actually [opposite truth]"
- **Example**: "Most 'best practices' are just outdated group think"
- **Pro**: Stops the scroll, creates curiosity
- **Con**: Must deliver on the promise

### Prediction Hook
- **Format**: "[Specific prediction] by [timeframe]. Here's why..."
- **Example**: "AI won't replace PMs by 2027. It will replace the ones who don't adapt."
- **Pro**: Shows forward thinking, creates discussion
- **Con**: Will be judged if prediction wrong

### Personal Experience Hook
- **Format**: "After [X experiences], I learned [insight]"
- **Example**: "After 15 years in product, I finally understand what 'product-market fit' means"
- **Pro**: Authentic, builds credibility
- **Con**: Requires genuine experience to back it up

### Question Hook
- **Format**: "Why do [common behavior]? The answer might surprise you"
- **Example**: "Why do successful founders ignore most VC advice?"
- **Pro**: Creates curiosity, invites engagement
- **Con**: Can feel clickbait if not delivered

## Framework Development Guidelines

### Good Frameworks Are:
1. **Memorable** - Easy to recall and apply
2. **Actionable** - Concrete steps, not vague principles
3. **Specific** - Clear boundaries and definitions
4. **Tested** - Based on real experience or research
5. **Original** - Your unique perspective or synthesis

### Framework Structures:
- **Numbered Steps**: "The 5-Step X Framework"
- **Acronyms**: "CLEAR Product Strategy" (Concise, Learnable, etc.)
- **Matrices**: "Urgent vs Important" style 2x2s
- **Before/After**: Evolution or transformation model
- **Principles**: Core beliefs or rules to follow

### Example Frameworks:
- "The 3 Levels of Product Thinking"
- "IMPACT Framework for Career Growth"
- "The Strategic No: 4 Questions Before Saying Yes"
- "From Manager to Leader: 5 Mindset Shifts"

## Engagement Optimization

### Thought Leadership Post Performance
- **Average engagement**: 1.8x higher than standard posts
- **Share rate**: 2.4x more shares (people share expertise)
- **Comment quality**: 3x more substantive comments
- **Profile visits**: 5x more profile clicks
- **Long-term value**: Builds authority over time

### Optimal Post Structure
- **Length**: 500-1000 characters (longer acceptable for TL)
- **Components**: 3-5 distinct sections with separators
- **Formatting**: Heavy use of line breaks and visual structure
- **CTA**: Always invite perspective or debate

### Best Timing
- **Tuesday-Thursday**: 7-9 AM (catch morning commute)
- **Monday**: Avoid (information overload day)
- **Friday**: Good for weekend reading lists
- **Consistency**: Post regularly (weekly) to build authority

## Common Mistakes to Avoid

### 1. Vague Platitudes
- ❌ "Leadership is about inspiring people"
- ✅ "Leadership is making the decision no one else wants to make"

### 2. No Original Insight
- ❌ Repeating common advice everyone knows
- ✅ Challenging common advice with unique perspective

### 3. Too Abstract
- ❌ "Think strategically about product decisions"
- ✅ "Ask 'What are we NOT building?' before 'What should we build?'"

### 4. Lacking Credibility
- ❌ Sharing advice with no experience to back it up
- ✅ "After 50+ product launches, here's what I've learned..."

### 5. No Actionability
- ❌ "Be better at communication"
- ✅ "Start every meeting with the decision to be made"

## Error Handling

- Theme application failed: Verify theme name spelling
- Component addition failed: Check current draft is selected
- Composition too long: LinkedIn has 3,000 char limit
- Preview failed: Ensure at least hook and body added

## Notes

- Thought leadership posts get 1.8x more engagement than standard posts
- Share rate is 2.4x higher (people share valuable insights)
- Post consistently (weekly) to build authority over time
- Personal experience + framework = highest engagement
- Contrarian takes get 2x more comments but polarize audience
- Use separators liberally to improve readability
- Spacious formatting works better for longer content
- First 210 chars should include the provocative hook
- Always back up bold claims with experience or data
- Invite debate and discussion in CTA
- Hashtags should be industry-specific, not generic
- Best time: Tuesday-Thursday mornings
- Document posts can enhance thought leadership (45% higher engagement)
- Build a series of related posts to establish expertise
- Reference your previous posts to create content threads
