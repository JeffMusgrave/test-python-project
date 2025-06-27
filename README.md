# Test Setta Dummy Project

A simple FastAPI project for testing Setta SaaS deployment from GitHub.

## What is this?

This is a minimal Python project used to test deploying GitHub repositories to Setta Cloud. It simulates what a real user's Python project might look like.

## Structure

- `app.py` - Simple FastAPI application with test endpoints
- `requirements.txt` - Python dependencies (FastAPI and uvicorn)

## Functions for Setta

When Setta is added to this project, it would discover these functions:

- `calculate_sum(a: int, b: int)` - Adds two numbers
- `process_data(input_text: str, multiplier: float)` - Processes text with a multiplier

## Running Locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Then visit http://localhost:8000
