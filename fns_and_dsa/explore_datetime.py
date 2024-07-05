
import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print("Current Date and Time:", current_date)

def account_future_date():
    try:
        days = int(input("Enter a number of days to add to the current date: "))
        future_date = datetime.datetime.now() + datetime.timedelta(days=days)
        print("Future Date", future_date)
    except ValueError:
        print("Invalid input. Please enter a valid number of days.")

display_current_datetime()
account_future_date()
