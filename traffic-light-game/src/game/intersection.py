import threading
import time
import random
from .traffic_light import TrafficLight
from .vehicle import Vehicle

class SmartIntersection:
    def __init__(self):
        # 4 semáforos para cada direção
        self.traffic_lights = {
            'north': TrafficLight('north'),
            'south': TrafficLight('south'),
            'east': TrafficLight('east'),
            'west': TrafficLight('west')
        }
        
        self.vehicles = []
        self.vehicle_counter = 0
        self.running = True
        
        # Iniciar com Norte-Sul verde, Leste-Oeste vermelho
        self.traffic_lights['north'].set_state('green')
        self.traffic_lights['south'].set_state('green')
        
        # Iniciar threads de controle
        self.light_controller_thread = threading.Thread(target=self.auto_light_control)
        self.vehicle_spawner_thread = threading.Thread(target=self.spawn_vehicles)
        
    def start_threads(self):
        self.light_controller_thread.daemon = True
        self.vehicle_spawner_thread.daemon = True
        self.light_controller_thread.start()
        self.vehicle_spawner_thread.start()
        
    def auto_light_control(self):
        """Controla automaticamente os semáforos"""
        while self.running:
            # Norte-Sul verde por 5 segundos
            self.set_north_south_green()
            time.sleep(5)
            
            # Norte-Sul amarelo por 2 segundos
            self.set_north_south_yellow()
            time.sleep(2)
            
            # Norte-Sul vermelho, Leste-Oeste verde por 5 segundos
            self.set_east_west_green()
            time.sleep(5)
            
            # Leste-Oeste amarelo por 2 segundos
            self.set_east_west_yellow()
            time.sleep(2)
            
    def set_north_south_green(self):
        self.traffic_lights['north'].set_state('green')
        self.traffic_lights['south'].set_state('green')
        self.traffic_lights['east'].set_state('red')
        self.traffic_lights['west'].set_state('red')
        
    def set_north_south_yellow(self):
        self.traffic_lights['north'].set_state('yellow')
        self.traffic_lights['south'].set_state('yellow')
        
    def set_east_west_green(self):
        self.traffic_lights['north'].set_state('red')
        self.traffic_lights['south'].set_state('red')
        self.traffic_lights['east'].set_state('green')
        self.traffic_lights['west'].set_state('green')
        
    def set_east_west_yellow(self):
        self.traffic_lights['east'].set_state('yellow')
        self.traffic_lights['west'].set_state('yellow')
        
    def spawn_vehicles(self):
        """Gera veículos automaticamente"""
        while self.running:
            direction = random.choice(['north', 'south', 'east', 'west'])
            lane = random.randint(0, 2)
            vehicle = Vehicle(direction, lane, self.vehicle_counter)
            self.vehicles.append(vehicle)
            self.vehicle_counter += 1
            time.sleep(random.uniform(1, 3))  # Spawn a cada 1-3 segundos
            
    def update_vehicles(self):
        for vehicle in self.vehicles[:]:  # Cópia da lista para remoção segura
            direction = vehicle.direction
            traffic_light = self.traffic_lights[direction]
            
            # Verificar se deve parar no semáforo
            if vehicle.should_stop_at_light() and traffic_light.get_light() != 'green':
                vehicle.waiting = True
            else:
                vehicle.move(traffic_light.get_light())
                
            # Remover veículos que saíram da tela
            if (vehicle.x < -50 or vehicle.x > 850 or 
                vehicle.y < -50 or vehicle.y > 650):
                self.vehicles.remove(vehicle)
                
    def get_vehicle_count_by_direction(self):
        counts = {'north': 0, 'south': 0, 'east': 0, 'west': 0}
        for vehicle in self.vehicles:
            counts[vehicle.direction] += 1
        return counts
        
    def stop(self):
        self.running = False