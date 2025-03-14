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
## `GET /semesters/<semester_id>`

NO REQUEST BODY

Response: `[{"id" : Integer, "semester" : String}, ...]`

Errors: 404 (if semester id does not exist)

## `DELETE /semesters/<semester_id>`

NO REQUEST BODY

Response: 204 (No Content)

Errors: 404 (if semester id wasn't found)

---

# Classes
## `GET /semesters/<semester_id>/classes`

NO REQUEST BODY

Response: `[{"id" : Integer, "title" : String, "credit" : Integer, "subject" : "String"}, ... ]`

Errors: 404 (if semester id is not found)

## `POST /semesters/<semester_id>/classes`

Request Body: `{"title" : String, "credit" : Integer, "subject": String}`

Errors: 404 (if semester id is not found)

Response: class id (Integer)

# Class
## `GET /semesters/<semester_id>/classes/[classes_id]`

NO REQUEST BODY

Response: `{"id" : Integer, "title" : String, "credit" : Integer, "subject": String, "assignments" : [Integer]}`

Errors: 404 (if semester id is not found), 404 (if class id is not found), 500 (if class is not in that semester or semester does not contain that class)

# RemoveClass
## `DELETE /classes/<class_id>`

NO REQUEST BODY

Response: 204 (No Content)

Errors: 404 (if class id wasn't found)

---

# Assignments
## `GET /semesters/<semester_id>/classes/<class_id>/assignments`

NO REQUEST BODY

Response: `[{"id" : Integer, "assignmentType" : String, "expectedTime" : Integer, "dueDate" : DateTimeField, "gradePercentage" : Decimal}, ...]`

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found), 500 (if class is not in that semester or semester does not contain that class)

## `POST /semesters/<semester_id>/classes/<class_id>/assignments`

Request Body: `{"assignmentType" : String, "expectedTime" : Integer, "dueDate" : DateTimeField, "gradePercentage" : Decimal}`

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found), 500 (if class is not in that semester or semester does not contain that class)

Response: assignment id (Integer)

# Assignment
## `GET /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>`

NO REQUEST BODY

Response: `{"assignmentType" : String, "expectedTime" : Integer, "dueDate" : DateTimeField, "gradePercentage" : Decimal}`

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found), 404 (if assignment id wasn't found), 500 (if class is not in that semester or semester does not contain that class), 500 (if assignment is not in that class or class does not contain this assignment)

# RemoveAssignment
## `DELETE /assignments/<assignment_id>`

NO REQUEST BODY

Response: 204 (No Content)

Errors: 404 (if assignment id wasn't found)

---

# Submissions
## `GET /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions`

NO REQUEST BODY

Response: `[{"id" : Integer, "actualTime" : Integer, "expectedGrade" : Integer, "submissionTime" : DateTimeField}, ...]`

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found), 404 (if assignment id wasn't found), 500 (if class is not in that semester or semester does not contain that class), 500 (if assignment is not in that class or class does not contain this assignment)

## `POST /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions`

Request Body: `{"actualTime" : Integer, "expectedGrade" : Integer}`

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found), 404 (if assignment id wasn't found), 500 (if class is not in that semester or semester does not contain that class), 500 (if assignment is not in that class or class does not contain this assignment)

Response: submission id (Integer) + ", " + submission time (DateTime)

# Submission
## `GET /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions/latest`
## `This request gets the "latest" submission`

NO REQUEST BODY

Response: `{"submissionNumber" : Integer, "actualTime" : Integer, "expectedTime" : Integer, "expectedGrade" : Integer, "gradePercentage" : Decimal, "submissionTime" : DateTimeField, "dueDate" : DateTimeField, "assignmentType" : String}`

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found), 404 (if assignment id wasn't found), 404 (there are no submissions for this assignment), 500 (if class is not in that semester or semester does not contain that class), 500 (if assignment is not in that class or class does not contain this assignment)

---

# Feedbacks
## `GET /semesters/<semester_id>/classes/<class_id>/feedback`

NO REQUEST BODY

Response: `[{"id" : Integer, "actualGrade" : Integer, "feedback" : String/Text}, ...]`

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found), 500 (if class is not in that semester or semester does not contain that class)

# Feedback
## `GET /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback`

NO REQUEST BODY

Response: `{"actualGrade" : Integer, "expectedGrade" : Integer, "gradePercentage" : Decimal, "feedback" : String/Text}`

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found), 404 (if assignment id wasn't found), 404 (if feedback does not exist), 500 (if class is not in that semester or semester does not contain that class), 500 (if assignment is not in that class or class does not contain this assignment)

## `POST /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback`


Request Body: `{"actualGrade" : Integer, "feedback" : String/Text}`

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found), 404 (if assignment id wasn't found), 404, (if submission id wasn't found), 500 (if feedback is already created for that assignment), 500 (if class is not in that semester or semester does not contain that class), 500 (if assignment is not in that class or class does not contain this assignment)

Response: feedback id (Integer)

## `PUT /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback`


Request Body: `{"actualGrade" : Integer, "feedback" : String/Text}`

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found), 404 (if assignment id wasn't found), 404 (if feedback has not been created for that assignment), 500 (if class is not in that semester or semester does not contain that class), 500 (if assignment is not in that class or class does not contain this assignment)

Response: feedback id (Integer)

## `PATCH /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback`

Request Body: `{"actualGrade" : Integer}`

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found), 404 (if assignment id wasn't found), 404 (if feedback has not been created for that assignment), 500 (if class is not in that semester or semester does not contain that class), 500 (if assignment is not in that class or class does not contain this assignment)

Response: feedback id (Integer)

# GPA
## `GET /semesters/<semester_id>/GPA`

NO REQUEST BODY

Errors: 404 (if semester id wasn't found), 404 (no feedback for any assignment)

Response: Tentative Calculated GPA (Double from 0.0 -> 4.0)

# ClassGrade
## `GET /classes/<class_id>/grade`

NO REQUEST BODY

Errors: 404 (if class id wasn't found), 404 (no feedback for any assignment)

Response: Tentative Calculated Grade (Double from 0.0 -> 100.0)
- Things to note: People can gain extra credit, figure that out. Also, currently, people can add negative grades.

# AssignmentRecommendation
## `GET /semesters/<semester_id>/recommendation`

NO REQUEST BODY

Errors: 404 (if semester id wasn't found)

Response: Assignment ID or All Completed Message (If there are no active assignments (i.e. no assignments without submissions))

# GradeExpectation
## `GET /semesters/<semester_id>/expectedGrades`

NO REQUEST BODY

Response: `[{"expectedGrade" : Double, "actualGrade" : Double}, ...]`

Errors: 404 (if semester id wasn't found), 404 (if no feedback)

# TimeExpectation
## `GET /semesters/<semester_id>/expectedTimes`

NO REQUEST BODY

Response: `[{"expectedTime" : Integer, "actualTime" : Integer}, ...]`

Errors: 404 (if semester id wasn't found), 404 (if no submissiosn)