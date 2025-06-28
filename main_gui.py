#!/usr/bin/env python3
"""
🎯 QUIZ EDUCATIVO: SEMÁFOROS E THREADS - Versão com Interface Gráfica
Ponto de entrada para a versão GUI do quiz educativo
"""

import sys
import os

# Adiciona o diretório atual ao path para importações
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from src.quiz_gui import QuizGUI
except ImportError as e:
    print("❌ Erro ao importar módulos da interface gráfica:")
    print(f"   {e}")
    print("\n🔧 Verifique se todos os arquivos estão no local correto:")
    print("   - src/quiz_gui.py")
    print("   - src/question_manager.py") 
    print("   - src/score_manager.py")
    print("   - src/content_summary.py")
    print("   - perguntas/perguntas.csv")
    sys.exit(1)

def main():
    """Função principal que inicia a interface gráfica."""
    try:
        # Verifica se o arquivo de perguntas existe
        csv_path = os.path.join(os.path.dirname(__file__), "perguntas", "perguntas.csv")
        if not os.path.exists(csv_path):
            print("❌ Arquivo de perguntas não encontrado!")
            print(f"   Procurando em: {csv_path}")
            print("\n🔧 Certifique-se de que o arquivo 'perguntas.csv' está na pasta 'perguntas/'")
            return
        
        # Cria e executa a interface gráfica
        print("🚀 Iniciando Quiz Educativo (Interface Gráfica)...")
        print("📚 Carregando perguntas sobre threads e semáforos...")
        
        app = QuizGUI()
        app.run()
        
    except KeyboardInterrupt:
        print("\n\n👋 Aplicação interrompida pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        print("🔧 Se o problema persistir, verifique a instalação do jogo.")

if __name__ == "__main__":
    main()
