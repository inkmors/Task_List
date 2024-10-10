import os

def readTask(listaTarefas, numberCont):
    os.system('clear')
    if(listaTarefas == []):
        print("Lista Vazia")
    else:
        print("### [ Lista de tarefas ] ###\n")
        for item in listaTarefas:
            numberCont += 1
            print(f"> {numberCont} | {item}<\n")
def newTask(listaTarefas):
    os.system('clear')
    insertInLista = input("Informe o novo item da lista\n")
    listaTarefas.append(insertInLista)
    print(f"{insertInLista} adicionado(a)..")

def editTask(listaTarefas, numberCont):
    os.system('clear')
    if listaTarefas == []:
        print("ERROR: Lista vazia, impossivel editar algo")
    else:
        readTask(listaTarefas, numberCont)
        try:
            valueInput = int(input("Informe o número do item para editar:\n")) - 1
            editTaskInput = input("Informe a nova tarefa:\n")
            if valueInput > len(listaTarefas):
                print("Número Inválido")
            else:
                listaTarefas[valueInput] = editTaskInput
                print(f"Tarefa {editTaskInput} editada..")
        except ValueError:
            print("ERROR: Digite um número")

def deleteTask(listaTarefas, numberCont):
    os.system('clear')
    if listaTarefas == []:
        print("ERROR: Lista Vazia, impossivel remover algo!")
    else:      
        readTask(listaTarefas, numberCont)
        try:
            deleteTaskInput = int(input('Informe o numero da tarefa a ser deletada\n')) - 1

            if deleteTaskInput > len(listaTarefas):
                print("Numero Invalido")  
            else:    
                listaTarefas.pop(deleteTaskInput)
                print(f"Tarefa {deleteTaskInput} deletada..")
        except ValueError:
            print("ERROR, digite um número")

    return listaTarefas                

def menuMain():
    os.system('clear')
    listaTarefas = []
    numberCont = 0
    #okay = False
    while True:
        print("\n##### Gerenciador de Tarefas ####")
        print("1. Ver tarefas")
        print("2. Nova tarefa")
        print("3. Editar tarefa")
        print("4. Deletar tarefa")
        print("0. Sair")
        print("####################################")

        operationType = int(input("Informe o tipo de operação que deseja realizar\n"))

        match operationType:
            case 0:
                print('Saindo...')
            case 1:
                readTask(listaTarefas, numberCont)
                continue
            case 2:
                newTask(listaTarefas)
                continue
            case 3:
                editTask(listaTarefas, numberCont)
                continue
            case 4:
                deleteTask(listaTarefas, numberCont)
                continue
            case _:
                print("ERROR: Opção inválida")
                continue

        return numberCont      

menuMain()