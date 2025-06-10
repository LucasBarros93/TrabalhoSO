import unittest
from src.game.intersection import Intersection
from src.game.traffic_light import TrafficLight
from src.game.vehicle import Vehicle

class TestIntersection(unittest.TestCase):

    def setUp(self):
        self.intersection = Intersection()
        self.traffic_light = TrafficLight()
        self.intersection.traffic_light = self.traffic_light

    def test_add_vehicle(self):
        vehicle = Vehicle(position=(0, 0))
        self.intersection.add_vehicle(vehicle)
        self.assertIn(vehicle, self.intersection.vehicles)

    def test_control_traffic_green_light(self):
        self.traffic_light.change_light('green')
        self.intersection.control_traffic()
        # Assuming vehicles can move when the light is green
        for vehicle in self.intersection.vehicles:
            self.assertEqual(vehicle.position[0], 1)  # Example position update

    def test_control_traffic_red_light(self):
        self.traffic_light.change_light('red')
        self.intersection.control_traffic()
        # Assuming vehicles cannot move when the light is red
        for vehicle in self.intersection.vehicles:
            self.assertEqual(vehicle.position[0], 0)  # Position should not change

if __name__ == '__main__':
    unittest.main()