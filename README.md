# 🎯 Quiz Educativo: Semáforos e Threads

Um jogo interativo desenvolvido para ensinar conceitos fundamentais de **Sistemas Operacionais**, especificamente sobre **threads** e **semáforos**, de forma prática e divertida.

## 📋 Descrição

Este projeto é um quiz educativo que permite aos estudantes testarem seus conhecimentos sobre programação concorrente, sincronização de threads e uso de semáforos. O jogo inclui um sistema completo com perguntas, explicações, pontuação e material teórico de apoio.

## 🎮 Funcionalidades

### Menu Principal
- **🎮 Começar Quiz**: Inicia uma sessão de perguntas personalizada
- **📚 Ver Resumo Teórico**: Material didático completo sobre o assunto
- **🏆 Ver Histórico de Pontuações**: Ranking dos melhores desempenhos
- **❓ Sobre o Jogo**: Informações sobre o projeto

### Sistema de Quiz
- Perguntas aleatórias do banco de dados
- Sistema de pontuação (10 pontos por acerto)
- Feedback imediato com explicações
- Relatório final de desempenho
- Salvamento opcional do histórico

### Conteúdo Educativo
- Conceitos básicos de threads
- Semáforos e sincronização
- Problemas comuns (deadlock, race conditions)
- Implementação em Python
- Exemplos práticos

## 📁 Estrutura do Projeto

```
Quiz_Threads_Semaforos/
├── perguntas/
│   ├── perguntas.csv          # Base de dados das perguntas
│   └── interp.py              # Script original de interpretação
├── src/
│   ├── __init__.py
│   ├── quiz_game.py           # Classe principal do jogo
│   ├── question_manager.py    # Gerenciador de perguntas
│   ├── score_manager.py       # Sistema de pontuação
│   └── content_summary.py     # Resumo teórico
├── data/
│   └── scores.json            # Histórico de pontuações (criado automaticamente)
├── utils/
│   ├── __init__.py
│   └── helpers.py             # Funções auxiliares
├── main.py                    # Ponto de entrada do programa
└── README.md                  # Este arquivo
```

## 🚀 Como Usar

### Executando o Jogo

1. **Clone ou baixe o projeto**
2. **Navegue até o diretório do projeto:**
   ```bash
   cd /caminho/para/Quiz_Threads_Semaforos
   ```
3. **Execute o jogo:**
   
   **Opção 1: Script de Inicialização (Recomendado)**
   ```bash
   ./start_quiz.sh
   ```
   Escolha entre:
   - **Interface Gráfica** (moderna e visual)
   - **Terminal/Console** (clássica)
   
   **Opção 2: Execução Direta**
   ```bash
   # Interface Gráfica
   python3 main_gui.py
   
   # Terminal/Console
   python3 main.py
   ```

### 🎨 Interface Gráfica vs Terminal

| Característica | Interface Gráfica | Terminal |
|----------------|------------------|----------|
| **Visual** | ✅ Design moderno e atrativo | ⚫ Texto simples |
| **Navegação** | 🖱️ Cliques e botões | ⌨️ Números e letras |
| **Progresso** | 📊 Barra visual | 📝 Texto |
| **Feedback** | 🎨 Cores e ícones | 📄 Mensagens |
| **Histórico** | 📋 Tabela organizada | 📃 Lista de texto |
| **Acessibilidade** | 👥 Mais intuitivo | 🖥️ Para terminais |

### Navegação

#### Interface Gráfica:
- Use **cliques** para navegar pelos menus
- **Radio buttons** para selecionar respostas
- **Botões** claramente identificados para cada ação
- **Scrolling** automático para conteúdo extenso

#### Terminal:
- Use os **números** para navegar pelos menus
- Digite **A, B, C ou D** para responder às perguntas
- Use **S/N** para confirmações
- Pressione **Enter** para continuar

## 📊 Sistema de Pontuação

- **10 pontos** por resposta correta
- **0 pontos** por resposta incorreta
- Porcentagem de acertos calculada automaticamente
- Mensagens de desempenho baseadas na porcentagem:
  - 90%+: "Excelente! Você é um expert!"
  - 80-89%: "Muito bom conhecimento!"
  - 70-79%: "Bom trabalho!"
  - 60-69%: "Não está mal, mas pode melhorar"
  - 50-59%: "Precisa revisar mais"
  - <50%: "Recomendo estudar o resumo teórico"

## 📚 Conteúdo Abordado

### Threads
- Conceitos básicos e definições
- Vantagens e desafios
- Estados de uma thread
- Implementação em Python

### Semáforos
- Funcionamento e objetivos
- Operações acquire() e release()
- Tipos de semáforos
- Exclusão mútua

### Problemas Comuns
- Race conditions (condições de corrida)
- Deadlock (impasse)
- Livelock
- Starvation (inanição)

### Python Threading
- Biblioteca threading
- GIL (Global Interpreter Lock)
- Boas práticas
- Exemplos práticos

## 🔧 Requisitos Técnicos

- **Python 3.6+**
- **Módulos padrão apenas** (csv, json, random, datetime, os, sys)
- **Terminal com suporte a caracteres UTF-8** (para emojis)

## 📝 Formato das Perguntas

O arquivo `perguntas.csv` deve seguir o formato:

```csv
pergunta,alternativa_a,alternativa_b,alternativa_c,alternativa_d,resposta_correta
"Qual é o objetivo de um semáforo?","Acelerar o programa","Controlar acesso a recursos","Criar threads","Debugar código","B"
```

## 🎯 Objetivos Pedagógicos

Este jogo foi desenvolvido para:

1. **Facilitar o aprendizado** de conceitos complexos através da gamificação
2. **Fornecer feedback imediato** para reforçar o aprendizado
3. **Oferecer material teórico** complementar organizado
4. **Permitir autoavaliação** através do sistema de pontuação
5. **Incentivar a prática** através de múltiplas tentativas

## 🔄 Expansibilidade

O projeto foi designed para ser facilmente expandível:

- **Novas perguntas**: Adicione ao arquivo CSV
- **Novos tópicos**: Expanda o resumo teórico
- **Novas funcionalidades**: Sistema modular permite fácil extensão
- **Diferentes formatos**: Estrutura flexível para outros tipos de questões

## 👨‍💻 Desenvolvido Para

- **Estudantes** de Sistemas Operacionais
- **Professores** que desejam uma ferramenta educativa interativa
- **Autodidatas** interessados em programação concorrente
- **Desenvolvedores** que querem revisar conceitos fundamentais

## 🐛 Troubleshooting

### Erro: "Arquivo de perguntas não encontrado"
- Verifique se `perguntas/perguntas.csv` existe
- Confirme que está executando do diretório correto

### Erro: "Erro ao importar módulos"
- Verifique se todos os arquivos estão nos locais corretos
- Confirme que os arquivos `__init__.py` existem nas pastas

### Caracteres não aparecem corretamente
- Use um terminal com suporte a UTF-8
- No Windows, tente usar PowerShell ou WSL

## 📈 Melhorias Futuras

- [ ] Interface gráfica com tkinter ou PyQt
- [ ] Modo multiplayer
- [ ] Diferentes níveis de dificuldade
- [ ] Estatísticas mais detalhadas
- [ ] Exportação de relatórios
- [ ] Integração com LMS (Learning Management Systems)

---

**🎓 Bons estudos e divirta-se aprendendo sobre threads e semáforos!**
