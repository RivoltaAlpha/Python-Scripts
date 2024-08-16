import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

LOG_FILE = 'vscode_time_log.json'


def generate_summary(logs, period='daily'):
    if not logs:
        print("No logs found.")
        return 0

    now = datetime.now()
    total_seconds = 0

    if period == 'daily':
        start_period = now.replace(hour=0, minute=0, second=0, microsecond=0)
    elif period == 'weekly':
        start_period = now - timedelta(days=now.weekday())  # Start of the week
    elif period == 'monthly':
        start_period = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    else:
        print("Invalid period specified.")
        return 0

    for log in logs:
        start_time = datetime.strptime(log['start_time'], '%Y-%m-%d %H:%M:%S')
        if start_time >= start_period:
            total_seconds += log['total_time_seconds']

    total_hours = total_seconds / 3600
    return total_hours


def load_logs():
    try:
        with open(LOG_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def plot_summary(data, period):
    periods = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.bar(periods, values, color='skyblue')
    plt.xlabel('Period')
    plt.ylabel('Hours Spent')
    plt.title(f'Time Spent on VSCode ({period.capitalize()})')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    period = input(
        "Enter the period for which you want to generate the report (daily, weekly, monthly): ").strip().lower()

    if period not in ['daily', 'weekly', 'monthly']:
        print("Invalid period specified. Please choose from 'daily', 'weekly', or 'monthly'.")
        return

    logs = load_logs()
    hours = generate_summary(logs, period)

    summary_data = {period.capitalize(): hours}

    plot_summary(summary_data, period)


# Example usage
if __name__ == "__main__":
    main()
