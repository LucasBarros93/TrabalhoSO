import pygame
import sys

def test_game_engine():
    print("Testando GameEngine...")
    
    try:
        from game.game_engine import GameEngine
        print("GameEngine importado com sucesso!")
        
        # Adicionar debug no GameEngine
        game = GameEngine()
        print("GameEngine criado!")
        
        # Verificar se tem método start
        if hasattr(game, 'start'):
            print("Método start encontrado!")
            print("Iniciando game.start()...")
            game.start()
        else:
            print("ERRO: GameEngine não tem método start!")
            
    except Exception as e:
        print(f"Erro ao testar GameEngine: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_game_engine()