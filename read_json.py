import json
import sys
import os

# Campos obrigatórios
REQUIRED_FIELDS = ["nome", "idade", "localização"]

def main():
    if len(sys.argv) != 2:
        file_path = input("Insira o caminho do ficheiro JSON: ")
    else:
        file_path = sys.argv[1]

    # 1. Ficheiro inexistente
    if not os.path.exists(file_path):
        print("Erro: Ficheiro Não Encontrado!")
        print("Processo Concluído!")
        return

    # 2. Ficheiro vazio
    if os.path.getsize(file_path) == 0:
        print("Erro: Ficheiro Vazio!")
        print("Processo Concluído!")
        return

    # 3. Ficheiro não contém JSON válido
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("Erro: Ficheiro Não Contém JSON Válido!")
        print("Processo Concluído!")
        return

    # 4. Campos obrigatórios em falta
    missing = [campo for campo in REQUIRED_FIELDS if campo not in data]
    if missing:
        print("Erro: Campos Obrigatórios em Falta!")
        print("Processo Concluído!")
        return

    # 5. JSON correto
    print(data)
    print("Processo Concluído!")


if __name__ == "__main__":
    main()
