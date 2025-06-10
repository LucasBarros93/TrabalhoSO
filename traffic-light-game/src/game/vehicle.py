import random

class Vehicle:
    def __init__(self, direction, lane, vehicle_id):
        self.direction = direction  # 'north', 'south', 'east', 'west'
        self.lane = lane  # 0, 1, 2 (múltiplas faixas)
        self.vehicle_id = vehicle_id
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        
        # Posições baseadas na direção
        if direction == 'north':
            self.x = 350 + lane * 40
            self.y = 600
            self.speed_x, self.speed_y = 0, -2
        elif direction == 'south':
            self.x = 410 - lane * 40
            self.y = 0
            self.speed_x, self.speed_y = 0, 2
        elif direction == 'east':
            self.x = 0
            self.y = 280 + lane * 40
            self.speed_x, self.speed_y = 2, 0
        elif direction == 'west':
            self.x = 800
            self.y = 320 - lane * 40
            self.speed_x, self.speed_y = -2, 0
            
        self.waiting = False
        
    def move(self, traffic_light_state):
        if traffic_light_state == 'green':
            self.x += self.speed_x
            self.y += self.speed_y
            self.waiting = False
        else:
            self.waiting = True
            
    def is_at_intersection(self):
        return (300 <= self.x <= 500 and 250 <= self.y <= 350)
        
    def should_stop_at_light(self):
        # Verifica se deve parar no semáforo baseado na direção
        if self.direction == 'north' and 320 <= self.y <= 370:
            return True
        elif self.direction == 'south' and 230 <= self.y <= 280:
            return True
        elif self.direction == 'east' and 320 <= self.x <= 370:
            return True
        elif self.direction == 'west' and 430 <= self.x <= 480:
            return True
        return False