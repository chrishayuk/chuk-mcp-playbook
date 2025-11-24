# Playbook: Visualize Data Pipeline

## Description
This playbook guides you through visualizing ETL (Extract, Transform, Load) and data processing pipelines including data sources, transformations, quality checks, and destination systems. Perfect for data engineering, analytics architecture, and compliance documentation.

## Prerequisites
- Access to the mcp-mermaid-renderer MCP server
- Understanding of data sources and destinations
- Knowledge of transformation steps
- List of data quality rules

## Steps

1. **Identify data sources**
   - List all source systems
   - Note data formats
   - Document extraction methods
   - Identify refresh schedules

2. **Map transformations**
   - Data cleaning steps
   - Enrichment processes
   - Aggregations
   - Quality checks

3. **Choose diagram type**
   - Use **sankey_diagram** for data flow volumes
   - Use **flowchart** for pipeline logic
   - Use **sequence_diagram** for orchestration

4. **Create visualization**
   - Show data flow from source to destination
   - Document transformations
   - Include volume estimates
   - Note processing schedules

## MCP Tools Required

### Primary Tool: render_sankey_diagram
See [render_sankey_diagram.md](./render_sankey_diagram.md)

### Primary Tool: render_flowchart
See [render_flowchart.md](./render_flowchart.md)

### Secondary Tool: render_sequence_diagram
See [render_sequence_diagram.md](./render_sequence_diagram.md)

## Example Usage

```json
{
  "nodes": [
    {"id": "crm", "label": "CRM Database"},
    {"id": "web", "label": "Web Analytics"},
    {"id": "mobile", "label": "Mobile App"},
    {"id": "staging", "label": "Staging Area"},
    {"id": "cleanse", "label": "Data Cleansing"},
    {"id": "transform", "label": "Transformation"},
    {"id": "warehouse", "label": "Data Warehouse"},
    {"id": "bi", "label": "BI Tools"},
    {"id": "ml", "label": "ML Models"}
  ],
  "links": [
    {"source": "crm", "target": "staging", "value": 10000},
    {"source": "web", "target": "staging", "value": 50000},
    {"source": "mobile", "target": "staging", "value": 30000},
    {"source": "staging", "target": "cleanse", "value": 90000},
    {"source": "cleanse", "target": "transform", "value": 85000},
    {"source": "transform", "target": "warehouse", "value": 85000},
    {"source": "warehouse", "target": "bi", "value": 60000},
    {"source": "warehouse", "target": "ml", "value": 25000}
  ],
  "title": "Data Pipeline Flow",
  "format": "svg",
  "theme": "default"
}
```

## Best Practices

1. **Show data volumes** - Indicate records processed
2. **Document schedules** - Batch vs real-time
3. **Include quality checks** - Validation rules
4. **Note transformations** - What changes where
5. **Track lineage** - Source to destination mapping
6. **Monitor performance** - Processing times
7. **Handle failures** - Error handling and retries

## Related Playbooks

- [render_sankey_diagram.md](./render_sankey_diagram.md)
- [render_flowchart.md](./render_flowchart.md)
- [render_database_schema_visualization.md](./render_database_schema_visualization.md)
- [render_microservices_architecture.md](./render_microservices_architecture.md)
