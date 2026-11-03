bug = {
    "id": 101,
    "titulo": "Botao de pagamento nao responde",
    "severidade": "alta"
}

print(f"Bug {bug['id']}: {bug['titulo']} ({bug['severidade']})")

bug["severidade"] = "media"
bug["aberto"] = True

print(bug)

print("aberto" in bug)
print("alta" in bug)
print(bug.get("responsavel"))
print(bug.get("responsavel", "sem dono"))
print(bug.get("severidade", "baixa"))
print(len(bug))