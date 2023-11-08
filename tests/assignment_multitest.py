from testplan.testing.multitest import testsuite, testcase, MultiTest

@testsuite
class AssignmentMultiTestSuite(object):
    @testcase
    def test_getAssignmentsNoSemester(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments error"
    
    @testcase
    def test_postSemesters1(self, env, result):
        post_data = {"semester": "Fall 2023"}
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
    def test_getAssignmentsNoClass(self, env, result):
        env.http_client.get("/semesters/2/classes/1/assignments")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments error"

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
        env.http_client.post("/semesters/2/classes", json=post_data)
        response = env.http_client.receive()

        assert response.json() == 4, "Verify /semesters/<semester_id>/classes endpoint"

    @testcase
    def test_postClass5(self, env, result):
        post_data = {"title" : "AI and Society", "credit" : 3, "subject" : "Humanities"}
        env.http_client.post("/semesters/2/classes", json=post_data)
        response = env.http_client.receive()

        assert response.json() == 5, "Verify /semesters/<semester_id>/classes endpoint"

    @testcase
    def test_getAssignmentWrongSemester(self, env, result):
        env.http_client.get("/semesters/2/classes/1/assignments")
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id>/assignments error"

    @testcase
    def test_getAssignmentsEmpty(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments")
        response = env.http_client.receive()

        assert response.json() == [], "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

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
        env.http_client.post("/semesters/1/classes/3/assignments", json=post_data)
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
        env.http_client.post("/semesters/2/classes/4/assignments", json=post_data)
        response = env.http_client.receive()

        assert response.json() == 6, "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

    @testcase
    def test_getAssignmentsAfterPost(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments")
        response = env.http_client.receive()

        expected_data = [{"id" : 1, "assignmentType" : "Exam", "expectedTime" : 350, "dueDate" : "2023-11-07 12:35:00", "gradePercentage" : 10.0},
                         {"id" : 2, "assignmentType" : "Homework", "expectedTime" : 120, "dueDate" : "2023-10-01 13:25:00", "gradePercentage" : 0.074}]

        assert response.json() == expected_data, "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

    @testcase
    def test_getAssignment3(self, env, result):
        env.http_client.get("/semesters/1/classes/2/assignments/3")
        response = env.http_client.receive()

        result.dict.match(
            response.json(), {"assignmentType" : "Presentation", "expectedTime" : 20, "dueDate" : "2023-10-31 10:15:00", "gradePercentage" : 2.0}, 
            "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id> endpoint"
        )

    @testcase
    def test_deleteAssignment3(self, env, result):
        env.http_client.delete("/assignments/3")
        response = env.http_client.receive()

        assert response.status_code == 204, "/assignments/<assignment_id> endpoint"

    @testcase
    def test_getAssignmentHoleError(self, env, result):
        env.http_client.get("/semesters/1/classes/2/assignments/3")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id> error"

    @testcase
    def test_getAssignmentTooSmall(self, env, result):
        env.http_client.get("/semesters/1/classes/2/assignments/0")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id> error"

    @testcase
    def test_getAssignmentTooLarge(self, env, result):
        env.http_client.get("/semesters/1/classes/2/assignments/7")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id> error"

    @testcase
    def test_getAssignmentNoSemester(self, env, result):
        env.http_client.get("/semesters/3/classes/2/assignments/2")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id> error"

    @testcase
    def test_getAssignmentNoClass(self, env, result):
        env.http_client.get("/semesters/1/classes/0/assignments/4")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id> error"

    @testcase
    def test_deleteAssignment5(self, env, result):
        env.http_client.delete("/assignments/5")
        response = env.http_client.receive()

        assert response.status_code == 204, "/assignments/<assignment_id> endpoint"
    
    @testcase
    def test_postAssignmentAfterDelete(self, env, result):
        post_data = {"assignmentType" : "Exam 2", "expectedTime" : 160, "dueDate" : "2023-11-15 16:30:00", "gradePercentage" : 17.5}
        env.http_client.post("/semesters/1/classes/1/assignments", json=post_data)
        response = env.http_client.receive()

        assert response.json() == 7, "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

    @testcase
    def test_postAssignmentNoSemester(self, env, result):
        post_data = {"assignmentType" : "Homework 2", "expectedTime" : 55, "dueDate" : "2023-11-10 12:30:00", "gradePercentage" : 2.5}
        env.http_client.post("/semesters/0/classes/1/assignments", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments error"

    @testcase
    def test_postAssignmentNoClass(self, env, result):
        post_data = {"assignmentType" : "Homework 2", "expectedTime" : 55, "dueDate" : "2023-11-10 12:30:00", "gradePercentage" : 2.5}
        env.http_client.post("/semesters/1/classes/6/assignments", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments error"

    @testcase
    def test_postAssignmentWrongSemester(self, env, result):
        post_data = {"assignmentType" : "Homework 2", "expectedTime" : 55, "dueDate" : "2023-11-10 12:30:00", "gradePercentage" : 2.5}
        env.http_client.post("/semesters/2/classes/2/assignments", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id>/assignments error"

    @testcase
    def test_deleteAssignmentHoleError(self, env, result):
        env.http_client.delete("/assignments/3")
        response = env.http_client.receive()

        assert response.status_code == 404, "/assignments/<assignment_id> error"

    @testcase
    def test_deleteAssignmentTooSmall(self, env, result):
        env.http_client.delete("/assignments/0")
        response = env.http_client.receive()

        assert response.status_code == 404, "/assignments/<assignment_id> error"

    @testcase
    def test_deleteAssignmentTooLarge(self, env, result):
        env.http_client.delete("/assignments/8")
        response = env.http_client.receive()

        assert response.status_code == 404, "/assignments/<assignment_id> error"

    @testcase
    def test_getAssignmentsAfterDelete(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments")
        response = env.http_client.receive()

        expected_data = [{"id" : 1, "assignmentType" : "Exam", "expectedTime" : 350, "dueDate" : "2023-11-07 12:35:00", "gradePercentage" : 10.0},
                         {"id" : 2, "assignmentType" : "Homework", "expectedTime" : 120, "dueDate" : "2023-10-01 13:25:00", "gradePercentage" : 0.074},
                         {"id" : 7, "assignmentType" : "Exam 2", "expectedTime" : 160, "dueDate" : "2023-11-15 16:30:00", "gradePercentage" : 17.5}]

        assert response.json() == expected_data, "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

    @testcase
    def test_deleteClass1(self, env, result):
        env.http_client.delete("/class/1")
        response = env.http_client.receive()

        assert response.status_code == 204, "Verify /class/<class_id> endpoint"

    @testcase
    def test_getAssignmentsAfterClassDelete(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments error"

    @testcase
    def test_getAssignmentAfterClassDelete(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments/5")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id> error"

    @testcase
    def test_postAssignmentsAfterClassDelete(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments error"

    @testcase
    def test_getAssignmentsCheckForFalseRemovalClass(self, env, result):
        env.http_client.get("/semesters/1/classes/2/assignments")
        response = env.http_client.receive()
      
        assert response.json() == [], "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

    @testcase
    def test_getAssignmentCheckForFalseRemovalClass(self, env, result):
        env.http_client.get("/semesters/1/classes/3/assignments/4")
        response = env.http_client.receive()
        
        result.dict.match(
            response.json(), {"assignmentType" : "Project", "expectedTime" : 250, "dueDate" : "2023-10-05 15:25:00", "gradePercentage" : 5.0}, 
            "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id> endpoint"
        )

    @testcase
    def test_deleteSemester1(self, env, result):
        env.http_client.delete("/semesters/1")
        response = env.http_client.receive()

        assert response.status_code == 204, "Verify /semesters/<semester_id> endpoint"

    @testcase
    def test_getAssignmentsAfterSemesterDelete(self, env, result):
        env.http_client.get("/semesters/1/classes/2/assignments")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments error"

    @testcase
    def test_getAssignmentAfterSemesterDelete(self, env, result):
        env.http_client.get("/semesters/1/classes/2/assignments/5")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id> error"

    @testcase
    def test_postAssignmentsAfterSemesterDelete(self, env, result):
        env.http_client.get("/semesters/1/classes/3/assignments")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments error"

    @testcase
    def test_getAssignmentsCheckForFalseRemovalSemester(self, env, result):
        env.http_client.get("/semesters/2/classes/5/assignments")
        response = env.http_client.receive()

        assert response.json() == [], "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

    @testcase
    def test_getAssignmentCheckForFalseRemovalSemester(self, env, result):
        env.http_client.get("/semesters/2/classes/4/assignments/6")
        response = env.http_client.receive()
        
        result.dict.match(
            response.json(), {"assignmentType" : "Quiz", "expectedTime" : 35, "dueDate" : "2023-11-19 10:45:00", "gradePercentage" : 8.2}, 
            "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id> endpoint"
        )

    @testcase
    def test_deleteSemester2(self, env, result):
        env.http_client.delete("/semesters/2")
        response = env.http_client.receive()

        assert response.status_code == 204, "Verify /semesters/<semester_id> endpoint"