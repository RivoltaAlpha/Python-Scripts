import psutil
import time
import json
from datetime import datetime

LOG_FILE = 'vscode_time_log.json'


def log_time(task, start_time, end_time):
    total_time_seconds = (end_time - start_time).total_seconds()
    log_entry = {
        "task": task,
        "start_time": start_time.strftime('%Y-%m-%d %H:%M:%S'),
        "end_time": end_time.strftime('%Y-%m-%d %H:%M:%S'),
        "total_time_seconds": total_time_seconds
    }

    # Read existing logs
    try:
        with open(LOG_FILE, 'r') as f:
            logs = json.load(f)
    except FileNotFoundError:
        logs = []

    # Add new log
    logs.append(log_entry)

    # Write logs back to file
    with open(LOG_FILE, 'w') as f:
        json.dump(logs, f, indent=4)


def track_vscode_time():
    vscode_running = False
    start_time = None

    while True:
        # Check if VSCode is running
        is_running = any("code" in proc.name().lower() for proc in psutil.process_iter())

        if is_running and not vscode_running:
            vscode_running = True
            start_time = datetime.now()
            print(f"VSCode started at {start_time}")

        if not is_running and vscode_running:
            vscode_running = False
            end_time = datetime.now()
            print(f"VSCode stopped at {end_time}")

            log_time("VSCode", start_time, end_time)
            print(f"Total time spent: {(end_time - start_time).total_seconds() / 60:.2f} minutes")

        time.sleep(5)  # Check every 5 seconds


# Example usage
track_vscode_time()


"""
To automate this:
On Windows:
Use Task Scheduler to create a trigger that runs the Python script every time VSCode is opened.
In Task Scheduler, create a new task.
Set the trigger to "On an event".
Choose "Basic" and select an event like the application event for VSCode starting.
Set the action to start the Python script.

Linux/MacOS:
Using cron: You can add a cron job with the
@reboot directive to run the script when the system starts.
crontab -e
@reboot /usr/bin/python3 /path/to/your_script.py

To stop the cron job:
crontab -e
@reboot /usr/bin/python3 /path/to/your_script.py
@reboot exit
"""