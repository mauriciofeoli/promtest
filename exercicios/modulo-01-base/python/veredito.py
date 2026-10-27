total = int(input("Total de testes: "))
passaram = int(input("Quantos passaram: "))

if passaram > total:
    print("Dado invalido: passaram mais testes que o total")
elif passaram == total:
    print("Suite aprovada")
else:
    print(f"Suite reprovada: {total - passaram} falharam")