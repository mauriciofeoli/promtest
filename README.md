# PromTest

PromTest (prompt + test) é meu workspace de estudo e de conteúdo sobre IA aplicada a QA. Meu caminho para dominar Inteligência Artificial, dos fundamentos ao avançado, com aplicação em Qualidade de Software. Só fontes gratuitas, 12 fases, um projeto por fase.

## Comece aqui

Não precisa colar prompt nenhum: o `CLAUDE.md` é o prompt, e o Claude Code lê esse arquivo sozinho ao abrir a pasta.

### Opção A: terminal com Claude Code (exige plano pago do Claude)

1. Instale o que precisa: [docs/SETUP.md](docs/SETUP.md) (no mínimo Git, VS Code e Claude Code).
2. Na primeira vez, dentro da pasta:

   ```bash
   cd PromTest
   git init
   git add . && git commit -m "estudo: estrutura inicial"
   claude
   ```

3. Confira se o tutor leu tudo: digite `/onde-paramos` (deve dizer Fase 0, nenhuma sessão ainda).
4. Comece: `/estudar 60` (60 = minutos disponíveis) ou escreva "vamos estudar".
5. Para parar, só se despeça ("por hoje é isso"). O tutor salva o progresso e faz o commit sozinho.

Nas próximas vezes, é só `cd PromTest` e `claude`.

### Opção B: claude.ai, sem instalar nada (plano gratuito)

1. Crie um Projeto "PromTest" no claude.ai.
2. Cole nas instruções do Projeto o bloco da aba "Tutor (PRD)" do documento do plano no Claude (o mesmo conteúdo está em [docs/PRD-tutor.md](docs/PRD-tutor.md)).
3. Abra uma conversa no Projeto e escreva "vamos estudar".

Nessa opção o progresso fica na aba Progresso do documento. Quando passar para a opção A, peça ao tutor para copiar esse progresso para `progresso.md`.

## Estrutura

```
PromTest/
├── CLAUDE.md            instruções do tutor (lidas pelo Claude Code)
├── plano.md             o plano completo: 12 fases, cursos, projetos
├── progresso.md         onde parei, fases, tópicos, registro
├── duvidas.md           dúvidas abertas e tópicos para revisar
├── sessoes/             uma nota por sessão (AAAA-MM-DD.md)
├── projetos/            um projeto por fase (fase-N-nome/)
├── templates/           modelos de sessão e de README
├── conteudo/          LinkedIn + Substack: guia (CLAUDE.md próprio), pautas, métricas, posts
├── docs/
│   ├── SETUP.md         instalação, extensões, Obsidian, conectores
│   └── PRD-tutor.md     como o tutor funciona
└── .claude/skills/      comandos /estudar /encerrar /onde-paramos /me-testa /revisao
```

## Comandos do tutor

| Comando | O que faz |
| --- | --- |
| `/estudar [minutos]` | Começa a sessão do ponto certo |
| `/onde-paramos` | Resumo rápido do progresso |
| `/me-testa [tópico]` | Quiz de 5 perguntas |
| `/revisao` | Revisão quinzenal e ajuste de ritmo |
| `/encerrar` | Registra a sessão, atualiza o progresso e propõe o commit |

## Fases

0 Base técnica · 1 Prompt · 2 APIs · 3 RAG · 4 Agentes, MCP e OpenClaw · 5 Código e automação · 6 Evals · 7 Fundamentos de ML · 8 Modelos abertos · 9 Multimodal · 10 Segurança · 11 IA aplicada a QA
