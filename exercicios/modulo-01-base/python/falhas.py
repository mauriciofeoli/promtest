falhas = ["Login", "Pagamento"]

nova_falha = input("Nome do teste que falhou: ")
falhas.append(nova_falha)

print(f"Total de falhas: {len(falhas)}")
print(f"Primeira falha: {falhas[0]}")
print(f"Ultima falha: {falhas[-1]}")