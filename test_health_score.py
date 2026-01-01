import unittest
from health_report import calculate_health_status


class TestHealthStatus(unittest.TestCase):

    def test_excellent(self):
        self.assertEqual(calculate_health_status(90), "Excellent")

    def test_good(self):
        self.assertEqual(calculate_health_status(75), "Good")

    def test_moderate(self):
        self.assertEqual(calculate_health_status(60), "Moderate")

    def test_risk(self):
        self.assertEqual(calculate_health_status(45), "Risk")

    def test_critical(self):
        self.assertEqual(calculate_health_status(30), "Critical")


if __name__ == "__main__":
    unittest.main()
