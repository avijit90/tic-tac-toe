import unittest
from unittest.mock import patch

from GameRunner import GameRunner


class MyTestCase(unittest.TestCase):

    def setUp(self):
        with patch(GameRunner, "__init__", lambda a, b, c, d: None) as mock:
            self.game_runner = GameRunner(None, None, None, None)

    def test_something(self):
        assert self.game_runner.input_service is None


if __name__ == '__main__':
    unittest.main()
