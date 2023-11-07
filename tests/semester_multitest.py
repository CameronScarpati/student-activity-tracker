from testplan.testing.multitest import testsuite, testcase, MultiTest
import time

@testsuite
class SemesterMultiTestSuite(object):
    @testcase
    def test_getSemestersEmpty(self, env, result):
        env.http_client.get("/semesters")
        response = env.http_client.receive()
        
        assert response.json() == [], "Verify /semesters endpoint"

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
    def test_postSemesters3(self, env, result):
        post_data = {"semester": "Summer 2024"}
        env.http_client.post("/semesters", json=post_data)
        response = env.http_client.receive()
        
        assert response.json() == 3, "Verify /semesters endpoint"

    @testcase
    def test_postSemesters4(self, env, result):
        post_data = {"semester": "Fall 2024"}
        env.http_client.post("/semesters", json=post_data)
        response = env.http_client.receive()
        
        assert response.json() == 4, "Verify /semesters endpoint"

    @testcase
    def test_postSemesters5(self, env, result):
        post_data = {"semester": "Spring 2025"}
        env.http_client.post("/semesters", json=post_data)
        response = env.http_client.receive()
        
        assert response.json() == 5, "Verify /semesters endpoint"

    @testcase
    def test_getSemestersFull(self, env, result):
        env.http_client.get("/semesters")
        response = env.http_client.receive()

        expected_data = [{"id" : 1, "semester" : "Fall 2023"},
                         {"id" : 2, "semester" : "Spring 2024"},
                         {"id" : 3, "semester" : "Summer 2024"},
                         {"id" : 4, "semester" : "Fall 2024"},
                         {"id" : 5, "semester" : "Spring 2025"}]
        
        assert response.json() == expected_data, "Verify /semesters endpoint"

    @testcase
    def test_postSemestersSameName(self, env, result):
        post_data = {"semester": "Fall 2024"}
        env.http_client.post("/semesters", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters error"

    @testcase
    def test_getSemester2(self, env, result):
        env.http_client.get("/semesters/2")
        response = env.http_client.receive()

        result.dict.match(
            response.json(), {"id": 2, "semester": "Spring 2024"}, 
            "Verify /semesters/<semester_id> endpoint"
        )
    
    @testcase
    def test_deleteSemester2(self, env, result):
        env.http_client.delete("/semesters/2")
        response = env.http_client.receive()

        assert response.status_code == 204, "Verify /semesters/<semester_id> endpoint"

    @testcase
    def test_getSemesterHoleError(self, env, result):
        env.http_client.get("/semesters/2")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id> error"

    @testcase
    def test_getSemesterTooSmall(self, env, result):
        env.http_client.get("/semesters/0")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id> error"

    @testcase
    def test_getSemesterTooLarge(self, env, result):
        env.http_client.get("/semesters/6")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id> error"

    @testcase
    def test_deleteSemesterHoleError(self, env, result):
        env.http_client.delete("/semesters/2")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id> error"

    @testcase
    def test_deleteSemesterTooSmall(self, env, result):
        env.http_client.delete("/semesters/0")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id> error"

    @testcase
    def test_deleteSemesterTooLarge(self, env, result):
        env.http_client.delete("/semesters/6")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id> error"

    @testcase
    def test_deleteSemester5(self, env, result):
        env.http_client.delete("/semesters/5")
        response = env.http_client.receive()

        assert response.status_code == 204, "Verify /semesters/<semester_id> endpoint"

    @testcase
    def test_getSemestersAfterDelete(self, env, result):
        env.http_client.get("/semesters")
        response = env.http_client.receive()

        expected_data = [{"id" : 1, "semester" : "Fall 2023"},
                         {"id" : 3, "semester" : "Summer 2024"},
                         {"id" : 4, "semester" : "Fall 2024"}]
        
        assert response.json() == expected_data, "Verify /semesters endpoint"

    @testcase
    def test_postSemestersAfterDelete(self, env, result):
        post_data = {"semester": "Spring 2025"}
        env.http_client.post("/semesters", json=post_data)
        response = env.http_client.receive()
        
        assert response.json() == 5, "Verify /semesters endpoint"

    @testcase
    def test_clearTable1(self, env, result):
        env.http_client.delete("/semesters/1")
        response = env.http_client.receive()

        assert response.status_code == 204

    @testcase
    def test_clearTable3(self, env, result):
        env.http_client.delete("/semesters/3")
        response = env.http_client.receive()

        assert response.status_code == 204

    @testcase
    def test_clearTable4(self, env, result):
        env.http_client.delete("/semesters/4")
        response = env.http_client.receive()

        assert response.status_code == 204

    @testcase
    def test_clearTable5(self, env, result):
        env.http_client.delete("/semesters/5")
        response = env.http_client.receive()
        
        assert response.status_code == 204