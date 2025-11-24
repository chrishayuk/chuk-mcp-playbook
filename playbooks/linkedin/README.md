# LinkedIn Playbooks

Comprehensive playbooks for creating high-performing LinkedIn content using the [chuk-mcp-linkedin](https://github.com/chrishayuk/chuk-mcp-linkedin) MCP server.

## Overview

These playbooks are based on 2025 performance data from 1M+ LinkedIn posts across 9K company pages. Each playbook provides step-by-step guidance for creating specific types of LinkedIn content optimized for engagement, reach, and impact.

## Available Playbooks

### 1. Create Simple Text Post
**File**: `create_simple_text_post.md`

**Use for**: Quick updates, thoughts, announcements, everyday content

**Optimal for**:
- First-time LinkedIn posters
- Quick professional updates
- Daily engagement posts
- Testing content ideas

**Key components**: Hook, Body, CTA, Hashtags

**Expected engagement**: 1x baseline (foundation for other formats)

---

### 2. Create Data-Driven Post
**File**: `create_data_driven_post.md`

**Use for**: Analytics, metrics, research findings, performance reports

**Optimal for**:
- B2B audiences
- Technical/analytical followers
- Building authority with data
- Quarterly/monthly reports

**Key components**: Stat hook, Charts (bar, metrics, progress, ranking), Big stats, Key takeaways

**Expected engagement**: 2.3x baseline (data posts outperform opinion posts)

**Special features**:
- Bar charts for comparisons
- Metrics charts for KPIs
- Progress bars for goal tracking
- Ranking charts for leaderboards

---

### 3. Create Thought Leadership Post
**File**: `create_thought_leadership_post.md`

**Use for**: Industry insights, frameworks, predictions, expert perspectives

**Optimal for**:
- Establishing authority
- Sharing frameworks/methodologies
- Positioning as industry expert
- Building professional brand

**Key components**: Bold hooks, Numbered frameworks, Timelines, Key takeaways, Checklists

**Expected engagement**: 1.8x baseline (thought leadership builds long-term authority)

**Special features**:
- Framework development guidance
- Timeline for process/evolution
- Thought leader theme optimization
- Contrarian voice options

---

### 4. Create Engagement Post
**File**: `create_engagement_post.md`

**Use for**: Sparking conversations, building community, gathering opinions

**Optimal for**:
- Maximizing comments
- Building engaged community
- Gathering audience insights
- Starting discussions

**Key components**: Question hooks, Poll previews, Checklists, Before/after, Pro/con

**Expected engagement**: 3-5x baseline (engagement-optimized posts)

**Special features**:
- Poll preview for 200%+ reach boost
- Relatable checklists for "me too" moments
- Before/after transformations
- Community builder theme

**Pro tip**: Poll posts (actual LinkedIn polls, not text posts) get 200%+ higher reach and are the most underused format in 2025

---

### 5. Create Storytelling Post
**File**: `create_storytelling_post.md`

**Use for**: Personal experiences, lessons learned, career journeys, transformations

**Optimal for**:
- Building authentic connection
- Sharing vulnerability
- Teaching through experience
- Memorable content

**Key components**: Story hooks, Narrative structure, Timelines, Before/after, Quotes

**Expected engagement**: 5x baseline (highest engagement format)

**Special features**:
- Multiple story structure options
- Vulnerability balance guidance
- Journey timelines
- Transformation visualizations

**Pro tip**: People remember stories 22x more than facts alone. Story posts also get 3x more shares.

---

### 6. Optimize Post for Engagement
**File**: `optimize_post_for_engagement.md`

**Use for**: Improving drafts before publishing, learning from low-performing posts

**Optimal for**:
- Auditing existing content
- Learning what works
- Improving before publishing
- Salvaging underperforming posts

**Key components**: Comprehensive audits (hook, body, CTA, hashtags), Component additions, Recommendations

**Expected improvement**: 2-5x more engagement after optimization

**Special features**:
- Hook audit (first 210 chars critical)
- Body structure analysis
- CTA strengthening
- Hashtag optimization
- A/B testing guidance

---

### 7. Troubleshooting Common Issues
**File**: `troubleshooting_common_issues.md`

**Use for**: Diagnosing and fixing errors during post creation

**Optimal for**:
- "Draft not found" errors
- "No post content to publish" errors
- Theme application failures
- Chart rendering issues
- Publish failures despite successful compose
- Session and authentication errors

**Key coverage**:
- 10 most common issues with detailed solutions
- Diagnostic workflow (step-by-step)
- Tool call order reference
- Error message quick reference table
- Workflow best practices

**Essential reading**: Reference this when any playbook steps fail

**Pro tip**: Most issues are caused by incorrect tool call order. The number one mistake is using `linkedin_switch` immediately after `linkedin_create` (unnecessary - the draft is already current!)

---

## Quick Reference: Which Playbook to Use?

### By Goal

| Goal | Recommended Playbook | Expected Engagement |
|------|---------------------|---------------------|
| Build authority | Thought Leadership | 1.8x baseline |
| Maximum engagement | Storytelling | 5x baseline |
| Community building | Engagement Post | 3-5x baseline |
| Share data/metrics | Data-Driven | 2.3x baseline |
| Quick daily post | Simple Text | 1x baseline |
| Improve draft | Optimize Post | 2-5x improvement |
| Maximum reach | Engagement (with poll) | 200%+ reach |
| Fix errors | Troubleshooting | N/A (diagnostic) |

### By Content Type

| Content Type | Best Playbook |
|--------------|---------------|
| Personal story | Storytelling |
| Industry prediction | Thought Leadership |
| Research findings | Data-Driven |
| Debate/discussion | Engagement |
| Product announcement | Simple Text → Optimize |
| Quarterly metrics | Data-Driven |
| Career lessons | Storytelling or Thought Leadership |
| Poll/survey | Engagement |
| Framework/methodology | Thought Leadership |
| Relatable moment | Engagement |

### By Experience Level

| Experience Level | Start Here |
|------------------|------------|
| New to LinkedIn | Simple Text Post |
| Comfortable posting | Engagement Post or Data-Driven |
| Building authority | Thought Leadership |
| Confident storyteller | Storytelling Post |
| Want to improve | Optimize Post |

---

## 2025 LinkedIn Performance Data

These playbooks are based on analysis of 1M+ posts. Key insights:

### Top Performing Formats (Engagement Rate):
1. **Document Posts (PDF)**: 45.85% engagement - HIGHEST
2. **Video Posts**: 1.4x engagement, 69% YoY growth
3. **Story Posts**: 5x baseline engagement
4. **Image Posts**: 2x more comments than text
5. **Poll Posts**: 200%+ higher reach (most underused)
6. **Carousel Posts**: Declining (-18% reach vs 2024)

### Critical Success Factors:
- **First 210 characters**: Determines if people click "see more"
- **First hour engagement**: Determines algorithm reach
- **Optimal length**: 300-800 characters (longer for stories)
- **Hashtags**: 3-5 optimal (10+ reduces reach by 18%)
- **Best times**: Tuesday-Thursday, 7-9 AM
- **Line breaks**: Critical for mobile (70% of users)

### Engagement Thresholds:
- **Baseline**: 10+ engagements in first hour
- **Good**: 50+ engagements (algorithm boost)
- **Viral**: 100+ engagements (maximum reach)

---

## Common Components Across Playbooks

### Hook Types
- **Question**: Invites immediate response
- **Stat**: Grabs attention with data
- **Bold**: Makes strong statement
- **Story**: Creates emotional connection

### Body Structures
- **Linear**: Straightforward narrative
- **Listicle**: Numbered or bulleted points
- **Problem-Solution**: Challenge then resolution

### Visual Components
- **Bar Chart**: Compare categories
- **Metrics Chart**: Show KPIs with ✅/❌
- **Progress Chart**: Completion percentages
- **Ranking Chart**: Leaderboards with medals
- **Comparison Chart**: Before/after, A vs B
- **Timeline**: Show evolution/journey
- **Checklist**: Relatable experiences
- **Poll Preview**: Invite opinions

### CTA Types
- **Direct**: Clear action request
- **Curiosity**: Question to spark discussion
- **Soft**: Gentle invitation

---

## Themes Available

The LinkedIn MCP server includes 10 pre-built themes:

| Theme | Use Case | Tone |
|-------|----------|------|
| `thought_leader` | Industry insights, frameworks | Authoritative, professional |
| `data_driven` | Analytics, metrics | Analytical, objective |
| `storyteller` | Personal experiences | Narrative, emotional |
| `community_builder` | Discussion, engagement | Conversational, inclusive |
| `technical_expert` | Technical content | Detailed, expert |
| `personal_brand` | Authentic connection | Personal, real |
| `corporate_professional` | Official announcements | Polished, formal |
| `contrarian_voice` | Debate, hot takes | Provocative, challenging |
| `coach_mentor` | Advice, guidance | Supportive, teaching |
| `entertainer` | Fun, humor | Light, entertaining |

---

## Getting Started

1. **Install the LinkedIn MCP Server**:
   ```bash
   pip install chuk-mcp-linkedin
   ```

2. **Configure your MCP client** to use the server

3. **Choose a playbook** based on your content goal

4. **Follow the step-by-step process** in the playbook

5. **Use the recommended tools** from the LinkedIn MCP server

6. **Preview before publishing** using `linkedin_preview_url`

---

## Critical: Correct Tool Call Order

**Most common mistake**: Using `linkedin_switch` immediately after `linkedin_create`

### ✅ Correct Workflow
```
1. linkedin_create(name="...", post_type="text")
   ↓ Draft becomes current automatically - do NOT switch!

2. linkedin_apply_theme(theme_name="...")
   ↓ Apply theme to current draft (optional)

3. linkedin_add_hook(...)
   ↓ Add components in any order

4. linkedin_add_body(...)
   ↓ Continue adding components

5. linkedin_compose_post(optimize=True)
   ↓ Compose BEFORE publishing

6. linkedin_publish(visibility="PUBLIC", dry_run=True)
   ↓ Test first with dry-run

7. linkedin_publish(visibility="PUBLIC", dry_run=False)
   ↓ Actual publish
```

### ❌ Common Mistakes That Cause Errors

**Mistake 1**: Switching to newly created draft
```
linkedin_create → linkedin_switch(draft_id) → ERROR: "Draft not found"
```
**Why it fails**: Draft is already current after creation

**Mistake 2**: Publishing without composing
```
linkedin_add_hook → linkedin_add_body → linkedin_publish → ERROR: "No post content"
```
**Why it fails**: Must compose components into final text first

**Mistake 3**: Applying theme too late
```
linkedin_create → linkedin_add_hook → linkedin_apply_theme → May not work
```
**Why it fails**: Theme should be applied immediately after creation (step 2)

### When to Use linkedin_switch

Only use `linkedin_switch` when:
- Switching between two existing drafts
- Resuming work on an old draft
- Working on multiple drafts in same session

Never use `linkedin_switch` when:
- Just created a new draft (it's already current!)
- Draft doesn't exist yet

### If Things Go Wrong

See `troubleshooting_common_issues.md` for:
- "Draft not found" errors
- "No post content to publish" errors
- Theme application failures
- Complete diagnostic workflow

---

## Best Practices

### Before Creating Content
- [ ] Define your goal (engagement, reach, authority)
- [ ] Choose appropriate playbook
- [ ] Understand your audience
- [ ] Have specific value to share

### While Creating
- [ ] Follow playbook steps in order
- [ ] Use recommended components
- [ ] Preview first 210 characters
- [ ] Check mobile formatting
- [ ] Verify 3-5 hashtags

### Before Publishing
- [ ] Generate preview URL and review
- [ ] Check character count (300-800 optimal)
- [ ] Verify CTA invites specific response
- [ ] Schedule for optimal time (Tue-Thu 7-9 AM)
- [ ] Plan to respond to comments in first hour

### After Publishing
- [ ] Respond to every comment (first hour critical)
- [ ] Monitor engagement in first 60 minutes
- [ ] Note what worked for future posts
- [ ] Track performance metrics
- [ ] Learn and iterate

---

## Advanced Tips

### Combine Playbooks
- Start with Simple Text, then Optimize
- Use Storytelling + Data-Driven for case studies
- Combine Thought Leadership + Engagement for frameworks with discussion

### Series Strategy
- Create content series using same playbook
- Reference previous posts to create threads
- Build authority through consistent format

### Testing & Iteration
- Test different hook styles
- A/B test posting times
- Track which CTAs get most comments
- Document what works for your audience

---

## Support

- **LinkedIn MCP Server**: [GitHub Repository](https://github.com/chrishayuk/chuk-mcp-linkedin)
- **Documentation**: [Full Docs](https://github.com/chrishayuk/chuk-mcp-linkedin/tree/main/docs)
- **Issues**: [Report Issues](https://github.com/chrishayuk/chuk-mcp-linkedin/issues)

---

## Contributing

Have suggestions for new playbooks or improvements? Please contribute:

1. Fork the repository
2. Create a new playbook following the existing format
3. Submit a pull request with detailed description

---

**Last Updated**: November 24, 2025
**Based on**: 2025 LinkedIn performance data (1M+ posts, 9K company pages)
