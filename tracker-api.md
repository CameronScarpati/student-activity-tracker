# Tracker API Design

---

# Semesters
## `POST /semesters`

Request Body: `{"semester" : String}`

Response: semester id (Integer)

Errors: 500 (if semester is already created)

## `GET /semesters/[semester_id]`

NO REQUEST BODY

Response: `[{"id" : Integer, "semester" : String, "classes" : [Integer]}, ...]`

Errors: 404 (if semester id does not exist)

## `GET /semesters`

NO REQUEST BODY

Response: `[{"id" : Integer, "semester" : String}, ...]`

---

# Classes
## `POST /semesters/[semester_id]/classes`

Request Body: `{"title" : String, "credit" : Integer, "subject": String}`

Response: class id (Integer)

## `GET /semesters/[semester_id]/classes/[classes_id]`

NO REQUEST BODY

Response: `{"id" : Integer, "title" : String, "credit" : Integer, "subject": String, "assignments" : [Integer]}`

Errors: 404 (if semester id is not found), 404 (if class id is not found), 500 (if class is not in that semester or semester does not contain that class)

Note: assignments contains a list of assignment ids

## `GET /classes`

NO REQUEST BODY

Response: `[{"id" : Integer, "title" : String, "credit" : Integer, "subject" : "String"}, ... ]`

---

# Assignments

## `POST /semesters/[semester_id]/classes/[class_id]/assignments`

Request Body: `{"assignmentType" : String, "expectedTime" : Integer, "dueDate" : DateTimeField, "gradePercentage" : Decimal}`

Response: assignment id (Integer)

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found)

## `GET /semesters/[semester_id]/classes/[class_id]/assignments`

NO REQUEST BODY

Response: `[{"id" : Integer, "assignmentType" : String, "expectedTime" : Integer, "dueDate" : DateTimeField, "gradePercentage" : Decimal}, ...]`

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found), 404 (if class has no current assignments inputed)

## `GET /semesters/[semester_id]/classes/[class_id]/assignments/[assignment_id]`

NO REQUEST BODY

Response: `{"id" : Integer, "assignmentType" : String, "expectedTime" : Integer, "dueDate" : DateTimeField, "gradePercentage" : Decimal}`

Errors: 404 (if semester id wasn't found), 404 (if class id wasn't found), 404 (if assignment id wasn't found), 500 (if assignment is not in that class/semester)