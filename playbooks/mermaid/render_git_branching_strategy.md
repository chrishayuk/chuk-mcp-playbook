# Playbook: Visualize Git Branching Strategy

## Description
This playbook guides you through visualizing Git branching strategies including Gitflow, trunk-based development, feature branching, release workflows, and hotfix processes. Perfect for team onboarding, documenting workflow policies, planning release strategies, and standardizing development practices.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Understanding of your team's Git workflow
- Knowledge of branching conventions and merge policies
- List of branch types and lifecycle

## Steps

1. **Identify branch types**
   - Main/master branch
   - Development branch
   - Feature branches
   - Release branches
   - Hotfix branches

2. **Map the workflow**
   - Document when branches are created
   - Note merge/rebase strategies
   - Identify code review points
   - Map deployment triggers

3. **Document branch lifecycle**
   - Branch creation points
   - Merge destinations
   - Delete/archive policies
   - Tag and version strategies

4. **Choose the appropriate diagram type**
   - Use **git_graph** for branching visualization
   - Use **flowchart** for workflow decision logic

5. **Create the visualization**
   - Show typical branch lifecycle
   - Include merge strategies
   - Document tagging conventions
   - Add notes for policies

## MCP Tools Required

### Primary Tool: render_git_graph
Best for visualizing Git branch structures and commit history.

See [render_git_graph.md](./render_git_graph.md) for full details.

### Secondary Tool: render_flowchart
Useful for documenting workflow decision logic and policies.

See [render_flowchart.md](./render_flowchart.md) for full details.

## Recommended Diagram Type

### Primary: Git Graph
**When to use**: Team onboarding, workflow documentation, release planning

**Strengths**:
- Shows branch structure clearly
- Visualizes merges and commits
- Represents parallel development
- Standard Git visualization format

**Example structure**:
```json
{
  "commits": [
    {"id": "c1", "branch": "main", "message": "Initial commit"},
    {"id": "c2", "branch": "develop", "message": "Setup dev branch"},
    {"id": "c3", "branch": "feature", "message": "Add feature"}
  ],
  "branches": ["main", "develop", "feature"],
  "merges": [
    {"from": "feature", "to": "develop", "commit": "c4"}
  ]
}
```

### Secondary: Flowchart
**When to use**: Documenting decision logic for branching and merging

**Strengths**:
- Shows decision points
- Documents approval gates
- Illustrates workflow branches
- Good for policy documentation

## Example Usage

### Scenario 1: Gitflow Workflow

**User Request**: "Visualize our Gitflow branching strategy with feature, release, and hotfix branches"

```json
{
  "commits": [
    {"id": "m1", "type": "NORMAL", "tag": "v1.0.0"},
    {"id": "m2", "type": "NORMAL"},
    {"id": "m3", "type": "NORMAL", "tag": "v1.1.0"},
    {"id": "m4", "type": "NORMAL"},
    {"id": "m5", "type": "NORMAL", "tag": "v1.2.0"}
  ],
  "branches": [
    {
      "name": "main",
      "commits": ["m1", "m2", "m3", "m4", "m5"]
    },
    {
      "name": "develop",
      "branch_from": "m1",
      "commits": ["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8"]
    },
    {
      "name": "feature/user-auth",
      "branch_from": "d2",
      "commits": ["f1", "f2", "f3"],
      "merge_into": {"branch": "develop", "at": "d4"}
    },
    {
      "name": "feature/payment",
      "branch_from": "d4",
      "commits": ["p1", "p2", "p3", "p4"],
      "merge_into": {"branch": "develop", "at": "d7"}
    },
    {
      "name": "release/1.1.0",
      "branch_from": "d5",
      "commits": ["r1", "r2"],
      "merge_into": [
        {"branch": "main", "at": "m3"},
        {"branch": "develop", "at": "d6"}
      ]
    },
    {
      "name": "hotfix/security-patch",
      "branch_from": "m3",
      "commits": ["h1", "h2"],
      "merge_into": [
        {"branch": "main", "at": "m4"},
        {"branch": "develop", "at": "d8"}
      ]
    }
  ],
  "title": "Gitflow Branching Strategy",
  "format": "svg",
  "theme": "default"
}
```

### Scenario 2: Trunk-Based Development

**User Request**: "Show our trunk-based development workflow with short-lived feature branches"

```json
{
  "commits": [
    {"id": "m1", "type": "NORMAL", "message": "Initial commit"},
    {"id": "m2", "type": "NORMAL", "message": "Add CI/CD"},
    {"id": "m3", "type": "NORMAL", "message": "Merge feature A"},
    {"id": "m4", "type": "NORMAL", "message": "Direct commit"},
    {"id": "m5", "type": "NORMAL", "message": "Merge feature B", "tag": "v1.1.0"},
    {"id": "m6", "type": "NORMAL", "message": "Hotfix"},
    {"id": "m7", "type": "NORMAL", "message": "Merge feature C"},
    {"id": "m8", "type": "NORMAL", "message": "Direct commit", "tag": "v1.2.0"}
  ],
  "branches": [
    {
      "name": "main",
      "commits": ["m1", "m2", "m3", "m4", "m5", "m6", "m7", "m8"]
    },
    {
      "name": "feature/user-profile",
      "branch_from": "m2",
      "commits": ["f1", "f2"],
      "merge_into": {"branch": "main", "at": "m3"}
    },
    {
      "name": "feature/notifications",
      "branch_from": "m4",
      "commits": ["n1", "n2", "n3"],
      "merge_into": {"branch": "main", "at": "m5"}
    },
    {
      "name": "feature/dashboard",
      "branch_from": "m6",
      "commits": ["d1", "d2"],
      "merge_into": {"branch": "main", "at": "m7"}
    }
  ],
  "title": "Trunk-Based Development Workflow",
  "format": "svg",
  "theme": "default"
}
```

### Scenario 3: GitHub Flow (Feature Branch Workflow)

**User Request**: "Visualize our GitHub flow with feature branches and pull requests"

```json
{
  "commits": [
    {"id": "m1", "type": "NORMAL", "message": "Initial release", "tag": "v1.0.0"},
    {"id": "m2", "type": "NORMAL", "message": "Merge PR #12"},
    {"id": "m3", "type": "NORMAL", "message": "Merge PR #13"},
    {"id": "m4", "type": "NORMAL", "message": "Merge PR #14", "tag": "v1.1.0"},
    {"id": "m5", "type": "NORMAL", "message": "Merge PR #15"},
    {"id": "m6", "type": "NORMAL", "message": "Merge hotfix PR #16"}
  ],
  "branches": [
    {
      "name": "main",
      "commits": ["m1", "m2", "m3", "m4", "m5", "m6"]
    },
    {
      "name": "feature/add-search",
      "branch_from": "m1",
      "commits": ["s1", "s2", "s3", "s4"],
      "merge_into": {"branch": "main", "at": "m2"}
    },
    {
      "name": "feature/improve-ui",
      "branch_from": "m1",
      "commits": ["u1", "u2"],
      "merge_into": {"branch": "main", "at": "m3"}
    },
    {
      "name": "feature/api-integration",
      "branch_from": "m2",
      "commits": ["a1", "a2", "a3"],
      "merge_into": {"branch": "main", "at": "m4"}
    },
    {
      "name": "feature/analytics",
      "branch_from": "m4",
      "commits": ["an1", "an2"],
      "merge_into": {"branch": "main", "at": "m5"}
    },
    {
      "name": "hotfix/security-vuln",
      "branch_from": "m5",
      "commits": ["h1"],
      "merge_into": {"branch": "main", "at": "m6"}
    }
  ],
  "title": "GitHub Flow - Feature Branch Workflow",
  "format": "svg",
  "theme": "default"
}
```

### Scenario 4: Release Branch Strategy

**User Request**: "Show how we manage release branches for multiple versions"

```json
{
  "commits": [
    {"id": "m1", "type": "NORMAL", "tag": "v1.0.0"},
    {"id": "m2", "type": "NORMAL"},
    {"id": "m3", "type": "NORMAL", "tag": "v2.0.0"},
    {"id": "m4", "type": "NORMAL"},
    {"id": "m5", "type": "NORMAL", "tag": "v3.0.0"}
  ],
  "branches": [
    {
      "name": "main",
      "commits": ["m1", "m2", "m3", "m4", "m5"]
    },
    {
      "name": "develop",
      "branch_from": "m1",
      "commits": ["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9"]
    },
    {
      "name": "release/1.x",
      "branch_from": "m1",
      "commits": ["r1.1", "r1.2"],
      "tag": ["v1.0.1", "v1.0.2"]
    },
    {
      "name": "release/2.x",
      "branch_from": "m3",
      "commits": ["r2.1", "r2.2", "r2.3"],
      "tag": ["v2.0.1", "v2.0.2", "v2.1.0"]
    },
    {
      "name": "feature/new-api",
      "branch_from": "d3",
      "commits": ["f1", "f2", "f3"],
      "merge_into": {"branch": "develop", "at": "d5"}
    },
    {
      "name": "feature/redesign",
      "branch_from": "d5",
      "commits": ["f4", "f5", "f6", "f7"],
      "merge_into": {"branch": "develop", "at": "d8"}
    }
  ],
  "title": "Multi-Version Release Branch Strategy",
  "format": "svg",
  "theme": "default"
}
```

### Scenario 5: Branching Decision Flow (Flowchart)

**User Request**: "Document the decision logic for when to create different branch types"

```json
{
  "nodes": [
    {"id": "start", "label": "Need to make changes", "shape": "circle"},
    {"id": "check_type", "label": "What type of change?", "shape": "diamond"},
    {"id": "check_urgency", "label": "Production issue?", "shape": "diamond"},
    {"id": "create_hotfix", "label": "Create hotfix/xxx branch from main", "shape": "rectangle"},
    {"id": "create_feature", "label": "Create feature/xxx branch from develop", "shape": "rectangle"},
    {"id": "create_release", "label": "Create release/x.x.x branch from develop", "shape": "rectangle"},
    {"id": "work", "label": "Make changes and commit", "shape": "rectangle"},
    {"id": "pr", "label": "Create pull request", "shape": "rectangle"},
    {"id": "review", "label": "Code review approved?", "shape": "diamond"},
    {"id": "fix_issues", "label": "Address review comments", "shape": "rectangle"},
    {"id": "merge_main", "label": "Merge to main and develop", "shape": "rectangle"},
    {"id": "merge_develop", "label": "Merge to develop", "shape": "rectangle"},
    {"id": "merge_release", "label": "Merge to main and back-merge to develop", "shape": "rectangle"},
    {"id": "tag", "label": "Create version tag", "shape": "rectangle"},
    {"id": "delete", "label": "Delete branch", "shape": "rectangle"},
    {"id": "end", "label": "Complete", "shape": "circle"}
  ],
  "edges": [
    {"from": "start", "to": "check_type"},
    {"from": "check_type", "to": "check_urgency", "label": "Bug fix"},
    {"from": "check_type", "to": "create_feature", "label": "New feature"},
    {"from": "check_type", "to": "create_release", "label": "Release"},
    {"from": "check_urgency", "to": "create_hotfix", "label": "Yes (urgent)"},
    {"from": "check_urgency", "to": "create_feature", "label": "No (normal)"},
    {"from": "create_hotfix", "to": "work"},
    {"from": "create_feature", "to": "work"},
    {"from": "create_release", "to": "work"},
    {"from": "work", "to": "pr"},
    {"from": "pr", "to": "review"},
    {"from": "review", "to": "fix_issues", "label": "No"},
    {"from": "fix_issues", "to": "review"},
    {"from": "review", "to": "merge_main", "label": "Yes (from hotfix)"},
    {"from": "review", "to": "merge_develop", "label": "Yes (from feature)"},
    {"from": "review", "to": "merge_release", "label": "Yes (from release)"},
    {"from": "merge_main", "to": "tag"},
    {"from": "merge_release", "to": "tag"},
    {"from": "tag", "to": "delete"},
    {"from": "merge_develop", "to": "delete"},
    {"from": "delete", "to": "end"}
  ],
  "direction": "TB",
  "title": "Git Branching Decision Flow",
  "format": "svg",
  "theme": "default"
}
```

## Alternative Approaches

### Option 1: Flowchart for Policy Documentation
Use flowcharts when:
- Documenting branching policies
- Showing merge approval gates
- Illustrating CI/CD triggers
- Training new team members

### Option 2: Multiple Diagrams by Scenario
Create separate diagrams for:
- Normal feature development
- Hotfix procedures
- Release preparation
- Emergency rollback

### Option 3: Comparison Diagrams
Show different strategies side-by-side:
- Gitflow vs trunk-based
- Rebase vs merge workflows
- Monorepo vs polyrepo

## Best Practices

### 1. Show Realistic Examples
- Use actual branch names from your conventions (feature/JIRA-123)
- Include realistic commit messages
- Show typical branch lifespans
- Document merge conflicts resolution

### 2. Document Branch Protection
- Note required reviewers
- Show CI/CD checks
- Include deployment gates
- Document approval requirements

### 3. Include Timing Information
- Show branch lifespan (hours, days, weeks)
- Note merge frequency
- Document release cadence
- Include deployment windows

### 4. Show Tag Strategy
- Document semantic versioning
- Show tag placement
- Note pre-release tags (alpha, beta, rc)
- Include build numbers

### 5. Document Merge Strategies
- Merge commit vs squash vs rebase
- Show merge direction
- Note conflict resolution process
- Include back-merge procedures

### 6. Add Branch Naming Conventions
- feature/TICKET-123-description
- hotfix/critical-bug-name
- release/1.2.3
- bugfix/issue-description

### 7. Include Cleanup Policy
- When to delete branches
- Archive vs delete
- Remote vs local cleanup
- Stale branch handling

## Common Variations

### Variation 1: Monorepo Strategy
Show branching for monorepos:
- Service-specific feature branches
- Coordinated releases
- Independent deployments
- Shared library updates

### Variation 2: Mobile App Release
iOS/Android specific workflows:
- App store submission branches
- Beta testing branches
- Production release branches
- Hotfix procedures

### Variation 3: Continuous Deployment
Zero-downtime deployment flow:
- Direct to main commits
- Automated testing gates
- Feature flags strategy
- Rollback procedures

### Variation 4: Open Source Project
Community contribution workflow:
- Fork-based development
- Pull request from forks
- Maintainer review process
- Contributor guidelines

### Variation 5: Enterprise Compliance
Regulated environment workflow:
- Approval gates
- Audit trail requirements
- Security scanning
- Compliance sign-offs

## Related Playbooks

### Core Diagram Types
- [render_git_graph.md](./render_git_graph.md) - Git branch visualization
- [render_flowchart.md](./render_flowchart.md) - Workflow decision logic

### Related Scenarios
- [render_deployment_pipeline.md](./render_deployment_pipeline.md) - CI/CD pipelines
- [render_approval_workflow.md](./render_approval_workflow.md) - Code review processes
- [render_release_roadmap.md](./render_release_roadmap.md) - Release planning

## Notes

- Keep branch names realistic and follow your naming conventions
- Show both successful and edge-case scenarios (merge conflicts, reverts)
- Document who can merge to which branches (team leads, maintainers)
- Include branch protection rules and required checks
- Note any automation (auto-delete, auto-merge dependabot)
- Document rollback procedures and emergency processes
- Export in SVG for team wikis and onboarding docs
- Update diagrams when workflows change
- Include links to actual CI/CD pipeline configurations
- Consider creating interactive diagrams for training
- Show actual terminal commands in notes or descriptions
- Document GitHub/GitLab/Bitbucket specific features used
