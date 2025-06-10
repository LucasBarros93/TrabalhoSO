import pygame
import sys
import math
from .intersection import SmartIntersection

class GameEngine:
    def __init__(self):
        self.running = True
        self.screen = None
        self.clock = None
        self.intersection = None
        self.font = None
        self.font_large = None
        
    def start(self):
        # Inicializar pygame
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("🚦 Smart Traffic Light System - SO Simulation")
        self.clock = pygame.time.Clock()
        
        # Fontes
        self.font = pygame.font.Font(None, 24)
        self.font_large = pygame.font.Font(None, 36)
        
        # Inicializar intersecção inteligente
        self.intersection = SmartIntersection()
        self.intersection.start_threads()
        
        print("🚦 Sistema de Semáforos Inteligente iniciado!")
        print("📊 Observe a sincronização automática dos semáforos")
        print("🚗 Veículos sendo gerados automaticamente")
        print("⌨️  Pressione ESC para sair")
        
        self.main_loop()
        
        # Finalizar
        self.intersection.stop()
        pygame.quit()
        print("Sistema finalizado!")

    def main_loop(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        if self.intersection:
            self.intersection.update_vehicles()

    def render(self):
        if self.screen:
            # Fundo (grama)
            self.screen.fill((34, 139, 34))  # Verde floresta
            
            # Desenhar estradas
            self.draw_roads()
            
            # Desenhar intersecção
            self.draw_intersection()
            
            # Desenhar semáforos
            self.draw_traffic_lights()
            
            # Desenhar veículos
            self.draw_vehicles()
            
            # Desenhar informações
            self.draw_info_panel()
            
            pygame.display.flip()

    def draw_roads(self):
        # Cor da estrada
        road_color = (64, 64, 64)  # Cinza escuro
        line_color = (255, 255, 255)  # Branco
        
        # Estrada horizontal (Leste-Oeste)
        pygame.draw.rect(self.screen, road_color, (0, 250, 800, 100))
        
        # Estrada vertical (Norte-Sul)
        pygame.draw.rect(self.screen, road_color, (300, 0, 100, 600))
        
        # Linhas divisórias horizontais
        for i in range(3):
            y = 270 + i * 20
            for x in range(0, 800, 40):
                if not (300 <= x <= 400):  # Não desenhar na intersecção
                    pygame.draw.rect(self.screen, line_color, (x, y, 20, 2))
                    
        # Linhas divisórias verticais
        for i in range(3):
            x = 320 + i * 20
            for y in range(0, 600, 40):
                if not (250 <= y <= 350):  # Não desenhar na intersecção
                    pygame.draw.rect(self.screen, line_color, (x, y, 2, 20))

    def draw_intersection(self):
        # Intersecção
        intersection_color = (96, 96, 96)  # Cinza mais claro
        pygame.draw.rect(self.screen, intersection_color, (300, 250, 100, 100))
        
        # Linhas de parada
        stop_line_color = (255, 255, 0)  # Amarelo
        
        # Norte
        pygame.draw.rect(self.screen, stop_line_color, (300, 240, 100, 3))
        # Sul
        pygame.draw.rect(self.screen, stop_line_color, (300, 357, 100, 3))
        # Leste
        pygame.draw.rect(self.screen, stop_line_color, (407, 250, 3, 100))
        # Oeste
        pygame.draw.rect(self.screen, stop_line_color, (290, 250, 3, 100))

    def draw_traffic_lights(self):
        positions = {
            'north': (380, 200),
            'south': (420, 370),
            'east': (450, 280),
            'west': (250, 320)
        }
        
        for direction, (x, y) in positions.items():
            self.draw_single_traffic_light(x, y, direction)

    def draw_single_traffic_light(self, x, y, direction):
        light = self.intersection.traffic_lights[direction]
        current_state = light.get_light()
        
        # Poste do semáforo
        pygame.draw.rect(self.screen, (100, 100, 100), (x-5, y-10, 10, 30))
        
        # Caixa do semáforo
        pygame.draw.rect(self.screen, (0, 0, 0), (x-15, y-10, 30, 50))
        pygame.draw.rect(self.screen, (200, 200, 200), (x-15, y-10, 30, 50), 2)
        
        # Luzes
        red_color = (255, 50, 50) if current_state == 'red' else (100, 20, 20)
        yellow_color = (255, 255, 50) if current_state == 'yellow' else (100, 100, 20)
        green_color = (50, 255, 50) if current_state == 'green' else (20, 100, 20)
        
        pygame.draw.circle(self.screen, red_color, (x, y), 6)
        pygame.draw.circle(self.screen, yellow_color, (x, y + 15), 6)
        pygame.draw.circle(self.screen, green_color, (x, y + 30), 6)
        
        # Label da direção
        label = self.font.render(direction.upper(), True, (255, 255, 255))
        self.screen.blit(label, (x - 20, y + 45))

    def draw_vehicles(self):
        for vehicle in self.intersection.vehicles:
            # Cor do veículo (mais escura se esperando)
            color = vehicle.color
            if vehicle.waiting:
                color = tuple(c // 2 for c in color)  # Escurecer se esperando
                
            # Desenhar veículo
            vehicle_rect = pygame.Rect(vehicle.x - 15, vehicle.y - 8, 30, 16)
            pygame.draw.rect(self.screen, color, vehicle_rect)
            pygame.draw.rect(self.screen, (0, 0, 0), vehicle_rect, 2)
            
            # Número do veículo
            text = self.font.render(str(vehicle.vehicle_id), True, (255, 255, 255))
            text_rect = text.get_rect(center=(vehicle.x, vehicle.y))
            self.screen.blit(text, text_rect)
            
            # Indicador de espera
            if vehicle.waiting:
                pygame.draw.circle(self.screen, (255, 0, 0), (vehicle.x, vehicle.y - 20), 5)

    def draw_info_panel(self):
        # Painel de informações
        panel_rect = pygame.Rect(10, 10, 200, 150)
        pygame.draw.rect(self.screen, (0, 0, 0, 128), panel_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), panel_rect, 2)
        
        # Título
        title = self.font_large.render("Sistema SO", True, (255, 255, 255))
        self.screen.blit(title, (20, 20))
        
        # Estados dos semáforos
        y_offset = 50
        for direction, light in self.intersection.traffic_lights.items():
            state = light.get_light()
            color = (255, 0, 0) if state == 'red' else (255, 255, 0) if state == 'yellow' else (0, 255, 0)
            
            text = self.font.render(f"{direction.upper()}: {state.upper()}", True, color)
            self.screen.blit(text, (20, y_offset))
            y_offset += 20
            
        # Contagem de veículos
        counts = self.intersection.get_vehicle_count_by_direction()
        total_vehicles = sum(counts.values())
        
        vehicle_text = self.font.render(f"Veículos: {total_vehicles}", True, (255, 255, 255))
        self.screen.blit(vehicle_text, (20, 130))
        
        # Instrução
        instruction = self.font.render("ESC: Sair", True, (200, 200, 200))
        self.screen.blit(instruction, (20, 570))

    def stop(self):
        self.running = False