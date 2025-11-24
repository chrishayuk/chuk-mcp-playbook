# Playbook: Visualize Deployment Pipeline

## Description
This playbook guides you through visualizing CI/CD pipelines, including build stages, testing phases, deployment steps, approval gates, and rollback procedures. Perfect for documenting DevOps workflows, troubleshooting pipeline issues, onboarding engineers, and optimizing delivery processes.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Understanding of your CI/CD pipeline stages
- Knowledge of build, test, and deployment steps
- List of approval gates and automation triggers

## ⚠️ CRITICAL: Participant Type Warning (for Sequence Diagrams)

**If using sequence diagrams, ONLY use these participant types:**
- `"actor"` - for human users
- `"participant"` - for ALL systems, services, pipelines, tools

**DO NOT USE**: `"boundary"`, `"control"`, `"entity"`, `"database"`, etc. These will cause rendering failures!

Use descriptive **labels** to distinguish roles: `{"id": "jenkins", "label": "Jenkins CI", "type": "participant"}` ✅

## Steps

1. **Identify pipeline stages**
   - Source code checkout
   - Build and compile
   - Unit tests
   - Integration tests
   - Security scans
   - Deployment stages
   - Post-deployment validation

2. **Map dependencies**
   - Parallel vs sequential stages
   - Conditional executions
   - Manual approval gates
   - Failure handling

3. **Document environments**
   - Development
   - Testing/QA
   - Staging
   - Production
   - Rollback procedures

4. **Choose the appropriate diagram type**
   - Use **flowchart** for pipeline logic and stages
   - Use **sequence_diagram** for deployment interactions
   - Use **timeline** for release schedules

5. **Create the visualization**
   - Show all stages clearly
   - Include decision points
   - Document approval gates
   - Add timing estimates

## MCP Tools Required

### Primary Tool: render_flowchart
Best for showing CI/CD pipeline stages, decision points, and flows.

See [render_flowchart.md](./render_flowchart.md) for full details.

### Primary Tool: render_sequence_diagram
Best for showing deployment interactions between systems.

See [render_sequence_diagram.md](./render_sequence_diagram.md) for full details.

### Secondary Tool: render_timeline
Useful for visualizing release schedules and deployment windows.

See [render_timeline.md](./render_timeline.md) for full details.

## Recommended Diagram Type

### Primary: Flowchart
**When to use**: Pipeline documentation, troubleshooting, optimization

**Strengths**:
- Shows stages and decision points
- Represents parallel execution
- Documents error handling
- Visualizes approval gates

### Primary: Sequence Diagram
**When to use**: Deployment orchestration, service interactions

**Strengths**:
- Shows interaction between deployment components
- Documents API calls during deployment
- Represents time-based sequences
- Good for complex multi-service deployments

## Example Usage

### Scenario 1: Standard CI/CD Pipeline

**User Request**: "Visualize our CI/CD pipeline from code commit to production deployment"

```json
{
  "nodes": [
    {"id": "start", "label": "Push to main", "shape": "circle"},
    {"id": "checkout", "label": "Checkout code", "shape": "rectangle"},
    {"id": "install", "label": "Install dependencies", "shape": "rectangle"},
    {"id": "lint", "label": "Run linters", "shape": "rectangle"},
    {"id": "unit_test", "label": "Run unit tests", "shape": "rectangle"},
    {"id": "build", "label": "Build application", "shape": "rectangle"},
    {"id": "integration_test", "label": "Integration tests", "shape": "rectangle"},
    {"id": "security_scan", "label": "Security scanning", "shape": "rectangle"},
    {"id": "quality_gate", "label": "Quality gate passed?", "shape": "diamond"},
    {"id": "build_docker", "label": "Build Docker image", "shape": "rectangle"},
    {"id": "push_registry", "label": "Push to registry", "shape": "rectangle"},
    {"id": "deploy_staging", "label": "Deploy to staging", "shape": "rectangle"},
    {"id": "smoke_test", "label": "Run smoke tests", "shape": "rectangle"},
    {"id": "staging_ok", "label": "Staging tests passed?", "shape": "diamond"},
    {"id": "approval", "label": "Manual approval required?", "shape": "diamond"},
    {"id": "wait_approval", "label": "Wait for approval", "shape": "rectangle"},
    {"id": "deploy_prod", "label": "Deploy to production", "shape": "rectangle"},
    {"id": "health_check", "label": "Health check", "shape": "rectangle"},
    {"id": "prod_ok", "label": "Production healthy?", "shape": "diamond"},
    {"id": "notify_success", "label": "Send success notification", "shape": "rectangle"},
    {"id": "rollback", "label": "Rollback deployment", "shape": "rectangle"},
    {"id": "notify_failure", "label": "Send failure alert", "shape": "rectangle"},
    {"id": "end_success", "label": "Complete", "shape": "circle"},
    {"id": "end_failure", "label": "Failed", "shape": "circle"}
  ],
  "edges": [
    {"from": "start", "to": "checkout"},
    {"from": "checkout", "to": "install"},
    {"from": "install", "to": "lint"},
    {"from": "lint", "to": "unit_test"},
    {"from": "unit_test", "to": "build"},
    {"from": "build", "to": "integration_test"},
    {"from": "integration_test", "to": "security_scan"},
    {"from": "security_scan", "to": "quality_gate"},
    {"from": "quality_gate", "to": "build_docker", "label": "Pass"},
    {"from": "quality_gate", "to": "notify_failure", "label": "Fail"},
    {"from": "build_docker", "to": "push_registry"},
    {"from": "push_registry", "to": "deploy_staging"},
    {"from": "deploy_staging", "to": "smoke_test"},
    {"from": "smoke_test", "to": "staging_ok"},
    {"from": "staging_ok", "to": "approval", "label": "Pass"},
    {"from": "staging_ok", "to": "notify_failure", "label": "Fail"},
    {"from": "approval", "to": "wait_approval", "label": "Yes"},
    {"from": "approval", "to": "deploy_prod", "label": "No (auto)"},
    {"from": "wait_approval", "to": "deploy_prod"},
    {"from": "deploy_prod", "to": "health_check"},
    {"from": "health_check", "to": "prod_ok"},
    {"from": "prod_ok", "to": "notify_success", "label": "Healthy"},
    {"from": "prod_ok", "to": "rollback", "label": "Unhealthy"},
    {"from": "rollback", "to": "notify_failure"},
    {"from": "notify_success", "to": "end_success"},
    {"from": "notify_failure", "to": "end_failure"}
  ],
  "direction": "TB",
  "title": "CI/CD Pipeline - Main Branch Deployment",
  "format": "svg",
  "theme": "default"
}
```

### Scenario 2: Kubernetes Blue/Green Deployment Sequence

**User Request**: "Show the sequence of steps for a blue/green deployment to Kubernetes"

```json
{
  "participants": [
    {"id": "cicd", "label": "CI/CD Pipeline", "type": "control"},
    {"id": "registry", "label": "Container Registry", "type": "database"},
    {"id": "k8s", "label": "Kubernetes API", "type": "control"},
    {"id": "blue", "label": "Blue Deployment", "type": "entity"},
    {"id": "green", "label": "Green Deployment", "type": "entity"},
    {"id": "service", "label": "K8s Service", "type": "boundary"},
    {"id": "ingress", "label": "Ingress Controller", "type": "boundary"},
    {"id": "monitor", "label": "Monitoring", "type": "control"}
  ],
  "messages": [
    {"from": "cicd", "to": "registry", "message": "Push new image v2.0", "arrow_type": "solid"},
    {"from": "cicd", "to": "k8s", "message": "Create green deployment", "arrow_type": "solid"},
    {"from": "k8s", "to": "green", "message": "Deploy pods with v2.0", "arrow_type": "solid", "activate": true},
    {"from": "green", "to": "registry", "message": "Pull image v2.0", "arrow_type": "solid"},
    {"from": "k8s", "to": "green", "message": "Wait for ready status", "arrow_type": "solid"},
    {"from": "green", "to": "k8s", "message": "All pods ready", "arrow_type": "dotted"},
    {"from": "cicd", "to": "monitor", "message": "Run health checks on green", "arrow_type": "solid"},
    {"from": "monitor", "to": "green", "message": "GET /health", "arrow_type": "solid"},
    {"from": "green", "to": "monitor", "message": "200 OK", "arrow_type": "dotted"},
    {"from": "cicd", "to": "service", "message": "Update service selector to green", "arrow_type": "solid"},
    {"from": "service", "to": "green", "message": "Route traffic to green", "arrow_type": "solid"},
    {"from": "cicd", "to": "monitor", "message": "Monitor metrics (5 min)", "arrow_type": "solid"},
    {"from": "monitor", "to": "cicd", "message": "No errors detected", "arrow_type": "dotted"},
    {"from": "cicd", "to": "k8s", "message": "Delete blue deployment", "arrow_type": "solid"},
    {"from": "k8s", "to": "blue", "message": "Terminate pods", "arrow_type": "solid"}
  ],
  "notes": [
    {"position": "right of", "participants": ["green"], "text": "Green deployment runs\nside-by-side with Blue"},
    {"position": "right of", "participants": ["service"], "text": "Zero-downtime\ncutover"}
  ],
  "title": "Kubernetes Blue/Green Deployment",
  "autonumber": true,
  "format": "svg",
  "theme": "default"
}
```

### Scenario 3: Multi-Environment Pipeline

**User Request**: "Show our deployment pipeline across dev, staging, and production environments"

```json
{
  "nodes": [
    {"id": "start", "label": "Merge to main", "shape": "circle"},
    {"id": "build", "label": "Build & Test", "shape": "rectangle"},
    {"id": "artifact", "label": "Create artifact", "shape": "rectangle"},

    {"id": "deploy_dev", "label": "Deploy to DEV", "shape": "rectangle"},
    {"id": "test_dev", "label": "Automated tests (DEV)", "shape": "rectangle"},
    {"id": "dev_ok", "label": "DEV passing?", "shape": "diamond"},

    {"id": "deploy_staging", "label": "Deploy to STAGING", "shape": "rectangle"},
    {"id": "test_staging", "label": "E2E tests (STAGING)", "shape": "rectangle"},
    {"id": "perf_test", "label": "Performance tests", "shape": "rectangle"},
    {"id": "staging_ok", "label": "STAGING passing?", "shape": "diamond"},

    {"id": "qa_approval", "label": "QA approval", "shape": "diamond"},
    {"id": "prod_approval", "label": "Production approval", "shape": "diamond"},

    {"id": "deploy_prod", "label": "Deploy to PRODUCTION", "shape": "rectangle"},
    {"id": "canary", "label": "Canary deployment (10%)", "shape": "rectangle"},
    {"id": "monitor", "label": "Monitor metrics", "shape": "rectangle"},
    {"id": "canary_ok", "label": "Canary healthy?", "shape": "diamond"},
    {"id": "full_rollout", "label": "Full rollout (100%)", "shape": "rectangle"},

    {"id": "rollback", "label": "Rollback", "shape": "rectangle"},
    {"id": "notify_success", "label": "Notify success", "shape": "rectangle"},
    {"id": "notify_fail", "label": "Notify failure", "shape": "rectangle"},
    {"id": "end_success", "label": "Complete", "shape": "circle"},
    {"id": "end_fail", "label": "Failed", "shape": "circle"}
  ],
  "edges": [
    {"from": "start", "to": "build"},
    {"from": "build", "to": "artifact"},
    {"from": "artifact", "to": "deploy_dev"},
    {"from": "deploy_dev", "to": "test_dev"},
    {"from": "test_dev", "to": "dev_ok"},
    {"from": "dev_ok", "to": "deploy_staging", "label": "Pass"},
    {"from": "dev_ok", "to": "notify_fail", "label": "Fail"},
    {"from": "deploy_staging", "to": "test_staging"},
    {"from": "test_staging", "to": "perf_test"},
    {"from": "perf_test", "to": "staging_ok"},
    {"from": "staging_ok", "to": "qa_approval", "label": "Pass"},
    {"from": "staging_ok", "to": "notify_fail", "label": "Fail"},
    {"from": "qa_approval", "to": "prod_approval", "label": "Approved"},
    {"from": "qa_approval", "to": "notify_fail", "label": "Rejected"},
    {"from": "prod_approval", "to": "deploy_prod", "label": "Approved"},
    {"from": "prod_approval", "to": "notify_fail", "label": "Rejected"},
    {"from": "deploy_prod", "to": "canary"},
    {"from": "canary", "to": "monitor"},
    {"from": "monitor", "to": "canary_ok"},
    {"from": "canary_ok", "to": "full_rollout", "label": "Healthy"},
    {"from": "canary_ok", "to": "rollback", "label": "Issues"},
    {"from": "full_rollout", "to": "notify_success"},
    {"from": "rollback", "to": "notify_fail"},
    {"from": "notify_success", "to": "end_success"},
    {"from": "notify_fail", "to": "end_fail"}
  ],
  "direction": "TB",
  "title": "Multi-Environment Deployment Pipeline",
  "format": "svg",
  "theme": "default"
}
```

### Scenario 4: GitHub Actions CI/CD Workflow

**User Request**: "Document our GitHub Actions workflow with parallel jobs"

```json
{
  "nodes": [
    {"id": "trigger", "label": "Push to main", "shape": "circle"},
    {"id": "checkout", "label": "Checkout code", "shape": "rectangle"},

    {"id": "lint", "label": "Lint (Node 18)", "shape": "rectangle"},
    {"id": "test_16", "label": "Test (Node 16)", "shape": "rectangle"},
    {"id": "test_18", "label": "Test (Node 18)", "shape": "rectangle"},
    {"id": "test_20", "label": "Test (Node 20)", "shape": "rectangle"},

    {"id": "build", "label": "Build production", "shape": "rectangle"},
    {"id": "sonar", "label": "SonarQube scan", "shape": "rectangle"},
    {"id": "snyk", "label": "Snyk security scan", "shape": "rectangle"},

    {"id": "wait_checks", "label": "All checks passed?", "shape": "diamond"},

    {"id": "docker", "label": "Build Docker image", "shape": "rectangle"},
    {"id": "push_ecr", "label": "Push to ECR", "shape": "rectangle"},
    {"id": "deploy", "label": "Deploy to ECS", "shape": "rectangle"},

    {"id": "fail", "label": "Notify failure", "shape": "rectangle"},
    {"id": "success", "label": "Notify success", "shape": "rectangle"},
    {"id": "end", "label": "Complete", "shape": "circle"}
  ],
  "edges": [
    {"from": "trigger", "to": "checkout"},
    {"from": "checkout", "to": "lint"},
    {"from": "checkout", "to": "test_16"},
    {"from": "checkout", "to": "test_18"},
    {"from": "checkout", "to": "test_20"},
    {"from": "lint", "to": "wait_checks"},
    {"from": "test_16", "to": "wait_checks"},
    {"from": "test_18", "to": "wait_checks"},
    {"from": "test_20", "to": "wait_checks"},
    {"from": "wait_checks", "to": "build", "label": "Pass"},
    {"from": "wait_checks", "to": "fail", "label": "Fail"},
    {"from": "build", "to": "sonar"},
    {"from": "build", "to": "snyk"},
    {"from": "sonar", "to": "docker"},
    {"from": "snyk", "to": "docker"},
    {"from": "docker", "to": "push_ecr"},
    {"from": "push_ecr", "to": "deploy"},
    {"from": "deploy", "to": "success"},
    {"from": "success", "to": "end"},
    {"from": "fail", "to": "end"}
  ],
  "direction": "TB",
  "title": "GitHub Actions CI/CD Workflow",
  "format": "svg",
  "theme": "default"
}
```

## Alternative Approaches

### Option 1: Sequence Diagram for Complex Deployments
Use sequence diagrams when:
- Documenting microservices deployment orchestration
- Showing API calls during deployment
- Visualizing database migration sequences
- Representing rollback procedures

### Option 2: Timeline for Release Schedules
Use timelines when:
- Planning deployment windows
- Showing release schedules
- Documenting freeze periods
- Visualizing deployment cadence

### Option 3: Multiple Diagrams by Type
Create separate diagrams for:
- Build pipeline
- Test pipeline
- Deployment pipeline
- Rollback procedures

## Best Practices

### 1. Show Parallel Execution
- Clearly indicate jobs that run in parallel
- Document dependencies between stages
- Show wait points where parallelism joins

### 2. Include Timing Estimates
- Add duration for each stage
- Note total pipeline time
- Identify bottlenecks
- Document SLA targets

### 3. Document Approval Gates
- Show manual approval steps
- Note who can approve
- Include approval timeout policies
- Document emergency override procedures

### 4. Show Error Handling
- Document failure paths
- Show retry logic
- Include rollback procedures
- Note notification channels

### 5. Include Security Scans
- SAST (static analysis)
- DAST (dynamic analysis)
- Dependency scanning
- Container scanning
- License compliance

### 6. Document Artifacts
- What gets built
- Where it's stored
- Retention policies
- Versioning strategy

### 7. Show Deployment Strategies
- Blue/green
- Canary
- Rolling update
- Recreate

## Common Variations

### Variation 1: Monorepo Pipeline
Pipeline for monorepo with multiple services:
- Detect changed services
- Build only affected services
- Run affected tests
- Deploy updated services only

### Variation 2: Mobile App Pipeline
iOS/Android specific steps:
- Code signing
- App store submission
- Beta distribution (TestFlight, Firebase)
- App review process

### Variation 3: Infrastructure as Code
Terraform/CloudFormation pipeline:
- Plan phase
- Manual review
- Apply phase
- Drift detection

### Variation 4: Database Migration Pipeline
Schema change deployment:
- Backup database
- Test migration on copy
- Run migration scripts
- Validate schema
- Rollback on failure

### Variation 5: Feature Flag Deployment
Progressive rollout:
- Deploy code (flag off)
- Enable for internal users
- Gradual percentage rollout
- Full enablement
- Remove flag (tech debt)

## Related Playbooks

### Core Diagram Types
- [render_flowchart.md](./render_flowchart.md) - Pipeline stages and logic
- [render_sequence_diagram.md](./render_sequence_diagram.md) - Deployment interactions
- [render_timeline.md](./render_timeline.md) - Release schedules

### Related Scenarios
- [render_git_branching_strategy.md](./render_git_branching_strategy.md) - Source control workflow
- [render_cloud_infrastructure_diagram.md](./render_cloud_infrastructure_diagram.md) - Deployment targets
- [render_approval_workflow.md](./render_approval_workflow.md) - Approval processes

## Notes

- Include CI/CD platform specifics (Jenkins, GitLab CI, GitHub Actions, CircleCI)
- Document environment-specific configurations
- Note secrets management approach
- Include monitoring and alerting integration
- Document rollback procedures clearly
- Show cache strategies for faster builds
- Include cost optimization notes (spot instances, build minutes)
- Document compliance requirements (SOX, HIPAA, PCI-DSS)
- Note disaster recovery procedures
- Export in SVG for runbook documentation
- Keep diagrams updated with pipeline changes
- Include links to actual pipeline configuration files
