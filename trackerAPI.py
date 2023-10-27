from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from trackerDatabase import *
import datetime

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
parser.add_argument("actualTime")
parser.add_argument("expectedGrade")
parser.add_argument("actualGrade")
parser.add_argument("feedback")

studentActivityTracker_DB.connect()
studentActivityTracker_DB.create_tables([SemesterDB, ClassDB, AssignmentDB, SubmissionDB, FeedbackDB])

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
        if SemesterDB.select().where(SemesterDB.id == int(semester_id)).exists() == False:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")

        foundSemester = SemesterDB.get(SemesterDB.id == int(semester_id))

        classes = []
        for aClass in ClassDB.select():
            if aClass.semester_id.id == int(semester_id):
                classes.append(aClass.id)

        return {"id" : int(semester_id), "semester" : foundSemester.semester, "classes" : classes}, 200

class Classes(Resource):
    def get(self, semester_id: int):
        if SemesterDB.select().where(SemesterDB.id == int(semester_id)).exists() == False:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")

        classes = []
        for aClass in ClassDB.select().where(ClassDB.semester_id == int(semester_id)):
            classes.append({"id" : aClass.id, "title" : aClass.title, 
                            "credit" : aClass.credit, "subject" : aClass.subject})
        
        return classes
    
    def post(self, semester_id: int):
        args = parser.parse_args()

        id = ClassDB.select().count() + 1

        if SemesterDB.select().where(SemesterDB.id == int(semester_id)).exists() == False:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")

        ClassDB.create(semester_id = semester_id, id = int(id), title = args["title"], 
                       credit = args["credit"], subject = args["subject"])

        return int(id), 201
    
class Class(Resource):
    def get(self, semester_id: int, class_id: int):
        if SemesterDB.select().where(SemesterDB.id == int(semester_id)).exists() == False:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).exists() == False:
            abort(404, message = "This class id does not exist. Please input a valid class id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).get().semester_id.id != int(semester_id):
            abort(500, message = "This class id is not contained within this semester. \
Please input a valid class id for this semester or a valid semester id for this class.")

        foundClass = ClassDB.get(ClassDB.id == int(class_id))

        return {"id" : int(class_id), "title" : foundClass.title, 
                "credit" : foundClass.credit, "subject" : foundClass.subject}, 200

class Assignments(Resource):
    def get(self, semester_id: int, class_id: int):
        if SemesterDB.select().where(SemesterDB.id == int(semester_id)).exists() == False:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).exists() == False:
            abort(404, message = "This class id does not exist. Please input a valid class id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).get().semester_id.id != int(semester_id):
            abort(500, message = "This class id is not contained within this semester. \
Please input a valid class id for this semester or a valid semester id for this class.")
        
        assignments = []

        for assignment in AssignmentDB.select().where(AssignmentDB.class_id == int(class_id)):
            dueDateString = assignment.dueDate.strftime("%Y-%m-%d %H:%M:%S")
            gradePercentage = float(assignment.gradePercentage)
                
            assignments.append({"id" : assignment.id, "assignmentType" : assignment.assignmentType
                                , "expectedTime" : assignment.expectedTime, "dueDate" : dueDateString
                                , "gradePercentage" : gradePercentage})
                
        return assignments, 200
    
    def post(self, semester_id: int, class_id: int):
        if SemesterDB.select().where(SemesterDB.id == int(semester_id)).exists() == False:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).exists() == False:
            abort(404, message = "This class id does not exist. Please input a valid class id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).get().semester_id.id != int(semester_id):
            abort(500, message = "This class id is not contained within this semester. \
Please input a valid class id for this semester or a valid semester id for this class.")

        args = parser.parse_args()
        id = AssignmentDB.select().count() + 1

        AssignmentDB.create(semester_id = semester_id, class_id = class_id, id = int(id), assignmentType = args["assignmentType"]
                       , expectedTime = args["expectedTime"], subject = args["subject"], dueDate = args["dueDate"]
                       , gradePercentage = args["gradePercentage"])

        return int(id), 201

class Assignment(Resource):
    def get(self, semester_id: int, class_id: int, assignment_id: int):
        if SemesterDB.select().where(SemesterDB.id == int(semester_id)).exists() == False:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).exists() == False:
            abort(404, message = "This class id does not exist. Please input a valid class id.")
        if int(assignment_id) > AssignmentDB.select().count() or int(assignment_id) < 1:
            abort(404, message = "This assignment id does not exist. Please input a valid assignment id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).get().semester_id.id != int(semester_id):
            abort(500, message = "This class id is not contained within this semester. \
Please input a valid class id for this semester or a valid semester id for this class.")
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).get().class_id.id != int(class_id):
            abort(500, message = "This assignment id is not contained within this class. \
Please input a valid assignment id for this class or a valid class id for this assignment.")
        
        foundAssignment = AssignmentDB.get(AssignmentDB.id == int(assignment_id))
        dueDateString = foundAssignment.dueDate.strftime("%Y-%m-%d %H:%M:%S")
        gradePercentage = float(foundAssignment.gradePercentage)
        
        return {"assignmentType" : foundAssignment.assignmentType, "expectedTime" : foundAssignment.expectedTime
            , "dueDate" : dueDateString, "gradePercentage" : gradePercentage}, 200

class Submissions(Resource):
    def get(self, semester_id: int, class_id: int, assignment_id: int):
        if SemesterDB.select().where(SemesterDB.id == int(semester_id)).exists() == False:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).exists() == False:
            abort(404, message = "This class id does not exist. Please input a valid class id.")
        if int(assignment_id) > AssignmentDB.select().count() or int(assignment_id) < 1:
            abort(404, message = "This assignment id does not exist. Please input a valid assignment id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).get().semester_id.id != int(semester_id):
            abort(500, message = "This class id is not contained within this semester. \
Please input a valid class id for this semester or a valid semester id for this class.")
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).get().class_id.id != int(class_id):
            abort(500, message = "This assignment id is not contained within this class. \
Please input a valid assignment id for this class or a valid class id for this assignment.")
        
        submissions = []

        for submission in SubmissionDB.select().where(SubmissionDB.assignment_id == assignment_id):
            submissionTime = submission.submissionTime.strftime("%Y-%m-%d %H:%M:%S")

            submissions.append({"id" : submission.id, "actualTime" : submission.actualTime
                               , "expectedGrade" : submission.expectedGrade, "submissionTime" : submissionTime})
                
        return submissions, 200
    
    def post(self, semester_id: int, class_id: int, assignment_id: int):
        if SemesterDB.select().where(SemesterDB.id == int(semester_id)).exists() == False:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).exists() == False:
            abort(404, message = "This class id does not exist. Please input a valid class id.")
        if int(assignment_id) > AssignmentDB.select().count() or int(assignment_id) < 1:
            abort(404, message = "This assignment id does not exist. Please input a valid assignment id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).get().semester_id.id != int(semester_id):
            abort(500, message = "This class id is not contained within this semester. \
Please input a valid class id for this semester or a valid semester id for this class.")
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).get().class_id.id != int(class_id):
            abort(500, message = "This assignment id is not contained within this class. \
Please input a valid assignment id for this class or a valid class id for this assignment.")

        args = parser.parse_args()
        id = SubmissionDB.select().count() + 1
        submissionTime = datetime.datetime.now()

        SubmissionDB.create(semester_id = semester_id, class_id = class_id, assignment_id = assignment_id, id = int(id)
                        , assignmentType = args["assignmentType"], actualTime = args["actualTime"]
                        , expectedGrade = args["expectedGrade"], submissionTime = submissionTime)

        return str(id) + ", " + str(submissionTime), 201
    
class Submission(Resource):
    def get(self, semester_id: int, class_id: int, assignment_id: int):
        if SemesterDB.select().where(SemesterDB.id == int(semester_id)).exists() == False:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).exists() == False:
            abort(404, message = "This class id does not exist. Please input a valid class id.")
        if int(assignment_id) > AssignmentDB.select().count() or int(assignment_id) < 1:
            abort(404, message = "This assignment id does not exist. Please input a valid assignment id.")
        if SubmissionDB.select().where(SubmissionDB.assignment_id == int(assignment_id)).get() == 0:
            abort(404, message = "There are no submissions for this assignment.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).get().semester_id.id != int(semester_id):
            abort(500, message = "This class id is not contained within this semester. \
Please input a valid class id for this semester or a valid semester id for this class.")
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).get().class_id.id != int(class_id):
            abort(500, message = "This assignment id is not contained within this class. \
Please input a valid assignment id for this class or a valid class id for this assignment.")
        
        foundSubmission = SubmissionDB.select().where(SubmissionDB.assignment_id == int(assignment_id)
                                                      ).order_by(SubmissionDB.submissionTime.desc()).limit(1).get()
        foundAssignment = AssignmentDB.get(AssignmentDB.id == foundSubmission.assignment_id)
        dueDateString = foundAssignment.dueDate.strftime("%Y-%m-%d %H:%M:%S")
        gradePercentage = float(foundAssignment.gradePercentage)
        submissionTimeString = foundSubmission.submissionTime.strftime("%Y-%m-%d %H:%M:%S")

        return {"submissionNumber" : foundSubmission.id, "actualTime" : foundSubmission.actualTime, "expectedTime" : foundAssignment.expectedTime
                , "expectedGrade" : foundSubmission.expectedGrade, "gradePercentage" : gradePercentage
                , "submissionTime" : submissionTimeString, "dueDate" : dueDateString, "assignmentType" : foundAssignment.assignmentType}, 200

class Feedbacks(Resource):
    def get(self, semester_id: int, class_id: int):
        if SemesterDB.select().where(SemesterDB.id == int(semester_id)).exists() == False:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).exists() == False:
            abort(404, message = "This class id does not exist. Please input a valid class id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).get().semester_id.id != int(semester_id):
            abort(500, message = "This class id is not contained within this semester. \
Please input a valid class id for this semester or a valid semester id for this class.")
        
        feedbacks = []

        for feedbackSelect in FeedbackDB.select().where(FeedbackDB.class_id == class_id):
            feedbacks.append({"id" : feedbackSelect.id, "actualGrade" : feedbackSelect.actualGrade
                              , "feedback" : feedbackSelect.feedback})
                
        return feedbacks, 200
    
class Feedback(Resource):
    def get(self, semester_id: int, class_id: int, assignment_id: int):
        if SemesterDB.select().where(SemesterDB.id == int(semester_id)).exists() == False:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).exists() == False:
            abort(404, message = "This class id does not exist. Please input a valid class id.")
        if int(assignment_id) > AssignmentDB.select().count() or int(assignment_id) < 1:
            abort(404, message = "This assignment id does not exist. Please input a valid assignment id.")
        if FeedbackDB.select().where(FeedbackDB.assignment_id == int(assignment_id)).get() == 0:
            abort(404, message = "There is no feedback for this assignment.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).get().semester_id.id != int(semester_id):
            abort(500, message = "This class id is not contained within this semester. \
Please input a valid class id for this semester or a valid semester id for this class.")
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).get().class_id.id != int(class_id):
            abort(500, message = "This assignment id is not contained within this class. \
Please input a valid assignment id for this class or a valid class id for this assignment.")
        
        foundFeedback = FeedbackDB.get(FeedbackDB.assignment_id == int(assignment_id))
        foundAssignment = AssignmentDB.get(AssignmentDB.id == foundFeedback.assignment_id)
        gradePercentage = float(foundAssignment.gradePercentage)

        return {"actualGrade" : foundFeedback.actualGrade, "expectedGrade" : foundAssignment.expectedGrade
                , "gradePercentage" : gradePercentage, "feedback" : foundFeedback.feedback}, 200
    
    def post(self, semester_id: int, class_id: int, assignment_id: int):
        if SemesterDB.select().where(SemesterDB.id == int(semester_id)).exists() == False:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).exists() == False:
            abort(404, message = "This class id does not exist. Please input a valid class id.")
        if int(assignment_id) > AssignmentDB.select().count() or int(assignment_id) < 1:
            abort(404, message = "This assignment id does not exist. Please input a valid assignment id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).get().semester_id.id != int(semester_id):
            abort(500, message = "This class id is not contained within this semester. \
Please input a valid class id for this semester or a valid semester id for this class.")
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).get().class_id.id != int(class_id):
            abort(500, message = "This assignment id is not contained within this class. \
Please input a valid assignment id for this class or a valid class id for this assignment.")
        if FeedbackDB.select().where(FeedbackDB.assignment_id == int(assignment_id)).count() > 0:
            abort(500, message = "Feedback has already been created")

        args = parser.parse_args()
        id = FeedbackDB.select().count() + 1

        FeedbackDB.create(semester_id = semester_id, class_id = class_id, assignment_id = assignment_id, id = int(id)
                        , actualGrade = args["actualGrade"], feedback = args["feedback"])

        return str(id), 201
    
    def put(self, semester_id: int, class_id: int, assignment_id: int):
        if SemesterDB.select().where(SemesterDB.id == int(semester_id)).exists() == False:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).exists() == False:
            abort(404, message = "This class id does not exist. Please input a valid class id.")
        if int(assignment_id) > AssignmentDB.select().count() or int(assignment_id) < 1:
            abort(404, message = "This assignment id does not exist. Please input a valid assignment id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).get().semester_id.id != int(semester_id):
            abort(500, message = "This class id is not contained within this semester. \
Please input a valid class id for this semester or a valid semester id for this class.")
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).get().class_id.id != int(class_id):
            abort(500, message = "This assignment id is not contained within this class. \
Please input a valid assignment id for this class or a valid class id for this assignment.")
        if FeedbackDB.select().where(FeedbackDB.assignment_id == int(assignment_id)).count() == 0:
            abort(500, message = "Feedback has not yet been created")

        args = parser.parse_args()
        foundFeedback = FeedbackDB.get(FeedbackDB.assignment_id == assignment_id)

        qry = foundFeedback.update(actualGrade = args["actualGrade"], feedback = args["feedback"])
        qry.execute()
        print(foundFeedback)

        return str(foundFeedback.id), 201
    
    def patch(self, semester_id: int, class_id: int, assignment_id: int):
        if SemesterDB.select().where(SemesterDB.id == int(semester_id)).exists() == False:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).exists() == False:
            abort(404, message = "This class id does not exist. Please input a valid class id.")
        if int(assignment_id) > AssignmentDB.select().count() or int(assignment_id) < 1:
            abort(404, message = "This assignment id does not exist. Please input a valid assignment id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).get().semester_id.id != int(semester_id):
            abort(500, message = "This class id is not contained within this semester. \
Please input a valid class id for this semester or a valid semester id for this class.")
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).get().class_id.id != int(class_id):
            abort(500, message = "This assignment id is not contained within this class. \
Please input a valid assignment id for this class or a valid class id for this assignment.")
        if FeedbackDB.select().where(FeedbackDB.assignment_id == int(assignment_id)).count() == 0:
            abort(500, message = "Feedback has not yet been created")

        args = parser.parse_args()
        foundFeedback = FeedbackDB.get(FeedbackDB.assignment_id == assignment_id)

        qry = foundFeedback.update(actualGrade = args["actualGrade"])
        qry.execute()
        print(foundFeedback)

        return str(foundFeedback.id), 201

api.add_resource(Semesters, "/semesters")
api.add_resource(Semester, "/semesters/<semester_id>")
api.add_resource(Classes, "/semesters/<semester_id>/classes")
api.add_resource(Class, "/semesters/<semester_id>/classes/<class_id>")
api.add_resource(Assignments, "/semesters/<semester_id>/classes/<class_id>/assignments")
api.add_resource(Assignment, "/semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>")
api.add_resource(Submissions, "/semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions")
api.add_resource(Submission, "/semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions/latest")
api.add_resource(Feedbacks, "/semesters/<semester_id>/classes/<class_id>/feedback")
api.add_resource(Feedback, "/semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback")


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5027)