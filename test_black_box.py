import unittest
from speed_controller import SpeedController

class TestSpeedControllerBlackBox(unittest.TestCase):
    """
    The unittest module will be able to run this class as a test
    suite containing multiple test cases. Each function is considered
    a separate test case. When unittest runs these tests, it will not
    run them in the order in which they appear in this class.
    
    Run this function with the following command:
    python -m unittest test_black_box.py
    """
    
    
    def setUp(self):
        """
        This will be executed before any of the tests are run.
        """
        self.controller = SpeedController(speed_limit=60)

    def test_example(self):
        """
        Example test 
        """
        
        # Input parameters
        road_condition:str = 'clear'
        traffic_density:int = 20
        slope_angle:int = 0
        
        # Expected value
        expected_result: float = 50
        
        # Run the function
        result = self.controller.update_speed(road_condition, traffic_density, slope_angle)
        
        # Assert result conditions
        self.assertEqual(result, expected_result, "Expected value does not match")
        
        

if __name__ == "__main__":
    unittest.main()