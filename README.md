<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.svg">
  <img src="assets/logo.svg" alt="PromTest" width="300">
</picture>

**Prompt + test.** Workspace de estudo de Inteligência Artificial, dos fundamentos ao avançado, com um tutor de IA e só fontes gratuitas.

![Fase atual](https://img.shields.io/badge/fase%20atual-0%20Base%20t%C3%A9cnica-blue)
![Roteiro](https://img.shields.io/badge/roteiro-21%20blocos-lightgrey)
![Fontes](https://img.shields.io/badge/fontes-100%25%20gratuitas-green)
![Ritmo](https://img.shields.io/badge/ritmo-acompanha%20o%20progresso-orange)

## Objetivo

Ganhar habilidade prática e aprender os fundamentos principais de IA, do básico ao avançado. No caminho entram etapas de DevOps e cloud (Linux, redes, Docker, CI/CD, AWS, Terraform, Kubernetes e observabilidade), intercaladas com as fases de IA num roteiro único. A última fase aplica o que foi aprendido em qualidade de software.

Três regras guiam o caminho:

- **Um projeto por bloco.** Só avanço quando o projeto do bloco está pronto, no meu ritmo e sem prazo fixo.
- **Cursos oficiais e gratuitos**, como Anthropic Academy, OpenAI Academy e Google.
- **Tudo registrado.** Cada sessão vira uma nota e um commit.

## Progresso

| Ordem | Bloco | Tema | Status |
| --- | --- | --- | --- |
| 1 | Fase 0 | Base técnica | Em andamento |
| 2 | Etapa 1 | Linux e terminal | Não iniciada |
| 3 | Fase 1 | Prompt e uso avançado | Não iniciada |
| 4 | Etapa 2 | Redes | Não iniciada |
| 5 | Fase 2 | APIs de modelos | Não iniciada |
| 6 | Etapa 3 | Git e scripting | Não iniciada |
| 7 | Fase 3 | RAG e dados | Não iniciada |
| 8 | Etapa 4 | Docker | Não iniciada |
| 9 | Fase 4 | Agentes, MCP e OpenClaw | Não iniciada |
| 10 | Etapa 5 | CI/CD com GitHub Actions | Não iniciada |
| 11 | Fase 5 | Agentes de código e automação | Não iniciada |
| 12 | Etapa 6 | AWS | Não iniciada |
| 13 | Etapa 7 | Terraform | Não iniciada |
| 14 | Fase 6 | Evals e confiabilidade | Não iniciada |
| 15 | Etapa 8 | Kubernetes | Não iniciada |
| 16 | Etapa 9 | Observabilidade e SRE | Não iniciada |
| 17 | Fase 7 | Fundamentos de ML e LLMs por dentro | Não iniciada |
| 18 | Fase 8 | Modelos abertos e fine-tuning | Não iniciada |
| 19 | Fase 9 | Multimodal | Não iniciada |
| 20 | Fase 10 | Segurança, ética e regulação | Não iniciada |
| 21 | Fase 11 | IA aplicada a QA | Não iniciada |

Fase é um bloco de IA; etapa é um bloco de DevOps e cloud.

O ritmo, os tópicos e as sessões estão em [progresso.md](progresso.md). O roteiro e as fases de IA estão em [plano.md](plano.md); as etapas de DevOps e cloud, com o projeto principal, em [trilha-devops.md](trilha-devops.md).

## Como funciona

O tutor é o próprio Claude Code. O arquivo [CLAUDE.md](CLAUDE.md) define como ele ensina, e ele o lê sozinho ao abrir a pasta. Cada sessão segue o mesmo ciclo:

```mermaid
flowchart LR
    A["/estudar"] --> B[Conceito em camadas]
    B --> C[Exercício]
    C --> D{Entendi?}
    D -- não --> B
    D -- sim --> E[Próximo tópico]
    E --> F["/encerrar"]
    F --> G[Nota da sessão + progresso + commit]
```

### Comandos do tutor

| Comando | O que faz |
| --- | --- |
| `/estudar [minutos]` | Começa a sessão do ponto certo |
| `/onde-paramos` | Resumo rápido do progresso |
| `/me-testa [tópico]` | Quiz curto sobre o tópico |
| `/revisao` | Revisão quinzenal e ajuste de ritmo |
| `/encerrar` | Registra a sessão, atualiza o progresso e faz o commit |

## Estrutura

```text
PromTest/
├── CLAUDE.md          instruções do tutor (lidas pelo Claude Code)
├── plano.md           roteiro único, regras de ritmo e as 12 fases de IA
├── trilha-devops.md   as 9 etapas de DevOps e cloud e seus projetos
├── progresso.md       onde parei, ritmo, roteiro, tópicos, registro
├── duvidas.md         dúvidas abertas e tópicos para revisar
├── sessoes/           uma nota por sessão (AAAA-MM-DD.md)
├── projetos/          um projeto por bloco (fase-N-nome/, devops-*/)
├── templates/         modelos de sessão e de README
├── conteudo/          LinkedIn e Substack: guia, pautas, métricas, posts
├── docs/
│   ├── SETUP.md       instalação, extensões, Obsidian, conectores
│   └── PRD-tutor.md   como o tutor funciona
└── .claude/skills/    comandos /estudar /encerrar /onde-paramos /me-testa /revisao
```

## Quer usar o método?

Não precisa colar prompt nenhum: o `CLAUDE.md` é o prompt. Escolha uma das opções abaixo.

<details>
<summary><strong>Opção A: terminal com Claude Code</strong> (exige plano pago do Claude)</summary>

1. Instale o que precisa: [docs/SETUP.md](docs/SETUP.md) (no mínimo Git, VS Code e Claude Code).
2. Baixe o repositório e abra o tutor:

   ```bash
   git clone https://github.com/mauriciofeoli/promtest.git PromTest
   cd PromTest
   claude
   ```

3. Confira se o tutor leu tudo: digite `/onde-paramos`.
4. Comece: `/estudar 60` (60 = minutos disponíveis) ou escreva "vamos estudar".
5. Para parar, só se despeça ("por hoje é isso"). O tutor salva o progresso e faz o commit sozinho.

Nas próximas vezes, é só `cd PromTest` e `claude`.

Para começar do zero com o seu próprio progresso, zere `progresso.md`, `duvidas.md` e a pasta `sessoes/`.

</details>

<details>
<summary><strong>Opção B: claude.ai, sem instalar nada</strong> (plano gratuito)</summary>

1. Crie um Projeto "PromTest" no claude.ai.
2. Cole nas instruções do Projeto o conteúdo de [docs/PRD-tutor.md](docs/PRD-tutor.md).
3. Abra uma conversa no Projeto e escreva "vamos estudar".

Nessa opção o progresso fica no próprio Projeto. Quando passar para a opção A, peça ao tutor para copiar esse progresso para `progresso.md`.

</details>
