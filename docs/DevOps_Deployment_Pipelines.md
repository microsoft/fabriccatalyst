---
layout: page
title: DevOps
subtitle: Deployment Pipelines
menubar: DevOps_docs_menu
show_sidebar: false
toc: true
---

# Part 4: Fabric Deployment Pipelines

## 4.1 Create Deployment Pipeline

1. Navigate to **Deployment Pipelines** in Microsoft Fabric
2. Click **Create Pipeline**

**Pipeline Configuration:**
```
Pipeline Name: PowerBI-Reports-Lifecycle
Description: Automated deployment from DEV to UAT to PROD
Pipeline Type: Standard (3-stage pipeline)
```

## 4.2 Configure Three-Stage Pipeline

**Stage Configuration:**

| Stage | Workspace | Source | Role |
|-------|-----------|--------|------|
| **Development** | `FABRIC-CATALYST-GH-DEV` | Git main branch | Source workspace |
| **Test** | `FABRIC-CATALYST-GH-STG` | Deployed from DEV | UAT environment |
| **Production** | `FABRIC-CATALYST-GH-PROD` | Deployed from UAT | Live environment |

<p align="center">
   <img src="{{ site.baseurl }}/assets/images/devops/Deployment_pipeline.png" width="600" alt="Three-Stage Deployment Pipeline" class="zoomable-devops"/>
</p>
<p align="center">
   <strong>Figure: Three-Stage Deployment Pipeline</strong>
</p>

## 4.3 Set Up Parameter Rules

> **⚠️ Critical:** Parameter rules can only be configured **AFTER** the first deployment

**Step 1: Initial Deployment (Without Rules)**
1. Deploy from DEV → UAT without parameter rules
2. Verify successful deployment
3. Items will initially use DEV parameters (expected)

**Step 2: Configure Parameter Rules (After First Deployment)**

**UAT Stage Parameter Rules:**
```
Parameter: Environment
DEV Value: DEV → UAT Value: UAT

Parameter: SrvName  
DEV Value: dev-server-endpoint → UAT Value: uat-server-endpoint

Parameter: DbName
DEV Value: dev-database-id → UAT Value: uat-database-id
```

**PROD Stage Parameter Rules:**
```
Parameter: Environment
UAT Value: UAT → PROD Value: PROD

Parameter: SrvName  
UAT Value: uat-server-endpoint → PROD Value: prod-server-endpoint

Parameter: DbName
UAT Value: uat-database-id → PROD Value: prod-database-id
```

<p align="center">
   <img src="{{ site.baseurl }}/assets/images/devops/Parameter_Rules.png" width="600" alt="Parameter Rules Configuration" class="zoomable-devops"/>
</p>
<p align="center">
   <strong>Figure: Parameter Rules Configuration</strong>
</p>

## Pipeline Permissions

**Step 1: Access Control**
Configure appropriate permissions:

**Pipeline Administrators:**
- Full pipeline management
- Configuration changes
- Deployment approvals

**Deployers:**
- Initiate deployments
- View deployment status
- Access deployment logs

**Viewers:**
- View pipeline status
- Access deployment history
- No deployment permissions

**Step 2: Approval Configuration**
1. **UAT Approvers**: QA Team, DevOps Team
2. **PROD Approvers**: DevOps Team, Business Stakeholders
3. Configure approval timeouts
4. Set up escalation procedures

## Deployment Process

**Step 1: Manual Deployment**
1. Navigate to deployment pipeline
2. Select source stage
3. Choose target stage
4. Review changes
5. Initiate deployment

**Step 2: Automated Deployment**
1. Configure GitHub Actions trigger
2. Set up automatic deployment on merge
3. Configure approval workflows
4. Monitor deployment status

**Step 3: Deployment Validation**
1. Verify parameter updates
2. Test data connections
3. Validate report functionality
4. Confirm security settings

## Monitoring and Alerts

**Step 1: Deployment Monitoring**
1. Monitor deployment status
2. Track deployment history
3. Monitor approval times
4. Track deployment failures

**Step 2: Alert Configuration**
1. Set up failure notifications
2. Configure success notifications
3. Set up approval reminders
4. Monitor pipeline health

**Step 3: Reporting**
1. Generate deployment reports
2. Track deployment metrics
3. Monitor approval patterns
4. Analyze deployment trends

## Best Practices

### Pipeline Management
- Regular pipeline testing
- Document pipeline configurations
- Monitor pipeline performance
- Regular security reviews

### Deployment Process
- Test deployments in lower environments first
- Validate changes before production deployment
- Maintain deployment documentation
- Regular backup and recovery testing

### Security
- Regular access reviews
- Monitor deployment activities
- Implement least privilege access
- Regular security audits

## Troubleshooting

### Common Issues
- **Deployment fails**: Check workspace capacity and permissions
- **Parameter not updated**: Verify parameter rule configuration
- **Approval not triggered**: Check approval gate configuration
- **Sync issues**: Verify Git integration status

### Solutions
- Verify workspace capacity and permissions
- Review parameter rule configuration
- Check approval gate settings
- Validate Git integration

{: .no_toc }
#### Next: [GitHub Actions Automation]({{ site.baseurl }}/docs/DevOps_GitHub_Actions/) 