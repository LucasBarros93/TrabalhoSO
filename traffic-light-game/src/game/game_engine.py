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
        yellow_color = (255, 255, 0)  # Amarelo para divisor central
        
        # Estrada horizontal (Leste-Oeste) - MÃO DUPLA
        pygame.draw.rect(self.screen, road_color, (0, 240, 800, 120))
        
        # Estrada vertical (Norte-Sul) - MÃO DUPLA  
        pygame.draw.rect(self.screen, road_color, (340, 0, 120, 600))
        
        # DIVISORES CENTRAIS (mão dupla)
        # Divisor central horizontal (amarelo)
        for x in range(0, 800, 30):
            if not (340 <= x <= 460):  # Não desenhar na intersecção
                pygame.draw.rect(self.screen, yellow_color, (x, 299, 15, 2))
        
        # Divisor central vertical (amarelo)
        for y in range(0, 600, 30):
            if not (240 <= y <= 360):  # Não desenhar na intersecção
                pygame.draw.rect(self.screen, yellow_color, (399, y, 2, 15))
        
        # FAIXAS DE ROLAMENTO
        # Faixas horizontais - lado superior (leste)
        for i in range(2):
            y = 260 + i * 20
            for x in range(0, 800, 40):
                if not (340 <= x <= 460):
                    pygame.draw.rect(self.screen, line_color, (x, y, 20, 1))
        
        # Faixas horizontais - lado inferior (oeste)  
        for i in range(2):
            y = 320 + i * 20
            for x in range(0, 800, 40):
                if not (340 <= x <= 460):
                    pygame.draw.rect(self.screen, line_color, (x, y, 20, 1))
                    
        # Faixas verticais - lado esquerdo (norte)
        for i in range(2):
            x = 360 + i * 20
            for y in range(0, 600, 40):
                if not (240 <= y <= 360):
                    pygame.draw.rect(self.screen, line_color, (x, y, 1, 20))
        
        # Faixas verticais - lado direito (sul)
        for i in range(2):
            x = 420 + i * 20
            for y in range(0, 600, 40):
                if not (240 <= y <= 360):
                    pygame.draw.rect(self.screen, line_color, (x, y, 1, 20))

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
        # Posições ajustadas para mão dupla
        positions = {
            'norte': (380, 200),  # Controla faixas esquerdas (norte)
            'sul': (430, 370),    # Controla faixas direitas (sul)
            'leste': (470, 270),  # Controla faixas superiores (leste)
            'oeste': (320, 330)   # Controla faixas inferiores (oeste)
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
        vermelho_color = (255, 50, 50) if current_state == 'vermelho' else (100, 20, 20)
        amarelo_color = (255, 255, 50) if current_state == 'amarelo' else (100, 100, 20)
        verde_color = (50, 255, 50) if current_state == 'verde' else (20, 100, 20)
        
        pygame.draw.circle(self.screen, vermelho_color, (x, y), 6)
        pygame.draw.circle(self.screen, amarelo_color, (x, y + 15), 6)
        pygame.draw.circle(self.screen, verde_color, (x, y + 30), 6)
        
        # Label da direção
        label = self.font.render(direction.upper(), True, (255, 255, 255))
        self.screen.blit(label, (x - 20, y + 45))

    def draw_vehicles(self):
        """Desenha todos os veículos na tela"""
        for vehicle in self.intersection.vehicles:
            # Cor do veículo (mais escura se esperando)
            color = vehicle.color
            if vehicle.waiting:
                color = tuple(c // 2 for c in color)  # Escurecer se esperando
                
            # Desenhar veículo com orientação correta
            vehicle_rect = pygame.Rect(
                vehicle.x - vehicle.width // 2, 
                vehicle.y - vehicle.height // 2, 
                vehicle.width, 
                vehicle.height
            )
            pygame.draw.rect(self.screen, color, vehicle_rect)
            pygame.draw.rect(self.screen, (0, 0, 0), vehicle_rect, 2)
            
            # Desenhar direção do veículo (seta pequena)
            self.draw_vehicle_direction(vehicle)
            
            # Número do veículo
            text = self.font.render(str(vehicle.vehicle_id), True, (255, 255, 255))
            text_rect = text.get_rect(center=(vehicle.x, vehicle.y))
            self.screen.blit(text, text_rect)
            
            # Indicador de espera
            if vehicle.waiting:
                pygame.draw.circle(self.screen, (255, 0, 0), (vehicle.x, vehicle.y - 20), 5)

    def draw_vehicle_direction(self, vehicle):
        """Desenha uma pequena seta indicando a direção do veículo"""
        arrow_size = 6
        
        if vehicle.direction == 'norte':
            # Seta para cima
            points = [
                (vehicle.x, vehicle.y - arrow_size),
                (vehicle.x - 3, vehicle.y + arrow_size//2),
                (vehicle.x + 3, vehicle.y + arrow_size//2)
            ]
        elif vehicle.direction == 'sul':
            # Seta para baixo
            points = [
                (vehicle.x, vehicle.y + arrow_size),
                (vehicle.x - 3, vehicle.y - arrow_size//2),
                (vehicle.x + 3, vehicle.y - arrow_size//2)
            ]
        elif vehicle.direction == 'leste':
            # Seta para direita
            points = [
                (vehicle.x + arrow_size, vehicle.y),
                (vehicle.x - arrow_size//2, vehicle.y - 3),
                (vehicle.x - arrow_size//2, vehicle.y + 3)
            ]
        elif vehicle.direction == 'oeste':
            # Seta para esquerda
            points = [
                (vehicle.x - arrow_size, vehicle.y),
                (vehicle.x + arrow_size//2, vehicle.y - 3),
                (vehicle.x + arrow_size//2, vehicle.y + 3)
            ]
        
        pygame.draw.polygon(self.screen, (255, 255, 255), points)

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
            color = (255, 0, 0) if state == 'vermelho' else (255, 255, 0) if state == 'amarelo' else (0, 255, 0)
            
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