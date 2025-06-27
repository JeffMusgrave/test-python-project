"""
Simple test app for Setta SaaS deployment testing.
"""

from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Hello from Setta test project!",
        "app_name": os.getenv("FLY_APP_NAME", "local"),
        "region": os.getenv("FLY_REGION", "local"),
    }


@app.get("/health")
async def health():
    return {"status": "healthy", "app": "test-setta-dummy"}


def calculate_sum(a: int, b: int) -> int:
    """Test function that Setta would discover."""
    return a + b


def process_data(input_text: str, multiplier: float = 1.5) -> str:
    """Another test function for Setta."""
    return f"Processed: {input_text} x {multiplier}"
