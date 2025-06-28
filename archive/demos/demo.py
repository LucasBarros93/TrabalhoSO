#!/usr/bin/env python3
"""
Script de demonstração do Quiz Educativo: Semáforos e Threads
Mostra algumas funcionalidades básicas do jogo
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.question_manager import QuestionManager
from src.score_manager import ScoreManager
from src.content_summary import ContentSummary

def demonstrar_quiz():
    """Demonstra as funcionalidades básicas do quiz."""
    print("🎯 DEMONSTRAÇÃO DO QUIZ EDUCATIVO: SEMÁFOROS E THREADS")
    print("=" * 60)
    
    # Demonstra carregamento de perguntas
    print("\n📚 1. CARREGAMENTO DE PERGUNTAS")
    print("-" * 30)
    qm = QuestionManager()
    print(f"Total de perguntas disponíveis: {qm.get_question_count()}")
    
    # Mostra algumas perguntas de exemplo
    print("\n📝 2. EXEMPLOS DE PERGUNTAS")
    print("-" * 30)
    sample_questions = qm.get_random_questions(3)
    
    for i, q in enumerate(sample_questions, 1):
        print(f"\nPergunta {i}: {q['pergunta']}")
        print(f"A) {q['alternativa_a']}")
        print(f"B) {q['alternativa_b']}")
        print(f"C) {q['alternativa_c']}")
        print(f"D) {q['alternativa_d']}")
        print(f"Resposta correta: {q['resposta_correta']}")
        print("-" * 40)
    
    # Demonstra sistema de pontuação
    print("\n🏆 3. SISTEMA DE PONTUAÇÃO")
    print("-" * 30)
    sm = ScoreManager()
    
    # Simula algumas respostas
    sm.add_question(True)   # Acertou
    sm.add_question(False)  # Errou
    sm.add_question(True)   # Acertou
    sm.add_question(True)   # Acertou
    
    stats = sm.get_current_stats()
    print(f"Perguntas respondidas: {stats['total']}")
    print(f"Respostas corretas: {stats['correct']}")
    print(f"Porcentagem de acertos: {stats['percentage']}%")
    print(f"Pontuação: {stats['score']} pontos")
    print(f"Avaliação: {sm.get_performance_message()}")
    
    # Demonstra tópicos do resumo teórico
    print("\n📖 4. TÓPICOS DO RESUMO TEÓRICO")
    print("-" * 30)
    topics = [
        "🧵 Conceitos Básicos de Threads",
        "🚦 Semáforos e Sincronização",
        "⚠️ Problemas Comuns (Deadlock, Race Conditions)",
        "🐍 Threads em Python",
        "💡 Exemplos Práticos"
    ]
    
    for topic in topics:
        print(f"• {topic}")
    
    print("\n🎮 5. COMO EXECUTAR O JOGO COMPLETO")
    print("-" * 30)
    print("Para jogar o quiz interativo, execute:")
    print("python3 main.py")
    print("\nFuncionalidades disponíveis:")
    print("• Quiz interativo com feedback")
    print("• Sistema de pontuação e ranking")
    print("• Material teórico completo")
    print("• Histórico de partidas")
    
    print("\n✅ DEMONSTRAÇÃO CONCLUÍDA!")
    print("🎓 O jogo está pronto para uso educativo!")

if __name__ == "__main__":
    demonstrar_quiz()
