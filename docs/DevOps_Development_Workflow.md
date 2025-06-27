---
layout: page
title: DevOps
subtitle: Development Workflow
menubar: DevOps_docs_menu
show_sidebar: false
toc: true
---

# Part 6: Development Workflow

## 6.1 Feature Development Process

**Step 1: Local Development**
1. Create Power BI report in Desktop
2. Configure environment parameters
3. Save as `.pbip` format

**Step 2: Feature Workspace Development**
1. Publish report to Feature Workspace
2. Connect workspace to feature branch
3. Initial sync: Workspace → Git

**Step 3: Git Integration**
1. Make changes in Feature Workspace
2. Regular commits to feature branch
3. Test thoroughly in feature environment

## 6.2 Deployment Process

**Step 4: Pull Request Creation**
1. Create PR: `feature/[name]` → `main`
2. Include detailed description of changes
3. Request code review from team

**Step 5: Code Review & Merge**
1. Team reviews Power BI changes
2. Approve and merge PR to main branch
3. Delete feature branch after merge

**Step 6: DEV Workspace Sync**
> **⚠️ Critical Manual Step**

After PR merge, manually sync DEV workspace:
1. Go to `FABRIC-CATALYST-GH-DEV` workspace
2. Navigate to Git integration
3. Click **"Update all"**

<p align="center">
   <img src="{{ site.baseurl }}/assets/images/devops/ws_dev_sync_git_2.png" width="500" alt="Manual DEV Workspace Sync" class="zoomable-devops"/>
</p>
<p align="center">
   <strong>Figure: Manual DEV Workspace Sync</strong>
</p>

## 6.3 Manual Sync Requirements

**Current Limitation:** Git → Workspace sync is currently manual

**Required Manual Steps:**
1. **After PR merge:** Manually sync DEV workspace from main branch
2. **Before deployment:** Ensure DEV workspace has latest changes
3. **Verification:** Confirm reports updated in DEV workspace

**Future Enhancement:** Microsoft is working on automatic Git → Workspace sync

{: .no_toc }
#### Next: [Testing & Validation]({{ site.baseurl }}/docs/DevOps_Testing_Validation/) 