# Asteroids — Python Game

Asteroids is a small arcade-style game I built to practice clean game-loop structure, collision handling, and simple 2D rendering.  
The goal was not to recreate the original perfectly, but to understand how these games work under the hood.

[GitHub](https://github.com/ntino67/asteroids)

---

## Features

- Core **game loop** with update + render phases
- Player ship with rotation, acceleration, and inertia
- Screen wrap-around (leaving one edge re-enters on the opposite side)
- Randomly generated asteroids with velocity + direction
- Collision detection (ship–asteroid and bullet–asteroid)
- Basic particle-like explosion effect
- Minimal UI: score, lives, clean black starfield look

---

## Architecture

The game is structured around a few predictable components:

### **Game loop**

Handles:

- input
- physics updates
- collision resolution
- rendering

This separates logic from drawing and keeps each frame consistent.

### **Entities**

- **Ship**
- **Asteroids** (large → medium → small upon destruction)
- **Bullets**

Each entity has:

- position
- velocity
- orientation
- update()
- draw()

### **Collision system**

Axis-aligned radius-based checks for speed and simplicity.

### **Rendering**

Depending on the version you built:

- either Pygame
- or a minimal custom renderer

The focus is on behavior, not polishing graphics.

---

## Why this project matters

It’s a small game, but it introduces several fundamentals that apply to any interactive system:

- consistent time-stepped updates
- state machines (alive, exploding, invulnerable, etc.)
- deterministic physics loops
- clean separation between model and rendering
- debugging moving objects and collision boundaries
- the importance of predictable input handling

Building a game forces you to write code that **reacts** rather than just computes.

---

## What I learned

- How arcade physics differ from real physics
- Why state updates must be decoupled from drawing
- How even simple games require structural discipline
- How to avoid “spaghetti game loops”
- How to design small, composable entity classes

It reinforced the idea that good architecture matters even in tiny projects.

---

## Links

- [Back to Projects](/projects/)
