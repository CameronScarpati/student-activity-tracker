from testplan.testing.multitest import testsuite, testcase, MultiTest
import time

@testsuite
class SubmissionMultiTestSuite(object):
    @testcase
    def test_getSubmissionsNoSemester(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments/1/submissions")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions error"

    @testcase
    def test_getSubmissionNoSemester(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments/1/submissions/latest")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions/latest error"

    @testcase
    def test_postSemesters1(self, env, result):
        post_data = {"semester" : "Fall 2023"}
        env.http_client.post("/semesters", json=post_data)
        response = env.http_client.receive()
        
        assert response.json() == 1, "Verify /semesters endpoint"

    @testcase
    def test_postSemesters2(self, env, result):
        post_data = {"semester": "Spring 2024"}
        env.http_client.post("/semesters", json=post_data)
        response = env.http_client.receive()
        
        assert response.json() == 2, "Verify /semesters endpoint"

    @testcase
    def test_getSubmissionsNoClass(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments/1/submissions")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions error"

    @testcase
    def test_getSubmissionNoClass(self, env, result):
        env.http_client.get("/semesters/2/classes/1/assignments/1/submissions/latest")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions/latest error"

    @testcase
    def test_postClass1(self, env, result):
        post_data = {"title" : "Multivariable Calculus", "credit" : 3, "subject" : "Mathematics"}
        env.http_client.post("/semesters/1/classes", json=post_data)
        response = env.http_client.receive()
        
        assert response.json() == 1, "Verify /semesters/<semester_id>/classes endpoint"

    @testcase
    def test_postClass2(self, env, result):
        post_data = {"title" : "Storytelling as Performance", "credit" : 3, "subject" : "Theater"}
        env.http_client.post("/semesters/2/classes", json=post_data)
        response = env.http_client.receive()
        
        assert response.json() == 2, "Verify /semesters/<semester_id>/classes endpoint"

    @testcase
    def test_postClass3(self, env, result):
        post_data = {"title" : "Program Design and Data Structures", "credit" : 3, "subject" : "Computer Science"}
        env.http_client.post("/semesters/1/classes", json=post_data)
        response = env.http_client.receive()
        
        assert response.json() == 3, "Verify /semesters/<semester_id>/classes endpoint"

    @testcase
    def test_postClass4(self, env, result):
        post_data = {"title" : "Atlantic History in the Digital Age", "credit" : 3, "subject" : "History"}
        env.http_client.post("/semesters/1/classes", json=post_data)
        response = env.http_client.receive()
        
        assert response.json() == 4, "Verify /semesters/<semester_id>/classes endpoint"

    @testcase
    def test_postClass5(self, env, result):
        post_data = {"title" : "AI and Society", "credit" : 3, "subject" : "Humanities"}
        env.http_client.post("/semesters/2/classes", json=post_data)
        response = env.http_client.receive()
        
        assert response.json() == 5, "Verify /semesters/<semester_id>/classes endpoint"

    @testcase
    def test_getSubmissionsNoAssignment(self, env, result):
        env.http_client.get("/semesters/1/classes/3/assignments/1/submissions")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions error"

    @testcase
    def test_getSubmissionNoAssignment(self, env, result):
        env.http_client.get("/semesters/2/classes/2/assignments/1/submissions/latest")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions/latest error"
    
    @testcase
    def test_postAssignments1(self, env, result):
        post_data = {"assignmentType" : "Exam", "expectedTime" : 350, "dueDate" : "2023-11-07 12:35:00", "gradePercentage" : 10.0}
        env.http_client.post("/semesters/1/classes/1/assignments", json=post_data)
        response = env.http_client.receive()
        
        assert response.json() == 1, "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

    @testcase
    def test_postAssignments2(self, env, result):
        post_data = {"assignmentType" : "Homework", "expectedTime" : 120, "dueDate" : "2023-10-01 13:25:00", "gradePercentage" : 0.074}
        env.http_client.post("/semesters/1/classes/1/assignments", json=post_data)
        response = env.http_client.receive()
        
        assert response.json() == 2, "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

    @testcase
    def test_postAssignments3(self, env, result):
        post_data = {"assignmentType" : "Presentation", "expectedTime" : 20, "dueDate" : "2023-10-31 10:15:00", "gradePercentage" : 2.0}
        env.http_client.post("/semesters/2/classes/2/assignments", json=post_data)
        response = env.http_client.receive()
        
        assert response.json() == 3, "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

    @testcase
    def test_postAssignments4(self, env, result):
        post_data = {"assignmentType" : "Project", "expectedTime" : 250, "dueDate" : "2023-10-05 15:25:00", "gradePercentage" : 5.0}
        env.http_client.post("/semesters/1/classes/4/assignments", json=post_data)
        response = env.http_client.receive()
        
        assert response.json() == 4, "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

    @testcase
    def test_postAssignments5(self, env, result):
        post_data = {"assignmentType" : "Reading", "expectedTime" : 90, "dueDate" : "2023-10-03 8:45:00", "gradePercentage" : 0.5}
        env.http_client.post("/semesters/2/classes/5/assignments", json=post_data)
        response = env.http_client.receive()
        
        assert response.json() == 5, "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

    @testcase
    def test_postAssignments6(self, env, result):
        post_data = {"assignmentType" : "Quiz", "expectedTime" : 35, "dueDate" : "2023-11-19 10:45:00", "gradePercentage" : 8.2}
        env.http_client.post("/semesters/2/classes/2/assignments", json=post_data)
        response = env.http_client.receive()
        
        assert response.json() == 6, "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

    @testcase
    def test_getSubmissionsEmpty(self, env, result):
        env.http_client.get("/semesters/2/classes/2/assignments/3/submissions")
        response = env.http_client.receive()
        
        assert response.json() == [], "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions endpoint"

    @testcase
    def test_getSubmissionNonePosted(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments/2/submissions/latest")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions/latest error"

    @testcase
    def test_getSubmissionsWrongSemester(self, env, result):
        env.http_client.get("/semesters/1/classes/2/assignments/3/submissions")
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions error"

    @testcase
    def test_getSubmissionWrongSemester(self, env, result):
        env.http_client.get("/semesters/2/classes/4/assignments/4/submissions/latest")
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions/latest error"

    @testcase
    def test_getSubmissionsWrongClass(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments/4/submissions")
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions error"

    @testcase
    def test_getSubmissionWrongClass(self, env, result):
        env.http_client.get("/semesters/2/classes/5/assignments/2/submissions/latest")
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions/latest error"

    @testcase
    def test_postSubmissions1(self, env, result):
        post_data = {"actualTime" : 300, "expectedGrade" : 78}
        env.http_client.post("/semesters/1/classes/1/assignments/1/submissions", json=post_data)
        response = env.http_client.receive()

        actual_data = response.json()
        indexOfComma = actual_data.index(",")
        actual_data = actual_data[:indexOfComma]
        assert actual_data == "1", "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions endpoint"

    @testcase
    def test_postSubmissions2(self, env, result):
        post_data = {"actualTime" : 320, "expectedGrade" : 88}
        env.http_client.post("/semesters/1/classes/1/assignments/1/submissions", json=post_data)
        response = env.http_client.receive()
        
        actual_data = response.json()
        indexOfComma = actual_data.index(",")
        actual_data = actual_data[:indexOfComma]
        assert actual_data == "2", "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions endpoint"

    @testcase
    def test_postSubmissions3(self, env, result):
        post_data = {"actualTime" : 40, "expectedGrade" : 85}
        env.http_client.post("/semesters/1/classes/4/assignments/4/submissions", json=post_data)
        response = env.http_client.receive()
        
        actual_data = response.json()
        indexOfComma = actual_data.index(",")
        actual_data = actual_data[:indexOfComma]
        assert actual_data == "3", "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions endpoint"

    @testcase
    def test_postSubmissions4(self, env, result):
        post_data = {"actualTime" : 70, "expectedGrade" : 100}
        env.http_client.post("/semesters/1/classes/1/assignments/2/submissions", json=post_data)
        response = env.http_client.receive()
        
        actual_data = response.json()
        indexOfComma = actual_data.index(",")
        actual_data = actual_data[:indexOfComma]
        assert actual_data == "4", "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions endpoint"

    @testcase
    def test_postSubmissions5(self, env, result):
        post_data = {"actualTime" : 45, "expectedGrade" : 89}
        env.http_client.post("/semesters/1/classes/4/assignments/4/submissions", json=post_data)
        response = env.http_client.receive()
        
        actual_data = response.json()
        indexOfComma = actual_data.index(",")
        actual_data = actual_data[:indexOfComma]
        assert actual_data == "5", "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions endpoint"

    @testcase
    def test_postSubmissions6(self, env, result):
        post_data = {"actualTime" : 70, "expectedGrade" : 100}
        env.http_client.post("/semesters/2/classes/5/assignments/5/submissions", json=post_data)
        response = env.http_client.receive()

        actual_data = response.json()
        indexOfComma = actual_data.index(",")
        actual_data = actual_data[:indexOfComma]
        assert actual_data == "6", "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions endpoint"

    @testcase
    def test_postSubmissions7(self, env, result):
        post_data = {"actualTime" : 55, "expectedGrade" : 97}
        env.http_client.post("/semesters/1/classes/4/assignments/4/submissions", json=post_data)
        response = env.http_client.receive()
        
        actual_data = response.json()
        indexOfComma = actual_data.index(",")
        actual_data = actual_data[:indexOfComma]
        assert actual_data == "7", "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions endpoint"

    @testcase
    def test_getSubmissionsAfterPost(self, env, result):
        env.http_client.get("/semesters/1/classes/4/assignments/4/submissions")
        response = env.http_client.receive()

        expected_data = [{"id": 3, "actualTime": 40, "expectedGrade": 85},
                         {"id": 5, "actualTime": 45, "expectedGrade": 89},
                         {"id": 7, "actualTime": 55, "expectedGrade": 97}]

        actual_data = response.json()
        for dictionary in actual_data:
            del dictionary["submissionTime"]
            
        assert actual_data == expected_data, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions endpoint"

    @testcase
    def test_getLatestSubmission(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments/1/submissions/latest")
        response = env.http_client.receive()
        
        actual_data = response.json()
        del actual_data["submissionTime"]

        result.dict.match(
            actual_data, {"submissionNumber" : 2, "actualTime" : 320, "expectedTime" : 350, "expectedGrade" : 88, "gradePercentage" : 10.0, "dueDate" : "2023-11-07 12:35:00", "assignmentType" : "Exam"}, 
            "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions/latest endpoint"
        )

    @testcase
    def test_postNoSemester(self, env, result):
        post_data = {"actualTime" : 60, "expectedGrade" : 100}
        env.http_client.post("/semesters/3/classes/2/assignments/3/submissions", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions error"

    @testcase
    def test_postNoClass(self, env, result):
        post_data = {"actualTime" : 60, "expectedGrade" : 100}
        env.http_client.post("/semesters/2/classes/6/assignments/3/submissions", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions error"

    @testcase
    def test_postNoAssignment(self, env, result):
        post_data = {"actualTime" : 60, "expectedGrade" : 100}
        env.http_client.post("/semesters/2/classes/3/assignments/0/submissions", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions error"

    @testcase
    def test_postWrongSemester(self, env, result):
        post_data = {"actualTime" : 60, "expectedGrade" : 100}
        env.http_client.post("/semesters/1/classes/2/assignments/3/submissions", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions error"

    @testcase
    def test_postWrongClass(self, env, result):
        post_data = {"actualTime" : 60, "expectedGrade" : 100}
        env.http_client.post("/semesters/1/classes/1/assignments/4/submissions", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions error"

    @testcase
    def test_deleteAssignment1(self, env, result):
        env.http_client.delete("/assignments/1")
        response = env.http_client.receive()

        assert response.status_code == 204, "/assignments/<assignment_id> endpoint"

    @testcase
    def test_getSubmissionsAfterAssignmentDelete(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments/1/submissions")
        response = env.http_client.receive()
            
        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions error"

    @testcase
    def test_getLatestSubmissionAfterAssignmentDelete(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments/1/submissions/latest")
        response = env.http_client.receive()
            
        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions error"

    @testcase
    def test_postSubmissionAfterAssignmentDelete(self, env, result):
        post_data = {"actualTime" : 60, "expectedGrade" : 100}
        env.http_client.post("/semesters/1/classes/1/assignments/1/submissions", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions error"

    @testcase
    def test_getSubmissionsAssignmentDeleteCheckForFalseRemoval(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments/2/submissions")
        response = env.http_client.receive()

        expected_data = [{"id": 4, "actualTime" : 70, "expectedGrade" : 100}]
        
        actual_data = response.json()
        for dictionary in actual_data:
            del dictionary["submissionTime"]
            
        assert actual_data == expected_data, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions endpoint"

    @testcase
    def test_getLatestSubmissionAssignmentDeleteCheckForFalseRemoval(self, env, result):
        env.http_client.get("/semesters/1/classes/4/assignments/4/submissions/latest")
        response = env.http_client.receive()
        
        actual_data = response.json()
        del actual_data["submissionTime"]

        result.dict.match(
            actual_data, {"submissionNumber" : 3, "actualTime" : 55, "expectedTime" : 250, "expectedGrade" : 97, "gradePercentage" : 5.0, "dueDate" : "2023-10-05 15:25:00", "assignmentType" : "Project"}, 
            "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions/latest endpoint"
        )

    @testcase
    def test_deleteClass1(self, env, result):
        env.http_client.delete("/class/1")
        response = env.http_client.receive()

        assert response.status_code == 204, "Verify /class/<class_id> endpoint"

    @testcase
    def test_getSubmissionsAfterClassDelete(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments/2/submissions")
        response = env.http_client.receive()
            
        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions error"

    @testcase
    def test_getLatestSubmissionAfterClassDelete(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments/2/submissions/latest")
        response = env.http_client.receive()
            
        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions error"

    @testcase
    def test_postSubmissionAfterClassDelete(self, env, result):
        post_data = {"actualTime" : 60, "expectedGrade" : 100}
        env.http_client.post("/semesters/1/classes/1/assignments/2/submissions", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions error"

    @testcase
    def test_getSubmissionsClassDeleteCheckForFalseRemoval(self, env, result):
        env.http_client.get("/semesters/1/classes/4/assignments/4/submissions")
        response = env.http_client.receive()

        expected_data = [{"id": 3, "actualTime": 40, "expectedGrade": 85},
                         {"id": 5, "actualTime": 45, "expectedGrade": 89},
                         {"id": 7, "actualTime": 55, "expectedGrade": 97}]
        
        actual_data = response.json()
        for dictionary in actual_data:
            del dictionary["submissionTime"]
            
        assert actual_data == expected_data, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions endpoint"

    @testcase
    def test_getLatestSubmissionClassDeleteCheckForFalseRemoval(self, env, result):
        env.http_client.get("/semesters/1/classes/4/assignments/4/submissions/latest")
        response = env.http_client.receive()
        
        actual_data = response.json()
        del actual_data["submissionTime"]

        result.dict.match(
            actual_data, {"submissionNumber" : 3, "actualTime" : 55, "expectedTime" : 250, "expectedGrade" : 97, "gradePercentage" : 5.0, "dueDate" : "2023-10-05 15:25:00", "assignmentType" : "Project"}, 
            "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions/latest endpoint"
        )

    @testcase
    def test_deleteSemester2(self, env, result):
        env.http_client.delete("/semesters/2")
        response = env.http_client.receive()

        assert response.status_code == 204, "Verify /semesters/<semester_id> endpoint"

    @testcase
    def test_postSemesters2Again(self, env, result):
        post_data = {"semester": "Spring 2024"}
        env.http_client.post("/semesters", json=post_data)
        response = env.http_client.receive()
        
        assert response.json() == 2, "Verify /semesters endpoint"

    @testcase
    def test_getSubmissionsAfterSemesterDelete(self, env, result):
        env.http_client.get("/semesters/2/classes/2/assignments/5/submissions")
        response = env.http_client.receive()
            
        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions error"

    @testcase
    def test_getLatestSubmissionAfterSemesterDelete(self, env, result):
        env.http_client.get("/semesters/2/classes/5/assignments/5/submissions/latest")
        response = env.http_client.receive()
            
        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions error"

    @testcase
    def test_postSubmissionAfterSemesterDelete(self, env, result):
        post_data = {"actualTime" : 60, "expectedGrade" : 100}
        env.http_client.post("/semesters/2/classes/2/assignments/6/submissions", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions error"

    @testcase
    def test_getSubmissionsSemesterDeleteCheckForFalseRemoval(self, env, result):
        env.http_client.get("/semesters/1/classes/4/assignments/4/submissions")
        response = env.http_client.receive()

        expected_data = [{"id": 3, "actualTime": 40, "expectedGrade": 85},
                         {"id": 5, "actualTime": 45, "expectedGrade": 89},
                         {"id": 7, "actualTime": 55, "expectedGrade": 97}]
        
        actual_data = response.json()
        for dictionary in actual_data:
            del dictionary["submissionTime"]
            
        assert actual_data == expected_data, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions endpoint"

    @testcase
    def test_getLatestSubmissionSemesterDeleteCheckForFalseRemoval(self, env, result):
        env.http_client.get("/semesters/1/classes/4/assignments/4/submissions/latest")
        response = env.http_client.receive()
        
        actual_data = response.json()
        del actual_data["submissionTime"]

        result.dict.match(
            actual_data, {"submissionNumber" : 3, "actualTime" : 55, "expectedTime" : 250, "expectedGrade" : 97, "gradePercentage" : 5.0, "dueDate" : "2023-10-05 15:25:00", "assignmentType" : "Project"}, 
            "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions/latest endpoint"
        )

    @testcase
    def test_clearTable1(self, env, result):
        env.http_client.delete("/semesters/1")
        response = env.http_client.receive()

        assert response.status_code == 204

    @testcase
    def test_clearTable2(self, env, result):
        env.http_client.delete("/semesters/2")
        response = env.http_client.receive()

        assert response.status_code == 204