from datetime import datetime

time_now = datetime.now()
time_wanted = datetime(2025, 1, 1)


def time_remaining():
    time_remaining = time_wanted - time_now
    print(f"1st January 2025 is in: {time_remaining}")


time_remaining()
