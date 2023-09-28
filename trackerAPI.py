from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from trackerDatabase import *

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("semester")
parser.add_argument("title")
parser.add_argument("credit")
parser.add_argument("subject")
parser.add_argument("message")
parser.add_argument("assignmentType")
parser.add_argument("expectedTime")
parser.add_argument("dueDate")
parser.add_argument("gradePercentage")

studentActivityTracker_DB.connect()
studentActivityTracker_DB.create_tables([SemesterDB, ClassDB, AssignmentDB, FeedbackDB])

class Semesters(Resource):
    def get(self):
        semesters = []

        for semester in SemesterDB.select():
            semesters.append({"id" : semester.id, "semester" : semester.semester})

        return semesters

    def post(self):
        args = parser.parse_args()
        id = SemesterDB.select().count() + 1

        try:
            SemesterDB.create(id = int(id), semester = args["semester"])
        except BaseException:
            abort(500, message = "This semester {} has already been created.".format(args["semester"])
                   + " Please try another.")

        return int(id), 201
    
class Semester(Resource):
    def get(self, semester_id: int):
        if int(semester_id) > SemesterDB.select().count() or int(semester_id) < 1:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")

        foundSemester = SemesterDB.get(SemesterDB.id == int(semester_id))

        classes = []
        for aClass in ClassDB.select():
            if aClass.semester_id.id == int(semester_id):
                classes.append(aClass.id)

        return {"id" : int(semester_id), "semester" : foundSemester.semester, "classes" : classes}, 200

class Classes(Resource):
    def get(self, semester_id: int):
        classes = []
        for aClass in ClassDB.select().where(ClassDB.semester_id == int(semester_id)):
            classes.append({"id" : aClass.id, "title" : aClass.title, "credit" : aClass.credit, "subject" : aClass.subject})
        
        return classes
    
    def post(self, semester_id: int):
        args = parser.parse_args()

        id = ClassDB.select().count() + 1

        if int(semester_id) > SemesterDB.select().count():
            abort(500, message = "This semester id does not exist. Please input a valid semester id.")

        ClassDB.create(semester_id = semester_id, id = int(id), title = args["title"], credit = args["credit"], subject = args["subject"])

        return int(id), 201
    
class Class(Resource):
    def get(self, semester_id: int, class_id: int):
        if int(semester_id) > SemesterDB.select().count() or int(semester_id) < 1:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")
        if int(class_id) > ClassDB.select().count() or int(class_id) < 1:
            abort(404, message = "This class id does not exist. Please input a valid class id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).get().semester_id.id != int(semester_id):
            abort(404, message = "This class id is not contained within this semester. Please input a valid class id for this semester or a valid semester id for this class.")

        foundClass = ClassDB.get(ClassDB.id == int(class_id))
        return {"id" : int(class_id), "title" : foundClass.title, "credit" : foundClass.credit, "subject" : foundClass.subject}, 200

api.add_resource(Semesters, "/semesters")
api.add_resource(Semester, "/semesters/<semester_id>")
api.add_resource(Classes, "/semesters/<semester_id>/classes")
api.add_resource(Class, "/semesters/<semester_id>/classes/<class_id>")
# api.add_resource(Assignments, "/semesters/<semester_id>/classes/<class_id>/assignments")
# api.add_resource(Assignment, "/semesters/<semester_id>/classes/<class_id/assignments/<assignment_id>")

if __name__ == "__main__":
    app.run(debug = True)