from testplan.testing.multitest import testsuite, testcase, MultiTest
import time

@testsuite
class AssignmentMultiTestSuite(object):
    @testcase
    def test_getAssignmentsBefore(self, env, result):
        env.http_client.get("/semesters/1/classes/1/assignments")
        response = env.http_client.receive()
        
        expected_data = [{"id": 1, "assignmentType": "Grade Assignment #2", "expectedTime": 40, "dueDate": "2023-10-03 11:59:59", "gradePercentage": 0.074},
                        {"id": 2, "assignmentType": "Grade Assignment #3", "expectedTime": 170, "dueDate": "2023-10-16 11:59:59", "gradePercentage": 0.074}]

        actual_data = response.json()
        
        assert actual_data == expected_data, "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"
    
    @testcase
    def test_getSemesterAssignmentTooSmall(self, env, result):
        env.http_client.get("/semesters/0/classes/1/assignments")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments error"

    @testcase
    def test_getSemesterAssignmentTooLarge(self, env, result):
        env.http_client.get("/semesters/8/classes/1/assignments")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments error"

    @testcase
    def test_getClassAssignmentTooSmall(self, env, result):
        env.http_client.get("/semesters/1/classes/0/assignments")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments error"

    @testcase
    def test_getClassAssignmentTooLarge(self, env, result):
        env.http_client.get("/semesters/1/classes/15/assignments")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments error"

    @testcase
    def test_getAssignmentTooSmall(self, env, result):
        env.http_client.get("/semesters/1/classes/15/assignments/0")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id> error"
    
    @testcase
    def test_getAssignmentTooLarge(self, env, result):
        env.http_client.get("/semesters/1/classes/15/assignments/10")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id> error"

    @testcase
    def test_getAssignmentWrongSemseter(self, env, result):
        env.http_client.get("/semesters/3/classes/2/assignments/1")
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id> error"

    @testcase
    def test_getAssignmentWrongClass(self, env, result):
        env.http_client.get("/semesters/1/classes/2/assignments/1")
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id> error"

    @testcase
    def test_postAssignmentSemesterTooSmall(self, env, result):
        post_data = {"assignmentType" : "Exam 3", "expectedTime" : 350, "dueDate" : "2023-11-7 12:35:00", "gradePercentage" : 10.0}
        env.http_client.post("/semesters/0/classes/2/assignments", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments error"
        
    @testcase
    def test_postAssignmentSemesterTooLarge(self, env, result):
        post_data = {"assignmentType" : "Exam 3", "expectedTime" : 350, "dueDate" : "2023-11-7 12:35:00", "gradePercentage" : 10.0}
        env.http_client.post("/semesters/65/classes/2/assignments", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments error"

    @testcase
    def test_postAssignmentClassTooSmall(self, env, result):
        post_data = {"assignmentType" : "Exam 3", "expectedTime" : 350, "dueDate" : "2023-11-7 12:35:00", "gradePercentage" : 10.0}
        env.http_client.post("/semesters/1/classes/0/assignments", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments error"

    @testcase
    def test_postAssignmentClassTooLarge(self, env, result):
        post_data = {"assignmentType" : "Exam 3", "expectedTime" : 350, "dueDate" : "2023-11-7 12:35:00", "gradePercentage" : 10.0}
        env.http_client.post("/semesters/1/classes/100/assignments", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id>/assignments error"

    @testcase
    def test_postAssignmentWrongSemester(self, env, result):
        post_data = {"assignmentType" : "Exam 3", "expectedTime" : 350, "dueDate" : "2023-11-7 12:35:00", "gradePercentage" : 10.0}
        env.http_client.post("/semesters/3/classes/2/assignments", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id> error"

    # @testcase
    # def test_postAssignment(self, env, result):
    #     post_data = {"assignmentType" : "Exam 3", "expectedTime" : 350, "dueDate" : "2023-11-7 12:35:00", "gradePercentage" : 10.0}
    #     env.http_client.post("/semesters/1/classes/2/assignments", json=post_data)
    #     response = env.http_client.receive()

    #     actual_data = response.json()
    #     assert actual_data == 3, "Verify /semesters/<semester_id>/classes/<class_id>/assignments endpoint"

    @testcase
    def test_getAssignment(self, env, result):
        env.http_client.get("/semesters/1/classes/2/assignments/3")
        response = env.http_client.receive()

        result.dict.match(
            response.json(), {"assignmentType": "Exam 3", "expectedTime": 350, "dueDate": "2023-11-07 12:35:00", "gradePercentage": 10.0}, 
            "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id> endpoint"
        )
    
    # @testcase
    # def test_getAssignment(self, env, result):
    #     env.http_client.get("/semesters/1/classes/1/assignments/2")
    #     response = env.http_client.receive()

    #     result.dict.match(
    #         response.json(), {"assignmentType": "Grade Assignment #3", "expectedTime": 170, "dueDate": "2023-10-16 11:59:59", "gradePercentage": 0.074}, 
    #         "Verify /semesters/<semester_id>/classes/<class_id>/assignments/<assignment_id> endpoint"
    #     )