# Playbook: Visualize Cloud Infrastructure

## Description
This playbook guides you through visualizing cloud infrastructure across AWS, Azure, GCP, or multi-cloud environments. Perfect for documenting infrastructure architecture, planning cloud migrations, compliance documentation, and communicating deployment strategies to stakeholders.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Understanding of your cloud infrastructure
- Knowledge of services, VPCs, regions, and networking
- List of security groups, load balancers, and connectivity

## Steps

1. **Identify cloud resources**
   - List compute resources (EC2, Lambda, ECS, Kubernetes)
   - Document storage services (S3, EBS, RDS, DynamoDB)
   - Note networking components (VPC, subnets, load balancers)
   - Identify security components (WAF, IAM, security groups)

2. **Map network topology**
   - Document VPCs and subnets
   - Note availability zones and regions
   - Identify VPN connections and peering
   - Map internet gateways and NAT gateways

3. **Document data flow**
   - Show traffic patterns
   - Note ingress and egress points
   - Document service dependencies
   - Map CDN and edge locations

4. **Choose the appropriate diagram type**
   - Use **architecture_diagram** for detailed infrastructure
   - Use **block_diagram** for simplified logical views
   - Use **c4_context_diagram** for high-level cloud strategy

5. **Create the visualization**
   - Group by VPC or region
   - Show security boundaries
   - Document connectivity
   - Include disaster recovery components

## MCP Tools Required

### Primary Tool: render_architecture_diagram
Best for detailed cloud infrastructure with multiple service types.

See [render_architecture_diagram.md](./render_architecture_diagram.md) for full details.

### Primary Tool: render_block_diagram
Best for simplified infrastructure overviews.

See [render_block_diagram.md](./render_block_diagram.md) for full details.

### Secondary Tool: render_c4_context_diagram
Useful for showing cloud strategy and external connections.

See [render_c4_context_diagram.md](./render_c4_context_diagram.md) for full details.

## Recommended Diagram Type

### Primary: Architecture Diagram
**When to use**: Infrastructure documentation, deployment planning, security reviews

**Strengths**:
- Shows diverse component types (compute, storage, network)
- Supports grouping by VPC, region, or availability zone
- Clearly represents connectivity and data flow
- Can show both AWS and on-premises components

### Primary: Block Diagram
**When to use**: Executive presentations, high-level overviews, cost optimization

**Strengths**:
- Simplified representation
- Focus on logical groupings
- Good for non-technical audiences
- Easy to understand

## Example Usage

### Scenario 1: Three-Tier Web Application on AWS

**User Request**: "Visualize our AWS infrastructure for a three-tier web application with high availability"

```json
{
  "components": [
    {"id": "route53", "label": "Route 53", "type": "dns", "description": "DNS routing"},
    {"id": "cloudfront", "label": "CloudFront", "type": "cdn", "description": "Global CDN"},
    {"id": "waf", "label": "AWS WAF", "type": "security", "description": "Web application firewall"},
    {"id": "alb", "label": "Application Load Balancer", "type": "load_balancer", "description": "Multi-AZ ALB"},
    {"id": "asg_web", "label": "Web Tier ASG", "type": "compute", "description": "EC2 Auto Scaling Group (2-10 instances)"},
    {"id": "asg_app", "label": "App Tier ASG", "type": "compute", "description": "EC2 Auto Scaling Group (2-8 instances)"},
    {"id": "rds_primary", "label": "RDS PostgreSQL Primary", "type": "database", "description": "us-east-1a"},
    {"id": "rds_replica", "label": "RDS Read Replica", "type": "database", "description": "us-east-1b"},
    {"id": "elasticache", "label": "ElastiCache Redis", "type": "cache", "description": "Multi-AZ cluster"},
    {"id": "s3_assets", "label": "S3 Assets Bucket", "type": "storage", "description": "Static assets"},
    {"id": "s3_backups", "label": "S3 Backup Bucket", "type": "storage", "description": "Database backups"},
    {"id": "sqs", "label": "SQS Queue", "type": "message_queue", "description": "Async job processing"},
    {"id": "lambda", "label": "Lambda Workers", "type": "compute", "description": "Background jobs"},
    {"id": "cloudwatch", "label": "CloudWatch", "type": "monitoring", "description": "Logs and metrics"},
    {"id": "igw", "label": "Internet Gateway", "type": "network", "description": "Public internet access"},
    {"id": "nat", "label": "NAT Gateway", "type": "network", "description": "Outbound connectivity"}
  ],
  "connections": [
    {"from": "route53", "to": "cloudfront", "label": "DNS resolution", "type": "sync"},
    {"from": "cloudfront", "to": "waf", "label": "HTTPS", "type": "sync"},
    {"from": "waf", "to": "alb", "label": "Filtered traffic", "type": "sync"},
    {"from": "alb", "to": "asg_web", "label": "HTTP/2", "type": "sync"},
    {"from": "asg_web", "to": "asg_app", "label": "REST API", "type": "sync"},
    {"from": "asg_web", "to": "s3_assets", "label": "Serve static files", "type": "sync"},
    {"from": "asg_app", "to": "elasticache", "label": "Cache queries", "type": "sync"},
    {"from": "asg_app", "to": "rds_primary", "label": "Read/Write", "type": "sync"},
    {"from": "asg_app", "to": "rds_replica", "label": "Read-only", "type": "sync"},
    {"from": "rds_primary", "to": "rds_replica", "label": "Replication", "type": "async"},
    {"from": "asg_app", "to": "sqs", "label": "Enqueue jobs", "type": "async"},
    {"from": "sqs", "to": "lambda", "label": "Trigger", "type": "async"},
    {"from": "lambda", "to": "rds_primary", "label": "Database updates", "type": "sync"},
    {"from": "rds_primary", "to": "s3_backups", "label": "Automated backups", "type": "async"},
    {"from": "asg_web", "to": "cloudwatch", "label": "Logs/Metrics", "type": "async"},
    {"from": "asg_app", "to": "cloudwatch", "label": "Logs/Metrics", "type": "async"},
    {"from": "igw", "to": "alb", "label": "Inbound traffic", "type": "sync"},
    {"from": "asg_app", "to": "nat", "label": "Outbound API calls", "type": "sync"}
  ],
  "groups": [
    {
      "id": "public_subnet_1a",
      "label": "Public Subnet (us-east-1a)",
      "components": ["alb", "nat"]
    },
    {
      "id": "private_subnet_1a",
      "label": "Private Subnet (us-east-1a)",
      "components": ["asg_web", "asg_app", "rds_primary"]
    },
    {
      "id": "private_subnet_1b",
      "label": "Private Subnet (us-east-1b)",
      "components": ["rds_replica", "elasticache"]
    },
    {
      "id": "vpc",
      "label": "VPC (10.0.0.0/16)",
      "components": ["public_subnet_1a", "private_subnet_1a", "private_subnet_1b", "igw", "nat"]
    },
    {
      "id": "edge",
      "label": "Edge Services",
      "components": ["route53", "cloudfront", "waf"]
    },
    {
      "id": "serverless",
      "label": "Serverless Components",
      "components": ["lambda", "sqs"]
    },
    {
      "id": "storage",
      "label": "Storage Layer",
      "components": ["s3_assets", "s3_backups"]
    }
  ],
  "title": "AWS Three-Tier Web Application Infrastructure",
  "direction": "TB",
  "format": "svg",
  "theme": "default"
}
```

### Scenario 2: Kubernetes Cluster on AWS

**User Request**: "Show our EKS cluster infrastructure with monitoring and CI/CD"

```json
{
  "components": [
    {"id": "github", "label": "GitHub", "type": "external", "description": "Source code repository"},
    {"id": "github_actions", "label": "GitHub Actions", "type": "ci_cd", "description": "CI/CD pipeline"},
    {"id": "ecr", "label": "ECR", "type": "container_registry", "description": "Docker image registry"},
    {"id": "eks_control", "label": "EKS Control Plane", "type": "kubernetes", "description": "Managed Kubernetes"},
    {"id": "node_group_1", "label": "Node Group 1", "type": "compute", "description": "t3.medium (2-5 nodes) us-east-1a"},
    {"id": "node_group_2", "label": "Node Group 2", "type": "compute", "description": "t3.medium (2-5 nodes) us-east-1b"},
    {"id": "ingress", "label": "Nginx Ingress", "type": "load_balancer", "description": "Ingress controller"},
    {"id": "cert_manager", "label": "Cert Manager", "type": "service", "description": "TLS certificate management"},
    {"id": "prometheus", "label": "Prometheus", "type": "monitoring", "description": "Metrics collection"},
    {"id": "grafana", "label": "Grafana", "type": "monitoring", "description": "Dashboards"},
    {"id": "loki", "label": "Loki", "type": "monitoring", "description": "Log aggregation"},
    {"id": "rds", "label": "RDS PostgreSQL", "type": "database", "description": "Multi-AZ"},
    {"id": "elasticache", "label": "ElastiCache", "type": "cache", "description": "Redis cluster"},
    {"id": "s3", "label": "S3", "type": "storage", "description": "Object storage"},
    {"id": "ebs", "label": "EBS CSI Driver", "type": "storage", "description": "Persistent volumes"},
    {"id": "alb", "label": "Application Load Balancer", "type": "load_balancer", "description": "AWS ALB"},
    {"id": "route53", "label": "Route 53", "type": "dns", "description": "DNS management"}
  ],
  "connections": [
    {"from": "github", "to": "github_actions", "label": "Push/PR", "type": "sync"},
    {"from": "github_actions", "to": "ecr", "label": "Push images", "type": "sync"},
    {"from": "github_actions", "to": "eks_control", "label": "kubectl apply", "type": "sync"},
    {"from": "eks_control", "to": "node_group_1", "label": "Schedule pods", "type": "sync"},
    {"from": "eks_control", "to": "node_group_2", "label": "Schedule pods", "type": "sync"},
    {"from": "node_group_1", "to": "ecr", "label": "Pull images", "type": "sync"},
    {"from": "node_group_2", "to": "ecr", "label": "Pull images", "type": "sync"},
    {"from": "route53", "to": "alb", "label": "DNS", "type": "sync"},
    {"from": "alb", "to": "ingress", "label": "HTTPS", "type": "sync"},
    {"from": "ingress", "to": "node_group_1", "label": "Route to services", "type": "sync"},
    {"from": "ingress", "to": "node_group_2", "label": "Route to services", "type": "sync"},
    {"from": "cert_manager", "to": "route53", "label": "DNS validation", "type": "sync"},
    {"from": "node_group_1", "to": "rds", "label": "Database queries", "type": "sync"},
    {"from": "node_group_1", "to": "elasticache", "label": "Cache", "type": "sync"},
    {"from": "node_group_1", "to": "s3", "label": "Object storage", "type": "sync"},
    {"from": "node_group_1", "to": "ebs", "label": "Persistent volumes", "type": "sync"},
    {"from": "prometheus", "to": "node_group_1", "label": "Scrape metrics", "type": "sync"},
    {"from": "prometheus", "to": "node_group_2", "label": "Scrape metrics", "type": "sync"},
    {"from": "grafana", "to": "prometheus", "label": "Query metrics", "type": "sync"},
    {"from": "loki", "to": "node_group_1", "label": "Collect logs", "type": "async"},
    {"from": "grafana", "to": "loki", "label": "Query logs", "type": "sync"}
  ],
  "groups": [
    {
      "id": "cicd",
      "label": "CI/CD Pipeline",
      "components": ["github", "github_actions", "ecr"]
    },
    {
      "id": "eks_cluster",
      "label": "EKS Cluster",
      "components": ["eks_control", "node_group_1", "node_group_2", "ingress", "cert_manager"]
    },
    {
      "id": "observability",
      "label": "Observability Stack",
      "components": ["prometheus", "grafana", "loki"]
    },
    {
      "id": "data_layer",
      "label": "Data Layer",
      "components": ["rds", "elasticache", "s3", "ebs"]
    }
  ],
  "title": "EKS Kubernetes Cluster Infrastructure",
  "direction": "TB",
  "format": "svg",
  "theme": "default"
}
```

### Scenario 3: Multi-Region Disaster Recovery Setup

**User Request**: "Show our multi-region AWS setup with disaster recovery"

```json
{
  "components": [
    {"id": "r53", "label": "Route 53", "type": "dns", "description": "Failover routing policy"},
    {"id": "cf_primary", "label": "CloudFront (Primary Origin)", "type": "cdn"},
    {"id": "alb_us_east", "label": "ALB us-east-1", "type": "load_balancer"},
    {"id": "ec2_us_east", "label": "EC2 Fleet us-east-1", "type": "compute", "description": "Primary region"},
    {"id": "rds_us_east", "label": "RDS us-east-1", "type": "database", "description": "Primary database"},
    {"id": "s3_us_east", "label": "S3 us-east-1", "type": "storage"},
    {"id": "alb_us_west", "label": "ALB us-west-2", "type": "load_balancer"},
    {"id": "ec2_us_west", "label": "EC2 Fleet us-west-2", "type": "compute", "description": "DR region (standby)"},
    {"id": "rds_us_west", "label": "RDS us-west-2", "type": "database", "description": "Read replica"},
    {"id": "s3_us_west", "label": "S3 us-west-2", "type": "storage"},
    {"id": "db_replication", "label": "Cross-Region Replication", "type": "network"},
    {"id": "s3_replication", "label": "S3 Replication", "type": "network"}
  ],
  "connections": [
    {"from": "r53", "to": "cf_primary", "label": "Primary routing", "type": "sync"},
    {"from": "cf_primary", "to": "alb_us_east", "label": "Active", "type": "sync"},
    {"from": "cf_primary", "to": "alb_us_west", "label": "Failover", "type": "sync", "style": "dotted"},
    {"from": "alb_us_east", "to": "ec2_us_east", "label": "HTTP", "type": "sync"},
    {"from": "ec2_us_east", "to": "rds_us_east", "label": "Read/Write", "type": "sync"},
    {"from": "ec2_us_east", "to": "s3_us_east", "label": "Storage", "type": "sync"},
    {"from": "alb_us_west", "to": "ec2_us_west", "label": "HTTP", "type": "sync"},
    {"from": "ec2_us_west", "to": "rds_us_west", "label": "Read-only", "type": "sync"},
    {"from": "ec2_us_west", "to": "s3_us_west", "label": "Storage", "type": "sync"},
    {"from": "rds_us_east", "to": "rds_us_west", "label": "Async replication", "type": "async"},
    {"from": "s3_us_east", "to": "s3_us_west", "label": "Cross-region replication", "type": "async"}
  ],
  "groups": [
    {
      "id": "global",
      "label": "Global Services",
      "components": ["r53", "cf_primary"]
    },
    {
      "id": "primary_region",
      "label": "Primary Region (us-east-1)",
      "components": ["alb_us_east", "ec2_us_east", "rds_us_east", "s3_us_east"]
    },
    {
      "id": "dr_region",
      "label": "DR Region (us-west-2)",
      "components": ["alb_us_west", "ec2_us_west", "rds_us_west", "s3_us_west"]
    }
  ],
  "title": "Multi-Region Disaster Recovery Infrastructure",
  "direction": "TB",
  "format": "svg",
  "theme": "default"
}
```

### Scenario 4: Serverless Architecture on AWS

**User Request**: "Visualize our serverless application architecture"

```json
{
  "components": [
    {"id": "r53", "label": "Route 53", "type": "dns"},
    {"id": "cf", "label": "CloudFront", "type": "cdn"},
    {"id": "s3_web", "label": "S3 Static Website", "type": "storage", "description": "React SPA"},
    {"id": "apigw", "label": "API Gateway", "type": "api_gateway", "description": "REST API"},
    {"id": "cognito", "label": "Cognito", "type": "auth", "description": "User authentication"},
    {"id": "lambda_auth", "label": "Lambda Authorizer", "type": "compute"},
    {"id": "lambda_users", "label": "Lambda - Users API", "type": "compute"},
    {"id": "lambda_orders", "label": "Lambda - Orders API", "type": "compute"},
    {"id": "lambda_process", "label": "Lambda - Order Processor", "type": "compute"},
    {"id": "dynamodb_users", "label": "DynamoDB Users", "type": "database"},
    {"id": "dynamodb_orders", "label": "DynamoDB Orders", "type": "database"},
    {"id": "sqs", "label": "SQS Queue", "type": "message_queue"},
    {"id": "sns", "label": "SNS Topic", "type": "notification"},
    {"id": "ses", "label": "SES", "type": "email", "description": "Email notifications"},
    {"id": "s3_uploads", "label": "S3 Uploads", "type": "storage"},
    {"id": "eventbridge", "label": "EventBridge", "type": "event_bus"},
    {"id": "cloudwatch", "label": "CloudWatch", "type": "monitoring"}
  ],
  "connections": [
    {"from": "r53", "to": "cf", "label": "DNS", "type": "sync"},
    {"from": "cf", "to": "s3_web", "label": "Serve SPA", "type": "sync"},
    {"from": "s3_web", "to": "apigw", "label": "API calls", "type": "sync"},
    {"from": "apigw", "to": "lambda_auth", "label": "Authorize", "type": "sync"},
    {"from": "lambda_auth", "to": "cognito", "label": "Validate token", "type": "sync"},
    {"from": "apigw", "to": "lambda_users", "label": "Invoke", "type": "sync"},
    {"from": "apigw", "to": "lambda_orders", "label": "Invoke", "type": "sync"},
    {"from": "lambda_users", "to": "dynamodb_users", "label": "Query", "type": "sync"},
    {"from": "lambda_orders", "to": "dynamodb_orders", "label": "Put item", "type": "sync"},
    {"from": "lambda_orders", "to": "sqs", "label": "Send message", "type": "async"},
    {"from": "sqs", "to": "lambda_process", "label": "Trigger", "type": "async"},
    {"from": "lambda_process", "to": "dynamodb_orders", "label": "Update", "type": "sync"},
    {"from": "lambda_process", "to": "sns", "label": "Publish", "type": "async"},
    {"from": "sns", "to": "ses", "label": "Email notification", "type": "async"},
    {"from": "s3_uploads", "to": "eventbridge", "label": "Object created", "type": "async"},
    {"from": "eventbridge", "to": "lambda_process", "label": "Trigger", "type": "async"},
    {"from": "lambda_users", "to": "cloudwatch", "label": "Logs", "type": "async"},
    {"from": "lambda_orders", "to": "cloudwatch", "label": "Logs", "type": "async"}
  ],
  "groups": [
    {
      "id": "frontend",
      "label": "Frontend",
      "components": ["r53", "cf", "s3_web"]
    },
    {
      "id": "api_layer",
      "label": "API Layer",
      "components": ["apigw", "lambda_auth", "cognito"]
    },
    {
      "id": "business_logic",
      "label": "Business Logic",
      "components": ["lambda_users", "lambda_orders", "lambda_process"]
    },
    {
      "id": "data_layer",
      "label": "Data Layer",
      "components": ["dynamodb_users", "dynamodb_orders", "s3_uploads"]
    },
    {
      "id": "messaging",
      "label": "Messaging & Events",
      "components": ["sqs", "sns", "eventbridge", "ses"]
    }
  ],
  "title": "Serverless Application Architecture",
  "direction": "TB",
  "format": "svg",
  "theme": "default"
}
```

## Alternative Approaches

### Option 1: Block Diagram for Simplified View
Use block diagrams when:
- Presenting to executives or non-technical stakeholders
- Showing high-level cost allocation
- Documenting logical architecture without implementation details
- Creating simplified training materials

### Option 2: C4 Context for Cloud Strategy
Use C4 context diagrams for:
- Showing hybrid cloud and on-premises integration
- Documenting multi-cloud strategy
- Presenting to business stakeholders
- Security and compliance reviews

### Option 3: Network-Focused Diagrams
Create network-centric views:
- VPC topology with subnets and routing
- Security group and NACL rules
- VPN and Direct Connect configurations
- Peering relationships

## Best Practices

### 1. Group by Logical Boundaries
- Use VPC groupings for network isolation
- Group by availability zone for resilience
- Organize by environment (dev, staging, prod)
- Separate by security zones (public, private, restricted)

### 2. Show High Availability
- Document multi-AZ deployments
- Show load balancer distribution
- Note auto-scaling configurations
- Indicate backup and replica instances

### 3. Document Security
- Mark security groups and NACLs
- Show WAF and firewall placement
- Note encryption at rest and in transit
- Document IAM boundaries

### 4. Include Cost Context
- Note instance types and sizes
- Document reserved vs on-demand
- Show data transfer patterns
- Identify expensive components

### 5. Show Connectivity Clearly
- Use solid lines for active paths
- Dotted lines for failover/backup
- Label with protocols and ports
- Note bandwidth or throughput limits

### 6. Document Compliance
- Mark PCI/HIPAA/SOC2 boundaries
- Show audit logging components
- Note data residency requirements
- Document backup and retention

### 7. Keep It Current
- Update after infrastructure changes
- Version control diagram definitions
- Include in infrastructure-as-code repos
- Automate generation from Terraform/CloudFormation

## Common Variations

### Variation 1: Multi-Cloud Architecture
Show infrastructure across multiple cloud providers:
- AWS for compute and storage
- GCP for data analytics
- Azure for enterprise integration
- Document inter-cloud connectivity

### Variation 2: Hybrid Cloud
Combine on-premises and cloud:
- Show Direct Connect or VPN
- Document data synchronization
- Note migration paths
- Include legacy systems

### Variation 3: Cost-Optimized View
Focus on cost structure:
- Highlight reserved instances
- Show spot fleet usage
- Document S3 storage classes
- Note data transfer costs

### Variation 4: Security-Focused View
Emphasize security architecture:
- Show DMZ and security zones
- Document encryption boundaries
- Note logging and monitoring
- Include incident response paths

### Variation 5: Environment Progression
Show dev → staging → prod:
- Document promotion paths
- Show environment differences
- Note scaling variations
- Include testing environments

## Related Playbooks

### Core Diagram Types
- [render_architecture_diagram.md](./render_architecture_diagram.md) - Detailed infrastructure
- [render_block_diagram.md](./render_block_diagram.md) - Simplified views
- [render_c4_context_diagram.md](./render_c4_context_diagram.md) - System context

### Related Scenarios
- [render_microservices_architecture.md](./render_microservices_architecture.md) - Application architecture
- [render_deployment_pipeline.md](./render_deployment_pipeline.md) - CI/CD infrastructure
- [render_data_pipeline.md](./render_data_pipeline.md) - Data infrastructure

## Notes

- For large infrastructures (>30 components), create multiple diagrams by domain or environment
- Include region and availability zone information in component descriptions
- Document DNS and domain configurations
- Note monitoring and alerting setup (CloudWatch, DataDog, etc.)
- Include disaster recovery RPO/RTO targets in notes
- Document backup strategies and retention policies
- Export in SVG format for infrastructure documentation
- Consider automating diagram generation from Terraform state or AWS Config
- Keep sensitive information (IPs, keys) out of diagrams
- Use consistent naming conventions matching your IaC code
- Document scaling limits and performance characteristics
- Include cost estimates or actual spend in component notes
