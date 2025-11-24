# Playbook: Create High-Engagement LinkedIn Post

## Description
This playbook creates a LinkedIn post optimized for maximum engagement (likes, comments, shares). These posts use proven engagement tactics like polls, questions, relatable content, and community-building elements. Based on 2025 data, engagement-focused posts with the right structure can achieve 3-5x more comments than standard posts.

## Prerequisites
- Access to the chuk-mcp-linkedin server
- Understanding of your audience's interests and pain points
- Goal to spark conversation and community interaction

## Steps

1. Create a new draft with community_builder theme
   - Initialize draft with engaging name
   - Apply "community_builder" theme for conversation focus
   - Set post type to "text" (or "poll" for maximum reach)

2. Add a question or curiosity-based hook
   - Use "question" hook type
   - Make it relatable to your audience
   - Create curiosity gap to encourage reading

3. Add relatable body content
   - Share common experience or pain point
   - Use "we" language to build community
   - Keep it conversational and accessible
   - Include specific, relatable examples

4. Add engagement components
   - Poll preview to invite opinions
   - Before/after to show transformation
   - Checklist to invite shared experiences
   - Pro/con to spark debate

5. Add strong conversation-starting CTA
   - Use "curiosity" CTA type
   - Ask specific question that invites stories
   - Make it easy to comment (not yes/no)
   - Encourage tagging others

6. Add hashtags and compose
   - Use mix of popular and niche hashtags
   - Compose with spacious formatting
   - Preview to check engagement potential

## MCP Tools Required

### chuk-mcp-linkedin

**Tool 1**: `linkedin_create`
- **Parameters**:
  - `name` (string): Draft name (e.g., "Community Discussion", "Audience Poll")
  - `post_type` (string): "text" or "poll"
    - "poll" gets 200%+ higher reach (most underused format)
    - "text" for discussion-based engagement
- **Returns**: Draft ID

**Tool 2**: `linkedin_apply_theme`
- **Parameters**:
  - `theme_name` (string): "community_builder"
    - Conversational, inclusive tone
    - Focus on fostering discussion
    - Relatable, accessible language
- **Returns**: Theme applied confirmation

**Tool 3**: `linkedin_add_hook`
- **Parameters**:
  - `hook_type` (string): "question" or "story"
    - `question`: Direct question to audience
    - `story`: Relatable personal anecdote
  - `text` (string): Hook text (< 210 chars)
- **Returns**: Updated draft with hook

**Tool 4**: `linkedin_add_body`
- **Parameters**:
  - `content` (string): Main content
  - `structure` (string): "linear" or "listicle"
- **Returns**: Updated draft with body

**Tool 5**: `linkedin_add_poll_preview`
- **Parameters**:
  - `question` (string): Poll question
  - `options` (list): 2-4 poll options
    - Keep options short and distinct
    - Avoid yes/no (use "Agree"/"Disagree"/"It depends")
  - `duration` (string): "1 day", "3 days", "1 week", "2 weeks"
- **Returns**: Updated draft with poll preview
- **Use for**: Maximum engagement, gathering opinions, sparking debate
- **Note**: Actual poll creation requires LinkedIn API (this adds preview to text post)

**Tool 6**: `linkedin_add_before_after`
- **Parameters**:
  - `title` (string): Comparison title
  - `before` (dict): Before state
    - `label` (string): "Before", "Old Way", etc.
    - `items` (list): List of characteristics
  - `after` (dict): After state
    - `label` (string): "After", "New Way", etc.
    - `items` (list): List of characteristics
- **Returns**: Updated draft with before/after comparison
- **Use for**: Transformations, improvements, evolution stories

**Tool 7**: `linkedin_add_checklist`
- **Parameters**:
  - `title` (string): Checklist title (e.g., "Can you relate?", "Signs you're...")
  - `items` (list): List of relatable items
  - `checked` (list): Optional pre-checked items
- **Returns**: Updated draft with checklist
- **Use for**: Relatable experiences, self-assessment, shared challenges

**Tool 8**: `linkedin_add_pro_con`
- **Parameters**:
  - `title` (string): Debate topic
  - `pros` (list): Pro arguments
  - `cons` (list): Con arguments
- **Returns**: Updated draft with pros/cons
- **Use for**: Balanced debate, inviting different perspectives

**Tool 9**: `linkedin_add_feature_list`
- **Parameters**:
  - `title` (string): List title
  - `features` (list): List of items with icons/emojis
    - Each item: {"icon": "💡", "title": "Feature", "description": "Details"}
- **Returns**: Updated draft with formatted feature list
- **Use for**: Options, choices, recommendations

**Tool 10**: `linkedin_add_separator`
- **Parameters**:
  - `style` (string): "line", "dots", or "stars"
- **Returns**: Updated draft with separator
- **Use for**: Visual breaks, section division

**Tool 11**: `linkedin_add_cta`
- **Parameters**:
  - `cta_type` (string): "curiosity" (recommended for engagement)
  - `text` (string): CTA text
    - Ask for stories: "Share your experience 👇"
    - Ask for opinions: "Agree or disagree?"
    - Encourage tags: "Tag someone who needs to see this"
- **Returns**: Updated draft with CTA

**Tool 12**: `linkedin_add_hashtags`
- **Parameters**:
  - `tags` (list): 3-5 hashtags
    - Mix of popular (100K+) and niche (10K-50K)
    - Community-focused tags work well
- **Returns**: Updated draft with hashtags

**Tool 13**: `linkedin_compose_post`
- **Parameters**:
  - `spacing` (string): "spacious"
- **Returns**: Composed post text

**Tool 14**: `linkedin_preview_url`
- **Parameters**: Optional draft_id
- **Returns**: Shareable preview URL

## Example Usage

**Input**: "Create an engagement post about remote work challenges"

**Process**:
1. Create draft: "Remote Work Discussion"
2. Apply theme: "community_builder"
3. Add hook: "Honest question: Is anyone else struggling with 'always on' culture in remote work?"
4. Add body: "I thought remote work would give me more flexibility. Instead, I'm answering Slack at 10 PM and starting calls at 7 AM to cover time zones."
5. Add poll preview: "When do you typically end your workday in remote work?" with options
6. Add checklist: "Signs you're in 'always on' culture" with relatable items
7. Add separator
8. Add CTA: "How do you set boundaries? Share your tips 👇"
9. Add hashtags: ["RemoteWork", "WorkLifeBalance", "RemoteLife"]
10. Compose and preview

**Output**:
```
Honest question: Is anyone else struggling with 'always on' culture in remote work?

I thought remote work would give me more flexibility.

Instead, I'm answering Slack at 10 PM and starting calls at 7 AM to cover time zones.

━━━━━━━━━━━━━━━━━━━━

📊 Quick Poll: When do you typically end your workday in remote work?

→ 5-6 PM (normal hours)
→ 7-8 PM (a bit late)
→ 9-10 PM (way too late)
→ What's an "end time"? 😅

━━━━━━━━━━━━━━━━━━━━

Signs you're in "always on" culture:

☐ Check Slack before getting out of bed
☐ Attend meetings across 4+ time zones
☐ "Quick question" at 9 PM
☐ Weekend messages feel urgent
☐ Guilt for not responding immediately
☐ Vacation but still on laptop

How do you set boundaries? Share your tips 👇

#RemoteWork #WorkLifeBalance #RemoteLife
```

## Expected Response Format

```
[QUESTION HOOK - Relatable, invites response]

[RELATABLE STORY - Shared experience]

[SEPARATOR]

[ENGAGEMENT COMPONENT - Poll, checklist, or comparison]

[SEPARATOR]

[STRONG CTA - Specific question inviting stories]

[Hashtags - Community-focused]
```

## Hook Strategies for Engagement

### Question Hook (Highest Engagement)
- **Format**: "Honest question: [relatable challenge]?"
- **Example**: "Honest question: Does anyone actually enjoy networking events?"
- **Why it works**: Invites immediate response, shows vulnerability
- **Tip**: Use "honest question" or "quick question" to lower barrier

### Relatable Experience Hook
- **Format**: "I thought [expectation]. Instead [reality]."
- **Example**: "I thought LinkedIn was for job searching. Instead, I built my entire network."
- **Why it works**: Creates "me too" moment
- **Tip**: Share the gap between expectation and reality

### Controversial Hook
- **Format**: "Unpopular opinion: [controversial take]"
- **Example**: "Unpopular opinion: Most networking advice makes networking worse"
- **Why it works**: Creates debate, polarizes (intentionally)
- **Tip**: Use sparingly, be prepared for disagreement

### Curiosity Hook
- **Format**: "Can you relate? [Common situation]"
- **Example**: "Can you relate? You practice the presentation 10 times, still blank in the meeting"
- **Why it works**: Creates immediate connection
- **Tip**: Make it specific and universal

## Engagement Component Selection

### Poll Preview (Highest Reach - 200%+)
**Best for**:
- Gathering opinions
- Quick engagement
- Data collection
- Inviting all perspectives

**Tips**:
- 3-4 options optimal (2 feels limiting, 5+ reduces clicks)
- Make options distinct and mutually exclusive
- Include a humor option (e.g., "What's sleep?" for work-life balance poll)
- 3-7 days duration works best (not 1 day or 2 weeks)

**Note**: This creates a text post with poll preview. For actual LinkedIn polls (200%+ reach boost), use post_type="poll" when creating draft.

### Before/After (High Shareability)
**Best for**:
- Transformation stories
- Learning journeys
- Process improvements
- Career progression

**Tips**:
- Make "before" relatable (where audience is now)
- Make "after" aspirational (where they want to be)
- Keep items parallel in structure
- Show realistic progression

### Checklist (High Relatability)
**Best for**:
- Shared experiences
- Self-assessment
- Common challenges
- Community building

**Tips**:
- 5-8 items optimal
- Mix of humorous and serious
- Make them specific enough to be relatable
- Invite people to share their score

### Pro/Con (High Comment Rate)
**Best for**:
- Balanced debates
- Decision frameworks
- Inviting perspectives
- Showing nuance

**Tips**:
- Present both sides fairly
- 3-5 points each side
- Avoid straw man arguments
- Invite readers to add points

## CTA Strategies for Maximum Comments

### Story-Inviting CTA (Best)
- **Format**: "Share your [specific experience] 👇"
- **Example**: "Share your worst interview story 👇"
- **Why it works**: Specific enough to answer, invites stories
- **Engagement**: 3-5x more comments

### Opinion-Inviting CTA
- **Format**: "Agree or disagree? Why?"
- **Example**: "Hot take or cold truth? What do you think?"
- **Why it works**: Invites debate and different perspectives
- **Engagement**: 2-3x more comments

### Tag-Inviting CTA
- **Format**: "Tag someone who [needs to see this]"
- **Example**: "Tag a founder who needs to hear this"
- **Why it works**: Expands reach, brings new people in
- **Engagement**: 2x more reach, 1.5x more comments

### Choice CTA
- **Format**: "A or B? Tell me why."
- **Example**: "Coffee or tea for deep work? Defend your choice."
- **Why it works**: Easy to answer, starts conversations
- **Engagement**: High volume, lower depth

### Avoid These CTAs:
- ❌ "Like if you agree" (lazy engagement)
- ❌ "Thoughts?" (too vague, gets few responses)
- ❌ "Yes or no?" (kills conversation)
- ❌ No CTA (missed opportunity)

## Engagement Optimization Tactics

### Respond to Every Comment (First Hour Critical)
- Reply within first hour to boost algorithm
- Ask follow-up questions in replies
- Thank people for sharing
- Keep conversation going

### Post Timing for Maximum Engagement
- **Best**: Tuesday-Thursday, 8-10 AM or 12-1 PM
- **Good**: Monday morning (fresh week), Friday afternoon (casual)
- **Avoid**: Weekends (unless B2C), early mornings (< 7 AM)

### First Hour Strategy
- Post at optimal time (8-9 AM Tue-Thu)
- Share to your Story immediately
- Engage with 5-10 posts before posting (warm up)
- Reply to first comments within minutes
- Ask friends/colleagues to comment early

### Engagement Benchmarks
- **Baseline**: 10+ engagements in first hour
- **Good**: 25-50 engagements (algorithm boost)
- **Excellent**: 100+ engagements (maximum reach)
- **Comment rate**: Aim for 5-10% of impressions

## Length and Formatting

### Optimal Length
- **Sweet spot**: 400-700 characters
- **Maximum**: 1,200 characters (longer kills engagement)
- **Hook**: First 210 characters (critical)

### Formatting Best Practices
- Line breaks every 1-2 sentences
- Emoji for visual breaks (sparingly)
- Separators between sections
- Spacious formatting (easier to scan)
- Lowercase can feel more conversational

### Mobile Optimization
- 70% of users on mobile
- Short sentences (scan-friendly)
- Avoid long paragraphs
- Test on mobile before posting

## Error Handling

- Theme application failed: Verify theme name is "community_builder"
- Poll preview failed: Check options list (2-4 items required)
- Composition too long: Keep total under 3,000 chars (ideally under 1,200)
- Low engagement: Post timing matters - try Tuesday 9 AM

## Notes

- Engagement posts get 3-5x more comments than standard posts
- Poll posts get 200%+ higher reach (most underused format)
- Questions in hooks increase comments by 50%
- Responding to comments within first hour boosts algorithm
- Tuesday-Thursday 8-10 AM is optimal posting time
- First hour engagement determines post reach
- Relatable > impressive for engagement posts
- Vulnerability and authenticity drive connection
- Community-builder theme optimizes for conversation
- Checklists with 5-8 items get highest completion/sharing
- Before/after posts get 2.4x more shares
- Avoid yes/no questions - invite stories instead
- Tag-inviting CTAs expand reach by 2x
- Keep it conversational, not corporate
- Reply to every comment in first 2 hours
