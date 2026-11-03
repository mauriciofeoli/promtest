bug = {
    "id": 101,
    "titulo": "Botao de pagamento nao responde",
    "severidade": "alta"
}

print(f"Bug {bug['id']}: {bug['titulo']} ({bug['severidade']})")

bug["severidade"] = "media"
bug["aberto"] = True

print(bug)