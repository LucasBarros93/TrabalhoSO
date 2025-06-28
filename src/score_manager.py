import json
import os
from datetime import datetime

class ScoreManager:
    """Gerencia o sistema de pontuação e histórico de partidas."""
    
    def __init__(self, scores_file="data/scores.json"):
        self.scores_file = scores_file
        self.current_score = 0
        self.total_questions = 0
        self.correct_answers = 0
        self.ensure_data_directory()
    
    def ensure_data_directory(self):
        """Garante que o diretório de dados existe."""
        if '__file__' in globals():
            script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            data_dir = os.path.join(script_dir, "data")
        else:
            # Fallback para quando __file__ não está disponível
            data_dir = "data"
        
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
    
    def reset_score(self):
        """Reseta a pontuação atual."""
        self.current_score = 0
        self.total_questions = 0
        self.correct_answers = 0
    
    def add_question(self, is_correct):
        """Adiciona uma pergunta ao contador e atualiza pontuação."""
        self.total_questions += 1
        if is_correct:
            self.correct_answers += 1
            self.current_score += 10  # 10 pontos por resposta correta
    
    def get_current_stats(self):
        """Retorna estatísticas da partida atual."""
        if self.total_questions == 0:
            percentage = 0
        else:
            percentage = (self.correct_answers / self.total_questions) * 100
        
        return {
            'score': self.current_score,
            'correct': self.correct_answers,
            'total': self.total_questions,
            'percentage': round(percentage, 1)
        }
    
    def get_performance_message(self):
        """Retorna uma mensagem baseada no desempenho."""
        stats = self.get_current_stats()
        percentage = stats['percentage']
        
        if percentage >= 90:
            return "🏆 Excelente! Você é um expert em semáforos e threads!"
        elif percentage >= 80:
            return "🎉 Muito bom! Você tem um ótimo conhecimento do assunto!"
        elif percentage >= 70:
            return "👍 Bom trabalho! Continue estudando para melhorar ainda mais!"
        elif percentage >= 60:
            return "📚 Não está mal, mas há espaço para melhorias!"
        elif percentage >= 50:
            return "⚠️ Você precisa revisar mais os conceitos de threads e semáforos."
        else:
            return "📖 Recomendo estudar o resumo teórico antes de tentar novamente."
    
    def save_score(self, player_name="Anônimo", score=None, percentage=None):
        """Salva a pontuação atual no histórico.
        
        Args:
            player_name (str): Nome do jogador
            score (int, optional): Pontuação específica. Se None, usa current_score
            percentage (float, optional): Porcentagem específica. Se None, calcula automaticamente
        """
        if '__file__' in globals():
            script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            full_path = os.path.join(script_dir, self.scores_file)
        else:
            # Fallback para quando __file__ não está disponível
            full_path = self.scores_file
        
        # Carrega scores existentes ou cria lista vazia
        scores = self.load_scores()
        
        # Usa valores fornecidos ou valores atuais
        final_score = score if score is not None else self.current_score
        final_percentage = percentage if percentage is not None else self.get_current_stats()['percentage']
        
        # Adiciona nova pontuação
        new_score = {
            'name': player_name,  # Mudando de 'player' para 'name' para consistência
            'score': final_score,
            'correct': self.correct_answers,
            'total': self.total_questions,
            'percentage': final_percentage,
            'date': datetime.now().strftime('%d/%m/%Y %H:%M')  # Formato brasileiro
        }
        
        scores.append(new_score)
        
        # Salva no arquivo
        try:
            with open(full_path, 'w', encoding='utf-8') as f:
                json.dump(scores, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"❌ Erro ao salvar pontuação: {e}")
            return False
    
    def load_scores(self):
        """Carrega o histórico de pontuações."""
        if '__file__' in globals():
            script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            full_path = os.path.join(script_dir, self.scores_file)
        else:
            # Fallback para quando __file__ não está disponível
            full_path = self.scores_file
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"❌ Erro ao carregar pontuações: {e}")
            return []
    
    def get_top_scores(self, limit=10):
        """Retorna os melhores scores ordenados por pontuação."""
        scores = self.load_scores()
        # Ordena por pontuação (decrescente) e depois por porcentagem
        scores.sort(key=lambda x: (x['score'], x['percentage']), reverse=True)
        return scores[:limit]
