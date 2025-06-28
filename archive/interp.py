import csv

with open("perguntas.csv", newline='', encoding='utf-8') as csvfile:
    leitor = csv.DictReader(csvfile)
    perguntas = list(leitor)

# Exemplo de uso:
for p in perguntas:
    print("Pergunta:", p['pergunta'])
    print("A)", p['alternativa_a'])
    print("B)", p['alternativa_b'])
    print("C)", p['alternativa_c'])
    print("D)", p['alternativa_d'])
    print("Resposta correta:", p['resposta_correta'])
    print("-" * 30)
