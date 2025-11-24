import unittest
from speed_controller import SpeedController

class TestSpeedControllerWhiteBox(unittest.TestCase):
    def setUp(self):
        self.controller = SpeedController()

    def test_wet_road_condition(self):
        result = self.controller.update_speed('wet',20,0)
        self.assertEqual(result,48,"Expected value does not match")

    def test_icy_road_condition(self):
        result = self.controller.update_speed('icy', 20, 0)
        self.assertEqual(result, 36, "Expected value does not match")

    def test_clear_road_condition(self):
        result = self.controller.update_speed('clear', 20, 0)
        self.assertEqual(result, 60, "Expected value does not match")
    
    def test_invalid_road_condition(self):
        with self.assertRaises(ValueError):
            self.controller.update_speed('muddy', 20, 0)
    
    def test_traffic_density_moderate(self):
        result = self.controller.update_speed('clear', 60, 0)
        self.assertEqual(result, 50, "Expected value does not match")

    def test_traffic_density_heavy(self):
        result = self.controller.update_speed('clear', 90, 0)
        self.assertEqual(result, 40, "Expected value does not match")
    
    def test_slope_uphill(self):
        result = self.controller.update_speed('clear', 20, 10)
        self.assertEqual(result, 70, "Expected value does not match")

    def test_slope_downhill(self):
        result = self.controller.update_speed('clear', 20, -10)
        self.assertEqual(result, 50, "Expected value does not match")

    def test_safety_mode(self):
        self.controller.set_safety_mode(True)
        result = self.controller.update_speed('clear', 20, -10)
        self.assertEqual(result, 50, "Expected value does not match")

    
    
