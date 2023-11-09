from testplan.testing.multitest import testsuite, testcase, MultiTest

@testsuite
class ExpectationMultiTestSuite(object):
    @testcase
    def test_getExpectedGradesNoSemester(self, env, result):
        env.http_client.get("/semesters/1/expectedGrades")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /classes/<class_id>/grade error"

    @testcase
    def test_getExpectedTimesNoSemester(self, env, result):
        env.http_client.get("/classes/1/expectedTimes")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /classes/<class_id>/grade error"

    @testcase
    def test_postSemesters1(self, env, result):
        post_data = {"semester": "Fall 2023"}
        env.http_client.post("/semesters", json=post_data)
        response = env.http_client.receive()
        
        assert response.json() == 1, "Verify /semesters endpoint"

    @testcase
    def test_getExpectedGradesNoFeedback(self, env, result):
        env.http_client.get("/semesters/1/expectedGrades")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /classes/<class_id>/grade error"

    @testcase
    def test_getExpectedTimesNoFeedback(self, env, result):
        env.http_client.get("/classes/1/expectedTimes")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /classes/<class_id>/grade error"

    @testcase
    def test_postClass1(self, env, result):
        post_data = {"title" : "Multivariable Calculus", "credit" : 3, "subject" : "Mathematics"}
        env.http_client.post("/semesters/1/classes", json=post_data)
        response = env.http_client.receive()

        assert response.json() == 1, "Verify /semesters/<semester_id>/classes endpoint"

    @testcase
    def test_postClass2(self, env, result):
        post_data = {"title" : "Storytelling as Performance", "credit" : 3, "subject" : "Theater"}
        env.http_client.post("/semesters/1/classes", json=post_data)
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
        env.http_client.post("/semesters/1/classes", json=post_data)
        response = env.http_client.receive()

        assert response.json() == 5, "Verify /semesters/<semester_id>/classes endpoint"

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
        env.http_client.post("/semesters/1/classes/2/assignments", json=post_data)
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
        env.http_client.post("/semesters/1/classes/5/assignments", json=post_data)
        response = env.http_client.receive()

        assert response.json() == 5, "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

    @testcase
    def test_postAssignments6(self, env, result):
        post_data = {"assignmentType" : "Quiz", "expectedTime" : 35, "dueDate" : "2023-11-19 10:45:00", "gradePercentage" : 8.2}
        env.http_client.post("/semesters/1/classes/2/assignments", json=post_data)
        response = env.http_client.receive()

        assert response.json() == 6, "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

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
        env.http_client.post("/semesters/1/classes/5/assignments/5/submissions", json=post_data)
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
    def test_postSubmissions8(self, env, result):
        post_data = {"actualTime" : 105, "expectedGrade" : 92}
        env.http_client.post("/semesters/1/classes/2/assignments/6/submissions", json=post_data)
        response = env.http_client.receive()

        actual_data = response.json()
        indexOfComma = actual_data.index(",")
        actual_data = actual_data[:indexOfComma]
        assert actual_data == "8", "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions endpoint"

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
        env.http_client.post("/semesters/1/classes/5/assignments/5/feedback", json=post_data)
        response = env.http_client.receive()

        assert response.json() == "4", "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback endpoint"

    @testcase
    def test_getExpectedGrades(self, env, result):
        env.http_client.get("/semesters/1/expectedGrades")
        response = env.http_client.receive()

        expected_data = [{"expectedGrade" : 88.0, "actualGrade" : 83.0},
                         {"expectedGrade" : 97.0, "actualGrade" : 100.0},
                         {"expectedGrade" : 100.0, "actualGrade" : 87.0},
                         {"expectedGrade" : 100.0, "actualGrade" : 0.0}]

        assert response.json() == expected_data, "Verify /classes/<class_id>/grade endpoint"

    @testcase
    def test_getExpectedTimes(self, env, result):
        env.http_client.get("/semesters/1/expectedTimes")
        response = env.http_client.receive()

        expected_data = [{"expectedTime" : 350.0, "actualTime" : 320.0},
                         {"expectedTime" : 120.0, "actualTime" : 70.0},
                         {"expectedTime" : 250.0, "actualTime" : 55.0},
                         {"expectedTime" : 90.0, "actualTime" : 70.0},
                         {"expectedTime" : 35.0, "actualTime" : 105.0}]

        assert response.json() == expected_data, "Verify /classes/<class_id>/grade endpoint"

    @testcase
    def test_putFeedback(self, env, result):
        put_data = {"actualGrade" : 82.5, "feedback" : "Late Assignment"}
        env.http_client.put("/semesters/1/classes/5/assignments/5/feedback", json=put_data)
        response = env.http_client.receive()

        assert response.json() == "4", "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback endpoint"

    @testcase
    def test_getExpectedGradesAfterPut(self, env, result):
        env.http_client.get("/semesters/1/expectedGrades")
        response = env.http_client.receive()

        expected_data = [{"expectedGrade" : 88.0, "actualGrade" : 83.0},
                         {"expectedGrade" : 97.0, "actualGrade" : 100.0},
                         {"expectedGrade" : 100.0, "actualGrade" : 87.0},
                         {"expectedGrade" : 100.0, "actualGrade" : 82.5}]

        assert response.json() == expected_data, "Verify /classes/<class_id>/grade endpoint"

    @testcase
    def test_patchFeedback(self, env, result):
        patch_data = {"actualGrade" : 95.0}
        env.http_client.patch("/semesters/1/classes/4/assignments/4/feedback", json=patch_data)
        response = env.http_client.receive()

        assert response.json() == "2", "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/feedback endpoint"

    @testcase
    def test_getExpectedGradesAfterPatch(self, env, result):
        env.http_client.get("/semesters/1/expectedGrades")
        response = env.http_client.receive()

        expected_data = [{"expectedGrade" : 88.0, "actualGrade" : 83.0},
                         {"expectedGrade" : 97.0, "actualGrade" : 95.0},
                         {"expectedGrade" : 100.0, "actualGrade" : 87.0},
                         {"expectedGrade" : 100.0, "actualGrade" : 82.5}]

        assert response.json() == expected_data, "Verify /classes/<class_id>/grade endpoint"

    @testcase
    def test_deleteAssignment6(self, env, result):
        env.http_client.delete("/assignments/6")
        response = env.http_client.receive()

        assert response.status_code == 204, "/assignments/<assignment_id> endpoint"

    @testcase
    def test_getExpectedGradesAfterAssignmentDelete(self, env, result):
        env.http_client.get("/semesters/1/expectedGrades")
        response = env.http_client.receive()

        expected_data = [{"expectedGrade" : 88.0, "actualGrade" : 83.0},
                         {"expectedGrade" : 97.0, "actualGrade" : 95.0},
                         {"expectedGrade" : 100.0, "actualGrade" : 87.0},
                         {"expectedGrade" : 100.0, "actualGrade" : 82.5}]

        assert response.json() == expected_data, "Verify /classes/<class_id>/grade endpoint"

    @testcase
    def test_getExpectedTimesAfterAssignmentDelete(self, env, result):
        env.http_client.get("/semesters/1/expectedTimes")
        response = env.http_client.receive()

        expected_data = [{"expectedTime" : 350.0, "actualTime" : 320.0},
                         {"expectedTime" : 120.0, "actualTime" : 70.0},
                         {"expectedTime" : 250.0, "actualTime" : 55.0},
                         {"expectedTime" : 90.0, "actualTime" : 70.0}]

        assert response.json() == expected_data, "Verify /classes/<class_id>/grade endpoint"

    @testcase
    def test_deleteClass1(self, env, result):
        env.http_client.delete("/class/1")
        response = env.http_client.receive()

        assert response.status_code == 204, "Verify /class/<class_id> endpoint"

    @testcase
    def test_getExpectedGradesAfterClassDelete(self, env, result):
        env.http_client.get("/semesters/1/expectedGrades")
        response = env.http_client.receive()

        expected_data = [{"expectedGrade" : 97.0, "actualGrade" : 95.0},
                         {"expectedGrade" : 100.0, "actualGrade" : 82.5}]

        assert response.json() == expected_data, "Verify /classes/<class_id>/grade endpoint"

    @testcase
    def test_getExpectedTimesAfterClassDelete(self, env, result):
        env.http_client.get("/semesters/1/expectedTimes")
        response = env.http_client.receive()

        expected_data = [{"expectedTime" : 250.0, "actualTime" : 55.0},
                         {"expectedTime" : 90.0, "actualTime" : 70.0}]

        assert response.json() == expected_data, "Verify /classes/<class_id>/grade endpoint"

    @testcase
    def test_deleteSemester1(self, env, result):
        env.http_client.delete("/semesters/1")
        response = env.http_client.receive()

        assert response.status_code == 204, "Verify /semesters/<semester_id> endpoint"