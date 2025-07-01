"""
Test Python app for Setta deployment.
This will be replaced with 'setta' command later.
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import os
import datetime

app = FastAPI()

# Simple HTML template - FIXED: Double curly braces for CSS
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Test Setta App</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
            background: #f5f5f5;
        }}
        .container {{
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #333;
            margin-bottom: 1rem;
        }}
        .info {{
            background: #e3f2fd;
            padding: 1rem;
            border-radius: 4px;
            margin: 1rem 0;
        }}
        .endpoint {{
            background: #f5f5f5;
            padding: 0.5rem;
            margin: 0.5rem 0;
            border-radius: 4px;
            font-family: monospace;
        }}
        .status {{
            color: #4caf50;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Test Setta App</h1>
        <p class="status">✓ Deployment Successful!</p>
        
        <div class="info">
            <h2>Deployment Info</h2>
            <p><strong>Deployed from:</strong> GitHub Repository</p>
            <p><strong>Server Time:</strong> {time}</p>
            <p><strong>Python Version:</strong> {python_version}</p>
            <p><strong>Port:</strong> {port}</p>
        </div>
        
        <h2>Available Endpoints</h2>
        <div class="endpoint">GET /</div>
        <div class="endpoint">GET /health</div>
        <div class="endpoint">GET /api/test</div>
        
        <div class="info" style="background: #fff3cd; margin-top: 2rem;">
            <p><strong>Note:</strong> This is a test deployment. In production, this will run the 'setta' command instead.</p>
        </div>
    </div>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
async def root():
    """Main page."""
    import sys

    return HTML_TEMPLATE.format(
        time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        python_version=sys.version.split()[0],
        port=os.getenv("PORT", "8080"),
    )


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat(),
        "service": "test-setta-app",
    }


@app.get("/api/test")
async def test_api():
    """Test API endpoint."""
    return {
        "message": "Hello from Test Setta App!",
        "timestamp": datetime.datetime.now().isoformat(),
        "environment": {"port": os.getenv("PORT", "8080"), "python_version": "3.11"},
    }


# This section allows running with: python app.py
# But buildpacks will auto-detect and use: uvicorn app:app
if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", "8080"))
    uvicorn.run(app, host="0.0.0.0", port=port)
