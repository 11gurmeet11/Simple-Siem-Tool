import schedule
import time
from datetime import datetime
from utils import collect_logs, analyze_logs, send_alert
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Function to check logs and send alerts
def job():
    try:
        logs = collect_logs()  # Collect logs
        errors = analyze_logs(logs)  # Analyze logs
        if errors:
            for error in errors:
                send_alert(error)  # Send alerts for each error
        else:
            logging.info(f'{datetime.now()}: No errors found in logs.')
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Schedule the job to run every 5 minutes
schedule.every(5).minutes.do(job)

# Keep the script running
while True:
    try:
        schedule.run_pending()  # Run the scheduled tasks
        time.sleep(1)  # Sleep for a short time to avoid excessive CPU usage
    except KeyboardInterrupt:
        logging.info("Scheduler stopped by user.")
        break
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        break