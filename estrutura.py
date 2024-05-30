import json
import os
from time import sleep


# class cor:
#     VERMELHO = '\033[91m'
#     VERDE = '\033[92m'
#     AMARELO = '\033[93m'
#     AZUL = '\033[94m'
#     MAGENTA = '\033[95m'
#     CIANO = '\033[96m'
#     RESET = '\033[0m'


arquivo = os.path.join(os.path.dirname(__file__), 'bd.json')



def adicionar_ponto_turistico(nome, bairro, tipo):
    with open(arquivo, 'r') as f:
        ponto_turisticos = json.load(f)

    ponto_turisticos.append({'nome': nome, 'bairro': bairro, 'tipo': tipo})

    with open(arquivo, 'w') as f:
        json.dump(ponto_turisticos, f, indent=4)
    print("😎 PONTO TURISTICO ADICIONADO COM SUCESSO!")

def listar_ponto_turisticos():
    with open(arquivo, 'r') as f:
        ponto_turisticos = json.load(f)

    if ponto_turisticos:
        print("*" *50)
        print("LISTA DE PONTOS TURISTICOS:")
        print("*" *50)
        for ponto_turistico in ponto_turisticos:
            print("*" *50)
            print(f"NOME: {ponto_turistico['nome']}, BAIRRO: {ponto_turistico['bairro']}, TIPO: {ponto_turistico['tipo']}")
            print("*" *50)
            print("=" *50)
    else:
        print("😒 NENHUM PONTO TURISTICO CADASTRADO.")

def atualizar_ponto_turistico(nome_antigo, novo_nome, novo_bairro):
    with open(arquivo, 'r') as f:
        ponto_turisticos = json.load(f)

    for ponto_turistico in ponto_turisticos:
        if ponto_turistico['nome'] == nome_antigo:
            ponto_turistico['nome'] = novo_nome
            ponto_turistico['bairro'] = novo_bairro
            break

    with open(arquivo, 'w') as f:
        json.dump(ponto_turisticos, f, indent=4)
    print("😙 PONTO TURISTICO ATUALIZADO COM SUCESSO!")

def excluir_ponto_turistico(nome):
    with open(arquivo, 'r') as f:
        ponto_turisticos = json.load(f)

    for ponto_turistico in ponto_turisticos:  
        if ponto_turistico['nome'] == nome:
            ponto_turisticos.remove(ponto_turistico)

    with open(arquivo, 'w') as f:
        json.dump(ponto_turisticos, f, indent=4)
        print("😡 PONTO TURISTICO EXCLUÍDO COM SUCESSO!")

def buscar_ponto_turistico (nome):
    with open(arquivo, 'r') as f:
        ponto_turisticos = json.load(f)
    
    encontrado = False

    for ponto_turistico in ponto_turisticos:
        if ponto_turistico['nome'] == nome:
            print(f"NOME: {ponto_turistico['nome']}, BAIRRO: {ponto_turistico['bairro']}")
            encontrado = True
    if not encontrado:
            print("😒 NENHUM PONTO TURISTICO CADASTRADO.")
    

# def linha_horizontal(cor):
#     return cor + "=" * 50 + cor['RESET']

def menu_inicial ():
    print ("*" *55)
    print (" ---->>>  BEM VINDO Ao CATÁLOGO DE PONTOS TURISTICOS DE RECIFE <<<---- ")
    print ("          1 - MÓDULO PONTO TURISTICO ")
    print ("          2 - MÓDULO ESTOQUE ")
    print ("          3 - SAIR ")
    print ("*" *55)
    
def exibir_menu():
    print("\nMENU:")
    print("1. ADICIONAR PONTO TURISTICO")
    print("2. LISTAR PONTO TURISTICOS")
    print("3. ATUALIZAR PONTO TURISTICO")
    print("4. EXCLUIR PONTO TURISTICO")
    print("5. LISTAR UM PONTO TURISTICO")
    print("6. VOLTAR AO MENU ANTERIOR")



def main():
    
    while True:
        menu_inicial()
        opcao_inicial = int(input("INFORME UMA OPÇÃO: "))

        match (opcao_inicial):
            case 2:
                print("MÓDULO EM DESENVOLVIMENTO")

            case 1:
                while True: 
                    exibir_menu()
                    opcao = input("ESCOLHA UMA OPÇÃO:\n>>> ")

                    if opcao == "1":
                        nome = input(" DIGITE O NOME:\n>>> ")
                        bairro = input(" DIGITE A BAIRRO:\n>>> ")
                        tipo = input(" DIGITE O TIPO:\n>>> ")
                        adicionar_ponto_turistico(nome, bairro, tipo)
                    elif opcao == "2":
                        listar_ponto_turisticos()
                    elif opcao == "3":
                        nome_antigo = input("DIGITE O NOME A SER ATUALIZADO:\n>>> ")
                        novo_nome = input("DIGITE O NOVO NOME:\n>>> ")
                        novo_bairro = input("DIGITE A NOVA BAIRRO:\n>>> ")
                        atualizar_ponto_turistico(nome_antigo, novo_nome, novo_bairro)
                    elif opcao == "4":
                        nome = input("DIGITE O NOME DO PONTO TURISTICO A SER EXCLUÍDO:\n>>> ")
                        excluir_ponto_turistico(nome)
                    elif opcao == "5":
                        nome = input("DIGITE O NOME DO PONTO TURISTICO:\n>>> ")
                        buscar_ponto_turistico(nome)
                    elif opcao == "6":
                        print("VOLTAR AO MENU ANTERIOR...")
                        sleep(3)
                        break
                    else:
                        print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
            case 3:
                print("🚀 SAINDO...")
                sleep(3)
                break
            case __:
                print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main()
