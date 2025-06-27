---
layout: page
title: DevOps
subtitle: Testing & Validation
menubar: DevOps_docs_menu
show_sidebar: false
toc: true
---

# Part 7: Testing & Validation

## 7.1 End-to-End Testing

**Test Python Script Locally First:**

Before running the complete CI/CD pipeline, test the deployment script locally:

```bash
# Install dependencies
pip install requests python-dotenv

# Test authentication and pipeline discovery
python scripts/deploy_all.py \
  "your-tenant-id" \
  "your-app-id" \
  "your-client-secret" \
  "PowerBI-Reports-Lifecycle" \
  0

# Expected output:
# 🚀 Starting Microsoft Fabric Deployment
# 📋 Pipeline: PowerBI-Reports-Lifecycle
# 📊 Source Stage Order: 0
# 🔐 Tenant ID: 12345678...
# --------------------------------------------------
# ✅ Successfully authenticated with Microsoft Fabric service
# ✅ Found pipeline: PowerBI-Reports-Lifecycle
# ✅ Found pipeline with ID: abc123def-456...
# 🚀 Deploying from 'Development' to 'Test'
# 📋 Operation ID: operation-456789
# 📊 Operation Status: Executing (Attempt 1/240)
# ⏳ Waiting for operation to complete...
# ✅ Deployment completed successfully!
# 🎉 Deployment completed successfully!
```

**Complete Workflow Test:**

1. **Feature Development**
   ```bash
   ✅ Create feature in Feature Workspace
   ✅ Sync to feature branch
   ✅ Create and merge PR
   ```

2. **Manual DEV Sync**
   ```bash
   ✅ Manually sync DEV workspace
   ✅ Verify latest changes in DEV
   ```

3. **Automated Deployment**
   ```bash
   ✅ GitHub Actions trigger on main branch
   ✅ UAT deployment with approval
   ✅ PROD deployment with approval
   ```

4. **Validation**
   ```bash
   ✅ Verify reports in UAT workspace
   ✅ Validate parameters updated correctly
   ✅ Confirm PROD deployment success
   ```

<p align="center">
   <img src="{{ site.baseurl }}/assets/images/devops/review_deployment_github.png" width="600" alt="GitHub Actions Approval Process" class="zoomable-devops"/>
</p>
<p align="center">
   <strong>Figure: GitHub Actions Approval Process</strong>
</p>

## 7.2 Validation Checklist

**Pre-Deployment Validation:**
- [ ] Service principal authentication working
- [ ] All workspaces assigned to active capacity
- [ ] Deployment pipeline permissions configured
- [ ] GitHub secrets properly set
- [ ] Environment protection rules active

**Post-Deployment Validation:**
- [ ] Reports deployed to correct workspaces
- [ ] Parameters updated for each environment
- [ ] Data connections working in all environments
- [ ] Approval gates functioning correctly
- [ ] Deployment logs available in GitHub Actions

{: .no_toc }
#### Next: [Best Practices & Troubleshooting]({{ site.baseurl }}/docs/DevOps_Best_Practices/) 