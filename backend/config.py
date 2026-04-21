import os

# Environment configuration for Kenosis project

class Config:
    CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY', 'default_claude_api_key')
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///default.db')
    # Add other settings here
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    # Example for more configurations
    # PORT = os.getenv('PORT', 5000)  

# Load environment variables

