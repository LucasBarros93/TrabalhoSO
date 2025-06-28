#!/bin/bash
# Script de inicialização do Quiz Educativo: Semáforos e Threads

echo "🎯 QUIZ EDUCATIVO: SEMÁFOROS E THREADS"
echo "======================================"
echo ""

# Verifica se Python 3 está disponível
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Por favor, instale Python 3.6 ou superior."
    exit 1
fi

# Verifica a versão do Python
python_version=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "🐍 Python detectado: versão $python_version"

# Verifica se o arquivo de perguntas existe
if [ ! -f "perguntas/perguntas.csv" ]; then
    echo "❌ Arquivo de perguntas não encontrado em perguntas/perguntas.csv"
    exit 1
fi

echo "📚 Arquivo de perguntas encontrado"

python3 main_gui.py
