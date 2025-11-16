# daily_reminder.py
# A simple daily reminder program using match-case, if statements, and loops.

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task based on priority using match-case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# Adjust reminder based on time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder = f"Note: {reminder}. Consider completing it when you have free time."

# Display the final reminder
print(f"\nReminder: {reminder}")
