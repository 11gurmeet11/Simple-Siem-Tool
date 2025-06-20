import os

# Database path
DB_PATH = os.getenv('DB_PATH', 'default_db_path')  # default if variable not exist

# Email configuration
EMAIL_SERVER = os.getenv('EMAIL_SERVER', 'smtp.example.com')
EMAIL_PORT = os.getenv('EMAIL_PORT', '587')  # Get as string first
try:
    EMAIL_PORT = int(EMAIL_PORT)  # Convert to integer
except ValueError:
    print("Error: EMAIL_PORT should be a valid integer. Using default 587.")
    EMAIL_PORT = 587  # Default port if invalid value

SENDER_EMAIL = os.getenv('SENDER_EMAIL', 'your_email@example.com')
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL', 'receiver_email@example.com')