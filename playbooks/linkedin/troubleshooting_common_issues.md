# Playbook: Troubleshooting Common LinkedIn Post Issues

## Description
This playbook helps diagnose and fix common issues when creating, composing, and publishing LinkedIn posts using the chuk-mcp-linkedin MCP server. Use this when posts fail to create, compose, or publish.

## Prerequisites
- Access to the chuk-mcp-linkedin server
- Basic understanding of draft workflow
- Access to tool call history or error messages

## Common Issues and Solutions

### Issue 1: "Draft not found" after creation

**Symptoms**:
- `linkedin_create` succeeds and returns draft_id
- `linkedin_switch` to that draft_id fails with "Draft not found"
- OR `linkedin_apply_theme` fails with "No active draft"

**Root cause**: Session/authentication state issue between tool calls

**Solution**:
1. Don't switch to newly created draft - it's already active
2. Immediately start adding components after creation
3. Only use `linkedin_switch` when changing between existing drafts

**Correct workflow**:
```
1. linkedin_create → draft becomes current automatically
2. linkedin_add_hook → adds to current draft
3. linkedin_add_body → adds to current draft
   (no linkedin_switch needed!)
```

**Incorrect workflow (causes errors)**:
```
1. linkedin_create → returns draft_id
2. linkedin_switch(draft_id) → ERROR: "Draft not found"
   (unnecessary - draft is already current!)
```

**Verification**:
```
linkedin_list → shows all drafts with "is_current": true/false
```

---

### Issue 2: "No post content to publish"

**Symptoms**:
- Components added successfully
- `linkedin_compose_post` succeeds and returns full text
- `linkedin_publish` fails with "No post content to publish"
- Dry-run publish works but real publish fails

**Root cause**: Composed content not persisted to draft before publish

**Solution A - Add explicit content update**:
After composing, explicitly update draft content:
```
1. linkedin_compose_post → get composed text
2. linkedin_get_info → verify components exist
3. Try publish again
```

**Solution B - Use get_info to verify**:
Before publishing, check draft state:
```
linkedin_get_info(draft_id) → shows all components and composition state
```

If components exist but composition is missing:
```
1. Re-run linkedin_compose_post
2. Check that optimize=True
3. Verify character count in response
4. Try publish immediately after
```

**Solution C - Export and manual post**:
If publish continues to fail:
```
1. linkedin_compose_post → copy the full text
2. linkedin_preview_url → get shareable preview
3. Manually post to LinkedIn using copied text
4. OR linkedin_export_draft → get JSON to debug
```

---

### Issue 3: Theme application fails

**Symptoms**:
- `linkedin_apply_theme` returns "No active draft"
- OR theme applied but components don't reflect theme

**Root cause**: Theme must be applied immediately after creation, before other operations

**Solution**:
Correct order of operations:
```
1. linkedin_create(name, post_type)
2. linkedin_apply_theme(theme_name) ← Must be #2
3. linkedin_add_hook(...)
4. linkedin_add_body(...)
5. ... other components
```

If you need to add theme later:
```
1. linkedin_switch(draft_id) ← Make it current first
2. linkedin_apply_theme(theme_name)
3. Components inherit theme from this point forward
```

**Verification**:
```
linkedin_get_info → check "theme" field is set
```

---

### Issue 4: Components added but don't appear in composition

**Symptoms**:
- Component additions return success
- `linkedin_compose_post` succeeds but missing components
- OR character count seems too low

**Root cause**: Components added to wrong draft or composition doesn't include all components

**Solution**:
1. **Verify current draft**:
   ```
   linkedin_list → check which draft "is_current": true
   ```

2. **Check draft contents**:
   ```
   linkedin_get_info → see all components added
   ```

3. **Recompose with optimization**:
   ```
   linkedin_compose_post(optimize=True)
   ```

4. **Check component count**:
   - If get_info shows 7 components but compose only shows 3, try:
   ```
   linkedin_compose_post(optimize=False, spacing="spacious")
   ```

---

### Issue 5: Hashtags don't appear or are malformed

**Symptoms**:
- `linkedin_add_hashtags` succeeds
- Composed post missing hashtags or shows ["tag1", "tag2"]

**Root cause**: Hashtags added incorrectly or composition issue

**Solution**:
1. **Correct hashtag format**:
   ```
   linkedin_add_hashtags(tags=["LinkedIn", "Marketing", "B2B"])
   # NOT: tags="#LinkedIn #Marketing"
   # NOT: tags="LinkedIn, Marketing"
   ```

2. **Verify hashtags in draft**:
   ```
   linkedin_get_info → check "hashtags" field
   ```

3. **Hashtag placement**:
   ```
   linkedin_add_hashtags(tags=[...], placement="end")
   # Default is "end" (after CTA)
   # Can also use "inline" (within content)
   ```

4. **Re-add if malformed**:
   ```
   # Hashtags are appended, so remove draft and recreate if needed
   # OR just ensure correct format on first add
   ```

---

### Issue 6: Character count too high (> 3,000)

**Symptoms**:
- `linkedin_compose_post` succeeds but shows > 3,000 characters
- Post feels too long
- LinkedIn won't accept (if publishing directly)

**Root cause**: Too many components or verbose content

**Solution**:
1. **Check character count**:
   ```
   linkedin_compose_post → look at character count in response
   ```

2. **Remove or shorten components**:
   - Long body text
   - Too many chart items (> 7)
   - Multiple charts (limit to 1-2)
   - Verbose CTA or takeaway

3. **Use compact spacing**:
   ```
   linkedin_compose_post(spacing="compact")
   # vs spacing="spacious" (default)
   ```

4. **Optimize structure**:
   - Hook: < 210 chars
   - Body: 300-800 chars
   - 1-2 charts max
   - CTA: 1-2 sentences
   - 3-5 hashtags

---

### Issue 7: Charts don't render or look wrong

**Symptoms**:
- Chart tools succeed but composed post shows raw data
- Bar chart has wrong scale
- Progress chart shows > 100%

**Root causes and solutions**:

**A. Bar chart scale issues**:
```
# If using percentages (0-100):
linkedin_add_bar_chart(
    title="Performance",
    data={"Sales": 85, "Marketing": 92},  # Values 0-100
    unit="%"
)

# If using actual numbers (will auto-scale):
linkedin_add_bar_chart(
    title="Revenue by Product",
    data={"Product A": 45000, "Product B": 32000},
    unit="$"
)
```

**B. Progress chart must be 0-100**:
```
# CORRECT:
linkedin_add_progress_chart(
    title="Q4 Goals",
    items={"Revenue": 85, "Users": 92, "Retention": 78}  # All 0-100
)

# INCORRECT:
linkedin_add_progress_chart(
    items={"Revenue": 125000}  # Must be percentage!
)
```

**C. Too many chart items**:
```
# Limit to 5-7 items per chart for readability
# If you have 15 metrics, create 2 separate charts or filter to top 5
```

**D. Check composed output**:
```
linkedin_compose_post → inspect chart rendering
# If charts look wrong, they'll show as text blocks
```

---

### Issue 8: Preview URL fails or expires

**Symptoms**:
- `linkedin_preview_url` returns error
- URL loads but shows blank page
- URL worked before but now shows "expired"

**Root causes and solutions**:

**A. Draft doesn't have content**:
```
linkedin_get_info → verify components exist
# If empty, add components first
# Then compose before generating preview URL
```

**B. Preview expired**:
```
# Default expiry: 3600 seconds (1 hour)
# Generate new preview URL:
linkedin_preview_url(draft_id=..., expires_in=7200)  # 2 hours
```

**C. Server configuration**:
```
# Preview URLs require:
# 1. OAUTH_SERVER_URL set (e.g., https://linkedin.chukai.io)
# 2. Artifact storage configured (memory, S3, etc.)
# 3. HTTP server running (not STDIO mode)

# Check with:
linkedin_test_connection(check_preview=True)
```

**D. Alternative - use local preview**:
```
linkedin_preview_html → generates local HTML preview
# Opens in browser automatically
# Doesn't require server URL
```

---

### Issue 9: Publish succeeds but post not visible on LinkedIn

**Symptoms**:
- `linkedin_publish` returns success
- No error message
- Post doesn't appear in LinkedIn feed

**Root causes and solutions**:

**A. Visibility setting**:
```
# Check what visibility was used:
linkedin_publish(visibility="PUBLIC")     # Everyone
linkedin_publish(visibility="CONNECTIONS") # Only connections

# If published as CONNECTIONS, only your network sees it
```

**B. OAuth token expired**:
```
# Test connection:
linkedin_test_connection(check_oauth=True)

# If expired, re-authenticate:
# (MCP server will prompt for OAuth flow)
```

**C. Rate limiting**:
```
# LinkedIn limits posts:
# - Max 1 post per minute
# - Max 25 posts per day (personal accounts)

# Wait 60 seconds between posts
```

**D. Content moderation**:
```
# LinkedIn may flag posts with:
# - Spam-like content
# - External links (reduces reach)
# - Excessive hashtags (> 10)
# - Banned words or phrases

# Check LinkedIn notifications for moderation notice
```

---

### Issue 10: Session or authentication errors

**Symptoms**:
- Random "not authenticated" errors
- Tools work, then suddenly fail
- "Session expired" messages

**Root causes and solutions**:

**A. OAuth token refresh needed**:
```
linkedin_test_connection(check_oauth=True)
# If fails, re-authenticate via OAuth flow
```

**B. Session provider issue**:
```
# Memory session provider (default for dev):
# - Sessions lost on server restart
# - Not persisted

# Redis session provider (production):
# - Persistent sessions
# - Survives restarts
```

**C. Multiple clients/sessions**:
```
# If using multiple MCP clients:
# - Each client has separate session
# - Drafts are session-isolated
# - Can't access drafts from other client

# Solution: Use same client consistently
# OR use Redis session provider with shared session IDs
```

---

## Diagnostic Workflow

When encountering issues, follow this diagnostic sequence:

### Step 1: Verify Connection
```
linkedin_test_connection(check_oauth=True, check_preview=True)
```
**Expected**: All checks pass
**If fails**: Re-authenticate or check server configuration

### Step 2: Check Current Draft
```
linkedin_list
```
**Expected**: See list of drafts with one marked "is_current": true
**If no drafts**: Create new draft
**If multiple current**: Should only be one - check session state

### Step 3: Inspect Draft Contents
```
linkedin_get_info(draft_id="...")
```
**Expected**: See all components, theme, metadata
**If empty**: Components weren't added to this draft
**If wrong draft**: Use linkedin_switch to correct draft

### Step 4: Compose and Verify
```
linkedin_compose_post(optimize=True)
```
**Expected**: Full text with all components, character count < 3000
**If missing components**: Re-add components, then compose again
**If too long**: Use compact spacing or remove components

### Step 5: Test Publish (Dry Run)
```
linkedin_publish(visibility="PUBLIC", dry_run=True)
```
**Expected**: Success with preview of what would be published
**If fails**: Check error message and apply relevant solution above

### Step 6: Publish
```
linkedin_publish(visibility="PUBLIC", dry_run=False)
```
**Expected**: Success with LinkedIn post ID
**If fails**: Check error message and apply relevant solution above

---

## Workflow Best Practices

### Recommended Workflow (Avoids Most Issues)

```
1. linkedin_create(name="...", post_type="text")
   ↓ draft becomes current automatically

2. linkedin_apply_theme(theme_name="data_driven")
   ↓ applies theme to current draft

3. linkedin_add_hook(hook_type="stat", text="...")
   ↓ adds to current draft

4. linkedin_add_body(content="...", structure="linear")
   ↓ adds to current draft

5. linkedin_add_bar_chart(title="...", data={...})
   ↓ adds to current draft

6. linkedin_add_key_takeaway(message="...")
   ↓ adds to current draft

7. linkedin_add_cta(cta_type="curiosity", text="...")
   ↓ adds to current draft

8. linkedin_add_hashtags(tags=[...])
   ↓ adds to current draft

9. linkedin_compose_post(optimize=True)
   ↓ generates final text

10. linkedin_publish(visibility="PUBLIC", dry_run=True)
    ↓ test publish first

11. linkedin_publish(visibility="PUBLIC", dry_run=False)
    ↓ actual publish
```

**Key points**:
- No linkedin_switch after create (draft is already current)
- Theme applied immediately after creation
- All components added in sequence
- Compose before publish
- Dry-run test before real publish

### What to Avoid

❌ **Don't do this**:
```
linkedin_create → linkedin_switch → ERROR
```
The newly created draft is already current!

❌ **Don't do this**:
```
linkedin_add_hook → linkedin_add_body → linkedin_publish
```
Must compose before publishing!

❌ **Don't do this**:
```
linkedin_compose_post → [add more components] → linkedin_publish
```
If you add components after compose, must re-compose!

❌ **Don't do this**:
```
linkedin_publish(visibility="PUBLIC") immediately on error
```
Investigate error first, don't spam publish attempts!

---

## Tool Call Order Reference

### Must be in this order:
1. `linkedin_create` ← FIRST (creates and activates draft)
2. `linkedin_apply_theme` ← SECOND (if using theme)
3. Add components (any order):
   - `linkedin_add_hook`
   - `linkedin_add_body`
   - `linkedin_add_*_chart`
   - `linkedin_add_cta`
   - `linkedin_add_hashtags`
4. `linkedin_compose_post` ← BEFORE PUBLISH
5. `linkedin_publish` ← LAST

### Can be called anytime:
- `linkedin_list` (view all drafts)
- `linkedin_get_info` (inspect specific draft)
- `linkedin_switch` (change current draft)
- `linkedin_preview_url` (after composing)
- `linkedin_get_preview` (after adding components)
- `linkedin_test_connection` (diagnostics)

### Should NOT be called after create:
- `linkedin_switch(newly_created_draft_id)` ← Unnecessary!

---

## Getting Help

If issues persist after following this guide:

1. **Export draft for analysis**:
   ```
   linkedin_export_draft(draft_id="...")
   # Returns JSON with full draft state
   ```

2. **Check server logs**:
   - Look for authentication errors
   - Check for rate limiting messages
   - Verify OAuth token validity

3. **Test with minimal post**:
   ```
   1. linkedin_create(name="Test", post_type="text")
   2. linkedin_add_hook(hook_type="question", text="Test post - please ignore")
   3. linkedin_add_body(content="Testing post creation.", structure="linear")
   4. linkedin_compose_post()
   5. linkedin_publish(visibility="CONNECTIONS", dry_run=True)
   ```

   If this fails, issue is with configuration, not content.

4. **Report issue**:
   - Include error messages
   - Include tool call sequence
   - Include draft JSON (from export)
   - Report at: https://github.com/chrishayuk/chuk-mcp-linkedin/issues

---

## Error Message Quick Reference

| Error Message | Likely Cause | Solution |
|---------------|--------------|----------|
| "Draft not found" | Wrong draft_id or session issue | Use `linkedin_list` to verify draft exists |
| "No active draft" | Theme applied before creation or after failed switch | Create draft first, or use `linkedin_switch` |
| "No post content to publish" | Didn't compose before publish | Run `linkedin_compose_post` first |
| "Character limit exceeded" | Post > 3,000 characters | Use compact spacing or reduce components |
| "Invalid visibility" | Wrong visibility value | Use "PUBLIC" or "CONNECTIONS" |
| "Authentication failed" | OAuth token expired | Run `linkedin_test_connection`, re-auth if needed |
| "Rate limit exceeded" | Too many posts too quickly | Wait 60 seconds between posts |
| "Session expired" | Session timeout | Re-authenticate via OAuth flow |
| "Invalid data format" | Wrong parameter type | Check tool documentation for correct format |

---

## Notes

- Most issues stem from incorrect tool call order
- Always compose before publishing
- Never switch to a newly created draft (it's already current)
- Theme must be applied before adding components
- Dry-run publish is your friend - always test first
- Check `linkedin_get_info` when in doubt about draft state
- Session isolation means drafts are per-session - can't cross sessions
- Memory session provider loses drafts on restart (use Redis for production)
- LinkedIn has rate limits - wait 60 seconds between posts
