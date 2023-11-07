from testplan.testing.multitest import testsuite, testcase, MultiTest
import time

@testsuite
class FeedbackMultiTestSuite(object):
    @testcase
    def test_getFeedbackNoSemester(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments/1/feedback")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

    @testcase
    def test_getFeedbacksNoSemester(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments/1/feedback")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/feedback error"

    @testcase
    def test_postFeedbackNoSemester(self, env, result):
        post_data = {"actualGrade" : 95, "feedback" : "Great Work!"}
        env.http_client.post("/semesters/1/classes/1/assignments/1/feedback", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

    @testcase
    def test_putFeedbackNoSemester(self, env, result):
        put_data = {"actualGrade" : 95, "feedback" : "Great Work!"}
        env.http_client.put("/semesters/1/classes/1/assignments/1/feedback", json=put_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

    @testcase
    def test_patchFeedbackNoSemester(self, env, result):
        patch_data = {"actualGrade" : 100}
        env.http_client.patch("/semesters/1/classes/1/assignments/1/feedback", json=patch_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

    @testcase
    def test_postSemesters1(self, env, result):
        post_data = {"semester" : "Fall 2023"}
        env.http_client.post("/semesters", json=post_data)
        response = env.http_client.receive()
        
        assert response.json() == 1, "Verify /semesters endpoint"

    @testcase
    def test_postSemesters2(self, env, result):
        post_data = {"semester" : "Spring 2024"}
        env.http_client.post("/semesters", json=post_data)
        response = env.http_client.receive()
        
        assert response.json() == 2, "Verify /semesters endpoint"

    @testcase
    def test_getFeedbackNoClass(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments/1/feedback")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

    @testcase
    def test_getFeedbacksNoClass(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments/1/feedback")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/feedback error"

    @testcase
    def test_postFeedbackNoClass(self, env, result):
        post_data = {"actualGrade" : 95, "feedback" : "Great Work!"}
        env.http_client.post("/semesters/1/classes/1/assignments/1/feedback", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

    @testcase
    def test_putFeedbackNoClass(self, env, result):
        put_data = {"actualGrade" : 95, "feedback" : "Great Work!"}
        env.http_client.put("/semesters/1/classes/1/assignments/1/feedback", json=put_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

    @testcase
    def test_patchFeedbackNoClass(self, env, result):
        patch_data = {"actualGrade" : 100}
        env.http_client.patch("/semesters/1/classes/1/assignments/1/feedback", json=patch_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

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
    def test_getFeedbackNoAssignment(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments/1/feedback")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

    @testcase
    def test_getFeedbacksNoAssignment(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments/1/feedback")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/feedback error"

    @testcase
    def test_postFeedbackNoAssignment(self, env, result):
        post_data = {"actualGrade" : 95, "feedback" : "Great Work!"}
        env.http_client.post("/semesters/1/classes/1/assignments/1/feedback", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

    @testcase
    def test_putFeedbackNoAssignment(self, env, result):
        put_data = {"actualGrade" : 95, "feedback" : "Great Work!"}
        env.http_client.put("/semesters/1/classes/1/assignments/1/feedback", json=put_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

    @testcase
    def test_patchFeedbackNoAssignment(self, env, result):
        patch_data = {"actualGrade" : 100}
        env.http_client.patch("/semesters/1/classes/1/assignments/1/feedback", json=patch_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

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
    def test_getFeedbackWrongSemester(self, env, result):
        env.http_client.get("/semesters/1/classes/2/assignments/1/feedback")
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

    @testcase
    def test_getFeedbacksWrongSemester(self, env, result):
        env.http_client.get("/semesters/1/classes/2/feedback")
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id>/feedback error"

    @testcase
    def test_putFeedbackWrongSemester(self, env, result):
        put_data = {"actualGrade" : 95, "feedback" : "Great Work!"}
        env.http_client.put("/semesters/2/classes/3/assignments/1/feedback", json=put_data)
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

    @testcase
    def test_patchFeedbackWrongSemester(self, env, result):
        patch_data = {"actualGrade" : 100}
        env.http_client.patch("/semesters/2/classes/4/assignments/1/feedback", json=patch_data)
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

    @testcase
    def test_getFeedbackWrongClass(self, env, result):
        env.http_client.get("/semesters/2/classes/2/assignments/4/feedback")
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

    @testcase
    def test_putFeedbackWrongClass(self, env, result):
        put_data = {"actualGrade" : 95, "feedback" : "Great Work!"}
        env.http_client.put("/semesters/2/classes/5/assignments/2/feedback", json=put_data)
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

    @testcase
    def test_patchFeedbackWrongClass(self, env, result):
        patch_data = {"actualGrade" : 100}
        env.http_client.patch("/semesters/1/classes/4/assignments/1/feedback", json=patch_data)
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

    @testcase
    def test_getFeedbackNoFeedback(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments/1/feedback")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

    @testcase
    def test_putFeedbackNoFeedback(self, env, result):
        put_data = {"actualGrade" : 95, "feedback" : "Great Work!"}
        env.http_client.put("/semesters/2/classes/5/assignments/5/feedback", json=put_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

    @testcase
    def test_patchFeedbackNoFeedback(self, env, result):
        patch_data = {"actualGrade" : 100}
        env.http_client.patch("/semesters/1/classes/4/assignments/4/feedback", json=patch_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

    @testcase
    def test_getFeedbackEmpty(self, env, result):
        env.http_client.get("/semesters/1/classes/1/feedback")
        response = env.http_client.receive()

        assert response.json() == [], "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback endpoint"

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
    def test_postFeedbackWrongSemester(self, env, result):
        post_data = {"actualGrade" : 95, "feedback" : "Great Work!"}
        env.http_client.post("/semesters/1/classes/2/assignments/1/feedback", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

    @testcase
    def test_postFeedbackWrongClass(self, env, result):
        post_data = {"actualGrade" : 95, "feedback" : "Great Work!"}
        env.http_client.post("/semesters/1/classes/4/assignments/2/feedback", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"
    
    @testcase
    def test_postFeedback1(self, env, result):
        post_data = {"actualGrade" : 83, "feedback" : "Practice Reading"}
        env.http_client.post("/semesters/1/classes/1/assignments/1/feedback", json=post_data)
        response = env.http_client.receive()

        assert response.json() == "1", "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback endpoint"

    @testcase
    def test_postFeedback2(self, env, result):
        post_data = {"actualGrade" : 100, "feedback" : "Perfect"}
        env.http_client.post("/semesters/1/classes/4/assignments/4/feedback", json=post_data)
        response = env.http_client.receive()

        assert response.json() == "2", "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback endpoint"

    @testcase
    def test_postFeedback3(self, env, result):
        post_data = {"actualGrade" : 87, "feedback" : "Study Vocab"}
        env.http_client.post("/semesters/1/classes/1/assignments/2/feedback", json=post_data)
        response = env.http_client.receive()

        assert response.json() == "3", "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback endpoint"

    @testcase
    def test_postFeedback4(self, env, result):
        post_data = {"actualGrade" : 0, "feedback" : "Please Study"}
        env.http_client.post("/semesters/2/classes/5/assignments/5/feedback", json=post_data)
        response = env.http_client.receive()

        assert response.json() == "4", "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback endpoint"

    @testcase
    def test_postFeedbackAlreadyCreated(self, env, result):
        post_data = {"actualGrade" : 87, "feedback" : "Practice Math"}
        env.http_client.post("/semesters/1/classes/1/assignments/1/feedback", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback error"

    @testcase
    def test_getFeedbacksAfterPost(self, env, result):
        env.http_client.get("/semesters/1/classes/1/feedback")
        response = env.http_client.receive()

        expected_data = [{"id" : 1, "actualGrade" : 83, "feedback" : "Practice Reading"},
                         {"id" : 3, "actualGrade" : 87, "feedback" : "Study Vocab"}]

        assert response.json() == expected_data, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback endpoint"

    @testcase
    def test_getFeedbackAfterPost(self, env, result):
        env.http_client.get("/semesters/1/classes/4/assignments/4/feedback")
        response = env.http_client.receive()

        result.dict.match(
            response.json(), {"actualGrade" : 100, "expectedGrade" : 97, "gradePercentage" : 5.0, "feedback" : "Perfect"}, 
            "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id> endpoint"
        )

    @testcase
    def test_putFeedback(self, env, result):
        put_data = {"actualGrade" : 95, "feedback" : "Great Work!"}
        env.http_client.put("/semesters/1/classes/1/assignments/2/feedback", json=put_data)
        response = env.http_client.receive()

        assert response.json() == "3", "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback endpoint"

    @testcase
    def test_getFeedbacksAfterPut(self, env, result):
        env.http_client.get("/semesters/1/classes/1/feedback")
        response = env.http_client.receive()

        expected_data = [{"id" : 1, "actualGrade" : 83, "feedback" : "Practice Reading"},
                         {"id" : 3, "actualGrade" : 95, "feedback" : "Great Work!"}]
        
        assert response.json() == expected_data, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback endpoint"

    @testcase
    def test_getFeedbackAfterPut(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments/2/feedback")
        response = env.http_client.receive()

        result.dict.match(
            response.json(), {"actualGrade" : 95, "expectedGrade" : 100, "gradePercentage" : 0.074, "feedback" : "Great Work!"}, 
            "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id> endpoint"
        )

    @testcase
    def test_patchFeedback(self, env, result):
        patch_data = {"actualGrade" : 67}
        env.http_client.patch("/semesters/1/classes/1/assignments/2/feedback", json=patch_data)
        response = env.http_client.receive()

        assert response.json() == "3", "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback endpoint"

    @testcase
    def test_getFeedbacksAfterPatch(self, env, result):
        env.http_client.get("/semesters/1/classes/1/feedback")
        response = env.http_client.receive()
    
        expected_data = [{"id" : 1, "actualGrade" : 83, "feedback" : "Practice Reading"},
                         {"id" : 3, "actualGrade" : 67, "feedback" : "Great Work!"}]

        assert response.json() == expected_data, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback endpoint"

    @testcase
    def test_getFeedbackAfterPatch(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments/2/feedback")
        response = env.http_client.receive()

        result.dict.match(
            response.json(), {"actualGrade" : 67, "expectedGrade" : 100, "gradePercentage" : 0.074, "feedback" : "Great Work!"}, 
            "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id> endpoint"
        )

    @testcase
    def test_deleteAssignment4(self, env, result):
        env.http_client.delete("/assignments/4")
        response = env.http_client.receive()

        assert response.status_code == 204, "/assignments/<assignment_id> endpoint"

    @testcase
    def test_getFeedbacksAfterAssignmentDelete(self, env, result):
        env.http_client.get("/semesters/1/classes/4/feedback")
        response = env.http_client.receive()

        assert response.json() == [], "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback endpoint"

    @testcase
    def test_deleteClass5(self, env, result):
        env.http_client.delete("/class/5")
        response = env.http_client.receive()

        assert response.status_code == 204, "Verify /class/<class_id> endpoint"

    @testcase
    def test_postClass5Again(self, env, result):
        post_data = {"title" : "AI and Society", "credit" : 3, "subject" : "Humanities"}
        env.http_client.post("/semesters/2/classes", json=post_data)
        response = env.http_client.receive()
 
        assert response.json() == 5, "Verify /semesters/<semester_id>/classes endpoint"

    @testcase
    def test_getFeedbacksAfterClassDelete(self, env, result):
        env.http_client.get("/semesters/2/classes/5/feedback")
        response = env.http_client.receive()

        assert response.json() == [], "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback endpoint"

    @testcase
    def test_deleteSemester1(self, env, result):
        env.http_client.delete("/semesters/1")
        response = env.http_client.receive()

        assert response.status_code == 204, "Verify /semesters/<semester_id> endpoint"

    @testcase
    def test_deleteSemester2(self, env, result):
        env.http_client.delete("/semesters/2")
        response = env.http_client.receive()

        assert response.status_code == 204, "Verify /semesters/<semester_id> endpoint"