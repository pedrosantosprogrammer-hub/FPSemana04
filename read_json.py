#!/usr/bin/env python3
import sys
import os
import json

REQUIRED_FIELDS = ["nome", "idade", "localização"]

def print_concluido():
    print("Processo Concluído!")

def main():
    # aceitar exactamente 1 argumento: caminho para o ficheiro JSON
    if len(sys.argv) != 2:
        print("Uso: python read_json.py <ficheiro.json>")
        print_concluido()
        return

    path = sys.argv[1]

    # 1) Ficheiro inexistente
    if not os.path.exists(path):
        print("Erro: Ficheiro Não Encontrado!")
        print_concluido()
        return

    # 2) Ficheiro vazio (size == 0)
    try:
        if os.path.getsize(path) == 0:
            print("Erro: Ficheiro Vazio!")
            print_concluido()
            return
    except OSError:
        # se houver problema a aceder ao ficheiro
        print("Erro: Ficheiro Não Encontrado!")
        print_concluido()
        return

    # 3) Ficheiro não contém JSON válido
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("Erro: Ficheiro Não Contém JSON Válido!")
        print_concluido()
        return
    except Exception:
        # qualquer outro erro de leitura
        print("Erro: Ficheiro Não Encontrado!")
        print_concluido()
        return

    # 4) Campos obrigatórios em falta
    if not isinstance(data, dict):
        # se o JSON não for object/dict
        print("Erro: Ficheiro Não Contém JSON Válido!")
        print_concluido()
        return

    missing = [c for c in REQUIRED_FIELDS if c not in data]
    if missing:
        print("Erro: Campos Obrigatórios em Falta!")
        print_concluido()
        return

    # 5) JSON correcto -> imprimir o dicionário (Python usa aspas simples ao imprimir)
    print(data)
    print_concluido()

if __name__ == "__main__":
    main()
