<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.svg">
  <img src="assets/logo.svg" alt="PromTest" width="300">
</picture>

**Prompt + test.** Workspace de estudo de Inteligência Artificial, DevOps, cloud e QA, dos fundamentos ao avançado, com um tutor de IA e só fontes gratuitas.

![Módulo atual](https://img.shields.io/badge/m%C3%B3dulo%20atual-1%20Base%20t%C3%A9cnica-blue)
![Módulos](https://img.shields.io/badge/m%C3%B3dulos-21-lightgrey)
![Fontes](https://img.shields.io/badge/fontes-100%25%20gratuitas-green)
![Ritmo](https://img.shields.io/badge/ritmo-livre%2C%20sem%20prazo-orange)

## Objetivo

Ganhar habilidade prática e aprender os fundamentos principais de IA, do básico ao avançado. É um plano único de 21 módulos, cada um de uma área: Base, IA, DevOps (Linux, redes, Docker, CI/CD, observabilidade), Cloud (AWS, Terraform, Kubernetes) e QA. Os módulos se alternam para que cada um prepare o seguinte, e o último aplica tudo em qualidade de software.

Três regras guiam o caminho:

- **Um projeto por módulo.** Só avanço quando o projeto do módulo está pronto, no meu ritmo e sem prazo fixo.
- **Cursos oficiais e gratuitos**, como Anthropic Academy, OpenAI Academy e Google.
- **Tudo registrado.** Cada sessão vira uma nota e um commit.

## Progresso

| Módulo | Área | Tema | Status |
| --- | --- | --- | --- |
| 1 | Base | Base técnica | Em andamento |
| 2 | DevOps | Linux e terminal | Não iniciado |
| 3 | IA | Prompt e uso avançado | Não iniciado |
| 4 | DevOps | Redes | Não iniciado |
| 5 | IA | APIs de modelos | Não iniciado |
| 6 | DevOps | Git e scripting | Não iniciado |
| 7 | IA | RAG e dados | Não iniciado |
| 8 | DevOps | Docker | Não iniciado |
| 9 | IA | Agentes, MCP e OpenClaw | Não iniciado |
| 10 | DevOps | CI/CD com GitHub Actions | Não iniciado |
| 11 | IA | Agentes de código e automação | Não iniciado |
| 12 | Cloud | AWS | Não iniciado |
| 13 | Cloud | Terraform | Não iniciado |
| 14 | IA | Evals e confiabilidade | Não iniciado |
| 15 | Cloud | Kubernetes | Não iniciado |
| 16 | DevOps | Observabilidade e SRE | Não iniciado |
| 17 | IA | Fundamentos de ML e LLMs por dentro | Não iniciado |
| 18 | IA | Modelos abertos e fine-tuning | Não iniciado |
| 19 | IA | Multimodal | Não iniciado |
| 20 | IA | Segurança, ética e regulação | Não iniciado |
| 21 | QA | IA aplicada a QA | Não iniciado |

O ritmo, os tópicos e as sessões estão em [progresso.md](progresso.md); o plano completo, com cada módulo e os projetos, em [plano.md](plano.md).

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
| `/revisao` | Revisão quinzenal do que aprendi |
| `/encerrar` | Registra a sessão, atualiza o progresso e faz o commit |

## Estrutura

```text
PromTest/
├── CLAUDE.md          instruções do tutor (lidas pelo Claude Code)
├── plano.md           o plano único: 21 módulos, ritmo e projetos
├── progresso.md       onde parei, ritmo, roteiro, tópicos, registro
├── duvidas.md         dúvidas abertas e tópicos para revisar
├── sessoes/           uma nota por sessão (AAAA-MM-DD.md)
├── projetos/          um projeto por módulo (modulo-NN-nome/, painel-testes/)
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
