# First Post

I built this static site generator to understand everything that happens between Markdown and a deployed website.  
No frameworks, no plugins, no hidden layers — just parsing, transforming, and writing files.

Most tools abstract this away. That’s useful, but it also hides the mechanics.  
I wanted to see the mechanics. I just want to learn at the end of the day.

---

## Why build my own SSG

Three reasons:

1. **Control**  
   I want a portfolio where nothing is accidental. No CSS I didn’t write, no JavaScript I didn’t ask for, no build pipeline I can’t explain.

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

There’s no configuration layer. No theme system. No plugins.  
Just functions that do exactly what they say.

---

## What I learned

- A static site is just a directory structure and predictable URLs
- The hardest part of Markdown is not the syntax — it’s the edge cases
- Good CSS matters more when the HTML is minimal
- Writing a generator forces a higher level of discipline in how pages are organized

This project made me rethink how much tooling I actually need for personal projects.

---

## What’s next

I’ll keep extending the generator as the site grows:  
more content types, better routing, maybe metadata blocks.  
But the goal stays the same: understand every layer.

For now, it’s enough. The site builds, the pages load, and the system is mine.
