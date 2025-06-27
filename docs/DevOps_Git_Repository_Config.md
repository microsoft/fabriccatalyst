---
layout: page
title: DevOps
subtitle: Git Repository Configuration
menubar: DevOps_docs_menu
show_sidebar: false
toc: true
---

# Part 3: Git Repository Configuration

## 3.1 Repository Structure

**Recommended Structure:**
```
PBIP_Fabric_Reference_Guide/
├── .github/
│   └── workflows/
│       └── fabric-deployment.yml     # CI/CD workflow
├── scripts/
│   └── deploy_all.py                # Deployment script
├── fabric/
│   └── workspace/                   # Synced .pbip files
│       ├── [ReportName].Report/
│       ├── [ReportName].SemanticModel/
│       └── README.md
├── docs/
│   └── deployment-guide.md         # Documentation
├── .gitignore                      # Security configurations
└── README.md                       # This guide
```

## 3.2 Branch Strategy

**Branch Mapping:**
```
Git Branch                    ↔ Fabric Workspace
─────────────────────────────────────────────────
main                         ↔ FABRIC-CATALYST-GH-DEV
feature/[feature-name]       ↔ FABRIC-CATALYST-GH-FEATURE
```

**Development Workflow:**
1. **Feature Development:** `feature/[name]` → Feature Workspace
2. **Integration:** Feature branch → `main` branch (via PR)
3. **Deployment:** `main` branch → DEV → UAT → PROD

## 3.3 Security Best Practices

**❌ Never Commit These to Git:**
- Database connection strings
- Server URLs or endpoints
- Workspace names or IDs
- Authentication tokens or passwords
- Capacity identifiers
- Environment-specific configuration

**✅ Secure Alternatives:**

**Option 1: Template Configuration**
```json
// config/template-config.json
{
  "environment": "TEMPLATE",
  "workspace": "PROJECT-NAME-{ENVIRONMENT}",
  "dataSourceSettings": {
    "serverName": "{SERVER-ENDPOINT-PLACEHOLDER}",
    "databaseName": "{DATABASE-NAME-PLACEHOLDER}"
  }
}
```

**Option 2: Fabric-Native Parameter Management**
- Configure parameter rules in deployment pipeline
- All sensitive values managed within Fabric
- No configuration files needed in Git

> **📝 This Guide Uses:** Option 2 (Fabric-Native) for maximum security

{: .no_toc }
#### Next: [Deployment Pipelines]({{ site.baseurl }}/docs/DevOps_Deployment_Pipelines/) 