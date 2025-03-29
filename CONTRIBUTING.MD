# Contributing to Fabric Catalyst

Thank you for your interest in contributing to this project! This guide will help you understand how to contribute effectively and ensure a smooth collaboration.

## About the Project

This project generates runtime pages using **Jekyll** and **Ruby**. Jekyll is a static site generator that transforms Markdown files into a fully functional website. The workflow automates the build and deployment process using GitHub Actions. Here's a brief overview of the process:

1. **Build**: The workflow installs Ruby dependencies, sets up Jekyll, and builds the site into the `_site` directory.
2. **Deploy**: The built site is uploaded as an artifact and deployed to GitHub Pages.

The workflow file responsible for this process is located at `.github/workflows/jekyll-build-deploy.yml`.

## How to Contribute

We welcome contributions of all kinds, from bug fixes to new features. Please follow these steps to contribute:

1. **Fork the Repository**: Create your own copy of the repository by forking it.
2. **Clone the Repository**: Clone your forked repository to your local machine.
   ```bash
   git clone https://github.com/your-username/fabriccatalyst.git
   ```
3. **Install Dependencies**: Ensure you have Ruby installed and run:
   ```bash
   bundle install
   ```
4. **Make Changes**: Implement your changes while following the project's structure and guidelines.
5. **Test Your Changes**: Run Jekyll locally to test your changes:
   ```bash
   bundle exec jekyll serve
   ```
   Open `http://localhost:4000` in your browser to preview the site.
6. **Commit and Push**: Commit your changes with a clear and concise message, then push them to your fork.
7. **Create a Pull Request**: Open a pull request to the main repository and describe your changes.

## Do's and Don'ts

### ✅ Do
- **Keep short commits**: Write concise and meaningful commit messages.
- **Check issues before creating a new one**: Avoid duplicates by reviewing existing issues.
- **Follow our patterns and code of conduct**: Maintain consistency and adhere to the project's guidelines.
- **Follow the writing structure of this project**: Ensure your contributions align with the existing content style.

### ❌ Don't
- **Submit large, unstructured commits**: Break down your changes into smaller, logical commits.
- **Ignore existing issues**: Always check if your contribution addresses an open issue.
- **Disregard the project's guidelines**: Respect the established patterns and code of conduct.
- **Introduce inconsistent writing styles**: Maintain the tone and structure of the project.

## Need Help?

If you have any questions or need assistance, feel free to open an issue or reach out to the maintainers.

Happy contributing!
