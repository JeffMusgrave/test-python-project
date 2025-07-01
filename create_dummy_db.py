"""
Create a dummy SQLite database for testing backup functionality.
"""

import sqlite3
import random
from datetime import datetime, timedelta
import os


def create_dummy_database():
    """Create a test SQLite database with sample data."""
    # Ensure data directory exists
    os.makedirs("/data", exist_ok=True)

    # Connect to database (creates if not exists)
    conn = sqlite3.connect("/data/project.db")
    cursor = conn.cursor()

    # Create tables
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS activity_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action TEXT NOT NULL,
            details TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
    )

    # Insert sample data
    documents = [
        ("Project Overview", "This is a test project for our SaaS platform."),
        ("Meeting Notes", "Discussion about architecture and scalability."),
        (
            "Task List",
            "1. Set up backup system\n2. Test restore process\n3. Monitor performance",
        ),
        ("Research Notes", "Comparing different storage solutions for SQLite backups."),
    ]

    for title, content in documents:
        cursor.execute(
            "INSERT INTO documents (title, content) VALUES (?, ?)", (title, content)
        )

    # Insert settings
    settings = [
        ("theme", "dark"),
        ("language", "en"),
        ("notifications", "enabled"),
        ("auto_save", "true"),
    ]

    for key, value in settings:
        cursor.execute(
            "INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)", (key, value)
        )

    # Insert activity log entries
    actions = [
        "login",
        "create_document",
        "update_settings",
        "export_data",
        "import_data",
    ]
    for i in range(20):
        timestamp = datetime.now() - timedelta(hours=random.randint(1, 168))
        action = random.choice(actions)
        cursor.execute(
            "INSERT INTO activity_log (action, details, timestamp) VALUES (?, ?, ?)",
            (action, f"Test action {i}", timestamp),
        )

    conn.commit()
    conn.close()

    print("Dummy database created at /data/project.db")

    # Show database info
    file_size = os.path.getsize("/data/project.db")
    print(f"Database size: {file_size:,} bytes")


if __name__ == "__main__":
    create_dummy_database()
