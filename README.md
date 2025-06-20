# SIEM System - Security Information and Event Management (SIEM)

A simple **Security Information and Event Management (SIEM)** system built in Python to monitor logs and send alerts based on certain log patterns. This system can be easily expanded and customized to suit enterprise-level monitoring and alerting needs.

## Features

- **Log collection and analysis**: Automatically collects logs from an SQLite database and analyzes them for specific patterns.
- **Real-time alerts**: Sends email alerts to administrators in case of errors or suspicious log patterns.
- **Automated log processing**: Scheduled log collection and analysis every 5 minutes using `schedule`.
- **Modular and extensible**: Easily configurable for different use cases and scalable for larger systems.

## Installation

### Prerequisites
- Python 3.x
- SQLite (for database)
- Email server for sending alerts (e.g., SMTP server)

### Install dependencies
```bash
pip install schedule smtplib
```

Set up the database
	1.	Create an SQLite database with a logs table:

```
    CREATE TABLE logs (
    id INTEGER PRIMARY KEY,
    log_message TEXT
);
```

Insert some sample logs into the database for testing purposes:
```
INSERT INTO logs (log_message) VALUES ('ERROR: System failure');
INSERT INTO logs (log_message) VALUES ('INFO: System running smoothly');
```

### Configuration

You can configure the system by modifying the config.py file. Here you can set:
	•	DB_PATH: Path to the SQLite database file (default: database.db).
	•	EMAIL_SERVER: SMTP server for sending alerts (e.g., smtp.company.com).
	•	EMAIL_PORT: Port for the SMTP server (default: 587).
	•	SENDER_EMAIL: Email address used to send alerts.
	•	RECEIVER_EMAIL: Email address where alerts will be sent.

### Usage

Running the SIEM system

To start the SIEM system, run the following command:
````
python main.py
````
This will start the SIEM system, which will:
	•	Collect logs from the database every 5 minutes.
	•	Analyze logs for errors or suspicious patterns.
	•	Send email alerts if any issues are detected.


### Email Alerts

Whenever an ERROR log is found, the system will send an email alert to the administrator with the details of the error.

````
siem_project/
│
├── main.py        # Main script for collecting and analyzing logs
├── utils.py       # Utility functions for logging, alerting, and log analysis
├── config.py      # Configuration file for system variables
├── database.db    # SQLite database to store logs
└── logs/          # Directory for logs (optional)
````

### Example

Given this folder structure:
````
Before running:
/siem_project
  ├── main.py
  ├── utils.py
  ├── config.py
  └── database.db
  ````

After running, the system will automatically check for errors in the logs and send email alerts if any ERROR logs are found.

Example log entries:
	•	Log Entry 1: ERROR: System failure
	•	Log Entry 2: INFO: System running smoothly

If the system detects ERROR logs, it will send an alert to the administrator.

### Contributing
We welcome contributions! If you have ideas for improvements, bug fixes, or new features, feel free to submit a pull request.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Disclaimer

This project is provided for educational and research purposes only. The author does not take any responsibility for:
	•	Misuse of the script
	•	Data loss
	•	Encrypted files being unrecoverable due to forgotten passwords
	•	Any damages caused by running or modifying this code

By using this software, you agree to use it at your own risk. No guarantees are made regarding security, performance, or suitability for any specific task.

Do not use this tool on systems or data you do not own or have explicit permission to access.
