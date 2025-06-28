#!/usr/bin/env python3
"""
🎯 QUIZ EDUCATIVO: SEMÁFOROS E THREADS
Sistema Operacional - Aprendizado Interativo

Jogo educativo para ensinar conceitos de threads e semáforos
em Sistemas Operacionais de forma prática e divertida.

Autor: Desenvolvido para estudantes de SO
Data: 2025
"""

import sys
import os

# Adiciona o diretório atual ao path para importações
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from src.quiz_game import QuizGame
except ImportError as e:
    print("❌ Erro ao importar módulos do jogo:")
    print(f"   {e}")
    print("\n🔧 Verifique se todos os arquivos estão no local correto:")
    print("   - src/quiz_game.py")
    print("   - src/question_manager.py") 
    print("   - src/score_manager.py")
    print("   - src/content_summary.py")
    print("   - utils/helpers.py")
    print("   - perguntas/perguntas.csv")
    sys.exit(1)

def main():
    """Função principal que inicia o jogo."""
    try:
        # Verifica se o arquivo de perguntas existe
        csv_path = os.path.join(os.path.dirname(__file__), "perguntas", "perguntas.csv")
        if not os.path.exists(csv_path):
            print("❌ Arquivo de perguntas não encontrado!")
            print(f"   Procurando em: {csv_path}")
            print("\n🔧 Certifique-se de que o arquivo 'perguntas.csv' está na pasta 'perguntas/'")
            return
        
        # Cria e executa o jogo
        print("🚀 Iniciando Quiz Educativo...")
        print("📚 Carregando perguntas sobre threads e semáforos...")
        
        game = QuizGame()
        game.run()
        
    except KeyboardInterrupt:
        print("\n\n👋 Jogo interrompido pelo usuário.")
        print("📚 Volte sempre para continuar aprendendo!")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        print("🔧 Se o problema persistir, verifique a instalação do jogo.")

if __name__ == "__main__":
    main()
