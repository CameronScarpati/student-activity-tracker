from testplan.testing.multitest import testsuite, testcase, MultiTest
import time

@testsuite
class SemesterMultiTestSuite(object):
    @testcase
    def test_get(self, env, result):
        env.http_client.get("/semesters")
        response = env.http_client.receive()
        
        expected_data = [{"id": 1, "semester": "Fall 2023"},
                        {"id": 2, "semester": "Summer 2024"},
                        {"id": 3, "semester": "Fall 2024"},
                        {"id": 4, "semester": "Spring 2025"},
                        {"id": 5, "semester": "Summer 2025"},
                        {"id": 6, "semester": "Fall 2025"}]
        
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
        env.http_client.get("/semesters/6")
        response = env.http_client.receive()

        result.dict.match(
            response.json(), {"id": 6, "semester": "Fall 2025", "classes": []}, "Verify /semester endpoint"
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