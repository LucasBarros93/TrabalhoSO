import os
import sys

def clear_screen():
    """Limpa a tela do terminal de forma multiplataforma."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_input(prompt, valid_options):
    """
    Obtém entrada válida do usuário.
    
    Args:
        prompt (str): Mensagem para o usuário
        valid_options (list): Lista de opções válidas
    
    Returns:
        str: Opção válida selecionada pelo usuário
    """
    while True:
        user_input = input(prompt).strip().upper()
        if user_input in valid_options:
            return user_input
        print(f"❌ Opção inválida! Escolha entre: {', '.join(valid_options)}")

def print_separator(char="=", length=60):
    """Imprime um separador visual."""
    print(char * length)

def print_header(title):
    """Imprime um cabeçalho formatado."""
    print_separator()
    print(f" {title} ".center(60))
    print_separator()

def press_enter_to_continue():
    """Pausa a execução até o usuário pressionar Enter."""
    input("\nPressione Enter para continuar...")

def format_percentage(correct, total):
    """Formata a porcentagem de acertos."""
    if total == 0:
        return "0.0%"
    percentage = (correct / total) * 100
    return f"{percentage:.1f}%"

def get_colored_text(text, color_code):
    """
    Retorna texto colorido para terminal (se suportado).
    
    Args:
        text (str): Texto a ser colorido
        color_code (str): Código de cor ANSI
    
    Returns:
        str: Texto formatado com cor
    """
    # Códigos de cor ANSI básicos
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'bold': '\033[1m',
        'end': '\033[0m'
    }
    
    if color_code in colors:
        return f"{colors[color_code]}{text}{colors['end']}"
    return text

def display_question_with_formatting(question_num, total_questions, question_data):
    """
    Exibe uma pergunta formatada.
    
    Args:
        question_num (int): Número da pergunta atual
        total_questions (int): Total de perguntas
        question_data (dict): Dados da pergunta
    """
    clear_screen()
    print_header(f"PERGUNTA {question_num}/{total_questions}")
    print()
    print(get_colored_text(f"📝 {question_data['pergunta']}", 'bold'))
    print()
    
    options = ['A', 'B', 'C', 'D']
    for i, option in enumerate(options):
        option_key = f"alternativa_{option.lower()}"
        print(f"{option}) {question_data[option_key]}")
    
    print()

def display_result(is_correct, correct_answer, user_answer):
    """
    Exibe o resultado da resposta.
    
    Args:
        is_correct (bool): Se a resposta está correta
        correct_answer (str): Resposta correta
        user_answer (str): Resposta do usuário
    """
    print()
    if is_correct:
        print(get_colored_text("✅ CORRETO!", 'green'))
        print(get_colored_text("🎉 Parabéns! Você acertou!", 'green'))
    else:
        print(get_colored_text("❌ INCORRETO!", 'red'))
        print(f"Sua resposta: {user_answer}")
        print(get_colored_text(f"Resposta correta: {correct_answer}", 'yellow'))
    print()

def get_explanation_for_topic(question_text):
    """
    Retorna uma explicação breve baseada no tópico da pergunta.
    
    Args:
        question_text (str): Texto da pergunta
    
    Returns:
        str: Explicação relacionada ao tópico
    """
    explanations = {
        'thread': "💡 Threads permitem execução paralela de tarefas, melhorando a eficiência do programa.",
        'semáforo': "🚦 Semáforos controlam o acesso a recursos compartilhados, evitando conflitos entre threads.",
        'acquire': "🔒 O método acquire() obtém permissão para usar um recurso protegido por semáforo.",
        'release': "🔓 O método release() libera a permissão, permitindo que outras threads usem o recurso.",
        'deadlock': "⚠️ Deadlock ocorre quando threads ficam esperando recursos uma das outras indefinidamente.",
        'condição de corrida': "🏃‍♂️ Race conditions acontecem quando o resultado depende da ordem de execução das threads.",
        'exclusão mútua': "🔐 Exclusão mútua garante que apenas uma thread acesse um recurso crítico por vez.",
        'threading': "🐍 A biblioteca threading do Python fornece ferramentas para trabalhar com threads de forma segura."
    }
    
    question_lower = question_text.lower()
    for keyword, explanation in explanations.items():
        if keyword in question_lower:
            return explanation
    
    return "📚 Continue estudando os conceitos de threads e semáforos para melhorar seu conhecimento!"

def validate_player_name(name):
    """
    Valida e formata o nome do jogador.
    
    Args:
        name (str): Nome inserido pelo usuário
    
    Returns:
        str: Nome validado e formatado
    """
    if not name or name.strip() == "":
        return "Anônimo"
    
    # Remove caracteres especiais e limita o tamanho
    clean_name = ''.join(c for c in name if c.isalnum() or c.isspace()).strip()
    return clean_name[:20] if clean_name else "Anônimo"
