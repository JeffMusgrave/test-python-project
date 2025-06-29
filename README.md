# Test Python App for Setta SaaS

This is a test Python application for testing GitHub deployments to Fly.io.

## Structure

- `app.py` - FastAPI application with test endpoints
- `requirements.txt` - Python dependencies (includes uvicorn for testing)

Note: No Procfile needed! The Setta platform controls how your app runs.

## How It Works

1. Push this to a GitHub repository (make it public)
2. Use the GitHub URL when creating a new project in Setta
3. The platform will:
   - Clone your repository
   - Install dependencies from requirements.txt
   - Run your app using the configured start command

## Current Test Mode

In test mode, the platform runs:

```bash
uvicorn app:app --host 0.0.0.0 --port 8080
```

## Future Production Mode

When Setta is ready, you'll just need:

**requirements.txt:**

```
setta>=1.0.0
# your other dependencies...
```

The platform will automatically run the `setta` command, which will:

- Find your Python code
- Serve the Setta UI
- Handle all the complexity

No need for:

- Procfile
- Dockerfile
- Web server configuration
- Complex setup

Just Python code + setta in requirements.txt = deployed app! 🚀
