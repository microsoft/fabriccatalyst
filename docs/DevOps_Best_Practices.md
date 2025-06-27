---
layout: page
title: DevOps
subtitle: Best Practices & Troubleshooting
menubar: DevOps_docs_menu
show_sidebar: false
toc: true
---

# Benefits & Best Practices

## Key Benefits

Your implementation provides:

- ✅ **Complete Automation:** End-to-end pipeline from development to production
- ✅ **Version Control:** Full Git-based change tracking and collaboration
- ✅ **Approval Gates:** Manual approvals for UAT and PROD deployments
- ✅ **Environment Isolation:** Separate workspaces for each deployment stage
- ✅ **Parameter Management:** Automatic environment-specific configuration
- ✅ **Audit Trail:** Complete deployment history in GitHub Actions
- ✅ **Rollback Capability:** Git-based version management and rollback

## Development Best Practices

### 1. Feature Development
- Always develop in feature workspaces connected to feature branches
- Use descriptive branch names: `feature/financial-dashboard-v2`
- Test thoroughly before creating pull requests

### 2. Git Workflow
- Use Pull Requests for all changes to main branch
- Include detailed commit messages for better tracking
- Review changes before approving PRs

### 3. Manual Sync Management
- Always manually sync DEV workspace after PR merge
- Verify changes are reflected before triggering deployments
- Document sync requirements for team

## Security Best Practices

### 1. Secrets Management
- Never store sensitive information in Git
- Use GitHub secrets for authentication
- Rotate service principal secrets regularly (24-month expiry)

### 2. Access Control
- Review workspace permissions periodically
- Use different approvers for UAT and PROD
- Implement principle of least privilege

### 3. Environment Protection
- Configure appropriate approval gates
- Use wait timers for production deployments
- Monitor deployment activities

## Operational Best Practices

### 1. Deployment Management
- Configure parameter rules after first deployment
- Monitor capacity usage during deployments
- Schedule deployments during low-usage periods

### 2. Pipeline Maintenance
- Keep deployment pipeline and workspaces in sync
- Regular testing of approval processes
- Monitor GitHub Actions workflow health

---

# Troubleshooting

## Common Issues & Solutions

| Issue | Symptoms | Solution |
|-------|----------|----------|
| **Authentication Fails** | Service principal can't access Fabric | Check credentials and permissions in Azure AD |
| **Pipeline Not Found** | GitHub Actions can't find pipeline | Verify pipeline name and service principal access |
| **Git Sync Fails** | Workspace won't sync with repository | Check Git connection and branch permissions |
| **DEV Workspace Outdated** | Old reports in DEV after PR merge | Manually sync DEV workspace from main branch |
| **Deployment Hangs** | Pipeline deployment stuck | Verify workspace capacity is active |
| **Parameters Not Updated** | Wrong environment values | Configure parameter rules after first deployment |
| **Approval Not Triggered** | No approval request in GitHub | Check environment protection rules |

## Debugging Steps

### For Authentication Issues:
1. Verify service principal credentials in GitHub secrets
2. Check API permissions in Azure AD
3. Confirm admin consent granted
4. Test authentication locally

### For Deployment Issues:
1. Check GitHub Actions logs
2. Verify workspace capacity status
3. Confirm pipeline permissions
4. Review parameter rule configuration

### For Git Sync Issues:
1. Check workspace Git connection
2. Verify branch permissions
3. Confirm repository access
4. Review authentication tokens

## Support Resources

### Microsoft Resources:
- [Fabric REST API Documentation](https://learn.microsoft.com/en-us/rest/api/fabric/)
- [Power BI Deployment Pipelines](https://learn.microsoft.com/en-us/power-bi/create-reports/deployment-pipelines-overview)
- [Fabric Git Integration](https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration)

### GitHub Resources:
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Environment Protection Rules](https://docs.github.com/en/actions/deployment/targeting-different-environments)

### Azure Resources:
- [Service Principal Setup](https://learn.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal)
- [Azure CLI Reference](https://docs.microsoft.com/en-us/cli/azure/)

{: .no_toc }
#### Next: [Case Studies]({{ site.baseurl }}/docs/DevOps_Case_Studies/) 