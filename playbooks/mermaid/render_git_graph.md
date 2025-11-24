# Playbook: Render Git Graph

## Description
This playbook creates git commit history graphs showing branches, commits, merges, and other git operations. Git graphs are perfect for visualizing git workflows, branching strategies, and repository history.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Understanding of git operations and workflow
- Clear sequence of git operations (commits, branches, merges)

## Steps

1. Plan the git workflow
   - Define branching strategy (main, feature branches, etc.)
   - List commits in chronological order
   - Identify branch points and merge points

2. Define git operations
   - Start with initial commit on main
   - Create branches as needed
   - Checkout branches
   - Make commits on appropriate branches
   - Merge branches back

3. Call the render_git_graph tool
   - Pass operations list with type and details
   - Use consistent branch names

4. Review the generated diagram
   - Verify the branching structure is correct
   - Check that merges are shown properly

## MCP Tools Required

### mcp-mermaid-renderer

**Tool**: `render_git_graph`
- **Parameters**:
  - `operations` (list of dict, required): Git operations in sequence. Each dict should have:
    - `operation`, `type`, or `action` (string): Must be "commit", "branch", "checkout", "merge", or "cherry-pick"
    - For branch operations: `name` or `branch` = branch name to create
    - For checkout operations: `branch` or `name` = branch to switch to
    - For merge operations: `source` or `branch` = branch to merge from
    - For commit operations:
      - `message` or `msg` = commit message
      - `id` or `tag` = commit ID/tag
      - `commit_type` = "NORMAL", "REVERSE", or "HIGHLIGHT"
    - For cherry-pick operations: `id` = commit ID to cherry-pick
  - `title` (string, optional): Graph title
  - `format` (string): Output format - "svg" (default, recommended) or "png"
  - `theme` (string): Mermaid theme - "default", "dark", "forest", "neutral"
  - `bgcolor` (string): Background color (default: "transparent")
  - `filename` (string, optional): Suggested filename
- **Returns**: Artifact metadata with download URLs

## Example Usage

**Input**: "Create a git graph showing a feature branch workflow"

**Process**:
1. Start with main branch
2. Create feature branch
3. Make commits on feature branch
4. Merge back to main

**Tool Call**:
```json
{
  "operations": [
    {"type": "commit", "message": "Initial commit", "id": "c1"},
    {"type": "branch", "name": "feature/login"},
    {"type": "checkout", "branch": "feature/login"},
    {"type": "commit", "message": "Add login form", "id": "c2"},
    {"type": "commit", "message": "Add validation", "id": "c3"},
    {"type": "checkout", "branch": "main"},
    {"type": "commit", "message": "Update README", "id": "c4"},
    {"type": "merge", "source": "feature/login"},
    {"type": "commit", "message": "Release v1.0", "id": "v1.0", "commit_type": "HIGHLIGHT"}
  ],
  "title": "Feature Branch Workflow",
  "format": "svg",
  "theme": "default"
}
```

**Output**:
```
Git graph rendered successfully!
- Format: SVG
- Operations: 9
- Branches: 2
- Download URL: [artifact link]
```

## Expected Response Format

The tool returns an artifact object with:
- `download_url`: URL to download the rendered diagram
- `source_code`: Editable Mermaid syntax
- `format`: Output format (svg or png)
- `diagram_type`: "git"

## Common Use Cases

1. **Workflow Documentation**: Git flow, GitHub flow, trunk-based development
2. **Training Materials**: Teaching git branching and merging
3. **Project History**: Visualizing repository development over time
4. **Release Planning**: Planning branch strategy for releases
5. **Troubleshooting**: Understanding complex merge scenarios
6. **Team Onboarding**: Explaining team's git workflow

## Best Practices

1. **Operation Order**: Operations must be in chronological sequence
2. **Branch Creation**: Create a branch before checking it out
3. **Checkout Before Commit**: Always checkout a branch before committing to it
4. **Merge Direction**: Merge from feature branch to main (not vice versa)
5. **Commit Messages**: Keep concise (3-6 words)
6. **Commit IDs**: Use for important commits or tags
7. **Commit Types**:
   - NORMAL: Regular commits
   - HIGHLIGHT: Important commits (releases, milestones)
   - REVERSE: Reverted commits
8. **Field Names**: Use "type" or "operation" for consistency

## Error Handling

- **Invalid Operation Type**: Must be commit, branch, checkout, merge, or cherry-pick
- **Missing Branch Name**: Branch operations need "name" field
- **Missing Source**: Merge operations need "source" field
- **Checkout Non-existent Branch**: Must create branch before checkout
- **Merge Without Checkout**: Checkout target branch before merging

## Notes

- Git graph starts on "main" branch by default
- Operations are executed in the order specified
- Branch operation creates a new branch from current branch
- Checkout operation switches to the specified branch
- Merge operation merges specified branch into current branch
- Cherry-pick copies a commit from another branch
- Commit types affect visual styling (HIGHLIGHT makes commits stand out)
- Tool accepts flexible field names: type/operation/action, branch/name/source
- For merge operations, use "source" to specify branch being merged
- For branch operations, use "name" to specify new branch name
- Common workflow: commit → branch → checkout → commit → checkout main → merge
- Maximum recommended operations: 15-20 for readability
- For complex histories, focus on main branches and major merges
