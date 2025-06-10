import threading
import time
import random
import math
from .traffic_light import TrafficLight
from .vehicle import Vehicle

class SmartIntersection:
    def __init__(self):
        # 4 semáforos para cada direção
        self.traffic_lights = {
            'norte': TrafficLight('norte'),
            'sul': TrafficLight('sul'),
            'leste': TrafficLight('leste'),
            'oeste': TrafficLight('oeste')
        }
        
        self.vehicles = []
        self.vehicle_counter = 0
        self.running = True
        self.spawn_lock = threading.Lock()
        self.min_spawn_distance = 75  # Reduzido de 90 para 75
        
        # Iniciar com Norte-Sul verde, Leste-Oeste vermelho
        self.traffic_lights['norte'].set_state('verde')
        self.traffic_lights['sul'].set_state('verde')
        
        # Iniciar threads de controle
        self.light_controller_thread = threading.Thread(target=self.auto_light_control)
        self.vehicle_spawner_thread = threading.Thread(target=self.spawn_vehicles)
        
        # Iniciar threads de controle
        self.light_controller_thread = threading.Thread(target=self.auto_light_control)
        self.vehicle_spawner_thread = threading.Thread(target=self.spawn_vehicles)
        
    def start_threads(self):
        self.light_controller_thread.daemon = True
        self.vehicle_spawner_thread.daemon = True
        self.light_controller_thread.start()
        self.vehicle_spawner_thread.start()
        
    def auto_light_control(self):
        """Controla automaticamente os semáforos - sistema independente por direção"""
        while self.running:
            # FASE 1: Norte e Sul verdes (eixo vertical)
            self.traffic_lights['norte'].set_state('verde')
            self.traffic_lights['sul'].set_state('verde')
            self.traffic_lights['leste'].set_state('vermelho')
            self.traffic_lights['oeste'].set_state('vermelho')
            print("🚦 FASE 1: Norte/Sul VERDE | Leste/Oeste VERMELHO")
            time.sleep(6)
            
            # FASE 2: Norte e Sul amarelos
            self.traffic_lights['norte'].set_state('amarelo')
            self.traffic_lights['sul'].set_state('amarelo')
            print("🚦 TRANSIÇÃO: Norte/Sul AMARELO")
            time.sleep(2)
            
            # FASE 3: Leste e Oeste verdes (eixo horizontal)
            self.traffic_lights['norte'].set_state('vermelho')
            self.traffic_lights['sul'].set_state('vermelho')
            self.traffic_lights['leste'].set_state('verde')
            self.traffic_lights['oeste'].set_state('verde')
            print("🚦 FASE 3: Leste/Oeste VERDE | Norte/Sul VERMELHO")
            time.sleep(6)
            
            # FASE 4: Leste e Oeste amarelos
            self.traffic_lights['leste'].set_state('amarelo')
            self.traffic_lights['oeste'].set_state('amarelo')
            print("🚦 TRANSIÇÃO: Leste/Oeste AMARELO")
            time.sleep(2)
            
    def set_north_south_green(self):
        self.traffic_lights['norte'].set_state('verde')
        self.traffic_lights['sul'].set_state('verde')
        self.traffic_lights['leste'].set_state('vermelho')
        self.traffic_lights['oeste'].set_state('vermelho')
        
    def set_north_south_yellow(self):
        self.traffic_lights['norte'].set_state('amarelo')
        self.traffic_lights['sul'].set_state('amarelo')
        
    def set_east_west_green(self):
        self.traffic_lights['norte'].set_state('vermelho')
        self.traffic_lights['sul'].set_state('vermelho')
        self.traffic_lights['leste'].set_state('verde')
        self.traffic_lights['oeste'].set_state('verde')
        
    def set_east_west_yellow(self):
        self.traffic_lights['leste'].set_state('amarelo')
        self.traffic_lights['oeste'].set_state('amarelo')
        
    def get_spawn_position(self, direction, lane):
        """Retorna a posição de spawn para mão dupla"""
        positions = {
            'norte': (350 + lane * 20, 600),  # Lado esquerdo
            'sul': (410 + lane * 20, 0),      # Lado direito
            'leste': (0, 250 + lane * 20),    # Lado superior
            'oeste': (800, 310 + lane * 20)   # Lado inferior
        }
        return positions.get(direction, (0, 0))
        
    def can_spawn_vehicle(self, direction, lane):
        """Verifica se pode spawnar um veículo - versão simplificada"""
        spawn_x, spawn_y = self.get_spawn_position(direction, lane)
        
        # Verificar apenas veículos na mesma direção e faixa
        for vehicle in self.vehicles:
            if vehicle.direction == direction and vehicle.lane == lane:
                # Verificar distância específica por direção
                if direction in ['norte', 'sul']:
                    if abs(vehicle.y - spawn_y) < self.min_spawn_distance:
                        return False
                else:  # leste, oeste
                    if abs(vehicle.x - spawn_x) < self.min_spawn_distance:
                        return False
                        
        return True
        
    def get_traffic_density(self):
        """Calcula a densidade de tráfego atual - limites rebalanceados"""
        total_vehicles = len(self.vehicles)
        if total_vehicles < 6:      # Aumentado de 3
            return 'low'
        elif total_vehicles < 12:   # Aumentado de 8
            return 'medium'
        else:
            return 'high'

    def spawn_vehicles(self):
        """Gera veículos automaticamente com frequência balanceada"""
        while self.running:
            traffic_density = self.get_traffic_density()
            
            # Frequência mais equilibrada
            if traffic_density == 'low':
                spawn_chance = 0.6   # 60% de chance para manter fluxo
                sleep_time = 1.0     # 1 segundo entre tentativas
            elif traffic_density == 'medium':
                spawn_chance = 0.3   # 30% de chance
                sleep_time = 1.5
            else:  # high
                spawn_chance = 0.1   # 10% de chance para evitar superlotação
                sleep_time = 2.0
                
            directions = ['norte', 'sul', 'leste', 'oeste']
            
            # Tentar spawnar em 2 direções por ciclo para manter fluxo
            selected_directions = random.sample(directions, 2)
            
            for direction in selected_directions:
                lane = random.randint(0, 2)
                
                if random.random() < spawn_chance:
                    with self.spawn_lock:
                        if self.can_spawn_vehicle(direction, lane):
                            vehicle = Vehicle(direction, lane, self.vehicle_counter)
                            self.vehicles.append(vehicle)
                            self.vehicle_counter += 1
                            print(f"Veículo {self.vehicle_counter} spawnou - {direction}, faixa {lane}")
                            
            time.sleep(sleep_time)
            
    def update_vehicles(self):
        """Atualiza todos os veículos com verificação rigorosa de colisão"""
        for vehicle in self.vehicles[:]:  # Cópia da lista para remoção segura
            direction = vehicle.direction
            traffic_light = self.traffic_lights[direction]
            current_light_state = traffic_light.get_light()
            
            # Verificar se pode se mover
            can_move_light = True
            can_move_collision = True
            
            # Verificar semáforo
            if vehicle.should_stop_at_light():
                if current_light_state not in ['verde', 'green']:
                    can_move_light = False
                    
            # Verificar colisões com outros veículos
            if not vehicle.can_move_safely(self.vehicles):
                can_move_collision = False
                
            # Mover apenas se ambas as condições permitirem
            if can_move_light and can_move_collision:
                vehicle.move(current_light_state)
            else:
                vehicle.waiting = True
                
            # Remover veículos que saíram da tela
            if (vehicle.x < -50 or vehicle.x > 850 or 
                vehicle.y < -50 or vehicle.y > 650):
                self.vehicles.remove(vehicle)
                
    def get_vehicle_count_by_direction(self):
        counts = {'norte': 0, 'sul': 0, 'leste': 0, 'oeste': 0}
        for vehicle in self.vehicles:
            counts[vehicle.direction] += 1
        return counts
        
    def stop(self):
        self.running = False