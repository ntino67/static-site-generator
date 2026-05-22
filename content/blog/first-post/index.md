# First Post

I built this static site generator to understand everything that happens between Markdown and a deployed website.

One thing that I really try to strive to is reducing noise, that's why I more often than not choose the rawest experience. Neovim config, CLI first, simplest tools first.
I feel like most of our tools nowadays are bloated and solving problems 99% people don't have.

---

## Why build my own SSG

Three reasons:

1. **Control**  
   I want a portfolio where nothing is accidental. No CSS I didn’t write, no JavaScript I didn’t ask for, no build pipeline I can’t explain.
   THIS is something I did and I know HOW this works, I feel like this is very important.

2. **Understanding**  
   Turning Markdown into HTML is a finite sequence of steps:
   - break into blocks
   - classify block types
   - parse inline formatting
   - generate nodes
   - assemble pages
   - apply templates

3. **Simplicity**  
   Existing SSGs solve problems I don’t have. I just want Markdown → HTML → clean pages.

---

## What the generator does

- Converts Markdown into a tree of HTML nodes
- Handles headings, paragraphs, code blocks, quotes, lists
- Handles inline bold, italics, and code spans
- Wraps content in a template
- Outputs a full static site folder

---

## What I learned

- A static site is just a directory structure and predictable URLs
- The hardest part of Markdown is not the syntax, it’s the edge cases
- Good CSS matters more when the HTML is minimal
- Writing a generator forces a higher level of discipline in how pages are organized

This project made me rethink how much tooling I actually need for personal projects.

---

## What's next

Trying to keep it updated as much as I can.
