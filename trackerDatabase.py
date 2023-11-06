from peewee import *

studentActivityTracker_DB = SqliteDatabase("trackerDatabase.db")

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
    semester_id = ForeignKeyField(SemesterDB, backref = "assignments")
    class_id = ForeignKeyField(ClassDB, backref = "assignments")
    id = AutoField()
    assignmentType = CharField()
    expectedTime = IntegerField()
    dueDate = DateTimeField()
    gradePercentage = DoubleField()
    
class SubmissionDB(BaseModel):
    semester_id = ForeignKeyField(SemesterDB, backref = "submissions")
    class_id = ForeignKeyField(ClassDB, backref = "submissions")
    assignment_id = ForeignKeyField(AssignmentDB, backref = "submissions")
    id = AutoField()
    actualTime = IntegerField()
    expectedGrade = DoubleField()
    submissionTime = DateTimeField()

class FeedbackDB(BaseModel):
    semester_id = ForeignKeyField(SemesterDB, backref = "feedbacks")
    class_id = ForeignKeyField(ClassDB, backref = "feedbacks")
    assignment_id = ForeignKeyField(AssignmentDB, backref = "feedbacks")
    id = AutoField()
    feedback = TextField()
    actualGrade = DoubleField()

if __name__ == "__main__":
    pass