import json
from datetime import datetime, timedelta
from codingTracker import LOG_FILE


def generate_summary(logs, period='daily'):

    if not logs:
        print("No logs found.")
        return

    now = datetime.now()
    total_seconds = 0

    if period == 'daily':
        start_period = now.replace(hour=0, minute=0, second=0, microsecond=0)
    elif period == 'weekly':
        start_period = now - timedelta(days=now.weekday())  # Start of the week
    elif period == 'monthly':
        start_period = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    for log in logs:
        start_time = datetime.strptime(log['start_time'], '%Y-%m-%d %H:%M:%S')
        if start_time >= start_period:
            total_seconds += log['total_time_seconds']

    total_hours = total_seconds / 3600
    print(f"Total time spent on VSCode ({period}): {total_hours:.2f} hours")


def load_logs():
    try:
        with open(LOG_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# Example usage
logs = load_logs()
generate_summary(logs, 'daily')
generate_summary(logs, 'weekly')
generate_summary(logs, 'monthly')
