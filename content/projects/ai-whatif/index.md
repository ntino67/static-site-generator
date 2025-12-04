# AI What-If — Health Risk Explorer

AI What-If is a full stack system to estimate heart-disease risk and propose lifestyle changes that reduce it.  
It combines statistical modeling, an HTTP API, and an interactive front-end.

[Demo](https://aiwhatif.nightingaleheart.com/)

---

## Features

- Random Forest model trained on cleaned survey data
- Counterfactual generation: “what should a user change to reduce risk?”
- R API (plumber) exposing prediction and explanations
- React + TypeScript UI for data input and visualization
- Docker/Podman containers for reproducible environments
- Validation, transformation, and error-handling pipelines

---

## Architecture

**Backend (R):**

- Data cleaning scripts
- Model training (Random Forest)
- Prediction API
- Counterfactual engine
- Logging + validation

**Frontend (React):**

- Controlled form for health data
- Risk visualization
- Counterfactual suggestions
- Async requests to the API

**DevOps:**

- Containerized backend
- Containerized frontend
- Shared environment variables
- Reproducible builds

---

## Why this project matters

I built a system that goes from raw data to a real user-facing tool.

This project taught me:

- how statistical models integrate into web software
- how to build an API around a non-traditional back-end
- how to keep a pipeline reproducible with containers
- how to clean and normalize messy real-world data
- how UI and data modeling influence each other

---

## Links

- [Back to Projects](/projects/)
