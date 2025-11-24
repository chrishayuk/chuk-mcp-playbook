# Playbook: Create Data-Driven LinkedIn Post with Charts

## Description
This playbook creates a data-driven LinkedIn post featuring statistics, metrics, and visual charts. Based on 2025 performance data, data-driven content gets 2.3x more engagement than opinion-based posts. Perfect for sharing insights, research, analytics, and performance metrics.

## Prerequisites
- Access to the chuk-mcp-linkedin server
- Data or statistics to share
- Understanding of chart types for data visualization

## Steps

1. Create a new draft with data_driven theme
   - Initialize draft with descriptive name
   - Apply "data_driven" theme for optimized formatting
   - Set post type to "text"

2. Add a stat-based hook
   - Use powerful statistic or metric
   - Make it surprising or counterintuitive
   - Keep < 210 characters

3. Add body content with context
   - Explain what the data means
   - Provide context and analysis
   - Use clear, concise language

4. Add visual charts
   - Choose appropriate chart type for data
   - Bar charts for comparisons
   - Metrics charts for key performance indicators
   - Progress bars for completion/growth tracking
   - Ranking charts for leaderboards

5. Add key takeaways or big stats
   - Highlight most important insights
   - Use big stat component for emphasis
   - Make actionable for readers

6. Add CTA and hashtags
   - Invite discussion about the data
   - Use 3-5 relevant hashtags
   - Compose and preview

## MCP Tools Required

### chuk-mcp-linkedin

**Tool 1**: `linkedin_create`
- **Parameters**:
  - `name` (string): Draft name (e.g., "Q4 Performance Report", "Industry Benchmark Data")
  - `post_type` (string): "text"
- **Returns**: Draft ID

**Tool 2**: `linkedin_apply_theme`
- **Parameters**:
  - `theme_name` (string): "data_driven"
    - Optimized for analytics and metrics
    - Professional, authoritative tone
    - Clear data presentation
- **Returns**: Confirmation of theme applied

**Tool 3**: `linkedin_add_hook`
- **Parameters**:
  - `hook_type` (string): "stat"
  - `text` (string): Powerful statistic (< 210 chars)
- **Returns**: Updated draft with hook

**Tool 4**: `linkedin_add_body`
- **Parameters**:
  - `content` (string): Data context and analysis
  - `structure` (string): "linear" or "listicle"
- **Returns**: Updated draft with body

**Tool 5**: `linkedin_add_bar_chart`
- **Parameters**:
  - `title` (string): Chart title
  - `data` (dict): Key-value pairs for chart
    - Keys: Category names
    - Values: Numeric values (0-100 or actual numbers)
  - `show_values` (bool): Display values on bars (default: true)
  - `color` (string): Bar color - "blue", "green", "red", "yellow" (default: "blue")
- **Returns**: Updated draft with bar chart visualization
- **Use for**: Comparing categories, showing rankings, progress metrics

**Tool 6**: `linkedin_add_metrics_chart`
- **Parameters**:
  - `title` (string): Metrics title
  - `metrics` (dict): Metric name to value/status
    - Values can include status indicators: ✅ (success), ❌ (failure), ⚠️ (warning)
    - Example: {"Revenue": "✅ +24%", "Churn": "✅ -12%"}
- **Returns**: Updated draft with metrics display
- **Use for**: KPIs, performance indicators, goal tracking

**Tool 7**: `linkedin_add_progress_chart`
- **Parameters**:
  - `title` (string): Progress title
  - `items` (dict): Item names to completion percentage
    - Keys: Task/goal names
    - Values: Percentage (0-100)
  - `bar_length` (int): Visual bar length in characters (default: 20)
- **Returns**: Updated draft with progress bars
- **Use for**: Goal completion, project progress, percentage-based metrics

**Tool 8**: `linkedin_add_ranking_chart`
- **Parameters**:
  - `title` (string): Ranking title
  - `items` (list): Ordered list of ranked items
    - Top 3 get medals: 🥇🥈🥉
    - Remaining items numbered
  - `show_medals` (bool): Show medals for top 3 (default: true)
- **Returns**: Updated draft with ranking chart
- **Use for**: Top performers, leaderboards, rankings

**Tool 9**: `linkedin_add_comparison_chart`
- **Parameters**:
  - `title` (string): Comparison title
  - `side_a` (dict): First side of comparison
    - `label` (string): Label (e.g., "Before", "Option A")
    - `items` (list): List of items/features
  - `side_b` (dict): Second side of comparison
    - `label` (string): Label (e.g., "After", "Option B")
    - `items` (list): List of items/features
- **Returns**: Updated draft with side-by-side comparison
- **Use for**: Before/after, A vs B comparisons, feature comparisons

**Tool 10**: `linkedin_add_big_stat`
- **Parameters**:
  - `stat` (string): The large statistic
  - `context` (string): Brief explanation or context
  - `emoji` (string): Optional emoji for emphasis
- **Returns**: Updated draft with emphasized statistic
- **Use for**: Highlighting key numbers, shocking statistics

**Tool 11**: `linkedin_add_key_takeaway`
- **Parameters**:
  - `takeaway` (string): Key insight or TLDR
  - `highlight` (bool): Add visual emphasis (default: true)
- **Returns**: Updated draft with highlighted takeaway
- **Use for**: Summary, main point, actionable insight

**Tool 12**: `linkedin_add_cta`
- **Parameters**:
  - `cta_type` (string): "direct", "curiosity", or "soft"
  - `text` (string): Call-to-action text
- **Returns**: Updated draft with CTA

**Tool 13**: `linkedin_add_hashtags`
- **Parameters**:
  - `tags` (list): 3-5 relevant hashtags
- **Returns**: Updated draft with hashtags

**Tool 14**: `linkedin_compose_post`
- **Parameters**:
  - `spacing` (string): "compact" or "spacious"
- **Returns**: Final composed post text

**Tool 15**: `linkedin_preview_url`
- **Parameters**: Optional draft_id
- **Returns**: Shareable preview URL

## Example Usage

**Input**: "Create a post about our Q4 SaaS metrics showing growth"

**Process**:
1. Create draft: "Q4 SaaS Metrics Report"
2. Apply theme: "data_driven"
3. Add hook: "Our SaaS grew 127% in Q4. Here's what the data reveals..."
4. Add body: "We analyzed 10,000+ data points across our product. The results surprised us."
5. Add bar chart: {"New Users": 85, "Engagement": 92, "Retention": 78, "Revenue": 95}
6. Add metrics chart: {"MRR Growth": "✅ +24%", "Churn Rate": "✅ -12%", "NPS Score": "✅ 72"}
7. Add big stat: "127%" with context "Year-over-year revenue growth"
8. Add key takeaway: "Focus on retention drives 2x more growth than acquisition"
9. Add CTA: "What metrics matter most in your SaaS?"
10. Add hashtags: ["SaaS", "DataDriven", "GrowthMetrics"]
11. Compose and preview

**Output**:
```
Our SaaS grew 127% in Q4. Here's what the data reveals...

We analyzed 10,000+ data points across our product. The results surprised us.

📊 Key Performance Metrics:

█████████████████░░░ New Users (85%)
█████████████████████ Engagement (92%)
███████████████░░░░░ Retention (78%)
████████████████████░ Revenue (95%)

💡 KPI Dashboard:

✅ MRR Growth: +24%
✅ Churn Rate: -12%
✅ NPS Score: 72

🎯 Big Number:

127%
Year-over-year revenue growth

💡 KEY TAKEAWAY:
Focus on retention drives 2x more growth than acquisition

What metrics matter most in your SaaS?

#SaaS #DataDriven #GrowthMetrics
```

## Expected Response Format

```
[STAT HOOK - Powerful data point]

[CONTEXT - What the data means]

[CHART 1 - Visual data representation]

[CHART 2 - Additional metrics if relevant]

[BIG STAT - Highlight key number]

[KEY TAKEAWAY - Main insight]

[CTA - Data-focused question]

[Hashtags - 3-5 data/industry tags]
```

## Chart Type Selection Guide

### Bar Chart (`linkedin_add_bar_chart`)
**Best for**:
- Comparing multiple categories
- Showing relative performance
- Progress across different metrics
- Rankings or competitions

**Example use cases**:
- Department performance comparison
- Product feature usage rates
- Customer satisfaction by region
- Monthly revenue by product line

**Tips**:
- Limit to 5-7 bars for readability
- Use consistent scale (0-100 or actual values)
- Color code for meaning (green = good, red = needs attention)

### Metrics Chart (`linkedin_add_metrics_chart`)
**Best for**:
- KPIs and key performance indicators
- Pass/fail status indicators
- Goal achievement tracking
- Quick performance snapshot

**Example use cases**:
- Monthly business metrics
- Project milestone status
- Quality metrics dashboard
- Health check results

**Tips**:
- Use ✅ for positive/achieved metrics
- Use ❌ for negative/missed metrics
- Use ⚠️ for warning/needs attention
- Keep to 4-6 metrics for scannability

### Progress Chart (`linkedin_add_progress_chart`)
**Best for**:
- Showing completion percentages
- Goal progress tracking
- Multi-stage project status
- Skills or learning progress

**Example use cases**:
- Project completion status
- Quarterly goal tracking
- Learning path progress
- Feature development roadmap

**Tips**:
- Use 0-100 percentage scale
- Order by completion (highest first) or priority
- Add context about what 100% means
- Update regularly to show progress over time

### Ranking Chart (`linkedin_add_ranking_chart`)
**Best for**:
- Leaderboards and top performers
- Best/worst lists
- Priority rankings
- Competition results

**Example use cases**:
- Top sales performers
- Most popular features
- Best content performers
- Industry rankings

**Tips**:
- Medals (🥇🥈🥉) make top 3 stand out
- Limit to top 5-10 for focus
- Include context for what's being ranked
- Consider showing your position if relevant

### Comparison Chart (`linkedin_add_comparison_chart`)
**Best for**:
- Before/after transformations
- A vs B comparisons
- Feature comparisons
- Decision frameworks

**Example use cases**:
- Before/after process improvement
- Old vs new product features
- Competitor comparison
- Traditional vs modern approaches

**Tips**:
- Keep item lists parallel in structure
- Use clear, contrasting labels
- Highlight key differences
- Balance number of items on each side

## Data Presentation Best Practices

### Make Data Accessible
- Avoid jargon and technical terms
- Explain what metrics mean in plain language
- Provide context for numbers (vs what? over what period?)
- Round numbers for readability (127% not 127.3%)

### Tell a Story with Data
- Start with the most surprising/important finding
- Use data to support a narrative, not just list facts
- Connect data to real-world impact
- End with actionable insight or lesson

### Visual Hierarchy
- Put most important data first (or biggest)
- Use charts to break up text walls
- Limit to 1-2 charts per post for clarity
- Use big stat component for emphasis

### Source and Credibility
- Mention data source if external
- Specify time period for metrics
- Be transparent about sample size
- Acknowledge limitations if significant

## Engagement Optimization

### Data-Driven Posts Perform Better
- 2.3x more engagement than opinion posts
- 45% more shares when including charts/visuals
- Comments increase 62% with specific numbers
- Best performing format after document posts

### Optimal Data Post Structure
- **Length**: 400-900 characters (slightly longer than standard)
- **Charts**: 1-2 per post (more reduces engagement)
- **Numbers**: 3-5 specific stats optimal
- **Takeaway**: Always include actionable insight

### Best Timing for Data Posts
- **Tuesday-Thursday**: 8-10 AM (B2B decision makers online)
- **Avoid Mondays**: Information overload
- **Quarterly**: End of quarter for reports/retrospectives
- **Monthly**: First week of month for previous month data

## Error Handling

### Common Issues

**"Draft not found" after creation**:
- Don't use `linkedin_switch` after `linkedin_create`
- New drafts are automatically set as current
- Only use switch when changing between existing drafts

**"No active draft" when applying theme**:
- Apply theme immediately after `linkedin_create` (step 2)
- If failed, verify draft exists with `linkedin_list`
- Never apply theme before creating draft

**"No post content to publish"**:
- Must run `linkedin_compose_post` before `linkedin_publish`
- If composed but still fails, verify with `linkedin_get_info`
- Try dry-run first: `linkedin_publish(dry_run=True)`
- If dry-run works but publish fails, see troubleshooting guide

**Chart creation failed**:
- Check data format is dict: `{"Label": value, "Label2": value2}`
- Progress charts require 0-100 percentages
- Bar charts accept any numbers (will auto-scale)
- Limit to 5-7 items per chart for readability

**Character limit exceeded**:
- Total must be < 3,000 characters
- Use `spacing="compact"` in `linkedin_compose_post`
- Reduce number of charts (optimal: 1-2)
- Shorten body content to 400-700 characters

### Verification Steps

Before publishing, verify:
```
1. linkedin_get_info → check all components added
2. linkedin_compose_post → get character count
3. linkedin_publish(dry_run=True) → test without publishing
4. linkedin_publish(dry_run=False) → actual publish
```

### If Issues Persist

See: `troubleshooting_common_issues.md` for comprehensive diagnostics

## Notes

- Data posts perform 2.3x better than opinion posts
- Charts increase engagement by 45% compared to text-only
- First 210 characters should include the key stat
- Use round numbers (127% not 127.34%) for readability
- Always provide context for statistics
- Source data if not original research
- Update metrics regularly if posting recurring reports
- Combine multiple chart types for comprehensive view
- Metrics with ✅/❌ indicators get 31% more engagement
- Data posts work best Tuesday-Thursday mornings
- Optimal: 1-2 charts per post (3+ reduces engagement)
- Always include actionable takeaway or insight
- B2B audiences particularly responsive to data content
