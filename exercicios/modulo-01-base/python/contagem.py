resultados = ["ok", "falha", "ok", "ok"]
ok = 0

for resultado in resultados:
    if resultado == "ok":
        ok = ok + 1

print(f"Total: {len(resultados)}")
print(f"Ok: {ok}")