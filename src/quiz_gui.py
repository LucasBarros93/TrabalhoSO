#!/usr/bin/env python3
"""
🎯 QUIZ EDUCATIVO: SEMÁFOROS E THREADS - Interface Gráfica
Interface gráfica moderna usando Tkinter para o quiz educativo
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import sys
import os

# Adiciona o diretório pai ao path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.question_manager import QuestionManager
from src.score_manager import ScoreManager
from src.content_summary import ContentSummary

class QuizGUI:
    """Interface gráfica principal do quiz educativo."""
    
    def __init__(self):
        self.question_manager = QuestionManager()
        self.score_manager = ScoreManager()
        self.content_summary = ContentSummary()
        
        # Configuração da janela principal
        self.root = tk.Tk()
        self.setup_main_window()
        
        # Estado do quiz (criado após a janela principal)
        self.current_questions = []
        self.current_question_index = 0
        self.selected_answer = tk.StringVar()
        self.player_name = ""
        
        self.create_main_menu()
    
    def setup_main_window(self):
        """Configura a janela principal."""
        # Configurações de cores personalizadas - Esquema Roxo/Azul
        self.colors = {
            'primary': '#6c5ce7',       # Roxo principal
            'secondary': '#74b9ff',     # Azul suave
            'accent': '#a29bfe',        # Roxo claro
            'success': '#00b894',       # Verde escuro para acertos
            'success_bg': '#00cec9',    # Verde água para fundo de acerto
            'error': '#e17055',         # Vermelho suave para erros
            'error_bg': '#fd79a8',      # Rosa avermelhado para fundo de erro
            'dark': '#2d3436',          # Cinza escuro
            'darker': '#636e72',        # Cinza médio
            'light': '#ddd',            # Cinza claro
            'text_light': '#f8f9fa',    # Texto claro
            'text_dark': '#2d3436',     # Texto escuro
            'background': '#74b9ff'     # Azul de fundo
        }
        
        self.root.title("🎯 Quiz Educativo: Semáforos e Threads")
        self.root.geometry("1000x700")
        self.root.configure(bg=self.colors['dark'])
        
        # Centraliza a janela na tela
        self.root.eval('tk::PlaceWindow . center')
        
        # Configuração de estilo
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.configure_styles()
    
    def configure_styles(self):
        """Configura os estilos customizados com esquema roxo/azul."""
        # Frame principal
        self.style.configure('Main.TFrame', background=self.colors['dark'])
        
        # Botões
        self.style.configure('Primary.TButton',
                           padding=(20, 10),
                           font=('Arial', 11, 'bold'),
                           background=self.colors['primary'],
                           foreground='white')
        
        self.style.configure('Secondary.TButton',
                           padding=(15, 8),
                           font=('Arial', 10),
                           background=self.colors['secondary'],
                           foreground='white')
        
        self.style.configure('Success.TButton',
                           padding=(15, 8),
                           font=('Arial', 10, 'bold'),
                           background=self.colors['success'],
                           foreground='white')
        
        # Labels
        self.style.configure('Title.TLabel',
                           background=self.colors['dark'],
                           foreground=self.colors['text_light'],
                           font=('Arial', 24, 'bold'))
        
        self.style.configure('Subtitle.TLabel',
                           background=self.colors['dark'],
                           foreground=self.colors['accent'],
                           font=('Arial', 14))
        
        self.style.configure('Question.TLabel',
                           background=self.colors['light'],
                           foreground=self.colors['text_dark'],
                           font=('Arial', 12, 'bold'),
                           wraplength=700)
        
        # Labels para feedback
        self.style.configure('Success.TLabel',
                           background=self.colors['success_bg'],
                           foreground='white',
                           font=('Arial', 20, 'bold'))
        
        self.style.configure('Error.TLabel',
                           background=self.colors['error_bg'],
                           foreground='white',
                           font=('Arial', 20, 'bold'))
    
    def create_main_menu(self):
        """Cria o menu principal."""
        # Reseta as cores da janela
        self.root.configure(bg=self.colors['dark'])
        
        self.clear_window()
        
        # Frame principal
        main_frame = ttk.Frame(self.root, style='Main.TFrame', padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = ttk.Label(main_frame, 
                               text="🎯 QUIZ EDUCATIVO",
                               style='Title.TLabel')
        title_label.pack(pady=(0, 10))
        
        subtitle_label = ttk.Label(main_frame,
                                 text="Semáforos e Threads - Sistema Operacional",
                                 style='Subtitle.TLabel')
        subtitle_label.pack(pady=(0, 30))
        
        # Frame para os botões
        buttons_frame = ttk.Frame(main_frame, style='Main.TFrame')
        buttons_frame.pack(expand=True)
        
        # Botões do menu
        buttons = [
            ("🎮 Começar Quiz", self.start_quiz_setup, 'Primary.TButton'),
            ("📚 Ver Resumo Teórico", self.show_theory_summary, 'Secondary.TButton'),
            ("🏆 Ver Histórico de Pontuações", self.show_score_history, 'Secondary.TButton'),
            ("❓ Sobre o Jogo", self.show_about, 'Secondary.TButton'),
            ("🚪 Sair", self.quit_game, 'Secondary.TButton')
        ]
        
        for i, (text, command, style) in enumerate(buttons):
            btn = ttk.Button(buttons_frame, text=text, command=command, style=style)
            btn.pack(pady=10, ipadx=20)
        
        # Status bar
        status_frame = ttk.Frame(main_frame, style='Main.TFrame')
        status_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(20, 0))
        
        status_text = f"📚 {len(self.question_manager.questions)} perguntas disponíveis"
        status_label = ttk.Label(status_frame, text=status_text, style='Subtitle.TLabel')
        status_label.pack()
    
    def start_quiz_setup(self):
        """Tela de configuração do quiz."""
        self.clear_window()
        
        main_frame = ttk.Frame(self.root, style='Main.TFrame', padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = ttk.Label(main_frame,
                               text="⚙️ CONFIGURAÇÃO DO QUIZ",
                               style='Title.TLabel')
        title_label.pack(pady=(0, 30))
        
        # Frame para configurações
        config_frame = ttk.LabelFrame(main_frame, text="Configurações", padding="20")
        config_frame.pack(pady=20, padx=50, fill=tk.X)
        
        # Nome do jogador
        ttk.Label(config_frame, text="👤 Seu nome:", font=('Arial', 12)).pack(anchor=tk.W)
        self.name_entry = ttk.Entry(config_frame, font=('Arial', 12), width=30)
        self.name_entry.pack(pady=(5, 15), fill=tk.X)
        self.name_entry.focus()
        
        # Número de perguntas
        ttk.Label(config_frame, text="📝 Número de perguntas:", font=('Arial', 12)).pack(anchor=tk.W)
        self.questions_var = tk.StringVar(value="10")
        questions_frame = ttk.Frame(config_frame)
        questions_frame.pack(pady=(5, 15), fill=tk.X)
        
        for num in ["5", "10", "15", "20"]:
            ttk.Radiobutton(questions_frame, text=f"{num} perguntas", 
                          variable=self.questions_var, value=num).pack(side=tk.LEFT, padx=(0, 20))
        
        # Botões
        buttons_frame = ttk.Frame(main_frame, style='Main.TFrame')
        buttons_frame.pack(pady=30)
        
        ttk.Button(buttons_frame, text="🚀 Começar Quiz!", 
                  command=self.start_quiz, style='Primary.TButton').pack(side=tk.LEFT, padx=10)
        ttk.Button(buttons_frame, text="🔙 Voltar", 
                  command=self.create_main_menu, style='Secondary.TButton').pack(side=tk.LEFT, padx=10)
    
    def start_quiz(self):
        """Inicia o quiz."""
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Aviso", "Por favor, digite seu nome!")
            return
        
        self.player_name = name
        num_questions = int(self.questions_var.get())
        
        # Prepara as perguntas
        self.current_questions = self.question_manager.get_random_questions(num_questions)
        if not self.current_questions:
            messagebox.showerror("Erro", "Não foi possível carregar as perguntas!")
            return
        
        self.current_question_index = 0
        self.score_manager = ScoreManager()  # Reset do score
        
        self.show_question()
    
    def show_question(self):
        """Mostra a pergunta atual."""
        if self.current_question_index >= len(self.current_questions):
            self.show_quiz_results()
            return
        
        # Reseta as cores da janela
        self.root.configure(bg=self.colors['dark'])
        
        self.clear_window()
        
        question = self.current_questions[self.current_question_index]
        question_num = self.current_question_index + 1
        total_questions = len(self.current_questions)
        
        main_frame = ttk.Frame(self.root, style='Main.TFrame', padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header com progresso
        header_frame = ttk.Frame(main_frame, style='Main.TFrame')
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(header_frame, 
                 text=f"👤 {self.player_name}",
                 style='Subtitle.TLabel').pack(side=tk.LEFT)
        
        ttk.Label(header_frame,
                 text=f"📊 Pergunta {question_num} de {total_questions}",
                 style='Subtitle.TLabel').pack(side=tk.RIGHT)
        
        # Barra de progresso
        progress_frame = ttk.Frame(main_frame)
        progress_frame.pack(fill=tk.X, pady=(0, 20))
        
        progress = ttk.Progressbar(progress_frame, length=400, mode='determinate')
        progress.pack()
        progress['value'] = (question_num / total_questions) * 100
        
        # Pergunta
        question_frame = ttk.LabelFrame(main_frame, text="Pergunta", padding="20")
        question_frame.pack(fill=tk.X, pady=(0, 20))
        
        question_label = ttk.Label(question_frame,
                                 text=question['pergunta'],
                                 style='Question.TLabel')
        question_label.pack()
        
        # Alternativas
        alternatives_frame = ttk.LabelFrame(main_frame, text="Alternativas", padding="20")
        alternatives_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.selected_answer.set("")  # Reset da seleção
        
        alternatives = [
            ('A', question['alternativa_a']),
            ('B', question['alternativa_b']),
            ('C', question['alternativa_c']),
            ('D', question['alternativa_d'])
        ]
        
        for letter, text in alternatives:
            alt_frame = ttk.Frame(alternatives_frame)
            alt_frame.pack(fill=tk.X, pady=5)
            
            ttk.Radiobutton(alt_frame, text=f"{letter}) {text}",
                          variable=self.selected_answer, value=letter,
                          style='TRadiobutton').pack(anchor=tk.W)
        
        # Botões
        buttons_frame = ttk.Frame(main_frame, style='Main.TFrame')
        buttons_frame.pack(pady=20)
        
        ttk.Button(buttons_frame, text="✅ Responder",
                  command=self.submit_answer, style='Primary.TButton').pack(side=tk.LEFT, padx=10)
        ttk.Button(buttons_frame, text="🔙 Menu Principal",
                  command=self.create_main_menu, style='Secondary.TButton').pack(side=tk.LEFT, padx=10)
    
    def submit_answer(self):
        """Processa a resposta do usuário."""
        if not self.selected_answer.get():
            messagebox.showwarning("Aviso", "Por favor, selecione uma alternativa!")
            return
        
        question = self.current_questions[self.current_question_index]
        correct_answer = question['resposta_correta'].upper()
        user_answer = self.selected_answer.get().upper()
        
        is_correct = user_answer == correct_answer
        self.score_manager.add_question(is_correct)
        
        self.show_answer_feedback(question, is_correct, user_answer)
    
    def show_answer_feedback(self, question, is_correct, user_answer):
        """Mostra o feedback da resposta com cores vibrantes."""
        self.clear_window()
        
        # Cores e configurações baseadas no resultado
        if is_correct:
            bg_color = self.colors['success_bg']
            result_text = "✅ PARABÉNS! CORRETO!"
            result_style = 'Success.TLabel'
            frame_bg = self.colors['success']
        else:
            bg_color = self.colors['error_bg']  
            result_text = "❌ OPS! INCORRETO!"
            result_style = 'Error.TLabel'
            frame_bg = self.colors['error']
        
        # Atualiza o fundo da janela temporariamente
        self.root.configure(bg=bg_color)
        
        main_frame = tk.Frame(self.root, bg=bg_color, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Resultado com fundo colorido
        result_frame = tk.Frame(main_frame, bg=frame_bg, padx=20, pady=15)
        result_frame.pack(fill=tk.X, pady=(0, 20))
        
        result_label = tk.Label(result_frame, text=result_text, 
                               font=('Arial', 24, 'bold'),
                               bg=frame_bg, fg='white')
        result_label.pack()
        
        # Feedback detalhado com fundo claro
        feedback_frame = tk.LabelFrame(main_frame, text="📋 Detalhes da Resposta", 
                                      font=('Arial', 12, 'bold'),
                                      bg=self.colors['light'], 
                                      fg=self.colors['text_dark'],
                                      padx=20, pady=15)
        feedback_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        # Pergunta
        tk.Label(feedback_frame, text="❓ Pergunta:", 
                font=('Arial', 12, 'bold'),
                bg=self.colors['light'], 
                fg=self.colors['text_dark']).pack(anchor=tk.W)
        tk.Label(feedback_frame, text=question['pergunta'], 
                font=('Arial', 11), wraplength=700,
                bg=self.colors['light'], 
                fg=self.colors['text_dark']).pack(anchor=tk.W, pady=(0, 10))
        
        # Sua resposta
        user_color = self.colors['success'] if is_correct else self.colors['error']
        tk.Label(feedback_frame, text="👤 Sua resposta:", 
                font=('Arial', 12, 'bold'),
                bg=self.colors['light'], 
                fg=user_color).pack(anchor=tk.W)
        user_alt = question[f'alternativa_{user_answer.lower()}'] if user_answer in 'ABCD' else "Não selecionada"
        tk.Label(feedback_frame, text=f"{user_answer}) {user_alt}",
                font=('Arial', 11, 'bold'),
                bg=self.colors['light'], 
                fg=user_color).pack(anchor=tk.W, pady=(0, 10))
        
        # Resposta correta
        correct_answer = question['resposta_correta'].upper()
        tk.Label(feedback_frame, text="✅ Resposta correta:", 
                font=('Arial', 12, 'bold'),
                bg=self.colors['light'], 
                fg=self.colors['success']).pack(anchor=tk.W)
        correct_alt = question[f'alternativa_{correct_answer.lower()}']
        tk.Label(feedback_frame, text=f"{correct_answer}) {correct_alt}",
                font=('Arial', 11, 'bold'),
                bg=self.colors['light'], 
                fg=self.colors['success']).pack(anchor=tk.W, pady=(0, 15))
        
        # Pontuação atual
        stats = self.score_manager.get_current_stats()
        score_text = f"📊 Pontuação: {stats['score']} pontos | Acertos: {stats['correct']}/{stats['total']} ({stats['percentage']}%)"
        tk.Label(feedback_frame, text=score_text, 
                font=('Arial', 11, 'bold'),
                bg=self.colors['light'], 
                fg=self.colors['primary']).pack(anchor=tk.W)
        
        # Botões com cores do esquema
        buttons_frame = tk.Frame(main_frame, bg=bg_color)
        buttons_frame.pack(pady=20)
        
        self.current_question_index += 1
        if self.current_question_index < len(self.current_questions):
            next_btn = tk.Button(buttons_frame, text="➡️ Próxima Pergunta",
                               command=self.show_question,
                               font=('Arial', 11, 'bold'),
                               bg=self.colors['primary'], fg='white',
                               padx=20, pady=8, relief='flat')
            next_btn.pack(side=tk.LEFT, padx=10)
        else:
            results_btn = tk.Button(buttons_frame, text="🏁 Ver Resultados",
                                  command=self.show_quiz_results,
                                  font=('Arial', 11, 'bold'),
                                  bg=self.colors['success'], fg='white',
                                  padx=20, pady=8, relief='flat')
            results_btn.pack(side=tk.LEFT, padx=10)
        
        menu_btn = tk.Button(buttons_frame, text="🔙 Menu Principal",
                           command=self.create_main_menu,
                           font=('Arial', 11),
                           bg=self.colors['secondary'], fg='white',
                           padx=20, pady=8, relief='flat')
        menu_btn.pack(side=tk.LEFT, padx=10)
    
    def show_quiz_results(self):
        """Mostra os resultados finais do quiz."""
        # Reseta as cores da janela
        self.root.configure(bg=self.colors['dark'])
        
        self.clear_window()
        
        main_frame = ttk.Frame(self.root, style='Main.TFrame', padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        ttk.Label(main_frame, text="🏁 RESULTADOS DO QUIZ",
                 style='Title.TLabel').pack(pady=(0, 30))
        
        # Resultados
        results_frame = ttk.LabelFrame(main_frame, text=f"Resultados de {self.player_name}", padding="20")
        results_frame.pack(fill=tk.X, pady=(0, 20))
        
        stats = self.score_manager.get_current_stats()
        performance_msg = self.score_manager.get_performance_message()
        
        results_text = f"""
📊 Pontuação Final: {stats['score']} pontos
✅ Respostas Corretas: {stats['correct']} de {stats['total']}
📈 Porcentagem de Acertos: {stats['percentage']}%
🎯 Avaliação: {performance_msg}
        """
        
        ttk.Label(results_frame, text=results_text.strip(),
                 font=('Arial', 12), justify=tk.LEFT).pack()
        
        # Opção de salvar com cores do novo esquema
        save_frame = tk.Frame(main_frame, bg=self.colors['dark'])
        save_frame.pack(pady=20)
        
        save_btn = tk.Button(save_frame, text="💾 Salvar Pontuação",
                           command=self.save_score,
                           font=('Arial', 11, 'bold'),
                           bg=self.colors['success'], fg='white',
                           padx=20, pady=8, relief='flat')
        save_btn.pack(side=tk.LEFT, padx=10)
        
        again_btn = tk.Button(save_frame, text="🔄 Jogar Novamente",
                            command=self.start_quiz_setup,
                            font=('Arial', 11, 'bold'),
                            bg=self.colors['primary'], fg='white',
                            padx=20, pady=8, relief='flat')
        again_btn.pack(side=tk.LEFT, padx=10)
        
        menu_btn = tk.Button(save_frame, text="🔙 Menu Principal",
                           command=self.create_main_menu,
                           font=('Arial', 11),
                           bg=self.colors['secondary'], fg='white',
                           padx=20, pady=8, relief='flat')
        menu_btn.pack(side=tk.LEFT, padx=10)
    
    def save_score(self):
        """Salva a pontuação no histórico."""
        stats = self.score_manager.get_current_stats()
        self.score_manager.save_score(self.player_name, stats['score'], stats['percentage'])
        messagebox.showinfo("Sucesso", "Pontuação salva com sucesso!")
    
    def show_theory_summary(self):
        """Mostra o resumo teórico."""
        self.clear_window()
        
        main_frame = ttk.Frame(self.root, style='Main.TFrame', padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        ttk.Label(main_frame, text="📚 RESUMO TEÓRICO",
                 style='Title.TLabel').pack(pady=(0, 20))
        
        # Texto com scroll
        text_frame = ttk.Frame(main_frame)
        text_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        text_widget = scrolledtext.ScrolledText(text_frame, wrap=tk.WORD, font=('Arial', 11))
        text_widget.pack(fill=tk.BOTH, expand=True)
        
        # Adiciona o conteúdo teórico
        summary_content = self.content_summary.get_full_summary()
        text_widget.insert(tk.END, summary_content)
        text_widget.config(state=tk.DISABLED)  # Torna somente leitura
        
        # Botão voltar
        ttk.Button(main_frame, text="🔙 Voltar",
                  command=self.create_main_menu, style='Secondary.TButton').pack()
    
    def show_score_history(self):
        """Mostra o histórico de pontuações."""
        self.clear_window()
        
        main_frame = ttk.Frame(self.root, style='Main.TFrame', padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        ttk.Label(main_frame, text="🏆 HISTÓRICO DE PONTUAÇÕES",
                 style='Title.TLabel').pack(pady=(0, 20))
        
        # Tabela de pontuações
        scores_frame = ttk.Frame(main_frame)
        scores_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        # Treeview para mostrar as pontuações
        columns = ('rank', 'name', 'score', 'percentage', 'date')
        tree = ttk.Treeview(scores_frame, columns=columns, show='headings', height=15)
        
        # Configurar cabeçalhos
        tree.heading('rank', text='#')
        tree.heading('name', text='Nome')
        tree.heading('score', text='Pontuação')
        tree.heading('percentage', text='Acertos (%)')
        tree.heading('date', text='Data')
        
        # Configurar larguras das colunas
        tree.column('rank', width=50)
        tree.column('name', width=200)
        tree.column('score', width=100)
        tree.column('percentage', width=120)
        tree.column('date', width=150)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(scores_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Carregar dados do histórico
        try:
            scores = self.score_manager.get_top_scores(50)  # Top 50
            for i, score in enumerate(scores, 1):
                tree.insert('', tk.END, values=(
                    i,
                    score['name'],
                    f"{score['score']} pts",
                    f"{score['percentage']}%",
                    score['date']
                ))
        except Exception as e:
            tree.insert('', tk.END, values=('', 'Nenhum histórico encontrado', '', '', ''))
        
        # Botão voltar
        ttk.Button(main_frame, text="🔙 Voltar",
                  command=self.create_main_menu, style='Secondary.TButton').pack()
    
    def show_about(self):
        """Mostra informações sobre o jogo."""
        about_text = """
🎯 QUIZ EDUCATIVO: SEMÁFOROS E THREADS

📖 Sobre o Jogo:
Este é um jogo educativo desenvolvido para ensinar conceitos fundamentais 
de Sistemas Operacionais, especificamente sobre threads e semáforos, 
de forma prática e divertida.

🎯 Objetivos:
• Facilitar o aprendizado através da gamificação
• Fornecer feedback imediato para reforçar o conhecimento
• Oferecer material teórico complementar
• Permitir autoavaliação através do sistema de pontuação

🔧 Tecnologias:
• Python 3.6+
• Tkinter (Interface Gráfica)
• CSV (Base de dados das perguntas)

👨‍💻 Desenvolvido para:
• Estudantes de Sistemas Operacionais
• Professores que desejam uma ferramenta educativa
• Autodidatas interessados em programação concorrente

🎓 Bons estudos!
        """
        
        messagebox.showinfo("Sobre o Jogo", about_text.strip())
    
    def quit_game(self):
        """Encerra o jogo."""
        if messagebox.askyesno("Sair", "Tem certeza que deseja sair do jogo?"):
            self.root.quit()
    
    def clear_window(self):
        """Limpa todos os widgets da janela."""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def run(self):
        """Executa a interface gráfica."""
        self.root.mainloop()


def main():
    """Função principal."""
    app = QuizGUI()
    app.run()

if __name__ == "__main__":
    main()
