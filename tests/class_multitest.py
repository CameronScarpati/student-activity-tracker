from testplan.testing.multitest import testsuite, testcase, MultiTest

@testsuite
class ClassMultiTestSuite(object):
    @testcase
    def test_getClassNoSemester(self, env, result):
        env.http_client.get("/semesters/1/classes")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semester/<semester_id>/classes error"

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
    def test_getClassesAfterPost(self, env, result):
        env.http_client.get("/semesters/1/classes")
        response = env.http_client.receive()
        
        expected_data = [{ "id" : 1, "title" : "Multivariable Calculus", "credit": 3, "subject" : "Mathematics"},
                         { "id" : 2, "title" : "Storytelling as Performance", "credit": 3, "subject" : "Theater"},
                         { "id" : 3, "title" : "Program Design and Data Structures", "credit": 3, "subject" : "Computer Science"},
                         { "id" : 4, "title" : "Atlantic History in the Digital Age", "credit": 3, "subject" : "History"},
                         { "id" : 5, "title" : "AI and Society", "credit": 3, "subject" : "Humanities"}]
        
        assert response.json() == expected_data, "Verify /semesters/<semester_id>/classes endpoint"

    @testcase
    def test_postClassTooSmall(self, env, result):
        post_data = {"title" : "Algorithms", "credit" : 3, "subject" : "Computer Science"}
        env.http_client.post("/semesters/0/classes", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes error"

    @testcase
    def test_postClassTooLarge(self, env, result):
        post_data = {"title" : "Algorithms", "credit" : 3, "subject" : "Computer Science"}
        env.http_client.post("/semesters/3/classes", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes error"

    @testcase
    def test_getClass3(self, env, result):
        env.http_client.get("/semesters/1/classes/3")
        response = env.http_client.receive()

        result.dict.match(
            response.json(), {"id" : 3, "title": "Program Design and Data Structures", "credit": 3, "subject" : "Computer Science"}, 
            "Verify /semesters/<semester_id>/classes/<class_id> endpoint"
        )

    @testcase
    def test_deleteClass3(self, env, result):
        env.http_client.delete("/class/3")
        response = env.http_client.receive()

        assert response.status_code == 204, "Verify /class/<class_id> endpoint"

    @testcase
    def test_getClassHoleError(self, env, result):
        env.http_client.get("/semesters/1/classes/3")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id> error"

    @testcase
    def test_getClassTooSmall(self, env, result):
        env.http_client.get("/semesters/1/classes/0")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id> error"

    @testcase
    def test_getClassTooLarge(self, env, result):
        env.http_client.get("/semesters/1/classes/6")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id> error"

    @testcase
    def test_getClassWrongSemester(self, env, result):
        env.http_client.get("/semesters/2/classes/1")
        response = env.http_client.receive()

        assert response.status_code == 500, "Verify /semesters/<semester_id>/classes/<class_id> error"

    @testcase
    def test_deleteClassHoleError(self, env, result):
        env.http_client.delete("/class/3")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /class/<class_id> error"

    @testcase
    def test_deleteClassTooSmall(self, env, result):
        env.http_client.delete("/class/0")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /class/<class_id> error"

    @testcase
    def test_deleteClassTooLarge(self, env, result):
        env.http_client.delete("/class/6")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /class/<class_id> error"

    @testcase
    def test_getClassesAfterDelete(self, env, result):
        env.http_client.get("/semesters/1/classes")
        response = env.http_client.receive()
        
        expected_data = [{ "id" : 1, "title" : "Multivariable Calculus", "credit": 3, "subject" : "Mathematics"},
                         { "id" : 2, "title" : "Storytelling as Performance", "credit": 3, "subject" : "Theater"},
                         { "id" : 4, "title" : "Atlantic History in the Digital Age", "credit": 3, "subject" : "History"},
                         { "id" : 5, "title" : "AI and Society", "credit": 3, "subject" : "Humanities"}]
  
        assert response.json() == expected_data, "Verify /semesters/<semester_id>/classes endpoint"

    @testcase
    def test_deleteClass5(self, env, result):
        env.http_client.delete("/class/5")
        response = env.http_client.receive()

        assert response.status_code == 204, "Verify /class/<class_id> endpoint"

    @testcase
    def test_postClassAfterDelete(self, env, result):
        post_data = {"title" : "Algorithms", "credit" : 3, "subject" : "Computer Science"}
        env.http_client.post("/semesters/1/classes", json=post_data)
        response = env.http_client.receive()

        assert response.json() == 5, "Verify /semesters/<semester_id>/classes endpoint"

    @testcase
    def test_deleteSemester1(self, env, result):
        env.http_client.delete("/semesters/1")
        response = env.http_client.receive()

        assert response.status_code == 204, "Verify /semesters/<semester_id> endpoint"

    @testcase
    def test_getClassAfterSemesterDelete(self, env, result):
        env.http_client.get("/semesters/1/classes/5")
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes/<class_id> error"

    @testcase
    def test_postClassAfterSemesterDelete(self, env, result):
        post_data = {"title" : "Algorithms", "credit" : 3, "subject" : "Computer Science"}
        env.http_client.post("/semesters/1/classes", json=post_data)
        response = env.http_client.receive()

        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes error"

    @testcase
    def test_getClassesAfterSemesterDelete(self, env, result):
        env.http_client.get("/semesters/1/classes")
        response = env.http_client.receive()
        
        assert response.status_code == 404, "Verify /semesters/<semester_id>/classes error"

    @testcase
    def test_deleteSemester2(self, env, result):
        env.http_client.delete("/semesters/2")
        response = env.http_client.receive()

        assert response.status_code == 204, "Verify /semesters/<semester_id> endpoint"