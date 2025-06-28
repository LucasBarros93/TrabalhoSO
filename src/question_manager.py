import csv
import random
import os

class QuestionManager:
    """Gerencia o carregamento e seleção de perguntas do quiz."""
    
    def __init__(self, csv_path="perguntas/perguntas.csv"):
        self.csv_path = csv_path
        self.questions = []
        self.load_questions()
    
    def load_questions(self):
        """Carrega as perguntas do arquivo CSV."""
        try:
            # Ajusta o caminho relativo ao diretório do script
            if '__file__' in globals():
                script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                full_path = os.path.join(script_dir, self.csv_path)
            else:
                # Fallback para quando __file__ não está disponível
                full_path = self.csv_path
            
            with open(full_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                self.questions = list(reader)
            
            print(f"✅ {len(self.questions)} perguntas carregadas com sucesso!")
            
        except FileNotFoundError:
            print(f"❌ Erro: Arquivo {self.csv_path} não encontrado!")
            self.questions = []
        except Exception as e:
            print(f"❌ Erro ao carregar perguntas: {e}")
            self.questions = []
    
    def get_random_questions(self, num_questions=10):
        """Retorna uma lista de perguntas aleatórias."""
        if not self.questions:
            return []
        
        # Se temos menos perguntas que o solicitado, retorna todas
        if len(self.questions) < num_questions:
            num_questions = len(self.questions)
        
        return random.sample(self.questions, num_questions)
    
    def get_all_questions(self):
        """Retorna todas as perguntas disponíveis."""
        return self.questions.copy()
    
    def validate_answer(self, question, user_answer):
        """Valida se a resposta do usuário está correta."""
        correct_answer = question['resposta_correta'].upper()
        user_answer = user_answer.upper()
        return user_answer == correct_answer
    
    def get_question_count(self):
        """Retorna o número total de perguntas disponíveis."""
        return len(self.questions)
