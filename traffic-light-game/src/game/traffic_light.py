import threading
import time

class TrafficLight:
    def __init__(self, direction):
        self.state = 'vermelho'
        self.direction = direction  # 'norte', 'sul', 'leste', 'oeste'
        self.lock = threading.Lock()
        self.timer = 0
        
    def change_light(self):
        with self.lock:
            if self.state == 'vermelho':
                self.state = 'verde'
            elif self.state == 'verde':
                self.state = 'amarelo'
            elif self.state == 'amarelo':
                self.state = 'vermelho'

    def get_light(self):
        return self.state
        
    def set_state(self, state):
        with self.lock:
            self.state = state