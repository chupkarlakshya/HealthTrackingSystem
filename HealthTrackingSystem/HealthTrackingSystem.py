import tkinter as tk
import random

fname = "data.txt"

win = tk.Tk()
win.title("Health Tracker")

# input fields
tk.Label(win, text="Date (YYYY-MM-DD)").pack()
date_entry = tk.Entry(win)
date_entry.pack()

tk.Label(win, text="Steps").pack()
steps_entry = tk.Entry(win)
steps_entry.pack()

tk.Label(win, text="Calories").pack()
cal_entry = tk.Entry(win)
cal_entry.pack()

tk.Label(win, text="Workout (minutes)").pack()
work_entry = tk.Entry(win)
work_entry.pack()

# output box
txt = tk.Text(win)
txt.pack()


# ADD RECORD
def Add():
    d = date_entry.get()
    s = steps_entry.get()
    c = cal_entry.get()
    w = work_entry.get()

    if d and s and c and w:
        f = open(fname, "a")
        f.write(d + "\n")
        f.write(s + "\n")
        f.write(c + "\n")
        f.write(w + "\n")
        f.write("END\n")
        f.close()

        txt.delete("1.0", tk.END)
        txt.insert(tk.END, "Saved\n")


tk.Button(win, text="Add", command=Add).pack()


# VIEW RECORDS (SAFE)
def View_Records():
    txt.delete("1.0", tk.END)

    try:
        lines = open(fname).readlines()
    except:
        txt.insert(tk.END, "No data\n")
        return

    record = []

    for line in lines:
        line = line.strip()

        if line == "END":
            if len(record) == 4:
                txt.insert(tk.END, "Date: " + record[0] + "\n")
                txt.insert(tk.END, "Steps: " + record[1] + "\n")
                txt.insert(tk.END, "Calories: " + record[2] + "\n")
                txt.insert(tk.END, "Workout: " + record[3] + " minutes\n")
                txt.insert(tk.END, "-------------------\n")
            record = []
        else:
            record.append(line)


tk.Button(win, text="View Records", command=View_Records).pack()


# MONTHLY RECORDS (SAFE VERSION)
def Monthly_Records():
    txt.delete("1.0", tk.END)

    try:
        lines = open(fname).readlines()
    except:
        txt.insert(tk.END, "No data\n")
        return

    records = []
    record = []

    for line in lines:
        line = line.strip()

        if line == "END":
            if len(record) == 4:
                records.append(record)
            record = []
        else:
            record.append(line)

    last30 = records[-30:]

    if not last30:
        txt.insert(tk.END, "Not enough data\n")
        return

    for r in last30:
        txt.insert(tk.END, "Date: " + r[0] + "\n")
        txt.insert(tk.END, "Steps: " + r[1] + "\n")
        txt.insert(tk.END, "Calories: " + r[2] + "\n")
        txt.insert(tk.END, "Workout: " + r[3] + " minutes\n")
        txt.insert(tk.END, "-------------------\n")


tk.Button(win, text="Monthly Records", command=Monthly_Records).pack()


# MOTIVATION FEATURE
messages = [
    "Great job! Keep going!",
    "Small steps every day make big changes!",
    "You are improving! Keep it up!",
    "You can do this!",
    "Proud of you for tracking your health!",
    "Stay active and stay healthy!",
    "Consistency wins!",
    "Believe in yourself!"
]

def Motivation():
    txt.delete("1.0", tk.END)
    msg = random.choice(messages)
    txt.insert(tk.END, msg + "\n")


tk.Button(win, text="Motivation", command=Motivation).pack()

# run window
win.mainloop()
