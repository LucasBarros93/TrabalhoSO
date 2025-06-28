# 🚦 TrabalhoSO: Simulador de Cruzamento de Trânsito

Um projeto educativo completo que combina **teoria** e **prática** para ensinar conceitos fundamentais de **Sistemas Operacionais**, incluindo threads, semáforos, escalonamento de processos e sincronização.

## 📋 Descrição

Este projeto oferece duas experiências de aprendizado complementares:

1. **🎮 Simulador de Cruzamento (Novo!)**: Um jogo visual interativo onde você controla um semáforo, gerenciando filas de carros que representam threads com diferentes prioridades
2. **🎯 Quiz Educativo**: Sistema de perguntas para testar conhecimentos sobre programação concorrente e sincronização

O projeto simula conceitos reais de SO de forma prática e visual, facilitando o entendimento de tópicos complexos.

## 🎮 Funcionalidades

### 🚦 Simulador de Cruzamento de Trânsito (Novo!)
- **Interface visual moderna**: HTML5, CSS3 e JavaScript modularizado
- **Gerenciamento de filas**: Até 3 carros por direção (Norte, Sul, Leste, Oeste)
- **Tipos de veículos**: 
  - 🚗 Carros comuns (prioridade normal)
  - 🚓 Polícia (alta prioridade)
  - 🚑 Ambulância (prioridade máxima)
- **Sistema de pontuação**: Baseado em eficiência e priorização
- **Mecânicas de jogo**:
  - Timeout de veículos (simula starvation)
  - Bloqueio de vias durante travessia
  - Notificações visuais de novos veículos
  - Animações de travessia
  - Sistema de contagem visual das filas
  - Imagens personalizadas para carros comuns
- **Backend Flask**: Servidor para servir a aplicação
- **Conceitos de SO demonstrados**:
  - **Threads**: Cada carro representa uma thread
  - **Semáforos**: O cruzamento é uma seção crítica
  - **Escalonamento**: O jogador atua como scheduler
  - **Prioridades**: Diferentes tipos de veículos
  - **Starvation**: Timeout de veículos

### 🎯 Quiz Educativo
#### Menu Principal
- **🎮 Começar Quiz**: Inicia uma sessão de perguntas personalizada
- **📚 Ver Resumo Teórico**: Material didático completo sobre o assunto
- **🏆 Ver Histórico de Pontuações**: Ranking dos melhores desempenhos
- **❓ Sobre o Jogo**: Informações sobre o projeto

#### Sistema de Quiz
- Perguntas aleatórias do banco de dados
- Sistema de pontuação (10 pontos por acerto)
- Feedback imediato com explicações
- Relatório final de desempenho
- Salvamento opcional do histórico

#### Conteúdo Educativo
- Conceitos básicos de threads
- Semáforos e sincronização
- Problemas comuns (deadlock, race conditions)
- Implementação em Python
- Exemplos práticos

## 📁 Estrutura do Projeto

```
TrabalhoSO/
├── 🚦 SIMULADOR DE CRUZAMENTO (NOVO!)
│   ├── index.html              # Estrutura principal do jogo
│   ├── style.css               # Estilos visuais modernos
│   ├── game.js                 # Lógica do jogo (modularizado)
│   ├── app.py                  # Backend Flask para servir aplicação
│   └── imagens/                # Assets visuais
│       └── car.png             # Imagem personalizada do carro comum
├── 🎯 QUIZ EDUCATIVO
│   ├── main.py                 # Interface terminal/console
│   ├── main_gui.py             # Interface gráfica (tkinter)
│   ├── start_quiz.sh           # Script de inicialização
│   ├── requirements.txt        # Dependências Python
│   ├── perguntas/
│   │   └── perguntas.csv       # Base de dados das perguntas
│   ├── src/
│   │   ├── __init__.py
│   │   ├── quiz_game.py        # Classe principal do jogo
│   │   ├── quiz_gui.py         # Interface gráfica tkinter
│   │   ├── question_manager.py # Gerenciador de perguntas
│   │   ├── score_manager.py    # Sistema de pontuação
│   │   └── content_summary.py  # Resumo teórico
│   ├── data/
│   │   └── scores.json         # Histórico de pontuações
│   └── utils/
│       ├── __init__.py
│       └── helpers.py          # Funções auxiliares
├── 📚 DOCUMENTAÇÃO E ARQUIVOS
│   ├── README.md               # Este arquivo
│   └── archive/                # Versões anteriores e demos
│       ├── interp.py           # Script original
│       ├── sugestao_cloudIA.html # Versão monolítica do simulador
│       └── demos/              # Demonstrações e testes
│           ├── demo.py         # Demonstração básica
│           ├── demo_colors.py  # Teste de cores
│           └── demo_gui.py     # Teste de interface
└── 📊 DADOS COMPARTILHADOS
    └── scores.json             # Histórico de pontuações global
```

## 🚀 Como Usar

### 🚦 Simulador de Cruzamento

1. **Navegue até o diretório do projeto:**
   ```bash
   cd /home/joaopedromm/bolao/python_codes/TrabalhoSO
   ```

2. **Opção 1: Executar diretamente no navegador**
   ```bash
   # Abra o arquivo index.html no seu navegador
   open index.html  # macOS
   xdg-open index.html  # Linux
   start index.html  # Windows
   ```

3. **Opção 2: Usar o servidor Flask (Recomendado)**
   ```bash
   # Instale as dependências (se necessário)
   pip install flask
   
   # Execute o servidor
   python3 app.py
   
   # Acesse no navegador: http://localhost:5000
   ```

4. **Como jogar:**
   - Clique em **"Start Game"** para iniciar
   - Carros aparecerão aleatoriamente nas 4 direções (Norte, Sul, Leste, Oeste)
   - Cada direção pode ter até **3 carros na fila**
   - Clique nos botões das pistas para liberar os carros
   - **Priorize veículos de emergência** (🚑 Ambulância, 🚓 Polícia) para evitar timeouts
   - Observe as **barras de tempo de espera** de cada carro
   - **Notificações** aparecem quando novos veículos chegam
   - Gerencie o tráfego para maximizar sua pontuação
   - Use **Pause** para pausar o jogo a qualquer momento

### 🎯 Quiz Educativo

1. **Execute o jogo:**
   
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

### Para o Simulador de Cruzamento:
- **Navegador moderno** (Chrome, Firefox, Safari, Edge)
- **Flask** (opcional, para servidor local): `pip install flask`
- **Pasta imagens/** com arquivo `car.png` (imagem personalizada do carro comum)
- **JavaScript habilitado** no navegador
- **Resolução mínima**: 1024x768 para melhor experiência visual

### Para o Quiz Educativo:
- **Python 3.6+**
- **Tkinter** (geralmente incluído com Python)
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
