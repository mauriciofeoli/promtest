# Guia de instalação

Tudo o que você precisa para começar, na ordem. Comandos para macOS/Linux; quando Windows muda, está indicado.

## Estratégia (decidida)

- **Fonte de verdade:** esta pasta de arquivos `.md`, versionada no Git e publicada num repositório privado no GitHub.
- **Onde você estuda:** VS Code + terminal, com o Claude Code como tutor (ele lê o `CLAUDE.md` sozinho).
- **Onde você lê e navega:** Obsidian, abrindo esta mesma pasta como vault. Não precisa de sincronização paga: o Git faz isso.
- **Notion:** fica de fora por enquanto. Duas fontes de verdade geram conflito e trabalho dobrado. Se quiser ver o progresso no celular, use o app do GitHub ou o Obsidian com o plugin Git. A seção "Opcional: Notion" explica como ligar depois, se fizer falta.
- **Claude.ai (web e celular):** conectado ao repositório do GitHub, consegue ler e atualizar os mesmos arquivos quando você estiver longe do computador.

```
          você
            │
   VS Code + Claude Code  ──lê/escreve──►  PromTest/ (.md + Git)
            │                                  │        │
            │                              Obsidian   GitHub (privado)
            │                              (leitura)      │
            └──────────── commits ─────────────────────► Claude.ai no celular
```

## 1. Programas básicos

| Programa | Para quê | Instalação | Custo |
| --- | --- | --- | --- |
| Git | Versionar e sincronizar | git-scm.com/downloads (Windows: Git for Windows) | Grátis |
| VS Code | Editor | code.visualstudio.com | Grátis |
| Python 3.12+ | Linguagem principal | python.org ou via uv (abaixo) | Grátis |
| uv | Gerenciar Python, ambientes e pacotes | `curl -LsSf https://astral.sh/uv/install.sh \| sh` (Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \| iex"`) | Grátis |
| Docker Desktop | n8n, bancos vetoriais, OpenClaw isolado | docker.com/products/docker-desktop | Grátis para uso pessoal |
| Node.js LTS | Servidores MCP via `npx`, TypeScript | nodejs.org | Grátis |
| GitHub CLI (gh) | Criar e gerenciar o repositório pelo terminal | cli.github.com | Grátis |
| Obsidian | Ler e navegar as notas | obsidian.md | Grátis |
| Ollama | Rodar modelos localmente, sem custo de API | ollama.com/download | Grátis |

Ollama e Docker só são necessários a partir dos módulos 7 e 9; instale quando chegar lá se quiser poupar espaço.

## 2. Claude Code

Instalação nativa (recomendada, atualiza sozinha):

```bash
# macOS, Linux, WSL
curl -fsSL https://claude.ai/install.sh | bash

# Windows PowerShell
irm https://claude.ai/install.ps1 | iex
```

Conferir e entrar:

```bash
claude --version
claude doctor
cd PromTest
claude          # abre a sessão e pede login no navegador
```

**Atenção ao custo:** o Claude Code exige um plano pago do Claude (Pro, Max, Team ou Enterprise) ou uma conta de API no Console. O plano gratuito do claude.ai não inclui o Claude Code. O Pro é a opção mais barata para começar; confira os preços atuais em claude.com/pricing.

Se ainda não quiser pagar, dá para seguir o plano no claude.ai (gratuito) usando o Projeto com as instruções de `docs/PRD-tutor.md`, e trazer para o Claude Code depois.

Documentação: code.claude.com/docs/en/setup

## 3. Extensões do VS Code

Ao abrir a pasta, o VS Code sugere estas extensões automaticamente (arquivo `.vscode/extensions.json`). Aceite a sugestão.

| Extensão | Para quê |
| --- | --- |
| Claude Code (Anthropic) | Tutor dentro do editor, com diffs lado a lado |
| Python e Pylance (Microsoft) | Python, autocompletar, tipos |
| Jupyter (Microsoft) | Notebooks para experimentos |
| Ruff | Lint e formatação de Python |
| Docker / Container Tools (Microsoft) | Containers e docker compose |
| GitLens | Histórico do Git |
| Markdown All in One e markdownlint | Escrever e checar os .md |
| YAML (Red Hat) | Arquivos de configuração e docker compose |
| Playwright Test (Microsoft) | Módulo 21, testes com IA |

## 4. Obsidian

1. Abra o Obsidian, escolha "Open folder as vault" e selecione a pasta `PromTest`.
2. Em Settings > Core plugins, ative **Templates** e aponte a pasta de templates para `templates`.
3. Em Settings > Community plugins, desative o modo restrito e instale:

| Plugin | Para quê |
| --- | --- |
| Obsidian Git | Commit e pull automáticos (sincroniza com o GitHub) |
| Dataview | Listas e tabelas automáticas a partir das sessões (ex.: todas as sessões do Módulo 5) |
| Tasks | Ver todos os checkboxes de tópicos em um só lugar |
| Calendar | Navegar pelas notas de sessão por data |

4. No Obsidian Git, configure: "Auto pull on startup" ligado e "Auto commit interval" de 30 minutos (ou deixe desligado e faça commit pelo Claude Code no `/encerrar`).

A pasta `.obsidian/` guarda as configurações do vault. O `.gitignore` ignora só as partes locais (layout das janelas e cache); plugins e configurações vão para o Git, então outro computador abre o vault já configurado.

## 5. Repositório no GitHub

```bash
cd PromTest
git init
git add .
git commit -m "estudo: estrutura inicial do plano"
gh auth login
gh repo create promtest --private --source=. --push
```

Deixe privado enquanto quiser. Quando for usar como portfólio, torne público ou crie um repositório separado só com os projetos.

## 6. Conectores e MCP

Nenhum é obrigatório para começar. Adicione conforme o módulo pedir.

| Conector | Quando | Como |
| --- | --- | --- |
| GitHub no claude.ai | Agora, para estudar pelo celular | claude.ai > Configurações > Conectores > GitHub, dando acesso ao repositório `promtest` |
| Context7 (documentação atualizada de bibliotecas) | Módulo 5 em diante | `claude mcp add --transport http context7 https://mcp.context7.com/mcp` (conferir na documentação do Context7) |
| Playwright MCP | Módulo 21 | `claude mcp add playwright -- npx @playwright/mcp@latest` (conferir na documentação do Playwright) |
| Servidor MCP próprio | Módulo 9 | Você vai construir um |

Para ver e remover: `claude mcp list` e `claude mcp remove <nome>`.

## 7. Opcional: Notion

Só se você quiser um painel bonito no celular. O Notion vira um espelho, nunca a fonte de verdade.

- **No claude.ai:** reconecte o conector do Notion em Configurações > Conectores.
- **No Claude Code:** `claude mcp add --transport http notion https://mcp.notion.com/mcp` e depois `/mcp` para autenticar. Em algumas versões a autenticação desse servidor no terminal falhou; se acontecer, use o conector pelo claude.ai.
- Peça ao tutor, no `/encerrar`, para também atualizar uma página de progresso no Notion.

## 8. Chaves de API (a partir do Módulo 5)

- Crie um arquivo `.env` na raiz (já está no `.gitignore`) a partir de `.env.example`.
- Para não gastar: use cotas gratuitas quando existirem e modelos locais pelo Ollama.
- Nunca cole chaves em notas, sessões ou commits.

## 9. Primeira sessão

```bash
cd PromTest
claude
```

Digite `/estudar 60` (60 minutos disponíveis). O tutor faz um diagnóstico do Módulo 1 e começa. Para terminar, `/encerrar`.
