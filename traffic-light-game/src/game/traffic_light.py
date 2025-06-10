import threading
import time

class TrafficLight:
    def __init__(self, direction):
        self.state = 'red'
        self.direction = direction  # 'north', 'south', 'east', 'west'
        self.lock = threading.Lock()
        self.timer = 0
        
    def change_light(self):
        with self.lock:
            if self.state == 'red':
                self.state = 'green'
            elif self.state == 'green':
                self.state = 'yellow'
            elif self.state == 'yellow':
                self.state = 'red'

    def get_light(self):
        return self.state
        
    def set_state(self, state):
        with self.lock:
            self.state = state