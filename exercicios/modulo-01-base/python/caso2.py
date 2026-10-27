id_do_caso = "CT-001"
titulo = "Login com credenciais válidas"
prioridade = 1
tempo_estimado_min = 2.5
email_usuario = "qa.teste@example.com"

print(f"ID do caso: {id_do_caso}")
print(f"Título: {titulo}")
print(f"Prioridade: {prioridade}")
print(f"Tempo estimado: {tempo_estimado_min} minutos")
print(f"Usuário de teste: {email_usuario}")
print(f"Tempo estimado em segundos: {tempo_estimado_min * 60} segundos")

print(type(tempo_estimado_min))