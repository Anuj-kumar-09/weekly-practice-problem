# Problem 1: Top-Scoring Students by Subject using csv (comma-separated values) file
# Write a newthon program that:
# • Reads a file marks.csv containing data in the format:
# • roll_no,name,subject,marks
# • 101,Alice,Math,78
# • 102,Bob,Science,88
# • ...
# • For each subject, find the student(s) with the highest marks.
# • Output results as:
# • Subject: Math → Alice (78)
# • Subject: Science → Bob (88)

import csv
from collections import defaultdict

data = [
    [101, "Alice", "Math", 78],
    [102, "Bob", "Science", 88],
    [103, "Ankit", "Math", 100],
    [104, "Anuj", "Science", 88],
    [105, "Raman", "Math", 100]]

with open('marks.csv', 'w', newline='') as f:
    a= csv.writer(f)
    a.writerows(data)

# Dictionary to store top scorers per subject
top_scorers = defaultdict(list)
max_marks = defaultdict(int)

# Read the CSV file
with open('marks.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        subject = row['subject']
        name = row['name']
        marks = int(row['marks'])

        if marks > max_marks[subject]:
            max_marks[subject] = marks
            top_scorers[subject] = [(name, marks)]
        elif marks == max_marks[subject]:
            top_scorers[subject].append((name, marks))

# Output the results
for subject, students in top_scorers.items():
    names = ', '.join([f"{name} ({marks})" for name, marks in students])
    print(f"Subject: {subject} → {names}")

    