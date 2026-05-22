import unittest
from unittest.mock import patch

from GameRunner import GameRunner


class MyTestCase(unittest.TestCase):

    def setUp(self):
        with patch.object(GameRunner, "__init__", return_value=None):
            self.game_runner = GameRunner(None, None, None, None)
            self.game_runner.input_service = None

    def test_something(self):
        assert self.game_runner.input_service is None


if __name__ == '__main__':
    unittest.main()
