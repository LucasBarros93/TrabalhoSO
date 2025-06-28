#!/usr/bin/env python3
"""
🖼️ Demonstração Visual da Interface Gráfica
Script para mostrar as principais telas da interface
"""

import tkinter as tk
from tkinter import ttk
import sys
import os

def create_demo_window():
    """Cria uma janela de demonstração da interface."""
    
    # Janela principal
    root = tk.Tk()
    root.title("🎯 Demo - Quiz Educativo GUI")
    root.geometry("800x600")
    root.configure(bg='#2c3e50')
    
    # Notebook para abas
    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # --- ABA 1: MENU PRINCIPAL ---
    menu_frame = ttk.Frame(notebook)
    notebook.add(menu_frame, text="📱 Menu Principal")
    
    # Título
    title_label = tk.Label(menu_frame, 
                          text="🎯 QUIZ EDUCATIVO", 
                          font=('Arial', 24, 'bold'),
                          bg='#2c3e50', fg='#ecf0f1')
    title_label.pack(pady=20)
    
    subtitle_label = tk.Label(menu_frame,
                             text="Semáforos e Threads - Sistema Operacional",
                             font=('Arial', 14),
                             bg='#2c3e50', fg='#ecf0f1')
    subtitle_label.pack(pady=(0, 30))
    
    # Botões do menu
    buttons_frame = tk.Frame(menu_frame, bg='#2c3e50')
    buttons_frame.pack(expand=True)
    
    menu_buttons = [
        "🎮 Começar Quiz",
        "📚 Ver Resumo Teórico", 
        "🏆 Ver Histórico de Pontuações",
        "❓ Sobre o Jogo",
        "🚪 Sair"
    ]
    
    for btn_text in menu_buttons:
        btn = tk.Button(buttons_frame, text=btn_text,
                       font=('Arial', 11, 'bold'),
                       bg='#3498db', fg='white',
                       width=30, pady=8,
                       relief='flat')
        btn.pack(pady=5)
    
    # Status
    status_label = tk.Label(menu_frame,
                           text="📚 100 perguntas disponíveis",
                           font=('Arial', 12),
                           bg='#2c3e50', fg='#ecf0f1')
    status_label.pack(side=tk.BOTTOM, pady=20)
    
    # --- ABA 2: TELA DE QUIZ ---
    quiz_frame = ttk.Frame(notebook)
    notebook.add(quiz_frame, text="🎮 Tela de Quiz")
    
    quiz_main = tk.Frame(quiz_frame, bg='#ecf0f1')
    quiz_main.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Header
    header_frame = tk.Frame(quiz_main, bg='#ecf0f1')
    header_frame.pack(fill=tk.X, pady=(0, 10))
    
    tk.Label(header_frame, text="👤 João Pedro", 
             font=('Arial', 12), bg='#ecf0f1').pack(side=tk.LEFT)
    tk.Label(header_frame, text="📊 Pergunta 3 de 10",
             font=('Arial', 12), bg='#ecf0f1').pack(side=tk.RIGHT)
    
    # Barra de progresso
    progress = ttk.Progressbar(quiz_main, length=400, mode='determinate')
    progress.pack(pady=(0, 20))
    progress['value'] = 30
    
    # Pergunta
    question_frame = tk.LabelFrame(quiz_main, text="Pergunta", 
                                  font=('Arial', 12, 'bold'), 
                                  bg='#ecf0f1', pady=10)
    question_frame.pack(fill=tk.X, pady=(0, 15))
    
    question_text = "Qual é uma vantagem do uso de threads?"
    tk.Label(question_frame, text=question_text,
             font=('Arial', 12, 'bold'), 
             bg='#ecf0f1', wraplength=600).pack()
    
    # Alternativas
    alt_frame = tk.LabelFrame(quiz_main, text="Alternativas",
                             font=('Arial', 12, 'bold'),
                             bg='#ecf0f1', pady=10)
    alt_frame.pack(fill=tk.X, pady=(0, 15))
    
    selected = tk.StringVar()
    alternatives = [
        "A) Eliminam bugs automaticamente",
        "B) Deixam o programa mais seguro", 
        "C) Reduzem o uso de memória",
        "D) Permitem dividir tarefas e usar melhor os núcleos do processador"
    ]
    
    for alt in alternatives:
        tk.Radiobutton(alt_frame, text=alt, variable=selected,
                      value=alt[0], font=('Arial', 11),
                      bg='#ecf0f1').pack(anchor=tk.W, pady=2)
    
    # Botões
    btn_frame = tk.Frame(quiz_main, bg='#ecf0f1')
    btn_frame.pack(pady=15)
    
    tk.Button(btn_frame, text="✅ Responder",
              font=('Arial', 11, 'bold'),
              bg='#2ecc71', fg='white', 
              padx=20, pady=8).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="🔙 Menu Principal",
              font=('Arial', 11),
              bg='#7f8c8d', fg='white',
              padx=20, pady=8).pack(side=tk.LEFT, padx=5)
    
    # --- ABA 3: RESULTADOS ---
    results_frame = ttk.Frame(notebook)
    notebook.add(results_frame, text="📊 Resultados")
    
    results_main = tk.Frame(results_frame, bg='#ecf0f1')
    results_main.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Título de resultados
    tk.Label(results_main, text="🏁 RESULTADOS DO QUIZ",
             font=('Arial', 20, 'bold'),
             bg='#ecf0f1', fg='#2c3e50').pack(pady=20)
    
    # Resultados
    results_info = tk.LabelFrame(results_main, text="Resultados de João Pedro",
                                font=('Arial', 12, 'bold'),
                                bg='#ecf0f1', pady=15)
    results_info.pack(fill=tk.X, pady=20)
    
    results_text = """📊 Pontuação Final: 80 pontos
✅ Respostas Corretas: 8 de 10
📈 Porcentagem de Acertos: 80%
🎯 Avaliação: Muito bom conhecimento!"""
    
    tk.Label(results_info, text=results_text,
             font=('Arial', 12), justify=tk.LEFT,
             bg='#ecf0f1').pack()
    
    # Botões de ação
    action_frame = tk.Frame(results_main, bg='#ecf0f1')
    action_frame.pack(pady=20)
    
    action_buttons = [
        ("💾 Salvar Pontuação", '#3498db'),
        ("🔄 Jogar Novamente", '#2ecc71'),
        ("🔙 Menu Principal", '#7f8c8d')
    ]
    
    for btn_text, color in action_buttons:
        tk.Button(action_frame, text=btn_text,
                 font=('Arial', 11, 'bold'),
                 bg=color, fg='white',
                 padx=15, pady=8).pack(side=tk.LEFT, padx=5)
    
    # --- ABA 4: HISTÓRICO ---
    history_frame = ttk.Frame(notebook)
    notebook.add(history_frame, text="🏆 Histórico")
    
    history_main = tk.Frame(history_frame, bg='#ecf0f1')
    history_main.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    tk.Label(history_main, text="🏆 HISTÓRICO DE PONTUAÇÕES",
             font=('Arial', 18, 'bold'),
             bg='#ecf0f1', fg='#2c3e50').pack(pady=15)
    
    # Tabela de exemplo
    table_frame = tk.Frame(history_main, bg='#ecf0f1')
    table_frame.pack(fill=tk.BOTH, expand=True, pady=10)
    
    # Cabeçalho
    headers = ["#", "Nome", "Pontuação", "Acertos (%)", "Data"]
    header_frame = tk.Frame(table_frame, bg='#34495e')
    header_frame.pack(fill=tk.X, pady=(0, 1))
    
    for header in headers:
        tk.Label(header_frame, text=header,
                font=('Arial', 11, 'bold'),
                bg='#34495e', fg='white',
                pady=8).pack(side=tk.LEFT, fill=tk.X, expand=True)
    
    # Dados de exemplo
    sample_data = [
        ("1", "Maria Silva", "90 pts", "90%", "24/06/2025"),
        ("2", "João Pedro", "80 pts", "80%", "24/06/2025"),
        ("3", "Ana Costa", "75 pts", "75%", "23/06/2025"),
        ("4", "Carlos Lima", "70 pts", "70%", "23/06/2025")
    ]
    
    for row in sample_data:
        row_frame = tk.Frame(table_frame, bg='#ecf0f1')
        row_frame.pack(fill=tk.X, pady=1)
        
        for cell in row:
            tk.Label(row_frame, text=cell,
                    font=('Arial', 10),
                    bg='#ecf0f1', 
                    pady=5).pack(side=tk.LEFT, fill=tk.X, expand=True)
    
    # Informações adicionais
    info_frame = tk.Frame(root, bg='#2c3e50')
    info_frame.pack(fill=tk.X, side=tk.BOTTOM)
    
    info_text = "🎨 Interface Gráfica Moderna | 🚀 Execute: python3 main_gui.py"
    tk.Label(info_frame, text=info_text,
             font=('Arial', 10),
             bg='#2c3e50', fg='#ecf0f1',
             pady=10).pack()
    
    return root

def main():
    """Executa a demonstração."""
    print("🖼️ Criando demonstração visual da interface...")
    
    try:
        root = create_demo_window()
        print("✅ Demonstração criada!")
        print("🎨 Navegue pelas abas para ver as diferentes telas")
        print("🔍 Feche a janela para encerrar")
        
        root.mainloop()
        
    except Exception as e:
        print(f"❌ Erro ao criar demonstração: {e}")

if __name__ == "__main__":
    main()
