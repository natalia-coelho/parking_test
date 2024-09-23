import json
import os

def read_config(file_path):
    if not os.path.exists(file_path):
        print("O arquivo não existe.")
        return

    with open(file_path, 'r') as file:
        try:
            config_data = json.load(file)
            if config_data:
                print(json.dumps(config_data, indent=4))
            else:
                print("O arquivo não contém informações.")
        except json.JSONDecodeError:
            print("O arquivo não contém informações ou está corrompido.")

def write_config(file_path):
    server_name = input("Informe o nome do servidor: ")
    server_ip = input("Informe o IP do servidor: ")
    server_password = input("Informe a senha do servidor: ")

    config_data = {
        "server_name": server_name,
        "server_ip": server_ip,
        "server_password": server_password
    }

    with open(file_path, 'w') as file:
        json.dump(config_data, file, indent=4)
    
    print("As informações foram salvas com sucesso.")
    print(json.dumps(config_data, indent=4))

def main():
    file_path = "config.json"
    
    print("O que você deseja fazer?")
    print("1 - Ler configuração")
    print("2 - Escrever configuração")
    
    choice = input("Escolha uma opção (1 ou 2): ")

    if choice == '1':
        read_config(file_path)
    elif choice == '2':
        write_config(file_path)
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()
