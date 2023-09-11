# Tracker Database Design

---

### Semesters

1. Semester (Date in YYYY Fall/Winter/Spring/Summer)
    2. Classes (All Classes Listed Under a Semester)

---

### Classes

1. Name of the Class (String &rarr; "Name")
2. Major Class (boolean &rarr; True/False)
3. How Many Credits (int &rarr; 1-4)
4. Subject (String &rarr; "Subject")
5. Assignments (All Assignments Listed Under a Specific Class)

---

### Assignments

1. Name of the Assignment
2. Assignment Type (String &rarr; "Quiz/Project/Paper/Homework(General)")
3. Expected Time? (int &rarr; "Minutes")
4. Due Date (Date in MM/DD/YYYY)
5. Grade Percentage in Syllabus (Double &rarr; 0.XX)

*&darr; Once the assignment is completed &darr;*

This is all under a specific assignment.
- Actual Time Taken
- Expected Grade

*&darr; Once the assignment is graded &darr;*

This is all under a specific assignment.
- Actual Grade

---

### Feedback

1. Feedback from teacher (String)