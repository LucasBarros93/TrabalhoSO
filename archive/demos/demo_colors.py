#!/usr/bin/env python3
"""
🎨 Demonstração do Novo Esquema de Cores
Mostra as telas com cores específicas para acertos e erros
"""

import tkinter as tk
from tkinter import ttk
import time

def create_color_demo():
    """Cria uma demonstração das cores do novo esquema."""
    
    # Cores do novo esquema
    colors = {
        'primary': '#6c5ce7',       # Roxo principal
        'secondary': '#74b9ff',     # Azul suave
        'accent': '#a29bfe',        # Roxo claro
        'success': '#00b894',       # Verde escuro para acertos
        'success_bg': '#00cec9',    # Verde água para fundo de acerto
        'error': '#e17055',         # Vermelho suave para erros
        'error_bg': '#fd79a8',      # Rosa avermelhado para fundo de erro
        'dark': '#2d3436',          # Cinza escuro
        'light': '#ddd',            # Cinza claro
        'text_light': '#f8f9fa',    # Texto claro
        'text_dark': '#2d3436'      # Texto escuro
    }
    
    root = tk.Tk()
    root.title("🎨 Demonstração do Esquema de Cores")
    root.geometry("900x600")
    root.configure(bg=colors['dark'])
    
    # Notebook para demonstrar diferentes estados
    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # --- ABA 1: MENU PRINCIPAL (Roxo/Azul) ---
    menu_frame = tk.Frame(notebook, bg=colors['dark'])
    notebook.add(menu_frame, text="📱 Menu Principal")
    
    tk.Label(menu_frame, text="🎯 QUIZ EDUCATIVO", 
             font=('Arial', 24, 'bold'),
             bg=colors['dark'], fg=colors['text_light']).pack(pady=20)
    
    tk.Label(menu_frame, text="Semáforos e Threads - Sistema Operacional",
             font=('Arial', 14),
             bg=colors['dark'], fg=colors['accent']).pack(pady=(0, 30))
    
    # Botões com esquema roxo/azul
    buttons_frame = tk.Frame(menu_frame, bg=colors['dark'])
    buttons_frame.pack(expand=True)
    
    menu_buttons = [
        ("🎮 Começar Quiz", colors['primary']),
        ("📚 Ver Resumo Teórico", colors['secondary']),
        ("🏆 Ver Histórico", colors['secondary']),
        ("❓ Sobre o Jogo", colors['secondary'])
    ]
    
    for btn_text, color in menu_buttons:
        btn = tk.Button(buttons_frame, text=btn_text,
                       font=('Arial', 11, 'bold'),
                       bg=color, fg='white',
                       width=25, pady=8, relief='flat')
        btn.pack(pady=8)
    
    # --- ABA 2: RESPOSTA CORRETA (Verde) ---
    correct_frame = tk.Frame(notebook, bg=colors['success_bg'])
    notebook.add(correct_frame, text="✅ Resposta Correta")
    
    # Header de sucesso
    success_header = tk.Frame(correct_frame, bg=colors['success'], padx=20, pady=15)
    success_header.pack(fill=tk.X, padx=20, pady=(20, 10))
    
    tk.Label(success_header, text="✅ PARABÉNS! CORRETO!",
             font=('Arial', 24, 'bold'),
             bg=colors['success'], fg='white').pack()
    
    # Detalhes do feedback
    details_frame = tk.LabelFrame(correct_frame, text="📋 Detalhes da Resposta",
                                 font=('Arial', 12, 'bold'),
                                 bg=colors['light'], fg=colors['text_dark'],
                                 padx=20, pady=15)
    details_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    
    tk.Label(details_frame, text="❓ Pergunta: Qual é uma vantagem do uso de threads?",
             font=('Arial', 11, 'bold'),
             bg=colors['light'], fg=colors['text_dark']).pack(anchor=tk.W, pady=5)
    
    tk.Label(details_frame, text="👤 Sua resposta: D) Permitem dividir tarefas",
             font=('Arial', 11, 'bold'),
             bg=colors['light'], fg=colors['success']).pack(anchor=tk.W, pady=5)
    
    tk.Label(details_frame, text="✅ Resposta correta: D) Permitem dividir tarefas",
             font=('Arial', 11, 'bold'),
             bg=colors['light'], fg=colors['success']).pack(anchor=tk.W, pady=5)
    
    tk.Label(details_frame, text="📊 Pontuação: 80 pontos | Acertos: 8/10 (80%)",
             font=('Arial', 11, 'bold'),
             bg=colors['light'], fg=colors['primary']).pack(anchor=tk.W, pady=10)
    
    # Botões de ação
    btn_frame = tk.Frame(correct_frame, bg=colors['success_bg'])
    btn_frame.pack(pady=20)
    
    tk.Button(btn_frame, text="➡️ Próxima Pergunta",
              font=('Arial', 11, 'bold'),
              bg=colors['primary'], fg='white',
              padx=20, pady=8, relief='flat').pack(side=tk.LEFT, padx=5)
    
    tk.Button(btn_frame, text="🔙 Menu Principal",
              font=('Arial', 11),
              bg=colors['secondary'], fg='white',
              padx=20, pady=8, relief='flat').pack(side=tk.LEFT, padx=5)
    
    # --- ABA 3: RESPOSTA INCORRETA (Vermelho) ---
    wrong_frame = tk.Frame(notebook, bg=colors['error_bg'])
    notebook.add(wrong_frame, text="❌ Resposta Incorreta")
    
    # Header de erro
    error_header = tk.Frame(wrong_frame, bg=colors['error'], padx=20, pady=15)
    error_header.pack(fill=tk.X, padx=20, pady=(20, 10))
    
    tk.Label(error_header, text="❌ OPS! INCORRETO!",
             font=('Arial', 24, 'bold'),
             bg=colors['error'], fg='white').pack()
    
    # Detalhes do feedback
    details_frame2 = tk.LabelFrame(wrong_frame, text="📋 Detalhes da Resposta",
                                  font=('Arial', 12, 'bold'),
                                  bg=colors['light'], fg=colors['text_dark'],
                                  padx=20, pady=15)
    details_frame2.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    
    tk.Label(details_frame2, text="❓ Pergunta: O que pode causar deadlock?",
             font=('Arial', 11, 'bold'),
             bg=colors['light'], fg=colors['text_dark']).pack(anchor=tk.W, pady=5)
    
    tk.Label(details_frame2, text="👤 Sua resposta: A) Uso de listas em paralelo",
             font=('Arial', 11, 'bold'),
             bg=colors['light'], fg=colors['error']).pack(anchor=tk.W, pady=5)
    
    tk.Label(details_frame2, text="✅ Resposta correta: B) Threads esperando eternamente",
             font=('Arial', 11, 'bold'),
             bg=colors['light'], fg=colors['success']).pack(anchor=tk.W, pady=5)
    
    tk.Label(details_frame2, text="📊 Pontuação: 60 pontos | Acertos: 6/10 (60%)",
             font=('Arial', 11, 'bold'),
             bg=colors['light'], fg=colors['primary']).pack(anchor=tk.W, pady=10)
    
    # Botões de ação
    btn_frame2 = tk.Frame(wrong_frame, bg=colors['error_bg'])
    btn_frame2.pack(pady=20)
    
    tk.Button(btn_frame2, text="➡️ Próxima Pergunta",
              font=('Arial', 11, 'bold'),
              bg=colors['primary'], fg='white',
              padx=20, pady=8, relief='flat').pack(side=tk.LEFT, padx=5)
    
    tk.Button(btn_frame2, text="🔙 Menu Principal",
              font=('Arial', 11),
              bg=colors['secondary'], fg='white',
              padx=20, pady=8, relief='flat').pack(side=tk.LEFT, padx=5)
    
    # --- ABA 4: PALETA DE CORES ---
    colors_frame = tk.Frame(notebook, bg=colors['light'])
    notebook.add(colors_frame, text="🎨 Paleta de Cores")
    
    tk.Label(colors_frame, text="🎨 NOVO ESQUEMA DE CORES",
             font=('Arial', 20, 'bold'),
             bg=colors['light'], fg=colors['text_dark']).pack(pady=20)
    
    # Grid de cores
    grid_frame = tk.Frame(colors_frame, bg=colors['light'])
    grid_frame.pack(expand=True)
    
    color_samples = [
        ("🟣 Roxo Principal", colors['primary'], "Botões principais"),
        ("🔵 Azul Suave", colors['secondary'], "Botões secundários"),
        ("🟢 Verde Acerto", colors['success'], "Respostas corretas"),
        ("💚 Fundo Verde", colors['success_bg'], "Tela de acerto"),
        ("🔴 Vermelho Erro", colors['error'], "Respostas incorretas"),
        ("💗 Fundo Rosa", colors['error_bg'], "Tela de erro"),
        ("⚫ Fundo Escuro", colors['dark'], "Background principal"),
        ("🟪 Roxo Claro", colors['accent'], "Texto de destaque")
    ]
    
    for i, (name, color, desc) in enumerate(color_samples):
        row = i // 2
        col = i % 2
        
        color_frame = tk.Frame(grid_frame, bg=color, padx=20, pady=15)
        color_frame.grid(row=row, column=col, padx=10, pady=10, sticky='ew')
        
        tk.Label(color_frame, text=name,
                font=('Arial', 12, 'bold'),
                bg=color, fg='white').pack()
        
        tk.Label(color_frame, text=color,
                font=('Arial', 10),
                bg=color, fg='white').pack()
        
        tk.Label(color_frame, text=desc,
                font=('Arial', 9),
                bg=color, fg='white').pack()
    
    # Informações adicionais
    info_frame = tk.Frame(root, bg=colors['dark'])
    info_frame.pack(fill=tk.X, side=tk.BOTTOM)
    
    info_text = "🎨 Novo esquema de cores: Roxo/Azul para interface geral | Verde vibrante para acertos | Vermelho/Rosa para erros"
    tk.Label(info_frame, text=info_text,
             font=('Arial', 10),
             bg=colors['dark'], fg=colors['text_light'],
             wraplength=800, pady=10).pack()
    
    return root

def main():
    """Executa a demonstração."""
    print("🎨 Criando demonstração do novo esquema de cores...")
    
    try:
        root = create_color_demo()
        print("✅ Demonstração criada!")
        print("🌈 Navegue pelas abas para ver:")
        print("   • Menu Principal (Roxo/Azul)")
        print("   • Resposta Correta (Verde vibrante)")
        print("   • Resposta Incorreta (Vermelho/Rosa)")
        print("   • Paleta de Cores completa")
        print("🔍 Feche a janela para encerrar")
        
        root.mainloop()
        
    except Exception as e:
        print(f"❌ Erro ao criar demonstração: {e}")

if __name__ == "__main__":
    main()
