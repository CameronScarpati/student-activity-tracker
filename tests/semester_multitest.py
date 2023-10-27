from testplan.testing.multitest import testsuite, testcase, MultiTest
import time

@testsuite
class SemesterMultiTestSuite(object):
    @testcase
    def test_get(self, env, result):
        env.http_client.get("/semesters")
        response = env.http_client.receive()
        
        expected_data = [{"id": 1, "semester": "Fall 2023"},
                        {"id": 2, "semester": "Spring 2024"},
                        {"id": 3, "semester": "Summer 2024"},
                        {"id": 4, "semester": "Fall 2025"},
                        {"id": 5, "semester": "Spring 2026"},
                        {"id": 6, "semester": "Summer 2026"},
                        {"id": 7, "semester": "Fall 2026"}]
        
        actual_data = response.json()
        assert actual_data == expected_data, "Verify /semester endpoint"

    # @testcase
    # def test_post(self, env, result):
    #     post_data = {"semester": "Fall 2026"}
    #     env.http_client.post("/semesters", json=post_data)
    #     response = env.http_client.receive()
        
    #     actual_data = response.json()
    #     assert actual_data == 7, "Verify /semester endpoint"

    @testcase
    def test_getSpecificNoClasses(self, env, result):
        env.http_client.get("/semesters/7")
        response = env.http_client.receive()

        result.dict.match(
            response.json(), {"id": 7, "semester": "Fall 2026", "classes": []}, "Verify /semester endpoint"
        )

    @testcase
    def test_getSemesterClasses(self, env, result):
        env.http_client.get("/semesters/1")
        response = env.http_client.receive()

        result.dict.match(
            response.json(), {"id": 1, "semester": "Fall 2023", "classes": [1,2,3,4,5]}, "Verify /semester endpoint"
        )

    @testcase
    def test_getSemesterTooSmall(self, env, result):
        env.http_client.get("/semesters/0")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semester/<semester_id> error"

    @testcase
    def test_getSemesterTooLarge(self, env, result):
        env.http_client.get("/semesters/8")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semester/<semester_id> error"

        post_data = {"title" : "Methods of Linear Algebra", "credit" : "3", "subject": "Mathematics"}
        env.http_client.post("/semesters/0/classes", json=post_data)
        response = env.http_client.receive()