from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from trackerDatabase import *
from datetime import datetime

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
        id = SemesterDB.select(fn.Max(SemesterDB.id)).scalar()
        if id is not None:
            id += 1
        else:
            id = 1

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

        return {"id" : int(semester_id), "semester" : foundSemester.semester}, 200
    
    def delete(self, semester_id: int):
        if SemesterDB.select().where(SemesterDB.id == int(semester_id)).exists() == False:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")

        deleteSemester = SemesterDB.delete().where(SemesterDB.id == int(semester_id))
        deleteSemester.execute()
        deleteClasses = ClassDB.delete().where(ClassDB.semester_id == int(semester_id))
        deleteClasses.execute()
        deleteAssignments = AssignmentDB.delete().where(AssignmentDB.semester_id == int(semester_id))
        deleteAssignments.execute()
        deleteSubmissions = SubmissionDB.delete().where(SubmissionDB.semester_id == int(semester_id))
        deleteSubmissions.execute()
        deleteFeedbacks = FeedbackDB.delete().where(FeedbackDB.semester_id == int(semester_id))
        deleteFeedbacks.execute()

        return "", 204

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

        id = ClassDB.select(fn.Max(ClassDB.id)).scalar()
        if id is not None:
            id += 1
        else:
            id = 1

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

class RemoveClass(Resource):
    def delete(self, class_id: int):
        if ClassDB.select().where(ClassDB.id == int(class_id)).exists() == False:
            abort(404, message = "This class id does not exist. Please input a valid class id.")

        deleteClasses = ClassDB.delete().where(ClassDB.id == int(class_id))
        deleteClasses.execute()
        deleteAssignments = AssignmentDB.delete().where(AssignmentDB.class_id == int(class_id))
        deleteAssignments.execute()
        deleteSubmissions = SubmissionDB.delete().where(SubmissionDB.class_id == int(class_id))
        deleteSubmissions.execute()
        deleteFeedbacks = FeedbackDB.delete().where(FeedbackDB.class_id == int(class_id))
        deleteFeedbacks.execute()

        return "", 204

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
            datetimeObj = assignment.dueDate
            dueDateJSON = datetimeObj.strftime("%Y-%m-%d %H:%M:%S")
            gradePercentage = float(assignment.gradePercentage)
                
            assignments.append({"id" : assignment.id, "assignmentType" : assignment.assignmentType
                                , "expectedTime" : assignment.expectedTime, "dueDate" : dueDateJSON
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
        id = AssignmentDB.select(fn.Max(AssignmentDB.id)).scalar()
        if id is not None:
            id += 1
        else:
            id = 1

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
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).exists() == False:
            abort(404, message = "This assignment id does not exist. Please input a valid assignment id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).get().semester_id.id != int(semester_id):
            abort(500, message = "This class id is not contained within this semester. \
Please input a valid class id for this semester or a valid semester id for this class.")
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).get().class_id.id != int(class_id):
            abort(500, message = "This assignment id is not contained within this class. \
Please input a valid assignment id for this class or a valid class id for this assignment.")
        
        foundAssignment = AssignmentDB.get(AssignmentDB.id == int(assignment_id))
        datetimeObj = foundAssignment.dueDate
        dueDateJSON = datetimeObj.strftime("%Y-%m-%d %H:%M:%S")
        gradePercentage = float(foundAssignment.gradePercentage)
        
        return {"assignmentType" : foundAssignment.assignmentType, "expectedTime" : foundAssignment.expectedTime
            , "dueDate" : dueDateJSON, "gradePercentage" : gradePercentage}, 200

class RemoveAssignment(Resource):
    def delete(self, assignment_id: int):
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).exists() == False:
            abort(404, message = "This assignment id does not exist. Please input a valid assignment id.")

        deleteAssignments = AssignmentDB.delete().where(AssignmentDB.id == int(assignment_id))
        deleteAssignments.execute()
        deleteSubmissions = SubmissionDB.delete().where(SubmissionDB.assignment_id == int(assignment_id))
        deleteSubmissions.execute()
        deleteFeedbacks = FeedbackDB.delete().where(FeedbackDB.assignment_id == int(assignment_id))
        deleteFeedbacks.execute()

        return "", 204

class Submissions(Resource):
    def get(self, semester_id: int, class_id: int, assignment_id: int):
        if SemesterDB.select().where(SemesterDB.id == int(semester_id)).exists() == False:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).exists() == False:
            abort(404, message = "This class id does not exist. Please input a valid class id.")
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).exists() == False:
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
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).exists() == False:
            abort(404, message = "This assignment id does not exist. Please input a valid assignment id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).get().semester_id.id != int(semester_id):
            abort(500, message = "This class id is not contained within this semester. \
Please input a valid class id for this semester or a valid semester id for this class.")
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).get().class_id.id != int(class_id):
            abort(500, message = "This assignment id is not contained within this class. \
Please input a valid assignment id for this class or a valid class id for this assignment.")

        args = parser.parse_args()
        id = SubmissionDB.select(fn.Max(SubmissionDB.id)).scalar()
        if id is not None:
            id += 1
        else:
            id = 1
        submissionTime = datetime.now()

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
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).exists() == False:
            abort(404, message = "This assignment id does not exist. Please input a valid assignment id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).get().semester_id.id != int(semester_id):
            abort(500, message = "This class id is not contained within this semester. \
Please input a valid class id for this semester or a valid semester id for this class.")
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).get().class_id.id != int(class_id):
            abort(500, message = "This assignment id is not contained within this class. \
Please input a valid assignment id for this class or a valid class id for this assignment.")
        if not SubmissionDB.select().where(SubmissionDB.assignment_id == int(assignment_id)).exists():
            abort(404, message = "There are no submissions for this assignment.")
        
        submissionID = SubmissionDB.select().where(SubmissionDB.assignment_id == int(assignment_id)).count()
        foundSubmission = SubmissionDB.select().where(SubmissionDB.assignment_id == int(assignment_id)
                                                      ).order_by(SubmissionDB.submissionTime.desc()).limit(1).get()
        foundAssignment = AssignmentDB.get(AssignmentDB.id == foundSubmission.assignment_id)
        datetimeObj = foundAssignment.dueDate
        dueDateJSON = datetimeObj.strftime("%Y-%m-%d %H:%M:%S")
        gradePercentage = float(foundAssignment.gradePercentage)
        submissionTimeString = foundSubmission.submissionTime.strftime("%Y-%m-%d %H:%M:%S")

        return {"submissionNumber" : submissionID, "actualTime" : foundSubmission.actualTime, "expectedTime" : foundAssignment.expectedTime
                , "expectedGrade" : foundSubmission.expectedGrade, "gradePercentage" : gradePercentage
                , "submissionTime" : submissionTimeString, "dueDate" : dueDateJSON, "assignmentType" : foundAssignment.assignmentType}, 200

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

        for feedbackSelect in FeedbackDB.select().where(FeedbackDB.class_id == int(class_id)):
            feedbacks.append({"id" : feedbackSelect.id, "actualGrade" : feedbackSelect.actualGrade
                              , "feedback" : feedbackSelect.feedback})
                
        return feedbacks, 200
    
class Feedback(Resource):
    def get(self, semester_id: int, class_id: int, assignment_id: int):
        if SemesterDB.select().where(SemesterDB.id == int(semester_id)).exists() == False:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).exists() == False:
            abort(404, message = "This class id does not exist. Please input a valid class id.")
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).exists() == False:
            abort(404, message = "This assignment id does not exist. Please input a valid assignment id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).get().semester_id.id != int(semester_id):
            abort(500, message = "This class id is not contained within this semester. \
Please input a valid class id for this semester or a valid semester id for this class.")
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).get().class_id.id != int(class_id):
            abort(500, message = "This assignment id is not contained within this class. \
Please input a valid assignment id for this class or a valid class id for this assignment.")
        if FeedbackDB.select().where(FeedbackDB.assignment_id == int(assignment_id)).exists() == False:
            abort(404, message = "There is no feedback for this assignment.")
        
        foundFeedback = FeedbackDB.get(FeedbackDB.assignment_id == int(assignment_id))
        foundAssignment = AssignmentDB.get(AssignmentDB.id == int(assignment_id))
        gradePercentage = float(foundAssignment.gradePercentage)
        foundSubmission = SubmissionDB.select().where(SubmissionDB.assignment_id == int(assignment_id)
                                                      ).order_by(SubmissionDB.submissionTime.desc()).limit(1).get()

        return {"actualGrade" : foundFeedback.actualGrade, "expectedGrade" : foundSubmission.expectedGrade
                , "gradePercentage" : gradePercentage, "feedback" : foundFeedback.feedback}, 200
    
    def post(self, semester_id: int, class_id: int, assignment_id: int):
        if SemesterDB.select().where(SemesterDB.id == int(semester_id)).exists() == False:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).exists() == False:
            abort(404, message = "This class id does not exist. Please input a valid class id.")
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).exists() == False:
            abort(404, message = "This assignment id does not exist. Please input a valid assignment id.")
        if SubmissionDB.select().where(SubmissionDB.assignment_id == int(assignment_id)).exists() == False:
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
        id = FeedbackDB.select(fn.Max(FeedbackDB.id)).scalar()
        if id is not None:
            id += 1
        else:
            id = 1

        FeedbackDB.create(semester_id = semester_id, class_id = class_id, assignment_id = assignment_id, id = int(id)
                        , actualGrade = args["actualGrade"], feedback = args["feedback"])

        return str(id), 201
    
    def put(self, semester_id: int, class_id: int, assignment_id: int):
        if SemesterDB.select().where(SemesterDB.id == int(semester_id)).exists() == False:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).exists() == False:
            abort(404, message = "This class id does not exist. Please input a valid class id.")
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).exists() == False:
            abort(404, message = "This assignment id does not exist. Please input a valid assignment id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).get().semester_id.id != int(semester_id):
            abort(500, message = "This class id is not contained within this semester. \
Please input a valid class id for this semester or a valid semester id for this class.")
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).get().class_id.id != int(class_id):
            abort(500, message = "This assignment id is not contained within this class. \
Please input a valid assignment id for this class or a valid class id for this assignment.")
        if FeedbackDB.select().where(FeedbackDB.assignment_id == int(assignment_id)).count() == 0:
            abort(404, message = "Feedback has not yet been created")

        args = parser.parse_args()
        foundFeedback = FeedbackDB.select().where(FeedbackDB.assignment_id == int(assignment_id)).get()

        foundFeedback.actualGrade = args["actualGrade"]
        if args["feedback"] is None:
            args["feedback"] = ""
        foundFeedback.feedback = args["feedback"]
        foundFeedback.save()

        return str(foundFeedback.id), 201
    
    def patch(self, semester_id: int, class_id: int, assignment_id: int):
        if SemesterDB.select().where(SemesterDB.id == int(semester_id)).exists() == False:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).exists() == False:
            abort(404, message = "This class id does not exist. Please input a valid class id.")
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).exists() == False:
            abort(404, message = "This assignment id does not exist. Please input a valid assignment id.")
        if ClassDB.select().where(ClassDB.id == int(class_id)).get().semester_id.id != int(semester_id):
            abort(500, message = "This class id is not contained within this semester. \
Please input a valid class id for this semester or a valid semester id for this class.")
        if AssignmentDB.select().where(AssignmentDB.id == int(assignment_id)).get().class_id.id != int(class_id):
            abort(500, message = "This assignment id is not contained within this class. \
Please input a valid assignment id for this class or a valid class id for this assignment.")
        if FeedbackDB.select().where(FeedbackDB.assignment_id == int(assignment_id)).count() == 0:
            abort(404, message = "Feedback has not yet been created")

        args = parser.parse_args()

        foundFeedback = FeedbackDB.select().where(FeedbackDB.assignment_id == assignment_id).get()
        foundFeedback.actualGrade = args["actualGrade"]
        foundFeedback.save(only=[FeedbackDB.actualGrade])

        return str(foundFeedback.id), 201

class GPA(Resource):
    def get(self, semester_id: int):
        if SemesterDB.select().where(SemesterDB.id == int(semester_id)).exists() == False:
            abort(404, message = "This semester id does not exist. Please input a valid semester id.")
        if FeedbackDB.select().where(FeedbackDB.semester_id == int(semester_id)).count() == 0:
            abort(404, message = "Feedback has not yet been created")

        totalCreditHours = 0
        totalCreditGPA = 0
        for aClass in ClassDB.select().where(ClassDB.semester_id == semester_id):
            totalCreditHours += aClass.credit
            gradeSum = 0
            totalPercentEarned = 0
            if FeedbackDB.select().where(FeedbackDB.class_id == aClass.id).exists() == False:
                totalCreditGPA += 4.0 * aClass.credit
            else:
                for feedback in FeedbackDB.select().where(FeedbackDB.class_id == aClass.id):
                    assignment = AssignmentDB.select().where(AssignmentDB.id == feedback.assignment_id).get()
                    gradeSum += float(feedback.actualGrade) * (float(assignment.gradePercentage) / 100.0)
                    totalPercentEarned += assignment.gradePercentage
                totalCreditGPA += self.findGPA((gradeSum / float(totalPercentEarned)) * 100) * aClass.credit

        return (totalCreditGPA / totalCreditHours)

    def findGPA(self, gradePercent: int):
        if gradePercent >= 92.5:
            return 4.0
        elif gradePercent >= 89.5:
            return 3.7
        elif gradePercent >= 86.5:
            return 3.3
        elif gradePercent >= 82.5:
            return 3.0
        elif gradePercent >= 79.5:
            return 2.7
        elif gradePercent >= 76.5:
            return 2.3
        elif gradePercent >= 72.5:
            return 2.0
        elif gradePercent >= 69.5:
            return 1.7
        elif gradePercent >= 66.5:
            return 1.3
        elif gradePercent >= 62.5:
            return 1.0
        elif gradePercent >= 59.5:
            return 0.7
        else:
            return 0.0

class ClassGrade(Resource):
    def get(self, class_id: int):
        if ClassDB.select().where(ClassDB.id == int(class_id)).exists() == False:
            abort(404, message = "This class id does not exist. Please input a valid class id.")
        if FeedbackDB.select().where(FeedbackDB.semester_id == int(class_id)).count() == 0:
            abort(404, message = "Feedback has not yet been created")

        gradeSum = 0
        totalPercentEarned = 0
        for feedback in FeedbackDB.select().where(FeedbackDB.class_id == class_id):
            assignment = AssignmentDB.select().where(AssignmentDB.id == feedback.assignment_id).get()
            gradeSum += float(feedback.actualGrade) * (float(assignment.gradePercentage) / 100.0)
            totalPercentEarned += assignment.gradePercentage

        return gradeSum / float(totalPercentEarned) * 100

api.add_resource(Semesters, "/semesters")
api.add_resource(Semester, "/semesters/<semester_id>")
api.add_resource(Classes, "/semesters/<semester_id>/classes")
api.add_resource(Class, "/semesters/<semester_id>/classes/<class_id>")
api.add_resource(RemoveClass, "/class/<class_id>")
api.add_resource(Assignments, "/semesters/<semester_id>/classes/<class_id>/assignments")
api.add_resource(Assignment, "/semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>")
api.add_resource(RemoveAssignment, "/assignments/<assignment_id>")
api.add_resource(Submissions, "/semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions")
api.add_resource(Submission, "/semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions/latest")
api.add_resource(Feedbacks, "/semesters/<semester_id>/classes/<class_id>/feedback")
api.add_resource(Feedback, "/semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback")
api.add_resource(GPA, "/semesters/<semester_id>/GPA")
api.add_resource(ClassGrade, "/classes/<class_id>/grade")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5027)