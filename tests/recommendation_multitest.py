from testplan.testing.multitest import testsuite, testcase, MultiTest

@testsuite
class RecommendationMultiTestSuite(object):
    @testcase
    def test_getRecommendationNoSemester(self, env, result):
        env.http_client.get("/semesters/1/recommendation")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/recommendation error"

    @testcase
    def test_postSemesters1(self, env, result):
        post_data = {"semester" : "Fall 2023"}
        env.http_client.post("/semesters", json=post_data)
        response = env.http_client.receive()
        
        assert response.json() == 1, "Verify /semesters endpoint"

    @testcase
    def test_getRecommendationNoAssignment(self, env, result):
        env.http_client.get("/semesters/1/recommendation")
        response = env.http_client.receive()

        assert response.json() == "All Assignments Completed", "Verify /semesters/<semester_id>/recommendation endpoint"

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
        post_data = {"assignmentType" : "Exam", "expectedTime" : 350, "dueDate" : "2023-11-08 12:35:00", "gradePercentage" : 10.0}
        env.http_client.post("/semesters/1/classes/1/assignments", json=post_data)
        response = env.http_client.receive()

        assert response.json() == 1, "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

    @testcase
    def test_postAssignments2(self, env, result):
        post_data = {"assignmentType" : "Homework", "expectedTime" : 120, "dueDate" : "2023-11-10 13:25:00", "gradePercentage" : 0.074}
        env.http_client.post("/semesters/1/classes/1/assignments", json=post_data)
        response = env.http_client.receive()

        assert response.json() == 2, "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

    @testcase
    def test_postAssignments3(self, env, result):
        post_data = {"assignmentType" : "Presentation", "expectedTime" : 20, "dueDate" : "2023-11-15 10:15:00", "gradePercentage" : 2.0}
        env.http_client.post("/semesters/1/classes/2/assignments", json=post_data)
        response = env.http_client.receive()

        assert response.json() == 3, "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

    @testcase
    def test_postAssignments4(self, env, result):
        post_data = {"assignmentType" : "Project", "expectedTime" : 250, "dueDate" : "2023-11-09 15:25:00", "gradePercentage" : 5.0}
        env.http_client.post("/semesters/1/classes/3/assignments", json=post_data)
        response = env.http_client.receive()

        assert response.json() == 4, "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

    @testcase
    def test_postAssignments5(self, env, result):
        post_data = {"assignmentType" : "Reading", "expectedTime" : 90, "dueDate" : "2023-11-12 8:45:00", "gradePercentage" : 6.5}
        env.http_client.post("/semesters/1/classes/5/assignments", json=post_data)
        response = env.http_client.receive()

        assert response.json() == 5, "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

    @testcase
    def test_postAssignments6(self, env, result):
        post_data = {"assignmentType" : "Reading", "expectedTime" : 60, "dueDate" : "2023-11-08 8:45:00", "gradePercentage" : 0.5}
        env.http_client.post("/semesters/1/classes/5/assignments", json=post_data)
        response = env.http_client.receive()

        assert response.json() == 6, "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

    @testcase
    def test_postAssignments7(self, env, result):
        post_data = {"assignmentType" : "Reading", "expectedTime" : 115, "dueDate" : "2023-11-14 8:45:00", "gradePercentage" : 0.5}
        env.http_client.post("/semesters/1/classes/5/assignments", json=post_data)
        response = env.http_client.receive()

        assert response.json() == 7, "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

    @testcase
    def test_postSubmissions1(self, env, result):
        post_data = {"actualTime" : 300, "expectedGrade" : 78}
        env.http_client.post("/semesters/1/classes/3/assignments/4/submissions", json=post_data)
        response = env.http_client.receive()

        actual_data = response.json()
        indexOfComma = actual_data.index(",")
        actual_data = actual_data[:indexOfComma]
        assert actual_data == "1", "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions endpoint"

    @testcase
    def test_postSubmissions2(self, env, result):
        post_data = {"actualTime" : 320, "expectedGrade" : 88}
        env.http_client.post("/semesters/1/classes/5/assignments/6/submissions", json=post_data)
        response = env.http_client.receive()

        actual_data = response.json()
        indexOfComma = actual_data.index(",")
        actual_data = actual_data[:indexOfComma]
        assert actual_data == "2", "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions endpoint"

    @testcase
    def test_postSubmissions3(self, env, result):
        post_data = {"actualTime" : 40, "expectedGrade" : 85}
        env.http_client.post("/semesters/1/classes/5/assignments/7/submissions", json=post_data)
        response = env.http_client.receive()

        actual_data = response.json()
        indexOfComma = actual_data.index(",")
        actual_data = actual_data[:indexOfComma]
        assert actual_data == "3", "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions endpoint"

    @testcase
    def test_getRecommendation(self, env, result):
        env.http_client.get("/semesters/1/recommendation")
        response = env.http_client.receive()

        assert response.json() == 1, "Verify /semesters/<semester_id>/recommendation endpoint"

    @testcase
    def test_postSubmissions4(self, env, result):
        post_data = {"actualTime" : 400, "expectedGrade" : 100}
        env.http_client.post("/semesters/1/classes/1/assignments/1/submissions", json=post_data)
        response = env.http_client.receive()

        actual_data = response.json()
        indexOfComma = actual_data.index(",")
        actual_data = actual_data[:indexOfComma]
        assert actual_data == "4", "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id>/submissions endpoint"

    @testcase
    def test_getRecommendationAfterSubmission(self, env, result):
        env.http_client.get("/semesters/1/recommendation")
        response = env.http_client.receive()

        assert response.json() == 5, "Verify /semesters/<semester_id>/recommendation endpoint"

    @testcase
    def test_deleteClass1(self, env, result):
        env.http_client.delete("/class/1")
        response = env.http_client.receive()

        assert response.status_code == 204, "Verify /class/<class_id> endpoint"

    @testcase
    def test_getRecommendationAfterClassDelete(self, env, result):
        env.http_client.get("/semesters/1/recommendation")
        response = env.http_client.receive()

        assert response.json() == 5, "Verify /semesters/<semester_id>/recommendation endpoint"

    @testcase
    def test_deleteSemester1(self, env, result):
        env.http_client.delete("/semesters/1")
        response = env.http_client.receive()

        assert response.status_code == 204, "Verify /semesters/<semester_id> endpoint"