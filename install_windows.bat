@echo off
REM ================================================================
REM Script de Instalação - TrabalhoSO Quiz Educativo (Windows)
REM ================================================================
REM Este script automatiza a instalação e configuração do projeto
REM de Quiz Educativo sobre Sistemas Operacionais no Windows.
REM
REM Requisitos:
REM - Python 3.6+ instalado e no PATH
REM - Conexão com a internet (para pip install)
REM
REM Uso: Duplo clique no arquivo ou execute via linha de comando
REM ================================================================

echo.
echo ============================================
echo   TrabalhoSO - Quiz Educativo sobre SO
echo   Script de Instalacao para Windows
echo ============================================
echo.

REM Verificar se Python está instalado
echo [1/4] Verificando instalacao do Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERRO: Python nao encontrado no PATH!
    echo.
    echo Por favor, instale Python 3.6+ de: https://python.org
    echo Certifique-se de marcar "Add Python to PATH" durante a instalacao
    echo.
    pause
    exit /b 1
)

python --version
echo Python encontrado com sucesso!
echo.

REM Verificar se pip está disponível
echo [2/4] Verificando pip...
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERRO: pip nao encontrado!
    echo Instalando pip...
    python -m ensurepip --upgrade
)

echo pip esta disponivel!
echo.

REM Instalar dependências
echo [3/4] Instalando dependencias...
if exist requirements.txt (
    echo Instalando pacotes do requirements.txt...
    python -m pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo AVISO: Erro ao instalar algumas dependencias
        echo O projeto pode ainda funcionar, pois usa principalmente modulos padrao
    )
) else (
    echo Arquivo requirements.txt nao encontrado
    echo Instalando dependencias basicas...
    REM Para futura expansão, se necessário
    echo Nenhuma dependencia externa necessaria no momento
)
echo.

REM Verificar estrutura do projeto
echo [4/4] Verificando estrutura do projeto...
if not exist "main.py" (
    echo ERRO: main.py nao encontrado!
    echo Certifique-se de estar no diretorio correto do projeto
    pause
    exit /b 1
)

if not exist "main_gui.py" (
    echo ERRO: main_gui.py nao encontrado!
    echo Certifique-se de estar no diretorio correto do projeto
    pause
    exit /b 1
)

if not exist "perguntas\perguntas.csv" (
    echo AVISO: perguntas/perguntas.csv nao encontrado!
    echo O quiz pode nao funcionar corretamente sem as perguntas
)

if not exist "src" (
    echo ERRO: Pasta src/ nao encontrada!
    echo Certifique-se de estar no diretorio correto do projeto
    pause
    exit /b 1
)

echo Estrutura do projeto verificada!
echo.

REM Testar importações básicas
echo Testando importacoes basicas do Python...
python -c "import tkinter; import csv; import json; import random; print('Modulos basicos OK!')" 2>nul
if %errorlevel% neq 0 (
    echo AVISO: Alguns modulos podem nao estar disponiveis
    echo O projeto deveria funcionar na maioria dos sistemas Python padrao
)

echo.
echo ============================================
echo        INSTALACAO CONCLUIDA COM SUCESSO!
echo ============================================
echo.
echo Como usar:
echo.
echo 1. Interface Grafica (Recomendado):
echo    python main_gui.py
echo.
echo 2. Interface Terminal:
echo    python main.py
echo.
echo 3. Script de inicializacao:
echo    start_quiz.sh (se estiver usando Git Bash/WSL)
echo.
echo Para mais informacoes, consulte o README.md
echo.
echo Pressione qualquer tecla para abrir o jogo...
pause >nul

REM Tentar abrir o jogo automaticamente
echo Abrindo o Quiz Educativo...
python main_gui.py

echo.
echo Obrigado por usar o TrabalhoSO Quiz Educativo!
pause
