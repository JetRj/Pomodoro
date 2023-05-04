import time

# Define the durations for work and break periods
WORK_DURATION = 25 * 60  # 25 minutes in seconds
BREAK_DURATION = 5 * 60  # 5 minutes in seconds

def start_timer(duration):
    """Starts a timer for the specified duration in seconds"""
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        time_left = int(end_time - time.time())
        print(f"Time remaining: {time_left // 60:02d}:{time_left % 60:02d}")
        time.sleep(1)
    print("Time's up!")

# Run the Pomodoro cycle
while True:
    print("Starting work period...")
    start_timer(WORK_DURATION)
    print("Time for a break!")
    start_timer(BREAK_DURATION)
