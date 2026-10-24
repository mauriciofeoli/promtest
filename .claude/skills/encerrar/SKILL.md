---
name: encerrar
description: Encerra a sessão de estudo, registra o que foi feito e atualiza o progresso. Use quando eu disser "encerrar", "acabou por hoje" ou "fecha a sessão".
allowed-tools: Read Write Edit Bash(git status *) Bash(git diff *) Bash(git add *) Bash(git commit *) Bash(git push *) Bash(date *)
---

Encerre a sessão de estudo.

1. Resuma a sessão em até 3 linhas.
2. Descubra a data de hoje com `date +%F`.
3. Crie `sessoes/<data>.md` a partir de `templates/sessao.md`, com `modulo` e `duracao_min` preenchidos. Se já existir, acrescente uma seção "Sessão 2" no mesmo arquivo.
4. Atualize `progresso.md`:
   - bloco "Onde paramos" (módulo atual, tópico, próximo passo, próximo módulo, última sessão);
   - marque os tópicos concluídos;
   - seção "Ritmo": sessões, minutos, média por sessão, sessões por semana, tópicos concluídos e minutos por tópico;
   - status, início ou conclusão no "Roteiro", se mudou. Ao concluir um módulo, troque a lista "Tópicos do módulo atual" pelos tópicos do próximo módulo do roteiro em `plano.md`;
   - uma linha nova no topo da tabela "Registro";
   - o campo `atualizado` do cabeçalho.
5. Atualize `duvidas.md` com dúvidas novas e erros dos exercícios (próxima revisão em 1 dia e em 7 dias); mova as resolvidas.
6. Faça o commit `estudo: modulo N - <tópico>` sem pedir aprovação (e `git push` se houver remoto).
7. Se a sessão rendeu algo real para um post, acrescente uma linha no topo de `conteudo/pautas.md` com status "Ideia". Se nada rendeu, pule.
8. Termine com o próximo passo e uma tarefa curta para eu fazer sozinho.
