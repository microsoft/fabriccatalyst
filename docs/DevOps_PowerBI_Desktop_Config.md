---
layout: page
title: DevOps
subtitle: Power BI Desktop Configuration
menubar: DevOps_docs_menu
show_sidebar: false
toc: true
---

# Part 1: Power BI Desktop Configuration

## 1.1 Enable Preview Features

Power BI Desktop must be configured to support the new .pbip format for seamless Fabric integration.

**Steps:**
1. Open **Power BI Desktop**
2. Navigate to **File → Options and Settings → Options**
3. Go to **Preview Features** section
4. Enable: **"Power BI Project (.pbip) save option"**

<p align="center">
   <img src="{{ site.baseurl }}/assets/images/devops/powerbi_desktop_pbip.png" width="600" alt="Enable Power BI Project (.pbip) Format" class="zoomable-devops"/>
</p>
<p align="center">
   <strong>Figure: Enable Power BI Project (.pbip) Format</strong>
</p>

> **⚠️ Important Notes:**
> - **TMDL and PBIR options**: Visible but should remain **unchecked**
> - **Restart required**: Restart Power BI Desktop after enabling
> - **Compatibility**: .pbip format ensures deployment pipeline compatibility

## 1.2 Configure Multi-Environment Parameters

Configure parameters in **Power Query Editor** to support multiple environments.

> **⚠️ Pro TIP:**
> - **Create a Power BI Template with these parameters to save time on new reports.**

**Step 1: Open Power Query Editor**
1. Click **"Transform Data"** in Power BI Desktop
2. Navigate to **Home → Manage Parameters**

**Step 2: Create Environment Parameter**
```
Name: Environment
Description: Current deployment environment (DEV, UAT, or PROD)
Required: ✅ Checked
Type: Text
Suggested Values: List of values
  - DEV
  - UAT
  - PROD
Current Value: DEV
```

**Step 3: Create Server Parameter**
```
Name: SrvName
Description: Database server name based on environment
Required: ✅ Checked
Type: Text
Suggested Values: Any value
Current Value: dev-server-id.database.fabric.microsoft.com
```

**Step 4: Create Database Parameter**
```
Name: DbName
Description: Database name based on environment
Required: ✅ Checked
Type: Text
Suggested Values: Any value
Current Value: adventureworks-dev-workspace-id
```

<p align="center">
   <img src="{{ site.baseurl }}/assets/images/devops/Manage_parameters_pbi_env.png" width="600" alt="Environment Parameter Configuration" class="zoomable-devops"/>
</p>
<p align="center">
   <strong>Figure: Environment Parameter Configuration</strong>
</p>

**Step 5: Apply Parameters to Data Source**
1. Navigate to your data source query
2. Right-click on **Source step** → **Edit Settings**
3. Configure connection:
   - **Server:** Select `SrvName` parameter
   - **Database:** Select `DbName` parameter
   - **Authentication:** Microsoft account or Organizational account

<p align="center">
   <img src="{{ site.baseurl }}/assets/images/devops/Manage_parameters_pbi_setup_param.png" width="600" alt="Apply Parameters to Data Source" class="zoomable-devops"/>
</p>
<p align="center">
   <strong>Figure: Apply Parameters to Data Source</strong>
</p>

## 1.3 Save as Power BI Project (.pbip)

**Naming Convention:**
```
[ProjectName]_[ReportType]_[Version].pbip
Example: SalesAnalytics_Dashboard_v1.0.pbip
```

**Folder Structure After Save:**
<p align="center">
   <img src="{{ site.baseurl }}/assets/images/devops/folder_structure_pbip.png" width="400" alt="Power BI Project Folder Structure" class="zoomable-devops"/>
</p>
<p align="center">
   <strong>Figure: Power BI Project Folder Structure</strong>
</p>

{: .no_toc }
#### Next: [Fabric Environment Setup]({{ site.baseurl }}/docs/DevOps_Fabric_Environment_Setup/) 