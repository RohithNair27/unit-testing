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
        self.controller = SpeedController(speed_limit=60)

    def test_example(self):
        # Input parameters
        road_condition:str = 'clear'
        traffic_density:int = 20
        slope_angle:int = 0
        
        # Expected value
        expected_result: float = 60
        
        # Run the function
        result = self.controller.update_speed(road_condition, traffic_density, slope_angle)
        
        # Assert result conditions
        self.assertEqual(result, expected_result, "Expected value does not match")
    
    # Category Partition - road condtions
    # one representative value from each category
    def test_road_condition_category_partition(self):
        valid_road_conditions:list =[['wet',48],['icy',36],['clear',60]]
        invalid_conditions:list=["bad_road", "", None, "super_clear"]
        traffic_density:int = 20
        slope_angle:int = 0
        for road_condition in valid_road_conditions:
            result = self.controller.update_speed(road_condition[0], traffic_density, slope_angle)
            self.assertEqual(result,road_condition[1],"Expected value does not match")
        for condition in invalid_conditions:
            with self.assertRaises(ValueError):
                self.controller.update_speed(condition, traffic_density, slope_angle)
    


    # Category Partition - traffic_density
    def test_traffic_density(self):
        valid_traffic:list = [[20,60],[60,50],[90,40]]
        road_condition:str = 'clear'
        slope_angle:int = 0
        for density in valid_traffic:
            result = self.controller.update_speed(road_condition, density[0], slope_angle)
            self.assertEqual(result,density[1],"Expected value does not match")
    
    # Category Partition - slope angle
    def test_slope_angle(self):
        road_condition:str = 'clear'
        traffic_density:int = 20
        valid_slope:list = [[-1,59],[+1,61]]
        invalid_slope:list = [[0,60]]
        for slope in valid_slope:
            result = self.controller.update_speed(road_condition, traffic_density, slope[0])
            self.assertEqual(result,slope[1],"Expected value does not match")
        for density in invalid_slope:
            result = self.controller.update_speed(road_condition, traffic_density, slope[0])
            self.assertEqual(result,slope[1],"Expected value does not match")

    # Boundary values - traffic_density
    def test_traffic_density_boundary(self):
        nominal_boundary_values = [[51,50],[79,50]]
        invalid_boundary_values = [[49,60],[81,40]]
        road_condition:str = 'clear'
        slope_angle:int = 0

        for density in nominal_boundary_values:
            result = self.controller.update_speed(road_condition, density[0], slope_angle)
            self.assertEqual(result,density[1],"Expected value does not match")
        for density in invalid_boundary_values:
            result = self.controller.update_speed(road_condition, density[0], slope_angle)
            self.assertEqual(result,density[1],"Expected value does not match")

    #Boundary values - slope
    def test_slope_angle_boundary(self):
        nominal_boundary_values = [[-10, 50], [10, 70]]
        invalid_boundary_values = [[-11, 49], [11, 71]]
        traffic_density: int = 20  
        road_condition: str = 'clear'

        for slope_pair in nominal_boundary_values:
            result = self.controller.update_speed(road_condition, traffic_density, slope_pair[0])
            self.assertEqual(result, slope_pair[1], f"Failed for nominal slope: {slope_pair[0]}")
            
        for slope_pair in invalid_boundary_values:
            result = self.controller.update_speed(road_condition, traffic_density, slope_pair[0])
            self.assertEqual(result, slope_pair[1], f"Failed for invalid slope: {slope_pair[0]}")

    
    

if __name__ == "__main__":
    unittest.main()