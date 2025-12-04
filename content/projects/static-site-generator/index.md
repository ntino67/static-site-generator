# Static Site Generator — Python

This portfolio is built with a custom static site generator I wrote from scratch.  
The goal was simple: understand every step between Markdown and a deployed website.

[GitHub](https://github.com/ntino67/static-site-generator)

---

## Features

- Block-level Markdown parsing: paragraphs, headings, quotes, code blocks, lists
- Inline parsing: bold, italics, code spans
- HTML tree construction (ParentNode, LeafNode)
- Template injection (`{{ content }}`)
- Clean URL structure (`/page/` → `/page/index.html`)
- Predictable output folder structure
- No frameworks, no plugins, no magic

---

## Why build my own generator

- Full control over how pages are built
- No dependency on third-party themes or build systems
- Transparent, minimal pipeline
- Ability to extend the system without breaking anything

It also forces the site’s design to stay **intentional**.

---

## Pipeline

1. Load Markdown file
2. Split into logical blocks
3. Determine each block’s type
4. Parse inline formatting
5. Build an HTML node tree
6. Inject into the HTML template
7. Write clean `index.html` files into output directories

The entire system stays readable and modifiable.

---

## What I learned

- HTML doesn’t need complexity if the structure is predictable
- A generator’s real job is not “format conversion” but “site architecture”
- Clean URLs and consistent folders simplify everything
- CSS becomes easier when HTML is minimal

---

## Links

- [Back to Projects](/projects/)
