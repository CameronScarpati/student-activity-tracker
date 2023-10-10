from testplan.testing.multitest import testsuite, testcase, MultiTest

@testsuite
class ExampleMultiTestSuite(object):
    @testcase
    def test_get(self, env, result):
        env.http_client.get("/_up")
        response = env.http_client.receive()
        result.dict.match(
            response.json(), {"version" : "TBA"}, "Verify _up endpoint"
        )
