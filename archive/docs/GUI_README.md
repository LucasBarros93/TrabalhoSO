# 🎨 Interface Gráfica - Quiz Educativo

## 📱 Versão GUI do Quiz

A interface gráfica oferece uma experiência visual moderna e intuitiva para o quiz educativo sobre semáforos e threads.

## 🚀 Como Executar

### Opção 1: Script de Inicialização (Recomendado)
```bash
./start_quiz.sh
```
Escolha a opção **1** para a interface gráfica.

### Opção 2: Execução Direta
```bash
python3 main_gui.py
```

## 🎨 Design e Funcionalidades

### 🏠 Menu Principal
- **Design moderno** com tema escuro elegante
- **Botões intuitivos** com ícones e descrições claras
- **Status bar** mostrando quantidade de perguntas disponíveis
- **Navegação simples** entre as funcionalidades

### 🎮 Interface de Quiz
- **Barra de progresso** visual em tempo real
- **Cabeçalho informativo** com nome do jogador e progresso
- **Layout limpo** para perguntas e alternativas
- **Radio buttons** para seleção de respostas
- **Feedback imediato** com cores (verde/vermelho)

### 📊 Tela de Resultados
- **Pontuação destacada** com design atrativo
- **Estatísticas completas** (acertos, porcentagem, avaliação)
- **Opções claras** para próximas ações
- **Mensagens motivacionais** baseadas no desempenho

### 📚 Resumo Teórico
- **Texto scrollável** com barra de rolagem
- **Formatação clara** e organizada
- **Conteúdo educativo completo** sobre threads e semáforos
- **Navegação fácil** de volta ao menu

### 🏆 Histórico de Pontuações
- **Tabela organizada** usando TreeView
- **Ranking automático** dos melhores desempenhos
- **Colunas informativas**: Posição, Nome, Pontuação, Acertos %, Data
- **Scroll vertical** para muitos registros

## 🎨 Paleta de Cores

| Cor | Código | Uso |
|-----|--------|-----|
| 🔵 Azul Primário | `#3498db` | Botões principais |
| 🟢 Verde Sucesso | `#2ecc71` | Respostas corretas |
| 🔴 Vermelho Erro | `#e74c3c` | Respostas incorretas |
| ⚫ Fundo Escuro | `#2c3e50` | Background principal |
| ⚪ Texto Claro | `#ecf0f1` | Textos sobre fundo escuro |

## 🖥️ Compatibilidade

### Sistemas Operacionais
- ✅ **Linux** (testado)
- ✅ **Windows** (compatível)
- ✅ **macOS** (compatível)

### Requisitos
- **Python 3.6+**
- **Tkinter** (incluído na maioria das instalações Python)
- **Resolução mínima**: 1000x700 pixels

## 🎯 Vantagens da Interface Gráfica

### 📈 Experiência do Usuário
- **Visual atrativo** aumenta o engajamento
- **Navegação intuitiva** reduz curva de aprendizado
- **Feedback visual imediato** melhora o aprendizado
- **Layout responsivo** se adapta ao conteúdo

### 🎓 Benefícios Educacionais
- **Maior concentração** com interface limpa
- **Menos distrações** que o terminal
- **Melhor organização** da informação
- **Experiência mais profissional**

### ⚡ Funcionalidades Avançadas
- **Barra de progresso** motiva a conclusão
- **Histórico visual** facilita comparações
- **Texto scrollável** para conteúdo extenso
- **Validação visual** de inputs

## 🔧 Personalização

### Modificando Cores
Edite o dicionário `colors` na classe `QuizGUI`:
```python
self.colors = {
    'primary': '#3498db',      # Cor primária
    'secondary': '#2ecc71',    # Cor secundária
    'danger': '#e74c3c',       # Cor de erro
    'warning': '#f39c12',      # Cor de aviso
    'dark': '#2c3e50',         # Fundo escuro
    'light': '#ecf0f1',        # Texto claro
}
```

### Alterando Fontes
Modifique as configurações de estilo:
```python
font=('Arial', 12, 'bold')  # (família, tamanho, estilo)
```

## 🐛 Solução de Problemas

### Interface não abre
1. Verifique se o Tkinter está instalado:
   ```bash
   python3 -c "import tkinter; print('Tkinter OK!')"
   ```

2. Verifique se há servidor X rodando (Linux):
   ```bash
   echo $DISPLAY
   ```

### Fontes ou caracteres estranhos
- Use um sistema com suporte completo a UTF-8
- No Windows, use PowerShell ou WSL

### Janela muito pequena
- Verifique a resolução mínima (1000x700)
- A janela é centralizada automaticamente

## 🚀 Próximas Melhorias

- [ ] **Temas personalizáveis** (claro/escuro)
- [ ] **Sons de feedback** para acertos/erros
- [ ] **Animações suaves** entre telas
- [ ] **Gráficos de estatísticas** com matplotlib
- [ ] **Modo tela cheia** para apresentações
- [ ] **Atalhos de teclado** para navegação rápida

---

**🎨 Desenvolvido com foco na experiência do usuário e eficácia educacional!**
