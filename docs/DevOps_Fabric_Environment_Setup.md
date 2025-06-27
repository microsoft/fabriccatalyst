---
layout: page
title: DevOps
subtitle: Fabric Environment Setup
menubar: DevOps_docs_menu
show_sidebar: false
toc: true
---

# Part 2: Microsoft Fabric Environment Setup

## 2.1 Enable Git Integration in Fabric

### Tenant Settings Configuration

**Option 1: Tenant-Wide Settings**
1. Navigate to **Microsoft Fabric Admin Portal**
2. Go to **Tenant Settings**
3. Enable **"Users can synchronize workspace items with their Git repositories"**

**Option 2: Capacity-Specific Settings (Recommended)**
1. Navigate to **Capacity Settings**
2. Select your Fabric capacity
3. Go to **Delegated Tenant Settings**
4. Configure Git integration settings

<p align="center">
   <img src="{{ site.baseurl }}/assets/images/devops/Tenant_setting_git.png" width="500" alt="Tenant Git Integration Settings" class="zoomable-devops"/>
</p>
<p align="center">
   <strong>Figure: Tenant Git Integration Settings</strong>
</p>

**Required Settings Configuration:**
```
✅ Users can synchronize workspace items with their Git repositories
✅ Users can sync workspace items with GitHub repositories  
✅ Users can export items to Git repositories in other geographical locations
✅ Users can export workspace items with applied sensitivity labels to Git repositories
✅ Users can create Fabric items
```

<p align="center">
   <img src="{{ site.baseurl }}/assets/images/devops/Capacity_setting_git.png" width="500" alt="Capacity Git Integration Settings" class="zoomable-devops"/>
</p>
<p align="center">
   <strong>Figure: Capacity Git Integration Settings</strong>
</p>

### Workspace Creation Settings
**Tenant-Level Configuration Required:**
<p align="center">
   <img src="{{ site.baseurl }}/assets/images/devops/ws_settings_tenant.png" width="500" alt="Workspace Creation Settings" class="zoomable-devops"/>
</p>
<p align="center">
   <strong>Figure: Workspace Creation Settings</strong>
</p>

## 2.2 Create Workspace Structure

Create workspaces following this naming convention:

<p align="center">
   <img src="{{ site.baseurl }}/assets/images/devops/ws_config_fabric.png" width="600" alt="Workspace Structure Overview" class="zoomable-devops"/>
</p>
<p align="center">
   <strong>Figure: Workspace Structure Overview</strong>
</p>

**Workspace Configuration:**

| Workspace Name | Purpose | Git Connection | Capacity Required |
|----------------|---------|----------------|-------------------|
| `FABRIC-CATALYST-GH-FEATURE` | Feature development | Feature branches | ✅ Yes |
| `FABRIC-CATALYST-GH-DEV` | Main development | Main branch | ✅ Yes |
| `FABRIC-CATALYST-GH-STG` | UAT testing | Pipeline managed | ✅ Yes |
| `FABRIC-CATALYST-GH-PROD` | Production | Pipeline managed | ✅ Yes |

## 2.3 Connect Workspaces to Git

### Connect DEV Workspace to Main Branch

1. Navigate to **DEV Workspace Settings**
2. Select **Git Integration** tab
3. Click **Connect to Git**

**Configuration:**
```
Git provider: GitHub
Organization: [your-github-org]
Repository: [your-repo-name]
Branch: main
Folder: / (root)
```

<p align="center">
   <img src="{{ site.baseurl }}/assets/images/devops/git_integration_dev_ws.png" width="500" alt="DEV Workspace Git Integration" class="zoomable-devops"/>
</p>
<p align="center">
   <strong>Figure: DEV Workspace Git Integration</strong>
</p>

### Connect Feature Workspace to Feature Branch

1. Navigate to **Feature Workspace Settings**
2. Select **Git Integration** tab
3. Click **Connect to Git**

**Configuration:**
```
Git provider: GitHub
Organization: [your-github-org]
Repository: [your-repo-name]
Branch: feature/[feature-name]
Folder: / (root)
```

<p align="center">
   <img src="{{ site.baseurl }}/assets/images/devops/git_integration_feature_ws.png" width="500" alt="Feature Workspace Git Integration" class="zoomable-devops"/>
</p>
<p align="center">
   <strong>Figure: Feature Workspace Git Integration</strong>
</p>

{: .no_toc }
#### Next: [Git Repository Configuration]({{ site.baseurl }}/docs/DevOps_Git_Repository_Config/) 