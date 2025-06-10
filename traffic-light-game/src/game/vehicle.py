import random

class Vehicle:
    def __init__(self, direction, lane, vehicle_id):
        self.direction = direction  # 'norte', 'sul', 'leste', 'oeste'
        self.lane = lane  # 0, 1, 2 (múltiplas faixas)
        self.vehicle_id = vehicle_id
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        
        # Definir dimensões baseadas na direção
        if direction in ['norte', 'sul']:
            # Veículos norte-sul: orientação vertical
            self.width = 16
            self.height = 30
        else:  # leste, oeste
            # Veículos leste-oeste: orientação horizontal
            self.width = 30
            self.height = 16
        
        # SISTEMA DE MÃO DUPLA - Posições realísticas
        if direction == 'norte':
            # Norte: lado ESQUERDO da estrada (faixas 350-390)
            self.x = 350 + lane * 20  # Faixas mais estreitas para mão dupla
            self.y = 600
            self.speed_x, self.speed_y = 0, -2
        elif direction == 'sul':
            # Sul: lado DIREITO da estrada (faixas 410-450)
            self.x = 410 + lane * 20
            self.y = 0
            self.speed_x, self.speed_y = 0, 2
        elif direction == 'leste':
            # Leste: lado SUPERIOR da estrada (faixas 250-290)
            self.x = 0
            self.y = 250 + lane * 20
            self.speed_x, self.speed_y = 2, 0
        elif direction == 'oeste':
            # Oeste: lado INFERIOR da estrada (faixas 310-350)
            self.x = 800
            self.y = 310 + lane * 20
            self.speed_x, self.speed_y = -2, 0
            
        self.waiting = False
        self.safe_distance = 35  # Reduzido para faixas menores
        
    def move(self, traffic_light_state):
        """Move o veículo se permitido"""
        if traffic_light_state in ['verde', 'green']:
            self.x += self.speed_x
            self.y += self.speed_y
            self.waiting = False
        else:
            self.waiting = True
            
    def get_bounds(self):
        """Retorna os limites do veículo para detecção de colisão"""
        return {
            'left': self.x - self.width // 2,
            'right': self.x + self.width // 2,
            'top': self.y - self.height // 2,
            'bottom': self.y + self.height // 2
        }
        
    def get_next_position(self):
        """Retorna onde o veículo estará na próxima frame"""
        next_x = self.x + self.speed_x
        next_y = self.y + self.speed_y
        return next_x, next_y
        
    def would_collide_at_position(self, x, y, other_vehicle):
        """Verifica se haveria colisão em uma posição específica"""
        my_left = x - self.width // 2
        my_right = x + self.width // 2
        my_top = y - self.height // 2
        my_bottom = y + self.height // 2
        
        other_bounds = other_vehicle.get_bounds()
        
        horizontal_overlap = (my_left < other_bounds['right'] and 
                            my_right > other_bounds['left'])
        vertical_overlap = (my_top < other_bounds['bottom'] and 
                          my_bottom > other_bounds['top'])
        
        return horizontal_overlap and vertical_overlap
        
    def is_vehicle_ahead(self, other_vehicle):
        """Verifica se outro veículo está à frente - adaptado para mão dupla"""
        if self.direction != other_vehicle.direction:
            return False
            
        # Tolerância reduzida para faixas menores
        lane_tolerance = 25
        
        if self.direction == 'norte':
            return (abs(self.x - other_vehicle.x) < lane_tolerance and
                    other_vehicle.y < self.y and
                    self.y - other_vehicle.y < self.safe_distance)
        elif self.direction == 'sul':
            return (abs(self.x - other_vehicle.x) < lane_tolerance and
                    other_vehicle.y > self.y and
                    other_vehicle.y - self.y < self.safe_distance)
        elif self.direction == 'leste':
            return (abs(self.y - other_vehicle.y) < lane_tolerance and
                    other_vehicle.x > self.x and
                    other_vehicle.x - self.x < self.safe_distance)
        elif self.direction == 'oeste':
            return (abs(self.y - other_vehicle.y) < lane_tolerance and
                    other_vehicle.x < self.x and
                    self.x - other_vehicle.x < self.safe_distance)
        return False
        
    def can_move_safely(self, all_vehicles):
        """Verifica se pode se mover sem colidir com outros veículos"""
        next_x, next_y = self.get_next_position()
        
        for other_vehicle in all_vehicles:
            if other_vehicle == self:
                continue
                
            if self.would_collide_at_position(next_x, next_y, other_vehicle):
                return False
                
            if self.is_vehicle_ahead(other_vehicle):
                return False
                
        return True
        
    def should_stop_at_light(self):
        """Verifica se deve parar no semáforo - adaptado para mão dupla"""
        if self.direction == 'norte' and 310 <= self.y <= 360:
            return True
        elif self.direction == 'sul' and 240 <= self.y <= 290:
            return True
        elif self.direction == 'leste' and 310 <= self.x <= 360:
            return True
        elif self.direction == 'oeste' and 440 <= self.x <= 490:
            return True
        return False