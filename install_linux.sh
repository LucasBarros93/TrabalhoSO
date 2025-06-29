#!/bin/bash
# ================================================================
# Script de Instalação - TrabalhoSO Quiz Educativo (Linux/macOS)
# ================================================================
# Este script automatiza a instalação e configuração do projeto
# de Quiz Educativo sobre Sistemas Operacionais em sistemas Unix.
#
# Requisitos:
# - Python 3.6+ instalado
# - pip disponível
# - Conexão com a internet (para pip install)
#
# Uso: chmod +x install_linux.sh && ./install_linux.sh
# ================================================================

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função para imprimir mensagens coloridas
print_header() {
    echo -e "${BLUE}============================================${NC}"
    echo -e "${BLUE}   TrabalhoSO - Quiz Educativo sobre SO${NC}"
    echo -e "${BLUE}   Script de Instalação para Linux/macOS${NC}"
    echo -e "${BLUE}============================================${NC}"
    echo ""
}

print_step() {
    echo -e "${GREEN}[${1}] ${2}${NC}"
}

print_warning() {
    echo -e "${YELLOW}AVISO: ${1}${NC}"
}

print_error() {
    echo -e "${RED}ERRO: ${1}${NC}"
}

print_success() {
    echo -e "${GREEN}✓ ${1}${NC}"
}

# Função para verificar se um comando existe
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Início do script
clear
print_header

# [1/5] Verificar se Python está instalado
print_step "1/5" "Verificando instalação do Python..."

if command_exists python3; then
    PYTHON_CMD="python3"
    PYTHON_VERSION=$(python3 --version)
    print_success "Python encontrado: $PYTHON_VERSION"
elif command_exists python; then
    # Verificar se é Python 3
    PYTHON_VERSION=$(python --version 2>&1)
    if [[ $PYTHON_VERSION == *"Python 3"* ]]; then
        PYTHON_CMD="python"
        print_success "Python encontrado: $PYTHON_VERSION"
    else
        print_error "Python 3.6+ é necessário. Encontrado: $PYTHON_VERSION"
        echo "Por favor, instale Python 3.6+ de: https://python.org"
        echo "Ou use o gerenciador de pacotes do seu sistema:"
        echo "  Ubuntu/Debian: sudo apt update && sudo apt install python3 python3-pip python3-tk"
        echo "  CentOS/RHEL: sudo yum install python3 python3-pip python3-tkinter"
        echo "  macOS: brew install python-tk"
        exit 1
    fi
else
    print_error "Python não encontrado no PATH!"
    echo "Por favor, instale Python 3.6+ de: https://python.org"
    echo "Ou use o gerenciador de pacotes do seu sistema:"
    echo "  Ubuntu/Debian: sudo apt update && sudo apt install python3 python3-pip python3-tk"
    echo "  CentOS/RHEL: sudo yum install python3 python3-pip python3-tkinter"
    echo "  macOS: brew install python-tk"
    exit 1
fi
echo ""

# [2/5] Verificar se pip está disponível
print_step "2/5" "Verificando pip..."

if command_exists pip3; then
    PIP_CMD="pip3"
elif command_exists pip; then
    PIP_CMD="pip"
else
    print_warning "pip não encontrado, tentando instalar..."
    if command_exists apt-get; then
        sudo apt-get update && sudo apt-get install -y python3-pip
    elif command_exists yum; then
        sudo yum install -y python3-pip
    elif command_exists brew; then
        brew install python3
    else
        print_error "Não foi possível instalar pip automaticamente"
        echo "Por favor, instale pip manualmente"
        exit 1
    fi
    PIP_CMD="pip3"
fi

print_success "pip está disponível!"
echo ""

# [3/5] Verificar tkinter
print_step "3/5" "Verificando tkinter (interface gráfica)..."

if $PYTHON_CMD -c "import tkinter" 2>/dev/null; then
    print_success "tkinter está disponível!"
else
    print_warning "tkinter não encontrado!"
    echo "O tkinter é necessário para a interface gráfica."
    echo "Instalando tkinter..."
    
    if command_exists apt-get; then
        sudo apt-get install -y python3-tk
    elif command_exists yum; then
        sudo yum install -y python3-tkinter
    elif command_exists dnf; then
        sudo dnf install -y python3-tkinter
    elif command_exists brew; then
        brew install python-tk
    else
        print_warning "Não foi possível instalar tkinter automaticamente"
        echo "Por favor, instale manualmente:"
        echo "  Ubuntu/Debian: sudo apt install python3-tk"
        echo "  CentOS/RHEL: sudo yum install python3-tkinter"
        echo "  macOS: brew install python-tk"
        echo ""
        echo "Você ainda poderá usar a interface de terminal"
    fi
fi
echo ""

# [4/5] Instalar dependências
print_step "4/5" "Verificando dependências..."

if [ -f "requirements.txt" ]; then
    echo "Verificando pacotes do requirements.txt..."
    
    # Tentar instalar normalmente primeiro
    $PIP_CMD install -r requirements.txt 2>/dev/null
    
    if [ $? -ne 0 ]; then
        print_warning "Ambiente Python gerenciado externamente detectado"
        echo "Tentando instalar em modo usuário..."
        
        # Tentar instalar para o usuário
        $PIP_CMD install --user -r requirements.txt 2>/dev/null
        
        if [ $? -ne 0 ]; then
            print_warning "Não foi possível instalar dependências via pip"
            echo "Isso é normal em alguns sistemas Linux modernos."
            echo "O projeto funciona apenas com módulos padrão do Python!"
            echo ""
            echo "Se precisar instalar dependências futuras, use:"
            echo "  • python3 -m venv venv && source venv/bin/activate"
            echo "  • pipx (recomendado para aplicações)"
            echo "  • pip install --user (instalar para usuário)"
        else
            print_success "Dependências instaladas para o usuário!"
        fi
    else
        print_success "Dependências instaladas com sucesso!"
    fi
else
    echo "Arquivo requirements.txt não encontrado"
    echo "✓ Nenhuma dependência externa necessária no momento"
    echo "O projeto usa apenas módulos padrão do Python!"
fi
echo ""

# [5/5] Verificar estrutura do projeto
print_step "5/5" "Verificando estrutura do projeto..."

# Verificar arquivos principais
if [ ! -f "main.py" ]; then
    print_error "main.py não encontrado!"
    echo "Certifique-se de estar no diretório correto do projeto"
    exit 1
fi

if [ ! -f "main_gui.py" ]; then
    print_error "main_gui.py não encontrado!"
    echo "Certifique-se de estar no diretório correto do projeto"
    exit 1
fi

if [ ! -f "perguntas/perguntas.csv" ]; then
    print_warning "perguntas/perguntas.csv não encontrado!"
    echo "O quiz pode não funcionar corretamente sem as perguntas"
fi

if [ ! -d "src" ]; then
    print_error "Pasta src/ não encontrada!"
    echo "Certifique-se de estar no diretório correto do projeto"
    exit 1
fi

print_success "Estrutura do projeto verificada!"
echo ""

# Testar importações básicas
echo "Testando importações básicas do Python..."
if $PYTHON_CMD -c "import csv; import json; import random; print('Módulos básicos OK!')" 2>/dev/null; then
    print_success "Todos os módulos básicos estão funcionando!"
else
    print_warning "Alguns módulos podem não estar disponíveis"
    echo "O projeto deveria funcionar na maioria dos sistemas Python padrão"
fi

# Criar script executável se não existir
if [ ! -f "start_quiz.sh" ]; then
    echo "Criando script de inicialização..."
    cat > start_quiz.sh << 'EOF'
#!/bin/bash
# Script de inicialização do Quiz Educativo

echo "Quiz Educativo sobre Sistemas Operacionais"
echo "==========================================="
echo ""
echo "Escolha a interface:"
echo "1) Interface Gráfica (Recomendado)"
echo "2) Interface Terminal"
echo ""
read -p "Digite sua escolha (1 ou 2): " choice

case $choice in
    1)
        echo "Abrindo interface gráfica..."
        python3 main_gui.py 2>/dev/null || python main_gui.py
        ;;
    2)
        echo "Abrindo interface terminal..."
        python3 main.py 2>/dev/null || python main.py
        ;;
    *)
        echo "Opção inválida. Abrindo interface gráfica..."
        python3 main_gui.py 2>/dev/null || python main_gui.py
        ;;
esac
EOF
    chmod +x start_quiz.sh
    print_success "Script start_quiz.sh criado!"
fi

echo ""
echo -e "${GREEN}============================================${NC}"
echo -e "${GREEN}       INSTALAÇÃO CONCLUÍDA COM SUCESSO!${NC}"
echo -e "${GREEN}============================================${NC}"
echo ""
echo "Como usar:"
echo ""
echo "1. Interface Gráfica (Recomendado):"
echo "   $PYTHON_CMD main_gui.py"
echo ""
echo "2. Interface Terminal:"
echo "   $PYTHON_CMD main.py"
echo ""
echo "3. Script de inicialização:"
echo "   ./start_quiz.sh"
echo ""
echo "Para mais informações, consulte o README.md"
echo ""

# Perguntar se quer abrir o jogo
read -p "Deseja abrir o Quiz Educativo agora? (s/N): " open_game
case $open_game in
    [Ss]*)
        echo "Abrindo o Quiz Educativo..."
        ./start_quiz.sh
        ;;
    *)
        echo "Você pode abrir o jogo mais tarde usando ./start_quiz.sh"
        ;;
esac

echo ""
echo "Obrigado por usar o TrabalhoSO Quiz Educativo!"
