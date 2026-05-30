# SJTUnotes

Shanghai Jiao Tong University course notes, built with MkDocs Material and deployed to GitHub Pages.

## Preview

Site: https://youyeyejie.github.io/SJTUnotes/

## Features

- Course notes organized by subject
- MathJax support for LaTeX formulas
- Giscus-based comments
- GitHub Pages deployment with GitHub Actions

## Local Development

Install dependencies:

```powershell
pip install -r requirements.txt
```

Start the local server:

```powershell
mkdocs serve
```

Build the static site:

```powershell
mkdocs build
```

## Project Structure

```text
docs/        Markdown source files
overrides/   Material theme overrides
scripts/     Formatting and maintenance scripts
mkdocs.yml   MkDocs configuration
```

## Deployment

This project is deployed with GitHub Pages through GitHub Actions.

Workflow file:

```text
.github/workflows/pages.yml
```

Pushing to `main` triggers a new deployment.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
