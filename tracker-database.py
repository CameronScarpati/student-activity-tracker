from peewee import *

studentActivityTracker_DB = SqliteDatabase("student-activity-tracker.db")

class BaseModel(Model):
    class Meta:
        database = studentActivityTracker_DB

class SemesterDB(BaseModel):
    id = AutoField()
    semester = CharField(unique = True)

class ClassDB(BaseModel):
    semester_id = ForeignKeyField(SemesterDB, backref = "classes")
    id = AutoField()
    title = CharField()
    credit = IntegerField()
    subject = CharField()

class AssignmentDB(BaseModel):
    # Creation
    semester_id = ForeignKeyField(SemesterDB, backref = "assignments")
    class_id = ForeignKeyField(ClassDB, backref = "assignments")
    id = AutoField()
    assignmentType = CharField()
    expectedTime = IntegerField()
    dueDate = DateTimeField()

    # Submission
    actualTime = IntegerField()
    expectedGrade = IntegerField()

    # Graded
    actualGrade = IntegerField()

class FeedbackDB(BaseModel):
    semester_id = ForeignKeyField(SemesterDB, backref = "feedbacks")
    class_id = ForeignKeyField(ClassDB, backref = "feedbacks")
    assignment_id = ForeignKeyField(AssignmentDB, backref = "feedbacks")
    id = AutoField()
    feedback = TextField()

if __name__ == "__main__":
    pass