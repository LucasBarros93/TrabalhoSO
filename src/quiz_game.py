import sys
import os

# Adiciona o diretório pai ao path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.question_manager import QuestionManager
from src.score_manager import ScoreManager
from src.content_summary import ContentSummary
from utils.helpers import (
    clear_screen, get_valid_input, print_header, press_enter_to_continue,
    display_question_with_formatting, display_result, get_explanation_for_topic,
    get_colored_text, validate_player_name, format_percentage
)

class QuizGame:
    """Classe principal que gerencia o jogo de quiz."""
    
    def __init__(self):
        self.question_manager = QuestionManager()
        self.score_manager = ScoreManager()
        self.running = True
    
    def show_main_menu(self):
        """Exibe o menu principal do jogo."""
        clear_screen()
        print(get_colored_text("🎯 QUIZ EDUCATIVO: SEMÁFOROS E THREADS", 'bold'))
        print(get_colored_text("Sistema Operacional - Aprendizado Interativo", 'cyan'))
        print("=" * 60)
        print()
        print("📋 MENU PRINCIPAL:")
        print("1. 🎮 Começar Quiz")
        print("2. 📚 Ver Resumo Teórico") 
        print("3. 🏆 Ver Histórico de Pontuações")
        print("4. ❓ Sobre o Jogo")
        print("0. 🚪 Sair")
        print()
        print("=" * 60)
    
    def start_quiz(self):
        """Inicia uma sessão de quiz."""
        if not self.question_manager.questions:
            print("❌ Não há perguntas disponíveis!")
            press_enter_to_continue()
            return
        
        # Configurações do quiz
        clear_screen()
        print_header("CONFIGURAÇÃO DO QUIZ")
        print()
        
        # Pergunta quantas questões o usuário quer
        total_questions = self.question_manager.get_question_count()
        print(f"📊 Temos {total_questions} perguntas disponíveis.")
        
        while True:
            try:
                num_questions = input(f"🔢 Quantas perguntas você quer responder? (1-{total_questions}): ").strip()
                num_questions = int(num_questions)
                if 1 <= num_questions <= total_questions:
                    break
                else:
                    print(f"❌ Por favor, escolha um número entre 1 e {total_questions}!")
            except ValueError:
                print("❌ Por favor, digite um número válido!")
        
        # Nome do jogador
        player_name = input("\n👤 Digite seu nome (ou Enter para 'Anônimo'): ").strip()
        player_name = validate_player_name(player_name)
        
        # Inicia o quiz
        self.run_quiz_session(num_questions, player_name)
    
    def run_quiz_session(self, num_questions, player_name):
        """Executa uma sessão completa de quiz."""
        # Reset da pontuação
        self.score_manager.reset_score()
        
        # Seleciona perguntas aleatórias
        questions = self.question_manager.get_random_questions(num_questions)
        
        print(f"\n🎯 Iniciando quiz para {player_name}!")
        print(f"📊 {len(questions)} perguntas selecionadas.")
        press_enter_to_continue()
        
        # Loop principal do quiz
        for i, question in enumerate(questions, 1):
            self.ask_question(i, len(questions), question)
        
        # Mostra resultado final
        self.show_final_results(player_name)
    
    def ask_question(self, question_num, total_questions, question):
        """Faz uma pergunta individual ao usuário."""
        # Exibe a pergunta
        display_question_with_formatting(question_num, total_questions, question)
        
        # Obtém resposta do usuário
        valid_options = ['A', 'B', 'C', 'D']
        user_answer = get_valid_input("🤔 Sua resposta: ", valid_options)
        
        # Valida a resposta
        is_correct = self.question_manager.validate_answer(question, user_answer)
        correct_answer = question['resposta_correta'].upper()
        
        # Atualiza pontuação
        self.score_manager.add_question(is_correct)
        
        # Exibe resultado
        display_result(is_correct, correct_answer, user_answer)
        
        # Mostra explicação
        explanation = get_explanation_for_topic(question['pergunta'])
        print(explanation)
        
        # Mostra progresso atual
        stats = self.score_manager.get_current_stats()
        print(f"\n📊 Progresso: {stats['correct']}/{stats['total']} corretas "
              f"({stats['percentage']}%) - {stats['score']} pontos")
        
        press_enter_to_continue()
    
    def show_final_results(self, player_name):
        """Exibe os resultados finais do quiz."""
        clear_screen()
        print_header("RESULTADO FINAL")
        
        stats = self.score_manager.get_current_stats()
        performance_msg = self.score_manager.get_performance_message()
        
        print(f"\n🎯 Parabéns, {player_name}!")
        print(f"📊 Perguntas respondidas: {stats['total']}")
        print(f"✅ Respostas corretas: {stats['correct']}")
        print(f"❌ Respostas incorretas: {stats['total'] - stats['correct']}")
        print(f"📈 Porcentagem de acertos: {stats['percentage']}%")
        print(f"🏆 Pontuação final: {stats['score']} pontos")
        print()
        print(get_colored_text(performance_msg, 'yellow'))
        print()
        
        # Pergunta se quer salvar a pontuação
        save_score = get_valid_input("💾 Deseja salvar sua pontuação? (S/N): ", ['S', 'N'])
        
        if save_score == 'S':
            if self.score_manager.save_score(player_name):
                print("✅ Pontuação salva com sucesso!")
            else:
                print("❌ Erro ao salvar pontuação.")
        
        print("\n🔄 Quer jogar novamente? Volte ao menu principal!")
        press_enter_to_continue()
    
    def show_theory_menu(self):
        """Exibe o menu do resumo teórico."""
        while True:
            clear_screen()
            ContentSummary.show_main_menu()
            
            option = input("\n🔍 Escolha uma opção: ").strip()
            
            if option == "0":
                break
            elif option in ["1", "2", "3", "4", "5"]:
                ContentSummary.show_content(option)
            else:
                print("❌ Opção inválida!")
                press_enter_to_continue()
    
    def show_score_history(self):
        """Exibe o histórico de pontuações."""
        clear_screen()
        print_header("HISTÓRICO DE PONTUAÇÕES")
        
        scores = self.score_manager.get_top_scores(15)
        
        if not scores:
            print("\n📝 Nenhuma pontuação salva ainda.")
            print("🎮 Jogue o quiz e salve sua pontuação para aparecer aqui!")
        else:
            print(f"\n🏆 Top {len(scores)} Pontuações:")
            print()
            print("Pos.  Nome              Pontos  Acertos    %     Data")
            print("-" * 60)
            
            for i, score in enumerate(scores, 1):
                name = score['player'][:15].ljust(15)
                points = str(score['score']).rjust(6)
                correct_total = f"{score['correct']}/{score['total']}".rjust(8)
                percentage = f"{score['percentage']}%".rjust(6)
                date = score['date'][:16]
                
                print(f"{i:2d}.  {name} {points} {correct_total} {percentage}  {date}")
        
        print()
        press_enter_to_continue()
    
    def show_about(self):
        """Exibe informações sobre o jogo."""
        clear_screen()
        print_header("SOBRE O JOGO")
        print("""
🎯 QUIZ EDUCATIVO: SEMÁFOROS E THREADS

📖 Objetivo:
   Este jogo foi desenvolvido para ensinar conceitos fundamentais de
   Sistemas Operacionais, especificamente sobre threads e semáforos,
   de forma interativa e educativa.

🎮 Como Jogar:
   • Escolha quantas perguntas quer responder
   • Leia cada pergunta com atenção
   • Selecione uma das 4 alternativas (A, B, C, D)
   • Receba feedback imediato e explicações
   • Acompanhe sua pontuação em tempo real

🏆 Sistema de Pontuação:
   • 10 pontos por resposta correta
   • Histórico salvo para acompanhar progresso
   • Ranking dos melhores desempenhos

📚 Conteúdo Abordado:
   • Conceitos básicos de threads
   • Semáforos e sincronização
   • Problemas comuns (deadlock, race conditions)
   • Implementação em Python
   • Exemplos práticos

👨‍💻 Desenvolvido para:
   Estudantes de Sistemas Operacionais que querem aprender
   sobre programação concorrente de forma prática e divertida.

🔧 Tecnologias:
   Python, CSV, JSON, Threading concepts
        """)
        press_enter_to_continue()
    
    def run(self):
        """Loop principal do jogo."""
        while self.running:
            self.show_main_menu()
            
            option = input("🔍 Escolha uma opção: ").strip()
            
            if option == "1":
                self.start_quiz()
            elif option == "2":
                self.show_theory_menu()
            elif option == "3":
                self.show_score_history()
            elif option == "4":
                self.show_about()
            elif option == "0":
                self.running = False
                clear_screen()
                print(get_colored_text("👋 Obrigado por jogar!", 'green'))
                print(get_colored_text("📚 Continue estudando threads e semáforos!", 'cyan'))
                print("=" * 60)
            else:
                print("❌ Opção inválida! Tente novamente.")
                press_enter_to_continue()

if __name__ == "__main__":
    game = QuizGame()
    game.run()
