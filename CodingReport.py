import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

LOG_FILE = 'vscode_time_log.json'


def generate_summary(logs, period='daily'):
    if not logs:
        print("No logs found.")
        return {}

    now = datetime.now()
    summary = {}

    if period == 'daily':
        start_period = now.replace(hour=0, minute=0, second=0, microsecond=0)
        for log in logs:
            start_time = datetime.strptime(log['start_time'], '%Y-%m-%d %H:%M:%S')
            if start_time >= start_period:
                date_key = start_time.date()
                if date_key not in summary:
                    summary[date_key] = 0
                summary[date_key] += log['total_time_seconds']

    elif period == 'weekly':
        start_period = now - timedelta(days=now.weekday())  # Start of the week
        for log in logs:
            start_time = datetime.strptime(log['start_time'], '%Y-%m-%d %H:%M:%S')
            if start_time >= start_period:
                date_key = start_time.date()
                week_start = date_key - timedelta(days=date_key.weekday())  # Start of the week
                if week_start not in summary:
                    summary[week_start] = {day: 0 for day in range(7)}
                day_index = (date_key - week_start).days
                summary[week_start][day_index] += log['total_time_seconds']

    elif period == 'monthly':
        start_period = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        for log in logs:
            start_time = datetime.strptime(log['start_time'], '%Y-%m-%d %H:%M:%S')
            if start_time >= start_period:
                date_key = start_time.date()
                month_key = start_time.strftime('%Y-%m')
                week_number = (start_time.day - 1) // 7 + 1
                week_key = f"{month_key}-W{week_number}"
                if week_key not in summary:
                    summary[week_key] = 0
                summary[week_key] += log['total_time_seconds']

    else:
        print("Invalid period specified.")
        return {}

    # Convert total_seconds to hours
    if period == 'weekly':
        for week_start, days in summary.items():
            summary[week_start] = {f"Day {i+1}": hours / 3600 for i, hours in days.items()}
    else:
        summary = {k: v / 3600 for k, v in summary.items()}
    return summary


def load_logs():
    try:
        with open(LOG_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def plot_summary(data, period):
    if period == 'weekly':
        for week_start, days in data.items():
            days_names = list(days.keys())
            values = list(days.values())
            plt.figure(figsize=(12, 8))
            plt.bar(days_names, values, color='skyblue')
            plt.xlabel('Day of Week')
            plt.ylabel('Hours Spent')
            plt.title(f'Time Spent on VSCode ({week_start})')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

    else:
        periods = list(data.keys())
        values = list(data.values())
        plt.figure(figsize=(12, 8))
        plt.bar(periods, values, color='skyblue')
        plt.xlabel('Date/Period')
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
    summary_data = generate_summary(logs, period)
    plot_summary(summary_data, period)


# Example usage
if __name__ == "__main__":
    main()
