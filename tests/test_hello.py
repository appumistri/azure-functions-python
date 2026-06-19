import sys
from pathlib import Path

# Add project root to sys.path so 'function_app' can be found
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import azure.functions as func
import unittest
from unittest.mock import patch, MagicMock


class TestFunctions(unittest.TestCase):
    name = "Appu"
    def test_hello(self):
        from SampleHttpTrigger import hello
        hello_req = func.HttpRequest(
            method="GET",
            url="/api/hello",
            params={"name": self.name},
            body=None,
        )
        r = hello.hello(hello_req)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.get_body().decode(), f"Hello, {self.name}.")
        
    def test_timer(self):
        from SampleHttpTrigger import hello as http_hello
        from SampleTimerTrigger import timer
        from utils.log import logger

        # Set a user first via HTTP trigger
        hello_req = func.HttpRequest(
            method="GET",
            url="/api/hello",
            params={"name": self.name},
            body=None,
        )
        http_hello.hello(hello_req)

        # Now simulate timer trigger and assert log
        with patch.object(logger, 'info') as mock_info:
            timer_req = MagicMock(spec=func.TimerRequest)
            timer_req.past_due = False
            timer.scheduled(timer_req)
            mock_info.assert_called_once_with(f"Last greeted user: {self.name}")
