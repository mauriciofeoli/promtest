# PromTest: PRD do tutor (POC)

## Resumo e objetivo

O Tutor de IA é o Claude configurado para conduzir você pelo `plano.md`, sessão a sessão, ensinando, cobrando prática e registrando o progresso nos arquivos deste repositório.

**Problema:** estudar IA sozinho leva a pular etapas, esquecer o que já viu e perder o fio entre conversas.

**Solução:** um tutor que sempre sabe onde você parou, ensina no seu nível, aplica exercícios, revisa seu código e atualiza o registro no fim de cada sessão.

**Objetivos**

1. Concluir as 12 fases do plano em cerca de 14 meses.
2. Entregar um projeto publicado por fase.
3. Manter no mínimo 4 sessões por semana.
4. Nunca perder contexto: qualquer sessão retoma de onde a última parou.

**Métricas**

- Tópicos concluídos por semana e porcentagem do plano concluída.
- Sessões por semana (contadas em `sessoes/`).
- Acerto nos quizzes (meta: 80% ou mais).
- Projetos publicados no GitHub.

## Onde cada coisa fica

| Peça | Onde | Papel |
| --- | --- | --- |
| Instruções do tutor | `CLAUDE.md` | O Claude Code lê automaticamente ao abrir a pasta |
| Comandos | `.claude/skills/` | `/estudar`, `/encerrar`, `/onde-paramos`, `/me-testa`, `/revisao` |
| Plano | `plano.md` | Referência, só muda quando você pede |
| Progresso | `progresso.md` | Onde paramos, fases, tópicos, registro |
| Sessões | `sessoes/AAAA-MM-DD.md` | Uma nota por dia de estudo |
| Dúvidas | `duvidas.md` | Abertas, para revisar, resolvidas |
| Projetos | `projetos/fase-N-nome/` | Código e README de cada fase |
| Leitura e navegação | Obsidian | Mesma pasta, aberta como vault |
| Sincronização | Git + GitHub privado | Histórico e acesso pelo celular |

## Fluxos

**Início de sessão:** `/estudar [minutos]` → lê progresso e dúvidas → revisão rápida se houver itens vencidos → diz fase, tópico e próximo passo → ensina.

**Sessão:** explicação em camadas → exercício → dicas graduais → correção → próximo conceito → curso ou documentação oficial do tópico.

**Fim de sessão:** `/encerrar` → resumo → nota da sessão → `progresso.md` e `duvidas.md` atualizados → commit aprovado por você → próximo passo e tarefa.

**Revisão quinzenal:** `/revisao` → resumo do período → quiz → comparação com o cronograma → ajuste de ritmo.

**Fim de fase:** conferir o critério "Pronto quando" → revisar projeto e README → rascunho do post de LinkedIn (sem emojis) → marcar a fase como concluída → carregar os tópicos da próxima fase em `progresso.md`.

## Regras pedagógicas

- **Prática primeiro:** 70% do tempo fazendo; toda explicação termina num exercício.
- **Tentar antes de ver a resposta:** dicas graduais em vez de solução pronta.
- **Camadas:** intuição, conceito, exemplo, código e armadilha comum.
- **Nível certo:** parte do que você já sabe de QA e Python; se ficar fácil, acelera.
- **Repetição espaçada:** o que errou volta no dia seguinte, em 1 semana e na revisão quinzenal.
- **Ensinar para aprender:** de vez em quando, você explica com suas palavras e o tutor corrige.
- **Fonte oficial sempre:** cada tópico aponta o curso gratuito ou a documentação.
- **Honestidade:** sem elogio vazio; erro é apontado com o porquê e o caminho para corrigir.

## Riscos e limites

| Risco ou limite | Como lidar |
| --- | --- |
| Claude Code exige plano pago | Começar pelo claude.ai gratuito com estas instruções num Projeto, e migrar depois |
| Ferramentas e cursos mudam rápido | O tutor pesquisa antes de afirmar e marca o que não confirmou |
| Esquecer o `/encerrar` | Na sessão seguinte, o tutor registra a anterior pelo que você contar e pelo `git diff` |
| Conflito entre computador e celular | Sempre `git pull` antes de estudar (o Obsidian Git faz sozinho ao abrir) |
| Vazamento de chaves | `.env` fora do Git; o tutor nunca grava segredos nos arquivos |
| Constância depende de você | Metas pequenas por sessão e registro visível do avanço |

## Plano da POC (2 semanas)

- [ ] Instalar o básico (docs/SETUP.md, seções 1 a 5)
- [ ] Primeira sessão com `/estudar`: diagnóstico da Fase 0
- [ ] Pelo menos 8 sessões em 2 semanas, cada uma terminando com `/encerrar`
- [ ] Projeto da Fase 0 publicado no GitHub
- [ ] Revisão do fim da POC: o que funcionou e o que ajustar no `CLAUDE.md`

**Critérios de sucesso:** toda sessão retomou do ponto certo sem você explicar o contexto; o registro está completo; o quiz e o projeto comprovam o aprendizado; você quer continuar.

## Versão para o claude.ai (sem Claude Code)

Se for estudar pelo claude.ai, crie um Projeto "PromTest", cole o conteúdo do `CLAUDE.md` nas instruções e conecte o GitHub com acesso ao repositório `promtest`. O tutor lê e atualiza os mesmos arquivos pelo conector.
