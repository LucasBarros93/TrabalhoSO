class ContentSummary:
    """Contém o resumo teórico sobre semáforos e threads."""
    
    @staticmethod
    def show_main_menu():
        """Mostra o menu principal do resumo teórico."""
        print("\n" + "="*60)
        print("📚 RESUMO TEÓRICO - SEMÁFOROS E THREADS")
        print("="*60)
        print("1. 🧵 Conceitos Básicos de Threads")
        print("2. 🚦 Semáforos e Sincronização")
        print("3. ⚠️  Problemas Comuns")
        print("4. 🐍 Threads em Python")
        print("5. 💡 Exemplos Práticos")
        print("0. ⬅️  Voltar ao Menu Principal")
        print("="*60)
    
    @staticmethod
    def show_threads_basics():
        """Explica conceitos básicos de threads."""
        print("\n" + "="*60)
        print("🧵 CONCEITOS BÁSICOS DE THREADS")
        print("="*60)
        print("""
📖 O que são Threads?
   • Threads são fluxos de execução independentes dentro de um processo
   • Permitem que um programa execute múltiplas tarefas simultaneamente
   • Compartilham o mesmo espaço de memória do processo pai

🎯 Vantagens das Threads:
   • Melhor aproveitamento de processadores multi-core
   • Responsividade: interface não trava enquanto processa dados
   • Paralelização de tarefas independentes
   • Menor overhead que criar novos processos

⚠️  Desafios das Threads:
   • Sincronização: coordenar acesso a recursos compartilhados
   • Race conditions: resultados dependem da ordem de execução
   • Debugging mais complexo
   • Possibilidade de deadlocks

🔄 Estados de uma Thread:
   • NEW: thread criada mas não iniciada
   • RUNNABLE: thread em execução ou pronta para executar
   • BLOCKED: thread aguardando um recurso
   • TERMINATED: thread finalizou sua execução
        """)
        input("\nPressione Enter para continuar...")
    
    @staticmethod
    def show_semaphores():
        """Explica semáforos e sincronização."""
        print("\n" + "="*60)
        print("🚦 SEMÁFOROS E SINCRONIZAÇÃO")
        print("="*60)
        print("""
📖 O que são Semáforos?
   • Mecanismo de sincronização para controlar acesso a recursos
   • Funcionam como um contador que controla quantas threads podem
     acessar um recurso simultaneamente
   • Inventados por Edsger Dijkstra em 1965

🔧 Operações Principais:
   • acquire() (P): decrementa contador, bloqueia se contador = 0
   • release() (V): incrementa contador, libera thread em espera

📊 Tipos de Semáforos:
   • Binário (Mutex): contador 0 ou 1, exclusão mútua
   • Contador: permite N acessos simultâneos

🎯 Exclusão Mútua:
   • Garante que apenas uma thread acesse recurso crítico por vez
   • Previne race conditions
   • Essencial para integridade dos dados

💼 Casos de Uso:
   • Controle de acesso a arquivos
   • Limitação de conexões simultâneas
   • Sincronização de threads produtoras/consumidoras
   • Proteção de variáveis globais
        """)
        input("\nPressione Enter para continuar...")
    
    @staticmethod
    def show_common_problems():
        """Explica problemas comuns com threads."""
        print("\n" + "="*60)
        print("⚠️  PROBLEMAS COMUNS")
        print("="*60)
        print("""
🏃‍♂️ Race Conditions (Condições de Corrida):
   • Ocorrem quando múltiplas threads acessam dados compartilhados
   • O resultado final depende da ordem de execução
   • Podem causar corrupção de dados
   • Solução: usar semáforos, mutexes ou locks

🔒 Deadlock (Impasse):
   • Duas ou mais threads ficam esperando eternamente
   • Cada thread possui um recurso que a outra precisa
   • Condições necessárias:
     - Exclusão mútua
     - Retenção e espera
     - Não preempção
     - Espera circular

🔄 Livelock:
   • Threads não estão bloqueadas mas não fazem progresso
   • Ficam reagindo umas às outras indefinidamente
   • Menos comum que deadlock

😴 Starvation (Inanição):
   • Thread nunca consegue acessar o recurso necessário
   • Outras threads sempre têm prioridade
   • Pode causar travamento de funcionalidades específicas

🛡️  Estratégias de Prevenção:
   • Ordenação de recursos (previne deadlock)
   • Timeout em operações de acquire
   • Algoritmos de detecção e recuperação
   • Design cuidadoso da sincronização
        """)
        input("\nPressione Enter para continuar...")
    
    @staticmethod
    def show_python_threading():
        """Explica threads em Python."""
        print("\n" + "="*60)
        print("🐍 THREADS EM PYTHON")
        print("="*60)
        print("""
📚 Biblioteca threading:
   • Módulo padrão do Python para trabalhar com threads
   • Fornece classes Thread, Lock, Semaphore, Condition, etc.
   • Interface orientada a objetos e fácil de usar

🧵 Criando Threads:
   import threading
   
   def minha_funcao():
       print("Executando em thread separada")
   
   thread = threading.Thread(target=minha_funcao)
   thread.start()  # Inicia a thread
   thread.join()   # Aguarda término

🚦 Semáforos em Python:
   semaforo = threading.Semaphore(2)  # Permite 2 acessos
   
   semaforo.acquire()  # Adquire permissão
   try:
       # código crítico aqui
       pass
   finally:
       semaforo.release()  # Libera permissão

🔒 GIL (Global Interpreter Lock):
   • Permite apenas uma thread Python por vez
   • Afeta threads CPU-intensivas
   • Threads I/O-intensivas ainda se beneficiam
   • Use multiprocessing para CPU-intensivas

💡 Boas Práticas:
   • Sempre use try/finally com acquire/release
   • Prefira context managers (with statement)
   • Evite muitas threads (overhead)
   • Use Queue para comunicação entre threads
        """)
        input("\nPressione Enter para continuar...")
    
    @staticmethod
    def show_practical_examples():
        """Mostra exemplos práticos."""
        print("\n" + "="*60)
        print("💡 EXEMPLOS PRÁTICOS")
        print("="*60)
        print("""
🏦 Exemplo: Conta Bancária (Race Condition)
   
   PROBLEMA:
   saldo = 100
   
   Thread 1: saldo = saldo + 50  # Depósito
   Thread 2: saldo = saldo - 30  # Saque
   
   Sem sincronização: resultado pode ser incorreto!
   
   SOLUÇÃO:
   import threading
   
   lock = threading.Lock()
   saldo = 100
   
   def depositar(valor):
       global saldo
       with lock:
           saldo += valor
   
   def sacar(valor):
       global saldo
       with lock:
           if saldo >= valor:
               saldo -= valor

🍽️  Exemplo: Jantar dos Filósofos (Deadlock)
   
   PROBLEMA:
   5 filósofos, 5 garfos, cada um precisa de 2 garfos
   Se todos pegarem o garfo da direita primeiro = DEADLOCK!
   
   SOLUÇÃO:
   • Numeração dos recursos (garfos)
   • Sempre pegar o garfo de menor número primeiro
   • Timeout nas operações
   • Waiter (garçom) controlando acesso

🏭 Exemplo: Produtor-Consumidor
   
   import threading
   import queue
   
   buffer = queue.Queue(maxsize=10)
   
   def produtor():
       for i in range(100):
           buffer.put(f"item_{i}")
   
   def consumidor():
       while True:
           item = buffer.get()
           # processa item
           buffer.task_done()

🌐 Casos Reais:
   • Servidores web: uma thread por cliente
   • Download de arquivos: threads para partes diferentes
   • Interface gráfica: thread separada para processamento
   • Jogos: threads para física, renderização, IA
        """)
        input("\nPressione Enter para continuar...")
    
    @staticmethod
    def show_content(option):
        """Mostra o conteúdo baseado na opção selecionada."""
        if option == "1":
            ContentSummary.show_threads_basics()
        elif option == "2":
            ContentSummary.show_semaphores()
        elif option == "3":
            ContentSummary.show_common_problems()
        elif option == "4":
            ContentSummary.show_python_threading()
        elif option == "5":
            ContentSummary.show_practical_examples()
        else:
            print("❌ Opção inválida!")
    
    @staticmethod
    def get_full_summary():
        """Retorna todo o conteúdo teórico formatado para a interface gráfica."""
        return """
🧵 CONCEITOS BÁSICOS DE THREADS
================================

📖 O que são Threads?
   • Threads são fluxos de execução independentes dentro de um processo
   • Permitem que um programa execute múltiplas tarefas simultaneamente
   • Compartilham o mesmo espaço de memória do processo pai

🎯 Vantagens das Threads:
   • Melhor aproveitamento de processadores multi-core
   • Responsividade: interface não trava enquanto processa dados
   • Paralelização de tarefas independentes
   • Menor overhead que criar novos processos

⚠️  Desafios das Threads:
   • Sincronização: coordenar acesso a recursos compartilhados
   • Race conditions: resultados dependem da ordem de execução
   • Debugging mais complexo
   • Possibilidade de deadlocks

🔄 Estados de uma Thread:
   • NEW: thread criada mas não iniciada
   • RUNNABLE: thread em execução ou pronta para executar
   • BLOCKED: thread aguardando um recurso
   • TERMINATED: thread finalizou sua execução


🚦 SEMÁFOROS E SINCRONIZAÇÃO
=============================

📖 O que são Semáforos?
   • Mecanismo de sincronização para controlar acesso a recursos
   • Mantém um contador interno que indica recursos disponíveis
   • Inventados por Edsger Dijkstra em 1965

🎯 Objetivo dos Semáforos:
   • Evitar condições de corrida (race conditions)
   • Garantir exclusão mútua no acesso a recursos críticos
   • Coordenar a execução de múltiplas threads

🔧 Operações Básicas:
   • acquire() ou P(): decrementa contador, bloqueia se for 0
   • release() ou V(): incrementa contador, libera threads bloqueadas

📊 Tipos de Semáforos:
   • Binário: contador 0 ou 1 (mutex)
   • Contagem: contador pode ser qualquer número inteiro positivo

💡 Exemplo Conceitual:
   Imagine um estacionamento com 5 vagas:
   • Semáforo iniciado com valor 5
   • Cada carro que entra faz acquire() → contador diminui
   • Cada carro que sai faz release() → contador aumenta
   • Se contador = 0, próximos carros ficam aguardando


⚠️  PROBLEMAS COMUNS
====================

🔴 Race Conditions (Condições de Corrida):
   • Ocorrem quando múltiplas threads acessam dados compartilhados
   • O resultado depende da ordem de execução das threads
   • Podem causar corrupção de dados

🔒 Deadlock (Impasse):
   • Duas ou mais threads ficam bloqueadas eternamente
   • Cada thread espera por um recurso que outra possui
   • Condições necessárias: exclusão mútua, posse e espera, não preempção, espera circular

🔄 Livelock:
   • Threads não ficam bloqueadas, mas também não progridem
   • Ficam respondendo umas às outras indefinidamente

😴 Starvation (Inanição):
   • Uma thread fica indefinidamente sem acesso a um recurso
   • Outras threads monopolizam o recurso

🛡️  Como Evitar:
   • Use semáforos e locks adequadamente
   • Sempre adquira recursos na mesma ordem
   • Use timeouts em operações de bloqueio
   • Minimize o tempo em seções críticas


🐍 THREADS EM PYTHON
====================

📚 Biblioteca threading:
   • Módulo padrão do Python para trabalhar com threads
   • Classe Thread para criar e gerenciar threads
   • Semáforos, locks, conditions e outros primitivos

🔒 GIL (Global Interpreter Lock):
   • Permite que apenas uma thread execute código Python por vez
   • Protege o interpretador, mas limita paralelismo real
   • Para CPU intensivo, considere multiprocessing

💻 Criando uma Thread:
import threading

def minha_funcao():
    print("Executando em thread separada")

# Criar e iniciar thread
thread = threading.Thread(target=minha_funcao)
thread.start()
thread.join()  # Aguarda conclusão

📦 Semáforos em Python:
import threading

# Criar semáforo com 3 recursos
semaforo = threading.Semaphore(3)

def usar_recurso():
    semaforo.acquire()  # Adquire recurso
    try:
        # Usa o recurso...
        print("Usando recurso")
    finally:
        semaforo.release()  # Libera recurso

🎯 Boas Práticas:
   • Sempre use try/finally com acquire/release
   • Use context managers (with statement)
   • Evite threads para CPU intensivo (use multiprocessing)
   • Para I/O bound, threads são eficientes


💡 EXEMPLOS PRÁTICOS
====================

🏦 Exemplo 1: Conta Bancária Compartilhada
import threading

saldo = 0
lock = threading.Lock()

def depositar(valor):
    global saldo
    with lock:
        temp = saldo
        temp += valor
        saldo = temp

def sacar(valor):
    global saldo
    with lock:
        if saldo >= valor:
            temp = saldo
            temp -= valor
            saldo = temp
            return True
        return False

🏭 Exemplo 2: Produtor-Consumidor
import threading
import queue

buffer = queue.Queue(maxsize=5)

def produtor():
    for i in range(10):
        item = f"item_{i}"
        buffer.put(item)
        print(f"Produzido: {item}")

def consumidor():
    while True:
        item = buffer.get()
        print(f"Consumido: {item}")
        buffer.task_done()

🎯 Resumo:
   • Threads permitem paralelismo em programas
   • Semáforos controlam acesso a recursos compartilhados
   • Cuidado com race conditions e deadlocks
   • Python threading é ideal para I/O bound
   • Sempre sincronize acesso a dados compartilhados

📚 Continue estudando e praticando! A programação concorrente é fundamental
   para criar aplicações modernas e eficientes.
        """
