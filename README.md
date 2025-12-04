# Static Site Generator Starter

A tiny static site generator written in Python. It converts Markdown files in `content/` into HTML files in `docs`, ready to be served by GitHub Pages or any static file host.

This starter is designed to be:

- Cross‑platform (Linux, macOS, Windows)
- Easy to fork / “Use this template”
- Simple to customize

---

## Features

- Write content in Markdown (`.md`)
- Nested folders (e.g. `content/blog/post/index.md`)
- Shared HTML template (`template.html`)
- Static files (CSS, images, etc.) copied from `static/` to `docs/`
- Configurable base path for links and images:
  - Local dev: `/`
  - GitHub Pages: `/static-site-generator/`

---

## Requirements

- Python 3.9+ (3.10+ recommended)
- Git (if you’re using GitHub)

To check your Python version:

```
python --version

# or on Windows:

py --version
```

---

## Project Structure

```
.
├── content/ # Your markdown content (source)
│ └── index.md
├── docs/ # Generated HTML site (output)
├── src/ # Python source code for the generator
│ ├── main.py
│ ├── gencontent.py
│ ├── copystatic.py
│ └── ...
├── static/ # CSS, images, etc. to be copied to docs/
├── template.html # Base HTML template
├── build_local.sh # Local dev build (Linux/macOS)
├── build_local.bat # Local dev build (Windows)
├── build_prod.sh # GitHub Pages build (Linux/macOS)
├── build_prod.bat # GitHub Pages build (Windows)
└── README.md
```

---

## How It Works

1. `src/main.py`:
   - Reads all Markdown files in `content/`
   - Renders them to HTML using `template.html`
   - Writes the output into `docs/` (mirroring the folder structure)
   - Copies everything from `static/` into `docs/`

2. The **base path** (for links and images) is:
   - The first CLI argument to `main.py`, or
   - `/` if none is provided

This starter uses:

- Local dev (root at `/`): basepath = `/`
- GitHub Pages (root at `/static-site-generator/`): basepath = `/static-site-generator/`

---

## Getting Started

### 1. Clone or Use This Template

On GitHub:

- Click **“Use this template”** → “Create a new repository”

Or clone directly:

```
git clone https://github.com/YOUR_USERNAME/static-site-generator.git
cd static-site-generator
```

---

## Local Development

Use the **local** scripts (base path = `/`).

### Linux / macOS

```
chmod +x build_local.sh
./build_local.sh
```

### Windows (cmd)

```
build_local.bat
```

This will:

- Run `python src/main.py /`
- Generate the site into `docs/`

Then open `docs/index.html` in your browser.

---

## Production Build (GitHub Pages)

Use the **prod** scripts (base path = `/static-site-generator/`).

### Linux / macOS

```
chmod +x build_prod.sh
./build_prod.sh
```

### Windows (cmd)

```
build_prod.bat
```

These call:

```
python3 src/main.py /static-site-generator/
```

which prepares the site so links and images work at:

```
https://YOUR_USERNAME.github.io/static-site-generator/
```

---

## Deploying to GitHub Pages

1. Push your repo to GitHub:

```
git add .
git commit -m "Initial commit"
git push -u origin main
```

2. On GitHub, open your repo:
   - Go to **Settings → Pages** (under “Code and automation”)
   - Source: `main` branch
   - Folder: `/docs`
   - Save

3. Run a production build locally:

```
./build_prod.sh # Linux/macOS

# or

build_prod.bat # Windows
```

4. Commit and push the updated `docs/`:

```
git add docs
git commit -m "Build site for GitHub Pages"
git push
```

5. Visit:

```
https://YOUR_USERNAME.github.io/static-site-generator/
```

---

## Customizing the Site

### Content

- Edit `content/index.md` to change the homepage.
- Add more pages, e.g.:

```
content/
about/
index.md
blog/
first-post/
index.md
```

Each `index.md` becomes an `index.html` under `docs/` with the same structure.

### Template

- Edit `template.html` to change the global layout:
  - `<head>` tags
  - Navigation
  - Footer
  - Where `{{ Title }}` and `{{ Content }}` are placed

### Static Assets

- Place CSS, images, fonts, etc. in `static/`
- They will be copied into `docs/` on build.

---

## Scripts Summary

```

# Local dev builds (root = /)

./build_local.sh # Linux/macOS
build_local.bat # Windows

# Production / GitHub Pages builds (root = /static-site-generator/)

./build_prod.sh # Linux/macOS
build_prod.bat # Windows
```

