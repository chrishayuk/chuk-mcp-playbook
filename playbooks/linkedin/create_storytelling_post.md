# Playbook: Create Storytelling LinkedIn Post

## Description
This playbook creates a narrative-driven LinkedIn post that uses storytelling to convey lessons, insights, or experiences. Story-based posts are among the highest-performing content on LinkedIn, generating 5x more engagement than dry facts. People remember stories 22x more than facts alone, making this format ideal for building connection and memorability.

## Prerequisites
- Access to the chuk-mcp-linkedin server
- Personal or professional story with a clear lesson
- Authentic experience to share (vulnerability creates connection)
- Clear takeaway or insight from the story

## Steps

1. Create a new draft with storyteller theme
   - Initialize draft with story-focused name
   - Apply "storyteller" theme for narrative formatting
   - Set post type to "text"

2. Add a story-based hook
   - Use "story" hook type
   - Start in the middle of action (in medias res)
   - Create curiosity or tension
   - Keep < 210 characters

3. Add narrative body content
   - Use linear structure for chronological flow
   - Include specific details (not generalizations)
   - Show vulnerability and authenticity
   - Build tension or challenge
   - Include dialogue if relevant

4. Add transition to lesson
   - Use separator to mark shift from story to insight
   - Add "key takeaway" to highlight the lesson
   - Connect story to broader principle

5. Add supporting components
   - Timeline to show journey or evolution
   - Before/after to show transformation
   - Quote if there was memorable moment
   - Big stat if there's a surprising outcome

6. Add reflective CTA and hashtags
   - Use soft or curiosity CTA
   - Invite similar stories from others
   - Create space for vulnerability
   - Compose and preview

## MCP Tools Required

### chuk-mcp-linkedin

**Tool 1**: `linkedin_create`
- **Parameters**:
  - `name` (string): Draft name (e.g., "Career Pivot Story", "Failure Lesson")
  - `post_type` (string): "text"
- **Returns**: Draft ID

**Tool 2**: `linkedin_apply_theme`
- **Parameters**:
  - `theme_name` (string): "storyteller"
    - Narrative-driven tone
    - Emotional connection focus
    - Personal, authentic voice
- **Returns**: Theme applied confirmation

**Tool 3**: `linkedin_add_hook`
- **Parameters**:
  - `hook_type` (string): "story"
  - `text` (string): Story opening (< 210 chars)
    - Start with moment of tension/conflict
    - Create curiosity gap
    - Make it personal and specific
- **Returns**: Updated draft with hook

**Tool 4**: `linkedin_add_body`
- **Parameters**:
  - `content` (string): Story narrative
  - `structure` (string): "linear" (recommended for stories)
    - Chronological flow
    - Clear beginning, middle, end
    - Specific details and moments
- **Returns**: Updated draft with story body

**Tool 5**: `linkedin_add_separator`
- **Parameters**:
  - `style` (string): "line", "dots", or "stars"
- **Returns**: Updated draft with separator
- **Use for**: Transitioning from story to lesson

**Tool 6**: `linkedin_add_key_takeaway`
- **Parameters**:
  - `takeaway` (string): The lesson or insight from story
  - `highlight` (bool): Add visual emphasis (default: true)
- **Returns**: Updated draft with highlighted takeaway
- **Use for**: Connecting story to universal lesson

**Tool 7**: `linkedin_add_timeline`
- **Parameters**:
  - `title` (string): Timeline title (e.g., "My Journey:", "The Evolution:")
  - `events` (list): Chronological story beats
    - Each item: {"time": "Year/Stage", "event": "What happened"}
  - `style` (string): "vertical" or "horizontal"
- **Returns**: Updated draft with timeline
- **Use for**: Showing progression, transformation journey

**Tool 8**: `linkedin_add_before_after`
- **Parameters**:
  - `title` (string): Transformation title
  - `before` (dict): Starting state
    - `label` (string): "Before", "Then", "Old Me"
    - `items` (list): Characteristics or behaviors
  - `after` (dict): End state
    - `label` (string): "After", "Now", "Current Me"
    - `items` (list): Characteristics or behaviors
- **Returns**: Updated draft with before/after
- **Use for**: Showing transformation, growth, change

**Tool 9**: `linkedin_add_quote`
- **Parameters**:
  - `quote` (string): Memorable quote from story
  - `author` (string): Who said it (or "I thought to myself")
  - `context` (string): When/where this was said
- **Returns**: Updated draft with formatted quote
- **Use for**: Highlighting pivotal moment, internal dialogue

**Tool 10**: `linkedin_add_big_stat`
- **Parameters**:
  - `stat` (string): Surprising number from story
  - `context` (string): What the number represents
  - `emoji` (string): Optional emoji for emphasis
- **Returns**: Updated draft with emphasized stat
- **Use for**: Highlighting unexpected outcome or scale

**Tool 11**: `linkedin_add_tip_box`
- **Parameters**:
  - `message` (string): Lesson or advice from experience
  - `icon` (string): Emoji icon (default: "💡")
- **Returns**: Updated draft with tip box
- **Use for**: Actionable takeaway from story

**Tool 12**: `linkedin_add_cta`
- **Parameters**:
  - `cta_type` (string): "soft" or "curiosity"
    - `soft`: Gentle invitation ("Would love to hear your story")
    - `curiosity`: Question about similar experiences
  - `text` (string): CTA text
- **Returns**: Updated draft with CTA

**Tool 13**: `linkedin_add_hashtags`
- **Parameters**:
  - `tags` (list): 3-5 hashtags
    - Use themes like #CareerStory, #Lessons, #Growth
- **Returns**: Updated draft with hashtags

**Tool 14**: `linkedin_compose_post`
- **Parameters**:
  - `spacing` (string): "spacious" (stories need breathing room)
- **Returns**: Composed post text

**Tool 15**: `linkedin_preview_url`
- **Parameters**: Optional draft_id
- **Returns**: Shareable preview URL

## Example Usage

**Input**: "Create a storytelling post about a career failure that led to growth"

**Process**:
1. Create draft: "Fired Three Times Story"
2. Apply theme: "storyteller"
3. Add hook: "I got fired from my third job at 29. Sitting in my car in the parking lot, I realized I'd been ignoring the pattern."
4. Add body: Full story with specific details of what happened and internal struggle
5. Add separator
6. Add timeline: Journey from each firing to lesson learned
7. Add key takeaway: "You don't fail at jobs. You fail at fit."
8. Add before/after: Mindset shift from "What's wrong with me?" to "What's right for me?"
9. Add tip box: "Pro tip: If you've been fired, it's data not destiny"
10. Add CTA: "Ever had a 'failure' that was actually redirection?"
11. Add hashtags: ["CareerGrowth", "Resilience", "FailureLesson"]
12. Compose and preview

**Output**:
```
I got fired from my third job at 29.

Sitting in my car in the parking lot, I realized I'd been ignoring the pattern.

Job 1: "Too creative" (translation: didn't follow process)
Job 2: "Not a culture fit" (translation: questioned everything)
Job 3: "Not meeting expectations" (translation: more interested in why than what)

Each time, I thought: "What's wrong with me?"

The answer wasn't what I expected.

━━━━━━━━━━━━━━━━━━━━

My Journey:

2015: First firing → Shame, tried to "fix" myself
2017: Second firing → Panic, tried to be someone else
2019: Third firing → Finally asked the right question

Not "What's wrong with me?"
But "What's right for me?"

━━━━━━━━━━━━━━━━━━━━

Before vs After:

BEFORE:
❌ Tried to fit every role
❌ Saw firing as personal failure
❌ Suppressed natural strengths
❌ Chased what I "should" do

AFTER:
✅ Sought roles that fit me
✅ Saw firings as data points
✅ Leaned into strengths
✅ Did what energized me

━━━━━━━━━━━━━━━━━━━━

💡 KEY TAKEAWAY:
You don't fail at jobs. You fail at fit.

Getting fired isn't always about performance.
Sometimes it's about alignment.

💡 Pro tip: If you've been fired, it's data not destiny. Ask "Was this the right fit?" before "What's wrong with me?"

━━━━━━━━━━━━━━━━━━━━

Today? I run my own company doing exactly what got me fired: questioning, creating, and building new things.

Ever had a "failure" that was actually redirection?

#CareerGrowth #Resilience #FailureLesson
```

## Expected Response Format

```
[STORY HOOK - Start in middle of action/tension]

[STORY BODY - Specific details, chronological flow]

[SEPARATOR]

[TIMELINE or BEFORE/AFTER - Show transformation]

[SEPARATOR]

[KEY TAKEAWAY - The universal lesson]

[TIP BOX - Actionable advice from experience]

[SEPARATOR]

[RESOLUTION - Where you are now]

[SOFT CTA - Invite similar stories]

[Hashtags]
```

## Story Structure Options

### Classic Story Arc
1. **Hook**: Start with moment of tension/conflict
2. **Setup**: Provide context, introduce stakes
3. **Challenge**: Describe the obstacle or problem
4. **Struggle**: Show the difficulty, include failures
5. **Turning Point**: The moment of realization/change
6. **Resolution**: Where you are now
7. **Lesson**: Universal takeaway

### In Medias Res (Start in Middle)
1. **Hook**: Drop into most intense moment
2. **Flashback**: Explain how you got there
3. **Continue**: Resume the story
4. **Resolution**: How it ended
5. **Lesson**: What you learned

### Before/After Transformation
1. **Hook**: State the dramatic change
2. **Before**: Paint picture of starting point
3. **Catalyst**: What sparked the change
4. **Journey**: The transformation process
5. **After**: Where you are now
6. **Lesson**: What you learned

## Hook Strategies for Stories

### Tension Hook
- **Format**: "I [intense moment]. Here's what happened..."
- **Example**: "I had $83 in my bank account when I quit my job"
- **Why it works**: Creates immediate stakes
- **Tip**: Choose your most dramatic moment

### Vulnerability Hook
- **Format**: "I was [vulnerable admission]"
- **Example**: "I was living in my car when I started my company"
- **Why it works**: Authenticity creates connection
- **Tip**: Be genuinely vulnerable, not performative

### Contradiction Hook
- **Format**: "Everyone told me [X]. I did [opposite]."
- **Example**: "Everyone said don't quit without a plan. I quit anyway."
- **Why it works**: Creates curiosity about outcome
- **Tip**: Must have surprising result to justify

### Mistake Hook
- **Format**: "I made [big mistake]. Here's what it taught me..."
- **Example**: "I turned down a $200K job offer. Best mistake I ever made."
- **Why it works**: Relatability + curiosity
- **Tip**: Focus on lesson, not regret

## Storytelling Best Practices

### Show, Don't Tell
- ❌ "I was scared"
- ✅ "My hands shook as I clicked 'send' on the resignation email"

### Use Specific Details
- ❌ "I didn't have much money"
- ✅ "I had $83 in my bank account and $2,400 in rent due"

### Include Dialogue
- ❌ "My boss wasn't happy"
- ✅ "My boss said: 'You're making the biggest mistake of your career'"

### Create Tension
- Show obstacles and setbacks
- Build to climax before resolution
- Don't reveal outcome too early

### Make It Universal
- Personal story + universal lesson
- "You" language to apply to reader
- Clear takeaway anyone can use

## Story Types That Perform Well

### Failure → Growth Stories (Highest Engagement)
- Getting fired, rejected, or failing
- What you learned from the experience
- Where you are now
- **Engagement**: 5x average

### Pivotal Moment Stories
- Decision that changed everything
- Advice that shifted perspective
- Chance encounter that mattered
- **Engagement**: 3x average

### Behind-the-Scenes Stories
- What building a business really looks like
- The unsexy parts of success
- Reality vs Instagram highlight reel
- **Engagement**: 4x average

### Unlikely Journey Stories
- How you got to where you are
- The non-linear path
- Unexpected turns and detours
- **Engagement**: 3.5x average

### Lesson Learned the Hard Way
- Mistake that cost you (money, time, opportunity)
- What you wish you'd known
- How others can avoid it
- **Engagement**: 4x average

## Vulnerability Balance

### Good Vulnerability:
- ✅ Authentic struggle with resolution
- ✅ Sharing to help others
- ✅ Owns the lesson learned
- ✅ Shows growth from experience

### Avoid:
- ❌ Trauma dumping without context
- ❌ Victim mentality without accountability
- ❌ Open wounds (share healed scars)
- ❌ Vulnerability for attention/pity

## Engagement Optimization

### Story Post Performance
- **Average engagement**: 5x standard posts
- **Share rate**: 3x higher (people share good stories)
- **Comment quality**: Longer, more personal responses
- **Profile visits**: 4x more clicks
- **Memorability**: 22x more memorable than facts

### Optimal Length
- **Sweet spot**: 700-1,200 characters
- **Hook**: First 210 chars should hook them in
- **Maximum**: 3,000 characters (but shorter often better)

### Formatting for Stories
- Short paragraphs (1-2 sentences each)
- Line breaks for dramatic pauses
- Separators to mark act breaks
- Spacious formatting (let story breathe)

### Best Timing
- **Tuesday-Thursday**: 7-8 AM (morning commute reading)
- **Sunday**: 8-10 AM (weekend inspiration)
- **Avoid**: Friday afternoon (checked out)

## Common Mistakes to Avoid

### 1. No Clear Lesson
- ❌ Just telling a story without takeaway
- ✅ Story + universal lesson anyone can apply

### 2. Too Vague
- ❌ "I had a tough time and learned a lot"
- ✅ "I had $83 left when I quit—here's what I learned"

### 3. Humblebrag
- ❌ "I was working 100 hours/week building my unicorn"
- ✅ "I worked 100 hours/week and almost burned out—here's why I stopped"

### 4. No Resolution
- ❌ Leaving story hanging without conclusion
- ✅ Show where you are now and what changed

### 5. Making It About You
- ❌ "Look how far I've come"
- ✅ "Here's what I learned that might help you"

## Error Handling

- Theme application failed: Verify "storyteller" theme name
- Story too long: Break into multiple posts or thread
- Composition failed: Ensure hook and body are added
- Low engagement: Check if lesson is clear and universal

## Notes

- Story posts get 5x more engagement than standard posts
- People remember stories 22x more than facts alone
- Vulnerability creates connection (but share healed scars, not open wounds)
- Specific details make stories memorable and believable
- Universal lesson is critical—personal story + broader application
- Timeline component visualizes transformation journey
- Before/after shows clear contrast and growth
- Stories with failure→growth arc perform best
- Tuesday morning (7-8 AM) optimal for story posts
- Longer posts acceptable for good stories (700-1,200 chars)
- Share rate 3x higher than standard posts
- Comment quality is higher—people share their own stories
- Personal brand building works best through storytelling
- Authenticity matters more than polish
- One story can be worth 100 tips
