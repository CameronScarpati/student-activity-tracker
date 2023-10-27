from testplan.testing.multitest import testsuite, testcase, MultiTest
import time

@testsuite
class ClassMultiTestSuite(object):
    # @testcase
    # def test_getClassesBefore(self, env, result):
    #     env.http_client.get("/semesters/2/classes")
    #     response = env.http_client.receive()
        
    #     expected_data = [{ "id": 6, "title": "Algorithms","credit": 3, "subject": "Computer Science"}]
        
    #     actual_data = response.json()
    #     assert actual_data == expected_data, "Verify /semesters/<semester_id>/classes endpoint"

    @testcase
    def test_getSemesterTooSmall(self, env, result):
        env.http_client.get("/semesters/0/classes")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semester/<semester_id>/classes error"

    @testcase
    def test_getSemesterTooLarge(self, env, result):
        env.http_client.get("/semesters/8/classes")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes error"

    @testcase
    def test_postSemesterClassTooSmall(self, env, result):
        post_data = {"title" : "Methods of Linear Algebra", "credit" : "3", "subject": "Mathematics"}
        env.http_client.post("/semesters/0/classes", json=post_data)
        response = env.http_client.receive()
        
        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes error"

    @testcase
    def test_postSemesterClassTooLarge(self, env, result):
        post_data = {"title" : "Methods of Linear Algebra", "credit" : "3", "subject": "Mathematics"}
        env.http_client.post("/semesters/15/classes", json=post_data)
        response = env.http_client.receive()
        
        assert response.status_code == 404, "Verify /semesters/<semester_id> error/classes"

    @testcase
    def test_getClassTooSmall(self, env, result):
        env.http_client.get("/semesters/1/classes/0")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id> error"

    # @testcase
    # def test_getClassTooLarge(self, env, result):
    #     env.http_client.get("/semesters/2/classes/7")
    #     response = env.http_client.receive()

    #     assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id> error"

    # @testcase
    # def test_post(self, env, result):
    #     post_data = {"title" : "Methods of Linear Algebra", "credit" : "3", "subject": "Mathematics"}
    #     env.http_client.post("/semesters/2/classes", json=post_data)
    #     response = env.http_client.receive()
        
    #     actual_data = response.json()
    #     assert actual_data == 7, "Verify /semesters/<semester_id>/classes endpoint"

    @testcase
    def test_getClassesAfter(self, env, result):
        env.http_client.get("/semesters/2/classes")
        response = env.http_client.receive()

        expected_data = [{ "id": 6, "title": "Algorithms","credit": 3, "subject": "Computer Science" },
                        { "id": 7, "title": "Methods of Linear Algebra", "credit": 3, "subject": "Mathematics" }]
        
        actual_data = response.json()
        assert actual_data == expected_data, "Verify /semesters/<semester_id>/classes endpoint"

    @testcase
    def test_getClass(self, env, result):
        env.http_client.get("/semesters/2/classes/7")
        response = env.http_client.receive()

        result.dict.match(
            response.json(), {"id": 7, "title" : "Methods of Linear Algebra", "credit" : 3, "subject": "Mathematics"}, 
            "Verify /semesters/<semester_id>/classes/<class_id> endpoint"
        )

    @testcase
    def test_getWrongSemester(self, env, result):
        env.http_client.get("/semesters/1/classes/7")
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id> error"