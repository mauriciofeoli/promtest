testes = ["login", "senha", "email", "cadastro"]
total = 0

for teste in testes:
    print(teste)
    total = total + 1

print(f"Total de testes: {total}")


# A saída é a mesma. Só muda a organização.

testes = ["login", "senha", "email"]

for teste in testes:
    print(teste)

#Leia total = total + 1 assim: "o novo total é o total de agora mais 1"

testes = ["login", "senha", "email"]
total = 0

for teste in testes:
    total = total + 1

print(f"Total: {total}")

#Revisão
tempos = [120, 45, 300, 80, 510]
lentos = 0

for tempo in tempos:
    if tempo > 100:
        lentos = lentos + 1

print(f"Lentos: {lentos} de {len(tempos)}")