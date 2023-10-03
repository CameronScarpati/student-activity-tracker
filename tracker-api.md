# Tracker API Design

---

# Semesters
## `GET /semesters`

NO REQUEST BODY

Response: `[{"id" : Integer, "semester" : String}, ...]`

## `POST /semesters`

Request Body: `{"semester" : String}`

Response: semester id (Integer)

Errors: 500 (if semester is already created)

Response: semester id (Integer)

# Semester
## `GET /semesters/[semester_id]`

NO REQUEST BODY

Response: `[{"id" : Integer, "semester" : String, "classes" : [Integer]}, ...]`

Errors: 404 (if semester id does not exist)

---

# Classes
## `GET /classes`

NO REQUEST BODY

Response: `[{"id" : Integer, "title" : String, "credit" : Integer, "subject" : "String"}, ... ]`

## `POST /semesters/[semester_id]/classes`

Request Body: `{"title" : String, "credit" : Integer, "subject": String}`

Response: class id (Integer)

# Class
## `GET /semesters/[semester_id]/classes/[classes_id]`

NO REQUEST BODY

Response: `{"id" : Integer, "title" : String, "credit" : Integer, "subject": String, "assignments" : [Integer]}`

Errors: 404 (if semester id is not found), 404 (if class id is not found), 500 (if class is not in that semester or semester does not contain that class)

Note: assignments contains a list of assignment ids

---

# Assignments
## `GET /semesters/[semester_id]/classes/[class_id]/assignments`

NO REQUEST BODY

Response: `[{"id" : Integer, "assignmentType" : String, "expectedTime" : Integer, "dueDate" : DateTimeField, "gradePercentage" : Decimal}, ...]`

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found), 500 (if class is not in that semester or semester does not contain that class)

## `POST /semesters/[semester_id]/classes/[class_id]/assignments`

Request Body: `{"assignmentType" : String, "expectedTime" : Integer, "dueDate" : DateTimeField, "gradePercentage" : Decimal}`

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found)

Response: assignment id (Integer)

# Assignment
## `GET /semesters/[semester_id]/classes/[class_id]/assignments/[assignment_id]`

NO REQUEST BODY

Response: `{"id" : Integer, "assignmentType" : String, "expectedTime" : Integer, "dueDate" : DateTimeField, "gradePercentage" : Decimal}`

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found), 404 (if assignment id wasn't found), 500 (if class is not in that semester or semester does not contain that class), 500 (if assignment is not in that class or class does not contain this assignment)

---

# Submissions
## `GET /semesters/[semester_id]/classes/[class_id]/assignments/[assignment_id]/submissions`

NO REQUEST BODY

Response: `[{"id" : Integer, "actualTime" : Integer, "expectedGrade" : Integer, "submissionTime" : DateTimeField}, ...]`

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found), 404 (if assignment id wasn't found), 500 (if class is not in that semester or semester does not contain that class), 500 (if assignment is not in that class or class does not contain this assignment)

## `POST /semesters/[semester_id]/classes/[class_id]/assignments/[assignment_id]/submissions`

Request Body: `{"actualTime" : Integer, "expectedGrade" : Integer}`

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found), 404 (if assignment id wasn't found), 500 (if class is not in that semester or semester does not contain that class), 500 (if assignment is not in that class or class does not contain this assignment)

Response: submission id (Integer) + ", " + submission time (DateTime)

# Submission
## `GET /semesters/[semester_id]/classes/[class_id]/assignments/[assignment_id]/submissions/[submission_id]`

NO REQUEST BODY

Response: `{"actualTime" : Integer, "expectedTime" : Integer, "expectedGrade" : Integer, "gradePercentage" : Decimal, "submissionTime" : DateTimeField, "dueDate" : DateTimeField, "assignmentType" : String}`

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found), 404 (if assignment id wasn't found), 404 (if submission id wasn't found), 500 (if class is not in that semester or semester does not contain that class), 500 (if assignment is not in that class or class does not contain this assignment), 500 (if submission is not for that assignment)

---

# Feedbacks
## `GET /semesters/[semester_id]/classes/[class_id]/assignments/[assignment_id]/feedbacks`

NO REQUEST BODY

Response: `[{"id" : Integer, "actualGrade" : Integer, "feedback" : String/Text}, ...]`

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found), 404 (if assignment id wasn't found), 500 (if class is not in that semester or semester does not contain that class), 500 (if assignment is not in that class or class does not contain this assignment)

## `POST /semesters/[semester_id]/classes/[class_id]/assignments/[assignment_id]/feedbacks`


Request Body: `{"actualGrade" : Integer, "feedback" : String/Text}`

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found), 404 (if assignment id wasn't found), 500 (if class is not in that semester or semester does not contain that class), 500 (if assignment is not in that class or class does not contain this assignment)

Response: feedback id (Integer)

# Feedback
## `GET /semesters/[semester_id]/classes/[class_id]/assignments/[assignment_id]/feedbacks/[feedback_id]`

NO REQUEST BODY

Response: `{"actualGrade" : Integer, "feedback" : String/Text}`

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found), 404 (if assignment id wasn't found), 404 (if feedback id wasn't found), 500 (if class is not in that semester or semester does not contain that class), 500 (if assignment is not in that class or class does not contain this assignment), 500 (if feedback is not for that assignment)