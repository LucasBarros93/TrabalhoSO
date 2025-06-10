import unittest
from src.game.vehicle import Vehicle
from src.game.traffic_light import TrafficLight

class TestVehicle(unittest.TestCase):

    def setUp(self):
        self.vehicle = Vehicle(position=(0, 0))

    def test_initial_position(self):
        self.assertEqual(self.vehicle.position, (0, 0))

    def test_move_vehicle_green_light(self):
        traffic_light = TrafficLight()
        traffic_light.change_light('green')
        self.vehicle.move(traffic_light)
        self.assertEqual(self.vehicle.position, (1, 0))  # Assuming move increments x by 1

    def test_move_vehicle_red_light(self):
        traffic_light = TrafficLight()
        traffic_light.change_light('red')
        initial_position = self.vehicle.position
        self.vehicle.move(traffic_light)
        self.assertEqual(self.vehicle.position, initial_position)  # Position should not change

if __name__ == '__main__':
    unittest.main()