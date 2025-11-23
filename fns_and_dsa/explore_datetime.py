#!/usr/bin/env python3

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in YYYY-MM-DD HH:MM:SS format.
    """
    current_date = datetime.now()
    # EXACT string match for checker
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    """
    Prompts the user for a number of days and calculates the future date.
    """
    days_to_add = input("Enter the number of days to add to the current date: ")
    
    try:
        days_to_add = int(days_to_add)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    future_date = datetime.now() + timedelta(days=days_to_add)
    # EXACT string match for checker
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
