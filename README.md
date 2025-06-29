# 🎯 TrabalhoSO: Quiz Educativo sobre Sistemas Operacionais

Um projeto educativo interativo para ensinar conceitos fundamentais de **Sistemas Operacionais**, incluindo threads, semáforos, escalonamento de processos e sincronização através de um sistema de quiz gamificado.

## 📋 Descrição

Este projeto oferece uma experiência de aprendizado interativa e gamificada:

**🎯 Quiz Educativo**: Sistema completo de perguntas e respostas para testar e consolidar conhecimentos sobre programação concorrente, sincronização e conceitos fundamentais de Sistemas Operacionais.

O projeto utiliza gamificação para facilitar o entendimento de tópicos complexos, oferecendo feedback imediato e material teórico complementar.

## 🎮 Funcionalidades

### 🎯 Quiz Educativo
#### Interface Dupla
- **🖥️ Interface Gráfica (tkinter)**: Design moderno e intuitivo
- **⌨️ Interface Terminal/Console**: Experiência clássica para terminais

#### Menu Principal
- **🎮 Começar Quiz**: Inicia uma sessão de perguntas personalizada
- **📚 Ver Resumo Teórico**: Material didático completo sobre o assunto
- **🏆 Ver Histórico de Pontuações**: Ranking dos melhores desempenhos
- **❓ Sobre o Jogo**: Informações sobre o projeto

#### Sistema de Quiz
- **Perguntas aleatórias** do banco de dados CSV
- **Sistema de pontuação** (10 pontos por acerto)
- **Feedback imediato** com explicações detalhadas
- **Relatório final** de desempenho com estatísticas
- **Salvamento opcional** do histórico de pontuações
- **Múltiplas tentativas** para reforçar o aprendizado

#### Conteúdo Educativo Abrangente
- **Conceitos básicos** de threads e processos
- **Semáforos e sincronização** em detalhes
- **Problemas clássicos** (deadlock, race conditions, starvation)
- **Implementação prática** em Python
- **Exemplos de código** comentados
- **Boas práticas** de programação concorrente

## 📁 Estrutura do Projeto

```
TrabalhoSO/
├── 🎯 APLICAÇÃO PRINCIPAL
│   ├── main.py                 # Interface terminal/console
│   ├── main_gui.py             # Interface gráfica (tkinter)
│   ├── start_quiz.sh           # Script de inicialização (Linux/macOS)
│   ├── requirements.txt        # Dependências Python
│   ├── README.md               # Este arquivo
│   ├── install_linux.sh       # Script de instalação para Linux
│   └── install_windows.bat     # Script de instalação para Windows
├── 📊 DADOS E CONTEÚDO
│   ├── perguntas/
│   │   └── perguntas.csv       # Base de dados das perguntas
│   └── data/
│       └── scores.json         # Histórico de pontuações
├── 🧩 CÓDIGO FONTE MODULAR
│   ├── src/
│   │   ├── __init__.py
│   │   ├── quiz_game.py        # Classe principal do jogo
│   │   ├── quiz_gui.py         # Interface gráfica tkinter
│   │   ├── question_manager.py # Gerenciador de perguntas
│   │   ├── score_manager.py    # Sistema de pontuação e histórico
│   │   └── content_summary.py  # Resumo teórico completo
│   └── utils/
│       ├── __init__.py
│       └── helpers.py          # Funções auxiliares e utilitários
└── 📚 DOCUMENTAÇÃO E ARQUIVOS
    └── archive/                # Versões anteriores e demos
        ├── interp.py           # Script original do projeto
        ├── docs/               # Documentação adicional
        │   └── GUI_README.md   # Documentação da interface gráfica
        └── demos/              # Demonstrações e testes
            ├── demo.py         # Demonstração básica
            ├── demo_colors.py  # Teste de cores no terminal
            └── demo_gui.py     # Teste da interface gráfica
```

## 🚀 Como Usar

### ⚡ Instalação Rápida

> 📖 **Para instruções detalhadas de instalação, consulte [INSTALL.md](INSTALL.md)**

**Windows:**
```batch
# Duplo clique no arquivo ou execute via linha de comando:
install_windows.bat
```

**Linux/macOS:**
```bash
# Torne o script executável e execute:
chmod +x install_linux.sh
./install_linux.sh
```

Os scripts de instalação irão:
- ✅ Verificar se Python 3.6+ está instalado
- ✅ Verificar e instalar dependências necessárias
- ✅ Validar a estrutura do projeto
- ✅ Testar módulos básicos
- ✅ Criar scripts de inicialização
- ✅ Oferecer abertura automática do jogo

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

### Para o Quiz Educativo:
- **Python 3.6+**
- **Tkinter** (geralmente incluído com Python)
- **Módulos padrão apenas** (csv, json, random, datetime, os, sys)
- **Terminal com suporte a caracteres UTF-8** (para emojis)

### Instalação de Dependências por Sistema:

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install python3 python3-pip python3-tk
```

**CentOS/RHEL:**
```bash
sudo yum install python3 python3-pip python3-tkinter
```

**macOS:**
```bash
brew install python-tk
```

**Windows:**
- Baixe Python de https://python.org
- Certifique-se de marcar "Add Python to PATH" durante a instalação
- Tkinter já vem incluído

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

### Problemas de Instalação

#### Erro: "externally-managed-environment" (Linux)
Este é um comportamento normal em distribuições Linux modernas. O projeto funciona apenas com módulos padrão!
```bash
# Alternativas se precisar instalar dependências futuras:
python3 -m venv venv && source venv/bin/activate  # Ambiente virtual
pip install --user package_name                   # Instalação para usuário
pipx install package_name                        # Para aplicações (recomendado)
```

#### Erro: "Arquivo de perguntas não encontrado"
- Verifique se `perguntas/perguntas.csv` existe
- Confirme que está executando do diretório correto

#### Erro: "Erro ao importar módulos"
- Verifique se todos os arquivos estão nos locais corretos
- Confirme que os arquivos `__init__.py` existem nas pastas

#### Caracteres não aparecem corretamente
- Use um terminal com suporte a UTF-8
- No Windows, tente usar PowerShell ou WSL

#### Erro: "tkinter não encontrado" (Linux)
```bash
# Ubuntu/Debian
sudo apt install python3-tk

# CentOS/RHEL/Fedora
sudo dnf install python3-tkinter

# Arch Linux
sudo pacman -S tk
```

#### Problemas de Permissão (Scripts)
```bash
# Tornar scripts executáveis
chmod +x install_linux.sh start_quiz.sh
```

## 📈 Melhorias Futuras

- [ ] 🌐 Interface web com Flask/Django
- [ ] 👥 Modo multiplayer
- [ ] 📊 Diferentes níveis de dificuldade
- [ ] 📈 Estatísticas mais detalhadas
- [ ] 📄 Exportação de relatórios em PDF
- [ ] 🎓 Integração com LMS (Learning Management Systems)
- [ ] 🔊 Suporte a áudio para acessibilidade
- [ ] 🌍 Internacionalização (i18n)
- [ ] 📱 Versão mobile responsiva
- [ ] 🤖 Sistema de hints automáticos

## 🤝 Contribuindo

Este projeto está aberto para contribuições! Para contribuir:

1. **Fork** o repositório
2. **Crie** uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. **Abra** um Pull Request

### Áreas que Precisam de Ajuda:
- 📝 Mais perguntas para o banco de dados
- 🎨 Melhorias na interface gráfica
- 🐛 Correção de bugs
- 📚 Documentação adicional
- 🧪 Testes automatizados

## 📄 Licença

Este projeto está sob licença educativa. Sinta-se livre para usar, modificar e distribuir para fins educacionais.

---

**🎓 Bons estudos e divirta-se aprendendo sobre threads e semáforos!**
