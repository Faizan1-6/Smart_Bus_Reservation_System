# Smart Bus Ticket Booking & Reservation System

A beginner-friendly Python 3 console application based on the supplied Smart Bus Reservation System PRD.

## Requirements

- Python 3
- No external packages are needed.
- Works in Windows Terminal, Command Prompt, PowerShell, VS Code, or Cursor.

## Files

- `main.py` — complete runnable application.
- `test_cases.txt` — manual testing checklist and expected results.
- `screenshots/README.md` — instructions for taking genuine screenshots of your own run.

## How to run on Windows

1. Download and extract `Smart_Bus_Reservation_System.zip`.
2. Open the extracted `Smart_Bus_Reservation_System` folder.
3. Click the folder address bar in File Explorer, type `cmd`, and press Enter. Alternatively, open this folder in VS Code/Cursor and choose **Terminal → New Terminal**.
4. Check Python is installed:

   ```bash
   python --version
   ```

   If that command is not recognized, try:

   ```bash
   py --version
   ```

5. Run the application:

   ```bash
   python main.py
   ```

   If your system uses the `py` launcher, run:

   ```bash
   py main.py
   ```

6. Use the numbered menu. Choose option `9` to exit.

## Main menu

1. View Available Routes
2. Search for a Route
3. Book a Ticket
4. View My Bookings
5. Cancel a Booking
6. View Seat Availability
7. Generate Booking Report
8. View Route Schedule
9. Exit

**Menu note:** The supplied PRD lists Exit as option 8 but also requires a Route Schedule feature without assigning it a menu number. This implementation exposes the required schedule as option 8 and uses option 9 for Exit, so both required actions are accessible.

## Sample booking walkthrough

1. Run `python main.py`.
2. Enter `1` to view routes.
3. Enter `3` to book a ticket.
4. Example input:
   - Passenger name: `Ahmed`
   - Passenger age: `24`
   - Route ID: `R101`
   - Number of seats: `2`
5. Expected result: booking ID `B1001`, fare per seat Rs. 1,200, total fare Rs. 2,400, and R101 availability drops from 40 to 38.
6. Enter `4` to see booking history.
7. Enter `5`, then `B1001`, to cancel it. R101 availability should return to 40.
8. Try cancelling `B1001` again. It must not restore seats a second time.
9. Enter `7` to generate a report. Cancelled fares must not count as confirmed revenue.

The example assumes a fresh program run. Booking records and route seat counts are held in memory only.

## Important limitation

This is a console application, not a website or mobile app. It has no database, login, payment gateway, or persistent storage. Closing the program clears bookings and resets the sample seat counts.

## Python concepts demonstrated

`print`, `input`, variables, strings, integers, lists, dictionaries, tuples, sets, `if/elif/else`, nested conditions, `for`, nested loops, `for-else`, `while`, `enumerate`, `break`, `continue`, input validation, and fare calculations.

## Before submission

- Run the application and complete the test cases in `test_cases.txt`.
- Fill in the Actual Result and Pass/Fail columns based on what really happens on your computer.
- Take genuine screenshots of the route listing, a successful booking, a cancellation, and the report. Do not claim a screenshot or test was completed unless you actually did it.
- Make sure you can explain the booking and cancellation logic in your own words.
