Health Tracker Application

This project is a simple Python Tkinter application designed to help users record basic daily health data.
The application stores all entries in a text file and provides features to view records, view monthly data, and display motivational messages.

Features
 -Add daily health records (Date, Steps, Calories, Workout Minutes)
 -View all saved records
 -View last 30 entries (Monthly Records)
 -Display motivational messages
 -Lightweight, easy-to-use Tkinter interface
 -Uses a simple text file for storage


Project Structure
HealthTracker/
│── smallhealthtracker.py
│── data.txt
│── README.md
│── requirements.txt


Technologies Used
 -Python 3
 -Tkinter (GUI)
 -Random module
 -Text file handling



Installation and Usage
1. Clone the repository:
git clone https://github.com/chupkarlakshya/HealthTrackingSystem.git

2. Navigate into the project directory:
cd HealthTrackingSystem

3. Install dependencies:
pip install -r requirements.txt

4. Run the application:
python HealthTrackingSystemr.py

How the Application Works

Users enter:

Date

Steps

Calories

Workout duration

The Add button saves the entry into data.txt in a structured 5-line format:

Date
Steps
Calories
Workout
END


The application supports:

Viewing all records

Viewing the latest 30 entries

Displaying motivational messages

Screenshots

(Add a folder named screenshots/ and include your images there.
You can embed them like this:)

![Screenshot](screenshots/app.png)

Testing

Manual testing of input handling

File creation and reading validation

Testing behavior with empty data file

Verification of monthly record extraction

GUI functionality testing

Future Enhancements

Add graphs or charts

Add editing and deleting record features

Replace text file with SQLite database

Provide weekly and monthly summaries

Improve UI layout and design