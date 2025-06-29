# 🚀 Guia de Instalação - TrabalhoSO Quiz Educativo

Este documento fornece instruções detalhadas para instalar e configurar o Quiz Educativo sobre Sistemas Operacionais.

## 📋 Pré-requisitos

### 🐍 Python
- **Versão**: Python 3.6 ou superior
- **Módulos necessários**: Apenas bibliotecas padrão (csv, json, random, datetime, tkinter)

### 💻 Sistema Operacional
- **Linux**: Ubuntu 18.04+, CentOS 7+, ou distribuições equivalentes
- **macOS**: 10.12+ com Homebrew (opcional)
- **Windows**: Windows 10+ com PowerShell

## ⚡ Instalação Automática (Recomendado)

### 🐧 Linux/macOS
```bash
# 1. Clone ou baixe o projeto
cd /path/to/TrabalhoSO

# 2. Execute o script de instalação
chmod +x install_linux.sh
./install_linux.sh

# 3. Siga as instruções na tela
```

### 🪟 Windows
```batch
# 1. Abra o diretório do projeto
# 2. Duplo clique em install_windows.bat
# OU execute via linha de comando:
install_windows.bat
```

## 🔧 Instalação Manual

### Passo 1: Verificar Python
```bash
# Verificar versão
python3 --version  # Linux/macOS
python --version   # Windows

# Deve retornar Python 3.6+ 
```

### Passo 2: Instalar tkinter (se necessário)
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install python3-tk

# CentOS/RHEL/Fedora
sudo dnf install python3-tkinter

# macOS (com Homebrew)
brew install python-tk

# Windows: já incluído com Python
```

### Passo 3: Verificar estrutura
```bash
# Verificar se todos os arquivos estão presentes
ls -la
# Deve conter: main.py, main_gui.py, src/, perguntas/, etc.
```

### Passo 4: Testar instalação
```bash
# Testar interface gráfica
python3 main_gui.py

# Testar interface terminal
python3 main.py
```

## 🎮 Primeiros Passos

### Usar Scripts de Inicialização
```bash
# Linux/macOS
./start_quiz.sh

# Windows
start_quiz.bat  # (criado automaticamente pelos scripts)
```

### Execução Direta
```bash
# Interface Gráfica (Recomendado)
python3 main_gui.py  # Linux/macOS
python main_gui.py   # Windows

# Interface Terminal
python3 main.py      # Linux/macOS
python main.py       # Windows
```

## 🛠️ Solução de Problemas

### Problema: "Python não encontrado"
**Solução:**
- **Linux**: `sudo apt install python3`
- **macOS**: `brew install python3`
- **Windows**: Baixar de https://python.org e marcar "Add to PATH"

### Problema: "tkinter não encontrado"
**Solução:**
```bash
# Ubuntu/Debian
sudo apt install python3-tk

# CentOS/RHEL
sudo dnf install python3-tkinter

# macOS
brew install python-tk
```

### Problema: "externally-managed-environment"
**Explicação:** Comportamento normal em Linux modernos. O projeto funciona apenas com módulos padrão!

**Se precisar instalar dependências futuras:**
```bash
# Opção 1: Ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Opção 2: Instalação para usuário
pip install --user package_name

# Opção 3: pipx (recomendado)
pipx install package_name
```

### Problema: "Arquivo de perguntas não encontrado"
**Solução:**
```bash
# Verificar se existe
ls perguntas/perguntas.csv

# Se não existir, o arquivo pode estar em outro local
find . -name "perguntas.csv"
```

### Problema: Caracteres estranhos no terminal
**Solução:**
- Use terminal com suporte UTF-8
- No Windows, prefira PowerShell ao CMD
- Configure a codificação: `export LANG=pt_BR.UTF-8`

## 📊 Verificação de Instalação

Execute este comando para verificar se tudo está funcionando:

```python
python3 -c "
import sys
print(f'Python: {sys.version}')

try:
    import tkinter
    print('✅ tkinter: OK')
except ImportError:
    print('❌ tkinter: Não encontrado')

try:
    import csv, json, random, datetime
    print('✅ Módulos padrão: OK')
except ImportError:
    print('❌ Módulos padrão: Erro')

import os
files = ['main.py', 'main_gui.py', 'src/', 'perguntas/']
for f in files:
    if os.path.exists(f):
        print(f'✅ {f}: OK')
    else:
        print(f'❌ {f}: Não encontrado')
"
```

## 🎯 Próximos Passos

Após a instalação bem-sucedida:

1. **📚 Leia o README.md** para entender todas as funcionalidades
2. **🎮 Execute o quiz** usando `./start_quiz.sh` ou diretamente
3. **📊 Explore as opções** do menu principal
4. **🤝 Contribua** com o projeto adicionando mais perguntas

## 📞 Suporte

Se encontrar problemas:

1. **📖 Consulte a seção Troubleshooting** no README.md
2. **🔍 Verifique os logs** de erro detalhadamente
3. **🐛 Reporte bugs** seguindo o template de contribuição
4. **💡 Sugira melhorias** através de issues

---

**🎓 Divirta-se aprendendo sobre Sistemas Operacionais!**
