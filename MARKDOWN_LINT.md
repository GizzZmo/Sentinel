# Markdown Linting Setup

This repository now includes automated markdown syntax checking using `markdownlint-cli`.

## Configuration

The markdown linting rules are configured in `.markdownlint.json`:

- **Line length**: 120 characters (up to 140 for headings and code blocks)
- **Disabled rules**: 
  - MD026: Trailing punctuation in headings
  - MD033: Inline HTML allowed
  - MD034: Bare URLs allowed
  - MD036: Emphasis as heading allowed

## Usage

### Install markdownlint-cli

```bash
npm install -g markdownlint-cli
```

### Check all markdown files

```bash
markdownlint *.md
```

### Auto-fix issues

```bash
markdownlint --fix *.md
```

### Check specific files

```bash
markdownlint README.md WIKI.md
```

## Status

The following files have been fully linted and corrected:
- ✅ README.md
- ✅ HowTo.md  
- ✅ WIKI.md
- ✅ filoversigt.md

Files with remaining long-line issues (technical content):
- ⚠️ Operatørmanual.md
- ⚠️ example.md
- ⚠️ example_minimal.md

The remaining line-length issues are in technical documentation with complex code examples 
and detailed explanations that are difficult to break without losing readability.