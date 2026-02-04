Python Datetime Countdown Experiment
This repository contains a small experiment exploring how to work with
Python’s datetime module to track whether the current date and time
has passed a specified target datetime.

The project demonstrates a common pitfall when comparing datetimes
using exact equality and shows a corrected approach that reliably
detects when a target time is reached.

---

Files

date check_first try.py
An initial trial implementation that continuously compares the current
time to a target datetime.

This version highlights why using exact datetime equality (==) is
unreliable, as datetime.now() includes microseconds, making an exact
match extremely unlikely in a loop.

update.py
An updated and reliable implementation of a real-time countdown timer.

This version:
Uses boundary crossing (<= 0) instead of equality
Displays remaining time in days, hours, minutes, and seconds
Ensures the target time is never missed, even if the loop runs late

---

Concepts Practised
Python datetime and timedelta
Real-time looping with delays
Time comparison pitfalls
Writing readable, human-friendly output
Defensive logic for time-based conditions

---

Notes
This repository is intended as a learning and experimentation project,
not a production-ready scheduler.

---

Requirements
Python 3.x

Note: The initial trial script uses an infinite loop and is intended
for experimentation only. Run it with caution, as it may consume
significant system resources.
