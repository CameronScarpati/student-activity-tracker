from testplan import test_plan
from testplan.testing.multitest import MultiTest
from testplan.testing.multitest.driver.app import App
from testplan.testing.multitest.driver.http.client import HTTPClient
import os
from tests.example_multitest import ExampleMultiTestSuite
@test_plan(name="Student-Activity-Tracker-Tests")
def main(plan):
    plan.add(
        MultiTest(
            "Example Multitest Suite",
            [ExampleMultiTestSuite()],
            environment=[
                # TODO: This should also include your DB! But right now it's hardcoded.
                App(name="rest", binary="python",
                    args=["./trackerAPI.py"], working_dir="."),
                HTTPClient(name="http_client", host="127.0.0.1", port=5027)
                # TODO: Similarly, we should most likely make the port configurable.
            ],
        )
    )


if __name__ == "__main__":
    import sys

    sys.exit(not main())