import time


def track_time(task):
    print(f"Tracking time for {task}...")
    start_time = time.time()
    input("Press Enter to stop tracking.")
    end_time = time.time()

    total_time = end_time - start_time
    print(f"You spent {total_time / 60:.2f} minutes on {task}.")


track_time("coding practice")
