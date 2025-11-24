# Playbook: Create Simple LinkedIn Text Post

## Description
This playbook creates a straightforward LinkedIn text post with a hook, body content, call-to-action, and hashtags. Perfect for quick updates, thoughts, or announcements.

## Prerequisites
- Access to the chuk-mcp-linkedin server
- Post content idea or topic
- Target audience understanding

## Steps

1. Create a new draft
   - Initialize a new draft with a descriptive name
   - Set post type to "text"

2. Add an engaging hook
   - Choose hook type based on content (question, stat, bold statement)
   - Keep within first 210 characters (LinkedIn's preview limit)
   - Make it attention-grabbing to prevent scroll-past

3. Add body content
   - Write main message clearly and concisely
   - Use line breaks for readability
   - Keep total length 300-800 characters for optimal engagement
   - Choose structure: linear, listicle, or problem-solution

4. Add call-to-action
   - Select CTA type: direct, curiosity, or soft
   - Encourage engagement (comments, shares, thoughts)

5. Add relevant hashtags
   - Choose 3-5 relevant hashtags (optimal range)
   - Mix popular and niche hashtags
   - Avoid over-hashtagging (10+ reduces reach)

6. Compose and preview
   - Compose final post from components
   - Generate preview to check formatting
   - Review character count and visual layout

## MCP Tools Required

### chuk-mcp-linkedin

**Tool 1**: `linkedin_create`
- **Parameters**:
  - `name` (string): Descriptive name for the draft (e.g., "Monday Motivation Post", "Product Launch")
  - `post_type` (string): "text" for simple text posts
- **Returns**: Draft ID and confirmation

**Tool 2**: `linkedin_add_hook`
- **Parameters**:
  - `hook_type` (string): Hook style to use:
    - `question` - Engaging question to spark curiosity
    - `stat` - Powerful statistic or number
    - `bold` - Bold statement or controversial take
    - `story` - Brief story opening
  - `text` (string): The actual hook text (keep < 210 chars)
- **Returns**: Updated draft with hook component

**Tool 3**: `linkedin_add_body`
- **Parameters**:
  - `content` (string): Main message content
  - `structure` (string): Content structure:
    - `linear` - Straightforward narrative
    - `listicle` - Bulleted or numbered list
    - `problem_solution` - Problem statement followed by solution
- **Returns**: Updated draft with body content

**Tool 4**: `linkedin_add_cta`
- **Parameters**:
  - `cta_type` (string): Call-to-action style:
    - `direct` - Direct request (e.g., "Comment below")
    - `curiosity` - Question to spark conversation
    - `soft` - Gentle invitation to engage
  - `text` (string): The CTA message
- **Returns**: Updated draft with CTA component

**Tool 5**: `linkedin_add_hashtags`
- **Parameters**:
  - `tags` (list): List of hashtags without # symbol
    - Optimal: 3-5 hashtags
    - Example: ["LinkedInTips", "CareerGrowth", "Leadership"]
- **Returns**: Updated draft with hashtags

**Tool 6**: `linkedin_compose_post`
- **Parameters**:
  - `spacing` (string): Component spacing ("compact" or "spacious")
  - `include_preview` (bool): Whether to include preview
- **Returns**: Composed post text with all components

**Tool 7**: `linkedin_get_preview`
- **Parameters**: None (uses current draft)
- **Returns**: Preview of post (first 210 characters)

**Tool 8**: `linkedin_preview_url` (optional)
- **Parameters**:
  - `draft_id` (string): Draft ID to preview (optional, uses current)
  - `expires_in` (int): URL expiration in seconds (default: 3600)
- **Returns**: Shareable preview URL

## Example Usage

**Input**: "Create a post about the importance of LinkedIn networking for career growth"

**Process**:
1. Create draft: "Networking Tips Post"
2. Add hook: question type - "Want to 10x your career opportunities?"
3. Add body: "Networking on LinkedIn isn't about collecting connections. It's about building real relationships. Here's what changed for me: → Engaged with 5 posts daily → Sent personalized connection requests → Helped others without expecting returns Result? 3 job offers in 6 months."
4. Add CTA: curiosity type - "What's your networking strategy?"
5. Add hashtags: ["CareerGrowth", "LinkedInNetworking", "ProfessionalDevelopment"]
6. Compose and preview

**Output**:
```
Want to 10x your career opportunities?

Networking on LinkedIn isn't about collecting connections.
It's about building real relationships.

Here's what changed for me:

→ Engaged with 5 posts daily
→ Sent personalized connection requests
→ Helped others without expecting returns

Result? 3 job offers in 6 months.

What's your networking strategy?

#CareerGrowth #LinkedInNetworking #ProfessionalDevelopment
```

## Expected Response Format

```
[HOOK - First 210 characters]

[BODY CONTENT with line breaks for readability]

[CALL TO ACTION]

[Hashtags]
```

## Hook Type Guidelines

### Question Hook
- Best for: Engagement, starting conversations
- Example: "Want to know the secret to viral LinkedIn posts?"
- Pro: High engagement potential
- Con: Can feel clickbait if not authentic

### Stat Hook
- Best for: Authority, data-driven content
- Example: "95% of LinkedIn posts get zero engagement."
- Pro: Grabs attention with concrete numbers
- Con: Needs to be verifiable and relevant

### Bold Statement Hook
- Best for: Thought leadership, controversial takes
- Example: "Most career advice on LinkedIn is terrible."
- Pro: Pattern interrupt, stops scrolling
- Con: Can alienate if too aggressive

### Story Hook
- Best for: Personal connection, relatability
- Example: "I got fired 3 times before age 30."
- Pro: Emotional connection, memorable
- Con: Requires compelling story to follow

## Body Structure Guidelines

### Linear Structure
- Straightforward narrative flow
- Best for: Opinions, stories, announcements
- Example: "I believe X because Y. Here's why it matters..."

### Listicle Structure
- Bullet points or numbered items
- Best for: Tips, lessons, frameworks
- Use → or • for visual appeal
- Keep items concise (one line each)

### Problem-Solution Structure
- State problem, then provide solution
- Best for: How-to content, advice
- Clear before/after or problem/solution contrast

## CTA Type Guidelines

### Direct CTA
- Clear action request
- Examples: "Comment below with your thoughts", "Share if you agree"
- Best for: When you want specific engagement

### Curiosity CTA
- Question to spark discussion
- Examples: "What's your biggest challenge?", "Agree or disagree?"
- Best for: Maximum comments and conversation

### Soft CTA
- Gentle invitation without pressure
- Examples: "Thoughts?", "Would love your perspective"
- Best for: Professional tone, B2B content

## Optimal Timing & Best Practices

### Best Posting Times (2025 Data)
- **Peak times**: Tuesday-Thursday, 7-9 AM or 12-2 PM
- **Secondary**: Monday/Friday, 5-6 PM
- **Avoid**: Weekends (unless B2C), late nights

### Character Count Optimization
- **First 210 chars**: Critical hook window (shows before "see more")
- **Optimal total**: 300-800 characters
- **Maximum**: 3,000 characters (but shorter performs better)

### Engagement Benchmarks
- **First hour**: Target 10+ engagements (baseline)
- **Good performance**: 50+ engagements (algorithm boost)
- **Viral threshold**: 100+ engagements (maximum reach)

### Hashtag Strategy
- **Optimal**: 3-5 hashtags
- **Mix**: 1-2 popular (100K+ followers), 2-3 niche (10K-50K)
- **Placement**: End of post (not mid-content)
- **Avoid**: 10+ hashtags (reduces reach by 18%)

## Error Handling

- Draft creation failed: Verify server connection
- Component addition failed: Check current draft exists
- Composition failed: Ensure at least hook and body are added
- Preview failed: Verify draft has content

## Notes

- LinkedIn shows first 210 characters before "see more" - make them count
- Use line breaks generously for mobile readability (70% of users)
- Posts with 300-800 chars get 20% more engagement than longer posts
- Text posts are baseline - consider document posts for 45% higher engagement
- First hour engagement is critical for algorithm reach
- Personal stories outperform corporate announcements 3:1
- Questions in posts get 50% more comments than statements
- Optimal hashtag count is 3-5 (not 10+)
