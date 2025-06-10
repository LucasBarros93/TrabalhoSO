import unittest
from src.game.traffic_light import TrafficLight

class TestTrafficLight(unittest.TestCase):

    def setUp(self):
        self.traffic_light = TrafficLight()

    def test_initial_light_state(self):
        self.assertEqual(self.traffic_light.get_light(), 'vermelho')

    def test_change_light(self):
        self.traffic_light.change_light()
        self.assertEqual(self.traffic_light.get_light(), 'verde')
        self.traffic_light.change_light()
        self.assertEqual(self.traffic_light.get_light(), 'vermelho')

if __name__ == '__main__':
    unittest.main()