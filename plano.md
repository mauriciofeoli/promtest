---
tipo: plano
status: referência (só alterar quando você pedir)
atualizado: 2026-10-24
---

# Plano de estudos: IA, DevOps, cloud e QA, do zero ao avançado

## Como usar este plano

Um plano só, com 21 módulos numa ordem única. Cada módulo pertence a uma área (Base, IA, DevOps, Cloud ou QA), mas a área é só uma etiqueta: ela diz de que tipo é o módulo, não cria um caminho separado. Cada módulo prepara o seguinte e tem objetivo, tópicos, fontes gratuitas, um projeto e um critério de "pronto".

- **Nível de partida:** zero em tudo, de propósito, como nível padrão para qualquer pessoa usar o plano. O Módulo 1 ensina terminal, Python, Git e Docker do zero; os módulos seguintes contam com isso. Quem já conhece um assunto passa rápido por ele no diagnóstico do módulo.
- **Ordem:** prática antes da teoria profunda. Você constrói com APIs e agentes (módulos 5 a 14) antes de estudar matemática e redes neurais (Módulo 17), porque a teoria fica mais clara depois de ver o modelo errar na prática. Os módulos de DevOps e cloud entram logo antes do módulo de IA que precisa deles.
- **Ritmo livre:** não há prazo nem meta de velocidade (veja "Ritmo").
- **Regra 70/30:** 70% do tempo construindo, 30% assistindo ou lendo.
- **Um projeto por módulo:** publicado no GitHub, com um post curto no LinkedIn sobre o que aprendeu. Os projetos se conectam entre si (veja "Como os projetos se conectam").
- **Com o tutor:** em cada tópico, peça explicação, exercícios, revisão de código ou resumo de artigo.
- **Atualização:** ferramentas, preços e cursos mudam rápido. Itens marcados "(conferir)" são verificados quando você chegar neles.
- **Custo:** todas as fontes são gratuitas. Os gastos possíveis são APIs pagas por uso (evitáveis com cotas grátis e modelos locais, como o Ollama) e a AWS nos módulos 12 e 13 e no projeto principal (veja "Cuidados com custo na AWS").

## Áreas

| Área | Módulos | O que cobre |
| --- | --- | --- |
| Base | 1 | Terminal, Python, Git, HTTP, Docker e SQL do zero |
| IA | 3, 5, 7, 9, 11, 14, 17, 18, 19, 20 | Prompt, APIs, RAG, agentes, evals, fundamentos de ML, modelos abertos, multimodal, segurança |
| DevOps | 2, 4, 6, 8, 10, 16 | Linux, redes, Git e scripting, Docker, CI/CD, observabilidade e SRE |
| Cloud | 12, 13, 15 | AWS, Terraform, Kubernetes |
| QA | 21, com temas de QA em todo o roteiro | IA para testar software e testes de sistemas de IA (veja "QA ao longo do roteiro") |

## Roteiro

A ordem abaixo é a ordem de estudo. Um módulo só começa quando o anterior estiver com o projeto pronto e o "pronto quando" atendido. A estimativa considera 1 a 2 horas por dia e dá só uma noção do tamanho de cada módulo; não é prazo.

| Módulo | Área | Tema | Estimativa | Por que aqui |
| --- | --- | --- | --- | --- |
| 1 | Base | Base técnica | 6 sem | Ponto de partida: terminal, Python, Git, HTTP e Docker do zero |
| 2 | DevOps | Linux e terminal | 3 sem | Aprofunda o terminal do Módulo 1 enquanto está fresco; servidores e agentes rodam em Linux |
| 3 | IA | Prompt e uso avançado | 4 sem | Não depende de infraestrutura e traz IA logo no começo |
| 4 | DevOps | Redes | 2 sem | Prepara o Módulo 5: chamar APIs exige entender DNS, HTTPS, portas e timeouts |
| 5 | IA | APIs de modelos | 4 sem | Usa o HTTP do Módulo 1 e as redes do Módulo 4 |
| 6 | DevOps | Git e scripting | 3 sem | Os projetos crescem: branches, PRs, pytest e o início do projeto principal |
| 7 | IA | RAG e dados | 4 sem | Bancos vetoriais sobem com o Docker básico do Módulo 1 |
| 8 | DevOps | Docker | 3 sem | O Módulo 9 roda o OpenClaw isolado em container |
| 9 | IA | Agentes, MCP e OpenClaw | 6 sem | Usa Linux (Módulo 2) e Docker (Módulo 8) para isolar agentes |
| 10 | DevOps | CI/CD com GitHub Actions | 2 sem | O Módulo 11 usa agentes de código no CI e o Módulo 14 roda evals no pipeline |
| 11 | IA | Agentes de código e automação | 4 sem | Claude Code em modo headless no pipeline do Módulo 10; n8n em Docker |
| 12 | Cloud | AWS | 4 sem | Primeira nuvem, feita à mão antes de automatizar |
| 13 | Cloud | Terraform | 3 sem | Fecha o deploy do projeto principal |
| 14 | IA | Evals e confiabilidade | 4 sem | Suíte de evals rodando no pipeline do Módulo 10 |
| 15 | Cloud | Kubernetes | 4 sem | Docker já firme; prepara a infraestrutura do Módulo 18 |
| 16 | DevOps | Observabilidade e SRE | 3 sem | Completa a observabilidade de IA do Módulo 14 com métricas, alertas e SLOs |
| 17 | IA | Fundamentos de ML e LLMs por dentro | 12 sem | Módulo teórico longo, com a base de engenharia já completa |
| 18 | IA | Modelos abertos e fine-tuning | 6 sem | Serve modelos com Docker, Kubernetes, Terraform e monitoramento |
| 19 | IA | Multimodal | 3 sem | Usa as APIs e os agentes dos módulos anteriores |
| 20 | IA | Segurança, ética e regulação | 2 sem | Red teaming dos agentes e revisão de segurança da infraestrutura |
| 21 | QA | IA aplicada a QA | 6 sem | Projeto final no CI, com deploy e monitoramento |

## Ritmo

O ritmo é seu. Não há prazo nem meta de velocidade: o objetivo é continuar estudando porque gosta, não cumprir um calendário.

- **Continuidade acima de velocidade:** uma sessão curta vale mais que nenhuma. Se o tempo do dia for pouco, o tutor propõe algo que caiba (uma revisão, um exercício, um trecho de documentação). Depois de uma pausa, a volta começa com uma revisão leve, sem cobrança.
- **O que fica registrado:** sessões, minutos e tópicos concluídos, na seção "Ritmo" de `progresso.md`. Serve para planejar o tamanho de cada sessão e para você ver o caminho já feito, não para medir atraso. Um tópico está concluído quando você fez o exercício sem receber a resposta pronta e, se houve quiz, acertou pelo menos 4 de 5.
- **Dentro da sessão:** se você acerta de primeira, o tutor avança e oferece desafios; se erra o mesmo ponto duas vezes, divide o tópico em partes menores e passa mais exercícios. O projeto e o "pronto quando" de cada módulo nunca são pulados.
- **Sem previsão de término:** as estimativas do roteiro dão só uma noção do tamanho de cada módulo. Ninguém compara o seu avanço com datas.
- **Revisão quinzenal:** olha o que você aprendeu e o que precisa voltar; se quiser, ajusta o que vem a seguir.

## Como os projetos se conectam

| Projeto | Usa | É usado por |
| --- | --- | --- |
| Módulo 1: cliente HTTP em Docker | | Módulo 4: a checagem de rede reaproveita o tratamento de erros e retries |
| Projeto principal: painel de execuções de teste (módulos 6, 8, 10, 13 e 16) | Módulos 2 e 4 | Módulos 14 e 21: a mesma estrutura de pipeline e deploy |
| Módulo 9: OpenClaw com skill própria | Módulos 2 e 8: Linux e container isolado | Módulo 20: red teaming |
| Módulo 11: app feito com Claude Code | Módulo 10: pipeline com testes | |
| Módulo 14: suíte de evals no CI | Módulo 10: GitHub Actions | Módulo 16: métricas de qualidade no Grafana |
| Módulo 18: modelo servido por API | Módulos 8, 13, 15 e 16 | Módulo 21 |
| Módulo 21: assistente de QA | Módulos 10, 13 e 16: CI, deploy e monitoramento | |

## QA ao longo do roteiro

O Módulo 21 concentra a parte de QA, mas o tema aparece antes, e o seu conhecimento de testes serve de ponte em cada um destes módulos:

| Módulo | O que tem de QA |
| --- | --- |
| 4 | Checagem de rede que vira o smoke test pós-deploy do projeto principal |
| 6 | pytest e testes como parte de todo pull request |
| 7 | 30 perguntas de avaliação e qualidade da busca medida com números |
| 9 | Servidor MCP que consulta resultados de testes |
| 10 | Testes como portão do pipeline: PR com teste quebrado é bloqueado |
| 11 | Fluxo no n8n que roda a suíte, resume as falhas com IA e manda o relatório |
| 14 | Golden datasets, LLM como juiz, testes de regressão de prompt |
| 15 | Teste de resiliência: apagar um Pod de propósito e testar o rollback |
| 16 | Alertas, SLO e postmortem, o primo do relatório de bug |
| 18 | Modelo ajustado para transformar histórias de usuário em casos de teste |
| 19 | Print de tela com erro vira relatório de bug |
| 20 | Red teaming do próprio agente |

## Módulo 1: Base técnica (Base, 6 semanas)

Objetivo: ter a caixa de ferramentas de quem constrói com IA, partindo do zero. Por padrão, o plano não supõe experiência prévia em programação, Python, Git ou Docker; quem já conhece um assunto passa rápido por ele. O conhecimento de QA entra como ponte nos exemplos (testar uma API, achar bug, pensar em cenários), mas nenhuma ferramenta é tida como conhecida.

**Tópicos (nesta ordem; cada um só começa quando o anterior estiver firme)**

1. **Terminal básico:** o que é o terminal, abrir, navegar entre pastas, criar e apagar arquivos, rodar comandos, ler mensagens de erro. Aprofundado no Módulo 2.
2. **Python do zero:** instalar e rodar, variáveis, texto, números, listas e dicionários, `if`, `for`, funções, ler e escrever arquivos, erros e `try/except`.
3. **Git e GitHub básico:** o que é versionar, `init`, `add`, `commit`, `push`, ler o histórico, branches, pull request. Aprofundado no Módulo 6.
4. **Python para IA:** ambientes virtuais (`uv`, venv), instalar bibliotecas, JSON e CSV, variáveis de ambiente e segredos (`.env`), tipagem, dataclasses e Pydantic, `async/await`.
5. **HTTP e APIs:** o que é uma API, métodos, status, headers, autenticação por chave, JSON e XML (ler, escrever e comparar os dois formatos), paginação, rate limit, retries com backoff, webhooks; ler o contrato OpenAPI de uma API pública e testá-la pelo Swagger UI. O lado de redes e servidor vem no Módulo 4.
6. **Docker:** o que é um container, imagens, volumes, `docker compose` (vai rodar n8n, bancos vetoriais e modelos locais). Dockerfile próprio e boas práticas vêm no Módulo 8.
7. **SQL básico:** `SELECT`, `JOIN`, `GROUP BY`; base para bancos vetoriais como o pgvector.
8. **Jupyter Notebooks:** para experimentos rápidos.
9. **TypeScript (opcional):** a segunda linguagem do AI engineer, útil para interfaces e agentes em Node. Fica a seu critério.

**Fontes gratuitas:** Kaggle Learn (Python, Pandas, SQL); tutorial oficial do Python em português (docs.python.org/pt-br/3/tutorial); documentação do `uv` (docs.astral.sh/uv); documentação do Git (git-scm.com/book/pt-br) e do Docker (docs.docker.com/get-started).

**Projeto:** um script em Python que consome uma API pública, trata erros e retries, e salva o resultado em JSON, rodando dentro de um container Docker.

**Pronto quando:** você sobe um serviço com docker compose e escreve um cliente HTTP robusto sem consultar tutorial.

## Módulo 2: Linux e terminal (DevOps, 3 semanas)

Objetivo: se virar num servidor Linux só pelo terminal, sem interface gráfica. Quase toda nuvem roda Linux.

**Tópicos**

- **Ambiente:** WSL2 com Ubuntu no Windows (o Linux de verdade, dentro do seu computador). Diferença entre o PowerShell do Módulo 1 e o Bash.
- **Sistema de arquivos:** a árvore a partir de `/`, `/home`, `/etc`, `/var/log`, caminhos absolutos e relativos, `find`, `grep`, `less`, `head`, `tail -f`.
- **Permissões:** usuário, grupo e outros; `ls -l`, `chmod`, `chown`, `sudo` e por que não usar `root` no dia a dia.
- **Processos:** `ps`, `top` ou `htop`, `kill`, sinais, primeiro e segundo plano, serviços com `systemctl` e `journalctl`.
- **Pacotes:** `apt update`, `apt install`, de onde vêm os pacotes.
- **Logs:** onde ficam, como ler, filtrar e acompanhar ao vivo (`journalctl`, `tail -f`, `grep`).
- **SSH:** par de chaves pública e privada, `ssh-keygen`, `ssh usuario@servidor`, `~/.ssh/config`, `scp`. A chave privada nunca sai do seu computador.
- **Bash:** variáveis, `if`, `for`, funções, código de saída (`$?`), pipes (`|`), redirecionamento (`>`, `>>`, `2>`), `set -euo pipefail`, agendamento com `cron`.

**Fontes gratuitas**

- Linux Foundation: Introduction to Linux (LFS101) (conferir se continua gratuito).
- Linux Journey (linuxjourney.com).
- MIT "The Missing Semester of Your CS Education" (missing.csail.mit.edu): aulas de shell, scripts e linha de comando.
- OverTheWire Bandit (overthewire.org/wargames/bandit): treino de terminal e SSH em formato de jogo.
- Documentação do WSL (learn.microsoft.com/windows/wsl).

**Projeto:** `modulo-02-saude-servidor`. Um script Bash que verifica a saúde da máquina (disco, memória, processos que mais consomem) e analisa um arquivo de log (quantos erros, quais os mais frequentes), gera um relatório em texto e roda sozinho pelo `cron`.

**Pronto quando:** você entra numa máquina por SSH com chave, acha por que um serviço caiu lendo os logs e escreve um script Bash que falha de forma clara quando algo dá errado.

## Módulo 3: Usuário avançado e engenharia de prompt (IA, 4 semanas)

Objetivo: usar qualquer IA no nível máximo e saber escrever prompts que funcionam de forma previsível.

**Conceitos**

- O que é um LLM, em linguagem simples: tokens, janela de contexto, temperatura, alucinação, data de corte do conhecimento.
- Modelo versus ferramenta versus agente; assistente versus agente autônomo.
- Pontos fortes e fracos de cada família (Claude, GPT, Gemini, Llama, Mistral, DeepSeek, Qwen) e como comparar.

**Engenharia de prompt**

- Anatomia de um prompt: papel, contexto, tarefa, formato de saída, exemplos, restrições.
- Zero-shot e few-shot; exemplos positivos e negativos.
- Chain-of-thought e raciocínio estendido; quando ele ajuda e quando atrapalha.
- Decomposição de tarefas e encadeamento de prompts (prompt chaining).
- Tags XML e delimitadores; saída estruturada em JSON.
- Ancoragem em documentos (grounding) e citação de fontes.
- Autocrítica e validação: pedir que a IA revise o próprio resultado.
- Meta-prompting: usar a IA para escrever e melhorar prompts.

**Recursos das ferramentas**

- Claude: projetos, artefatos, skills, conectores, pesquisa, memória.
- ChatGPT: GPTs personalizados, memória, Deep Research, tarefas agendadas, conectores.
- Gemini: Gems, Canvas, Deep Research, NotebookLM.
- Uso responsável: o que não colar numa IA (dados sensíveis, código de cliente), checagem de fatos.

**Cursos oficiais gratuitos**

- Anthropic Academy (anthropic.skilljar.com): Claude 101 e AI Fluency.
- Tutorial interativo de engenharia de prompt da Anthropic (GitHub "anthropics/courses").
- OpenAI Academy (academy.openai.com): AI Foundations.
- Google: Introduction to Generative AI e Introduction to Large Language Models.
- Guias oficiais de prompt da Anthropic, OpenAI e Google.

**Projeto:** uma biblioteca pessoal de 20 prompts testados nas três IAs, com comparação dos resultados e o que funcionou em cada uma.

**Pronto quando:** você explica por que um prompt falhou e corrige sem tentativa e erro às cegas.

## Módulo 4: Redes (DevOps, 2 semanas)

Objetivo: entender o caminho de uma requisição, do navegador até o servidor, e saber diagnosticar onde ela quebra.

**Tópicos**

- **TCP/IP:** endereço IP, máscara e sub-rede (notação CIDR, como `10.0.0.0/16`), IP público e privado, TCP versus UDP, o aperto de mão de 3 vias.
- **Portas:** o que é uma porta, as mais comuns (22, 80, 443, 5432), `ss -tulpn` para ver o que está escutando.
- **DNS:** como um nome vira IP, registros A, CNAME, MX e TXT, TTL e cache, `dig` e `nslookup`.
- **HTTP e HTTPS:** métodos, status, headers, `curl -v`; TLS, certificados e o que o cadeado garante. O Módulo 1 já cobre HTTP do ponto de vista de quem consome uma API; aqui o foco é o lado do servidor e o diagnóstico.
- **Load balancer:** distribuir tráfego entre servidores, camada 4 versus camada 7, health check.
- **Firewall:** regras de entrada e saída, `ufw` no Linux, a ideia que a AWS usa nos security groups.
- **Diagnóstico:** `ping`, `traceroute`, `curl`, `dig`, `nc` (netcat). Ordem de investigação: o nome resolve? a porta abre? o serviço responde?

**Fontes gratuitas**

- Cloudflare Learning Center (cloudflare.com/learning): DNS, HTTP, TLS, load balancing e firewall, com textos curtos.
- MDN Web Docs sobre HTTP (developer.mozilla.org/pt-BR/docs/Web/HTTP).
- Aulas de redes do "The Missing Semester" e manual do `dig` e do `curl`.

**Projeto:** `modulo-04-checagem-rede`. Um script em Python que recebe uma lista de sites e, para cada um, verifica se o DNS resolve, se a porta abre, o status HTTP, o tempo de resposta e quantos dias faltam para o certificado TLS vencer. Gera um relatório e termina com código de erro se algo falhar. Esse script vira o smoke test pós-deploy do projeto principal.

**Pronto quando:** dado "o site não abre", você descobre em poucos minutos se o problema é DNS, rede, porta, certificado ou a aplicação.

## Módulo 5: Construir com APIs de modelos (IA, 4 semanas)

Objetivo: sair do chat e colocar modelos dentro de programas. É aqui que você vira construtor.

**Tópicos**

- APIs da Anthropic, OpenAI e Gemini: mensagens, papéis (system, user, assistant), parâmetros (temperatura, max tokens, stop sequences).
- SDKs oficiais em Python; chaves de API e boas práticas de segredos.
- Streaming de respostas.
- Saídas estruturadas: JSON schema, validação com Pydantic, o que fazer quando o modelo devolve JSON quebrado.
- Tool use (function calling): definir ferramentas, receber a chamada, executar, devolver o resultado.
- Entradas multimodais: imagens e PDFs.
- Raciocínio estendido (extended thinking) e quando vale o custo.
- Prompt caching, processamento em lote (batch) e como reduzir custo.
- Tokens, preços, limites de taxa, retries e tratamento de erros.
- Interfaces simples: Streamlit ou Gradio em Python; Vercel AI SDK se for de TypeScript.
- Bibliotecas que unificam provedores (LiteLLM, por exemplo) para trocar de modelo sem reescrever código.

**Cursos oficiais gratuitos**

- Anthropic Academy: Claude Platform 101 e Building with the Claude API.
- Cursos da Anthropic no GitHub "anthropics/courses" (fundamentos de API, tool use).
- OpenAI Cookbook e a documentação da plataforma da OpenAI.
- Codelabs da API do Gemini (texto, multimodal, function calling, embeddings, streaming).

**Projeto:** um assistente de linha de comando que lê um arquivo (PDF ou CSV), responde perguntas sobre ele e devolve um relatório em JSON validado, funcionando com dois provedores diferentes.

**Pronto quando:** você implementa tool use do zero, sem framework, e sabe estimar quanto custa cada chamada.

## Módulo 6: Git e scripting (DevOps, 3 semanas)

Objetivo: trabalhar como numa equipe de engenharia: histórico limpo, branches, pull requests e scripts que automatizam tarefas repetitivas.

**Tópicos**

- **Git do dia a dia** (além do básico do Módulo 1): branches e `merge`, conflitos e como resolver, `rebase` simples, `git stash`, desfazer com segurança (`restore`, `revert`, `reset`), `.gitignore`, tags de versão.
- **GitHub:** pull request com revisão, issues, proteção da branch `main`, mensagens de commit claras.
- **Python para automação:** ler argumentos (`argparse`), variáveis de ambiente, chamar comandos do sistema (`subprocess`), ler e escrever JSON e CSV, chamar APIs (`requests` ou `httpx`), logs com `logging`.
- **Testes do próprio script:** `pytest` para funções de automação; o seu lado QA entra aqui.
- **Bash ou Python:** Bash para colar comandos curtos; Python quando houver lógica, dados ou testes.
- **Uma API pequena:** o que é um endpoint, FastAPI ou Flask para expor dados por HTTP.
- **Documentação da API com OpenAPI:** o contrato OpenAPI (antigo Swagger) gerado pelo FastAPI, com descrições, exemplos de requisição e resposta e códigos de status; Swagger UI e ReDoc; exportar o `openapi.json`.

**Fontes gratuitas**

- Pro Git em português (git-scm.com/book/pt-br).
- GitHub Skills (skills.github.com): cursos práticos dentro do próprio GitHub.
- "Automate the Boring Stuff with Python" (automatetheboringstuff.com), gratuito para ler online.
- Documentação do pytest e do FastAPI (fastapi.tiangolo.com/pt).

**Projeto:** `painel-testes` (início do projeto principal). Uma API pequena em Python que registra e lista execuções de teste (nome da suíte, quantos passaram, quantos falharam, duração), com testes em `pytest`, desenvolvida com branches e pull requests. Junto, um script que lê um relatório JUnit XML e envia os resultados para a API. A API sai documentada em OpenAPI, com Swagger UI no ar e o `openapi.json` versionado no repositório.

**Pronto quando:** você resolve um conflito de merge sem medo, abre um PR com descrição e testes, documenta cada endpoint no Swagger com exemplo e códigos de resposta, e automatiza em Python uma tarefa que antes fazia à mão.

## Módulo 7: RAG, embeddings e dados (IA, 4 semanas)

Objetivo: fazer a IA responder com base nos seus documentos, com fontes, sem inventar.

**Tópicos**

- Embeddings: o que são, similaridade de cosseno, modelos de embedding (abertos e por API).
- Ingestão: extração de PDF, HTML e planilhas; limpeza; metadados.
- Chunking: por tamanho, por estrutura, sobreposição; impacto na qualidade.
- Bancos vetoriais: pgvector (Postgres), Chroma, Qdrant; índices aproximados (HNSW).
- Busca híbrida: vetorial + palavra-chave (BM25); reranking.
- Técnicas avançadas: reescrita de consulta, HyDE, contextual retrieval, RAG com grafos (GraphRAG).
- Agentic RAG: o agente decide quando e onde buscar.
- Janela de contexto longa versus RAG: quando cada um vale a pena.
- Avaliação de RAG: relevância da recuperação, fidelidade da resposta, citações.
- Frameworks: LlamaIndex e LangChain para RAG, e como fazer sem framework.

**Fontes gratuitas**

- Cursos curtos da DeepLearning.AI sobre RAG e embeddings (conferir os títulos atuais).
- Artigo sobre contextual retrieval no blog de engenharia da Anthropic.
- Documentação do pgvector, Chroma e Qdrant.
- Artigo original de RAG (Lewis et al., 2020).

**Projeto:** um "pergunte à documentação" sobre um conjunto real de documentos (por exemplo, a documentação de uma ferramenta de testes), com busca híbrida, citações e um conjunto de 30 perguntas de avaliação.

**Pronto quando:** você mede a qualidade da recuperação com números e melhora um RAG ruim mudando chunking e busca, não só o prompt.

## Módulo 8: Docker (DevOps, 3 semanas)

Objetivo: empacotar qualquer aplicação para rodar igual em qualquer máquina. O Módulo 1 apresenta o Docker; aqui você escreve e otimiza as próprias imagens.

**Tópicos**

- **Imagens e containers:** camadas, tags, registro de imagens (Docker Hub, GitHub Container Registry), `docker run`, `ps`, `logs`, `exec`, `stop`, `rm`.
- **Dockerfile:** `FROM`, `WORKDIR`, `COPY`, `RUN`, `CMD`, `EXPOSE`; ordem das instruções e cache; `.dockerignore`.
- **Boas práticas:** imagem base pequena, build em múltiplos estágios (multi-stage), não rodar como `root`, nada de segredo dentro da imagem, `HEALTHCHECK`.
- **Dados e rede:** volumes, bind mounts, redes entre containers, variáveis de ambiente.
- **docker-compose:** vários serviços (API e banco Postgres), `depends_on`, healthchecks, arquivo `.env` local.
- **Segurança da imagem:** varredura de vulnerabilidades (Docker Scout ou Trivy) (conferir as opções gratuitas atuais).

**Fontes gratuitas**

- Documentação oficial do Docker (docs.docker.com/get-started), incluindo o guia de boas práticas de Dockerfile.
- Play with Docker (labs.play-with-docker.com), para treinar no navegador.
- Documentação do Docker Compose (docs.docker.com/compose).

**Projeto:** `painel-testes`, Módulo 8. A API ganha um `Dockerfile` multi-stage rodando sem `root` e um `docker-compose.yml` com a API e o Postgres. Os dados sobrevivem a `docker compose down`, e a API só sobe depois que o banco estiver saudável.

**Pronto quando:** você escreve um Dockerfile do zero, explica cada linha e sobe a aplicação com o banco usando um único comando.

## Módulo 9: Agentes, MCP, frameworks e OpenClaw (IA, 6 semanas)

Objetivo: entender e construir agentes que agem sozinhos com ferramentas, memória e outros agentes.

**Conceitos**

- O loop agêntico: o modelo pede uma ferramenta, o sistema executa, devolve o resultado, e repete até terminar.
- Padrões de workflow versus agente autônomo: encadeamento, roteamento, paralelização, orquestrador e trabalhadores, avaliador e otimizador.
- Planejamento, reflexão e ReAct.
- Memória: curto prazo (contexto), longo prazo (arquivos, banco), engenharia de contexto e compactação.
- Multiagentes e subagentes: quando dividir, custo em tokens, handoffs.
- Humano no circuito (human in the loop) e aprovações.
- Agentes de computador e navegador (computer use, browser agents).

**Protocolos**

- MCP (Model Context Protocol): clientes, servidores, ferramentas, recursos e prompts; escrever seu próprio servidor MCP em Python.
- A2A (Agent-to-Agent): agentes de equipes diferentes se descobrindo e chamando uns aos outros.
- Skills (arquivos SKILL.md) como forma de empacotar capacidades para agentes.

**Frameworks (aprender 2 a fundo, conhecer os outros)**

- Claude Agent SDK: o mesmo motor do Claude Code, com hooks, skills, subagentes e MCP.
- OpenAI Agents SDK: enxuto, com handoffs e tracing.
- LangGraph: agentes como grafos de estado; o mais usado em produção.
- CrewAI: equipes de agentes por papéis; bom para protótipos.
- Também conhecer: Pydantic AI, Google ADK, Microsoft Agent Framework, smolagents, LlamaIndex Agents, Mastra (TypeScript).

**OpenClaw (estudo de caso)**

- Agente pessoal open source (MIT), antes chamado Clawdbot e depois Moltbot, criado por Peter Steinberger no fim de 2025.
- Roda no seu computador ou servidor e conversa por Telegram, WhatsApp, Slack, Discord e outros canais.
- Arquitetura para estudar: gateway (processo que mantém o agente vivo), runtime do agente (loop e ferramentas), skills e ClawHub, memória em arquivos, comportamento definido em AGENTS.md, roteamento multiagente. Funciona com qualquer modelo.
- Riscos para estudar junto: acesso ao sistema operacional e prompt injection (instruções escondidas em páginas web podem virar comandos). Rode isolado, em container ou máquina separada, nunca com suas contas principais.

**Cursos oficiais gratuitos**

- Anthropic Academy: Introduction to MCP e MCP Advanced Topics.
- OpenAI Academy: Agents and Workflows.
- Hugging Face Agents Course.
- Cursos curtos da DeepLearning.AI sobre LangGraph, CrewAI e MCP (conferir os títulos atuais).
- Artigo "Building effective agents" do blog de engenharia da Anthropic e a especificação oficial do MCP.
- Documentação oficial do OpenClaw (docs.openclaw.ai).

**Projetos**

1. Um agente do zero, sem framework, com 3 ferramentas e loop próprio.
2. Um servidor MCP seu (por exemplo, que consulta resultados de testes) usado pelo Claude.
3. O mesmo agente reescrito em LangGraph e no Claude Agent SDK, comparando.
4. Um OpenClaw rodando em Docker, com uma skill escrita por você.

**Pronto quando:** você desenha a arquitetura de um agente, escolhe entre workflow e agente autônomo com argumento, e sabe onde ele pode ser atacado.

## Módulo 10: CI/CD com GitHub Actions (DevOps, 2 semanas)

Objetivo: cada mudança é testada e empacotada sozinha. Se um teste falha, nada chega à produção. É o encontro natural entre QA e DevOps.

**Tópicos**

- **Conceitos:** integração contínua (CI) versus entrega e implantação contínuas (CD); pipeline como portão de qualidade.
- **GitHub Actions:** workflows em YAML, gatilhos (`push`, `pull_request`, manual), jobs, steps, runners, actions prontas do Marketplace.
- **Testes no pipeline:** lint, testes unitários com `pytest`, testes de integração com o Postgres como serviço do job, relatório de testes e cobertura como artefato.
- **Build e publicação:** construir a imagem Docker e enviar ao GitHub Container Registry com tag de versão.
- **Segredos:** GitHub Secrets, variáveis de ambiente por ambiente, e por que nunca imprimir um segredo no log.
- **Boas práticas:** cache de dependências, matriz de versões, PR bloqueado quando o pipeline falha, pipeline rápido.

**Fontes gratuitas**

- Documentação do GitHub Actions (docs.github.com/pt/actions).
- GitHub Skills: cursos de Actions (conferir os títulos atuais).
- Documentação do GitHub Pages (docs.github.com/pt/pages) e do MkDocs (mkdocs.org), para o projeto extra.

**Projeto:** `painel-testes`, Módulo 10. Um workflow que, a cada PR, roda lint e testes (unitários e de integração com Postgres) e bloqueia o merge se falhar; a cada merge na `main`, constrói e publica a imagem no GitHub Container Registry. O workflow fica em `.github/workflows/` na raiz do repositório, filtrado pela pasta do projeto.

**Projeto extra:** site de documentação do PromTest. O plano de estudos e o progresso publicados como site com MkDocs e GitHub Pages, com menu e busca. Um workflow publica o site sozinho a cada merge na `main`, e só publica se o build passar e os links internos estiverem certos. Não bloqueia a conclusão do módulo.

**Pronto quando:** um PR com um teste quebrado é bloqueado sozinho, e o merge na `main` gera uma imagem nova sem você rodar nada.

## Módulo 11: Agentes de código e automação (IA, 4 semanas)

Objetivo: programar com agentes como parceiros e automatizar processos inteiros sem escrever tudo à mão.

**Agentes de código**

- Claude Code a fundo: CLAUDE.md, plan mode, gestão de contexto (compact, clear), subagentes, hooks, skills, MCP, modo headless e uso no CI.
- Outros: OpenAI Codex, Cursor, GitHub Copilot (agent mode), Gemini CLI; entender o que muda entre eles.
- Boas práticas: especificar antes de gerar, testes como guarda, revisão de código gerado, commits pequenos, segurança de dependências.
- "Vibe coding" versus engenharia assistida: onde termina a velocidade e começa a dívida técnica.

**Automação**

- n8n rodando localmente com Docker (gratuito): triggers, nós, webhooks, APIs, tratamento de erros, condicionais e loops, nós de IA e agentes dentro do fluxo, humano no circuito.
- Conhecer as alternativas: Make, Zapier, Power Automate.
- Agendamento e integrações com e-mail, planilhas, Slack ou Teams, GitHub.

**Cursos oficiais gratuitos**

- Anthropic Academy: Claude Code 101 e Claude Code in Action.
- Documentação oficial do Claude Code (code.claude.com/docs) e guia de boas práticas no blog de engenharia da Anthropic.
- Documentação e cursos oficiais do n8n (docs.n8n.io).

**Projetos**

1. Um app completo (API + interface + testes) construído com Claude Code a partir de uma especificação escrita por você.
2. Um fluxo no n8n que roda uma suíte de testes, resume as falhas com IA e manda o relatório no Teams ou Slack.

**Pronto quando:** você entrega uma funcionalidade inteira com um agente de código sem perder o controle do que foi gerado.

## Módulo 12: AWS (Cloud, 4 semanas)

Objetivo: entender as peças básicas da nuvem e publicar a aplicação de forma segura, primeiro pelo console, para saber o que o Terraform vai automatizar depois.

**Tópicos**

- **Conta e custo:** plano gratuito, alarme de orçamento (AWS Budgets), região, o que cobra por hora e o que cobra por uso.
- **IAM:** usuário root só para o essencial e com MFA; usuários, grupos, papéis (roles) e políticas; menor privilégio; chaves de acesso com rotação; IAM Identity Center para login no terminal (conferir a forma recomendada atual).
- **VPC:** sub-redes públicas e privadas, internet gateway, tabelas de rota, security groups (o firewall do Módulo 4), NAT e por que ele custa.
- **EC2:** instâncias, AMIs, tipos, par de chaves e SSH (o Módulo 2 de novo), user data para instalar Docker na subida.
- **S3:** buckets, objetos, bloqueio de acesso público, versionamento, ciclo de vida.
- **RDS:** Postgres gerenciado, sub-rede privada, backup, acesso só a partir da aplicação.
- **AWS CLI:** os mesmos passos pelo terminal.

**Fontes gratuitas**

- AWS Skill Builder (skillbuilder.aws): AWS Cloud Practitioner Essentials e os cursos gratuitos de fundamentos (conferir o catálogo gratuito atual).
- Documentação oficial da AWS para IAM, VPC, EC2, S3 e RDS, com os tutoriais "Getting started".
- Página do plano gratuito (aws.amazon.com/free) (conferir antes de criar a conta).

**Projeto:** `modulo-12-aws-console`. Publicar a imagem do painel de testes numa EC2 dentro de uma VPC própria, com o banco no RDS em sub-rede privada e relatórios guardados no S3, tudo criado pelo console e documentado passo a passo no README (com prints), usando um usuário IAM com permissões mínimas. No fim, apagar tudo e conferir a fatura.

**Pronto quando:** você desenha a arquitetura num papel (VPC, sub-redes, security groups, EC2, RDS, S3), explica por que o banco não fica na sub-rede pública e não deixa nenhum recurso esquecido gerando custo.

## Módulo 13: Terraform (Cloud, 3 semanas)

Objetivo: criar a mesma infraestrutura do Módulo 12 com código versionado, revisável e reproduzível, em vez de cliques.

**Tópicos**

- **Infraestrutura como código:** por que (revisão em PR, histórico, repetir em outro ambiente); declarativo versus imperativo.
- **Ciclo básico:** `init`, `fmt`, `validate`, `plan`, `apply`, `destroy`; ler um `plan` antes de aplicar.
- **Linguagem (HCL):** providers, resources, data sources, variables, outputs, `locals`.
- **Estado (state):** o que é, por que não vai para o Git, estado remoto em S3 com trava (conferir a forma atual de locking).
- **Organização:** módulos do Terraform (pacotes de código reutilizáveis, sem relação com os módulos deste plano), um diretório por ambiente, versões fixas de provider.
- **Segurança:** credenciais fora do código, `.tfvars` sensíveis fora do Git, varredura com ferramentas como Checkov ou tfsec (conferir).
- **Terraform no CI:** `plan` automático no PR e `apply` só com aprovação.
- **OpenTofu:** a alternativa de código aberto compatível; saber que existe.

**Fontes gratuitas**

- HashiCorp Developer: tutoriais "Get Started - AWS" (developer.hashicorp.com/terraform/tutorials).
- Documentação do provider AWS no Terraform Registry (registry.terraform.io).

**Projeto:** `painel-testes`, Módulo 13. A infraestrutura do Módulo 12 reescrita em Terraform, num módulo Terraform de rede e num de aplicação, com estado remoto em S3. O pipeline do Módulo 10 ganha um job que roda `terraform plan` em cada PR. Um `terraform destroy` apaga tudo no fim de cada sessão de estudo.

**Pronto quando:** você cria e destrói o ambiente inteiro com dois comandos e explica o que cada linha do `plan` vai mudar antes de aplicar.

## Módulo 14: Evals, observabilidade e confiabilidade (IA, 4 semanas)

Objetivo: provar com números que um sistema de IA funciona. Evals são os testes unitários da engenharia de IA, e é aqui que seu background de QA vira vantagem.

**Tópicos**

- Golden datasets: conjuntos de casos com resposta esperada, versionados.
- Tipos de avaliação: por código (regras, regex, schema), por comparação, por humano e LLM como juiz (LLM-as-judge), com calibração do juiz.
- Métricas: acurácia, fidelidade, relevância, taxa de alucinação, sucesso de tarefa em agentes, custo e latência.
- Testes de regressão de prompt e de modelo: um alarme quando a nota cai.
- Avaliação de agentes: trajetória (ferramentas certas na ordem certa), não só a resposta final.
- Observabilidade: tracing de chamadas, logs de ferramentas, custo por requisição. A parte de infraestrutura (Prometheus, Grafana, alertas, SLO) vem no Módulo 16.
- Guardrails: validação de entrada e saída, filtros, limites de ação.
- Segurança: prompt injection direta e indireta, vazamento de dados, jailbreaks, red teaming.
- Benchmarks públicos (MMLU, SWE-bench e outros): o que medem e por que não bastam.

**Ferramentas (código aberto ou com plano grátis)**

- promptfoo, DeepEval e Ragas para avaliação; Langfuse e LangSmith para tracing (conferir planos gratuitos atuais).
- Avaliação nativa das plataformas: console da Anthropic e evals da OpenAI.

**Fontes gratuitas**

- Curso de avaliação de prompts da Anthropic (GitHub "anthropics/courses").
- Guias de evals da Anthropic e da OpenAI.
- Cursos curtos da DeepLearning.AI sobre avaliação de LLMs e agentes (conferir).

**Projeto:** uma suíte de evals no CI para o projeto do Módulo 7 ou 9, com golden dataset, LLM como juiz calibrado, tracing e um relatório de regressão a cada mudança de prompt.

**Pronto quando:** você mostra um gráfico de qualidade antes e depois de uma mudança e explica uma falha silenciosa que os evals pegaram.

## Módulo 15: Kubernetes (Cloud, 4 semanas)

Objetivo: entender como rodar e escalar containers num cluster. Só comece com Docker firme: Kubernetes orquestra containers, então tudo que é confuso no Docker fica mais confuso aqui.

**Tópicos**

- **Por que existe:** vários containers em várias máquinas, recuperação automática, escala, atualização sem parar o serviço.
- **Cluster local:** `kind` ou `minikube`, e o `kubectl`. Fique no local: clusters gerenciados na nuvem (EKS) custam por hora.
- **Objetos principais:** Pod, Deployment, ReplicaSet, Service, Ingress, Namespace.
- **Configuração:** ConfigMap, Secret (e por que Secret não é criptografia), variáveis de ambiente.
- **Saúde e recursos:** liveness e readiness probes, requests e limits de CPU e memória.
- **Operação:** `kubectl get`, `describe`, `logs`, `exec`, rollout e rollback, escala manual e automática (HPA).
- **Empacotamento:** noções de Helm.

**Fontes gratuitas**

- Documentação e tutoriais oficiais (kubernetes.io/pt-br/docs/tutorials).
- Linux Foundation: Introduction to Kubernetes (LFS158), gratuito.
- Documentação do kind (kind.sigs.k8s.io) e do minikube.

**Projeto:** `modulo-15-kubernetes`. A imagem publicada pelo pipeline do painel de testes rodando num cluster `kind`, com Deployment de 2 réplicas, Service, ConfigMap, Secret, probes e limites de recursos, mais o Postgres. Teste de QA no fim: apagar um Pod de propósito e mostrar que o cluster recria; fazer uma atualização com erro e voltar com rollback.

**Pronto quando:** você sobe a aplicação no cluster só com manifestos escritos por você e diagnostica um Pod que não inicia usando `describe` e `logs`.

## Módulo 16: Observabilidade e SRE (DevOps, 3 semanas)

Objetivo: saber se a aplicação está saudável em produção antes do usuário reclamar, e decidir com números quanto de falha é aceitável.

**Tópicos**

- **Os três sinais:** métricas, logs e traces; o que cada um responde.
- **Métricas com Prometheus:** expor `/metrics` na aplicação, tipos (counter, gauge, histogram), PromQL básico, os "quatro sinais de ouro" (latência, tráfego, erros, saturação).
- **Painéis com Grafana:** fonte de dados, painel, variáveis; um painel por serviço que responde "está tudo bem?".
- **Logs:** logs estruturados em JSON, níveis, correlação por id de requisição; noções de Loki ou CloudWatch Logs.
- **Alertas:** regras no Prometheus e Alertmanager; alertar sobre sintoma, não sobre causa; evitar alerta que ninguém lê.
- **SRE:** SLI (o que se mede, por exemplo "porcentagem de requisições com sucesso em menos de 300 ms"), SLO (a meta, por exemplo 99,5% em 30 dias), SLA (o contrato), orçamento de erro (error budget).
- **Incidentes:** runbook, postmortem sem culpados, o paralelo com o relatório de bug do QA.
- **OpenTelemetry:** o padrão aberto de instrumentação; saber que existe.

**Fontes gratuitas**

- Livros de SRE do Google, gratuitos para ler online (sre.google/books), começando pelos capítulos sobre SLO e monitoramento.
- Documentação do Prometheus ("Getting started") e do Grafana (tutoriais oficiais).
- Documentação do OpenTelemetry (opentelemetry.io/docs).

**Projeto:** `painel-testes`, Módulo 16. A API passa a expor métricas; Prometheus e Grafana sobem pelo `docker-compose` e também na EC2; um painel mostra requisições, erros e latência; um alerta dispara quando a taxa de erro passa do limite; o README define 2 SLIs e seus SLOs e mostra o orçamento de erro.

**Pronto quando:** você provoca uma falha de propósito, vê o alerta disparar, encontra a causa pelo painel e pelos logs e escreve um postmortem curto.

## Módulo 17: Fundamentos de ML, deep learning e LLMs por dentro (IA, 12 semanas)

Objetivo: entender de verdade como os modelos funcionam, a ponto de construir um pequeno GPT do zero.

**Matemática essencial (3 semanas)**

- Álgebra linear: vetores, matrizes, produto escalar, multiplicação de matrizes.
- Cálculo: derivadas, regra da cadeia, gradiente.
- Probabilidade e estatística: distribuições, esperança, entropia, softmax.

**Machine learning clássico (3 semanas)**

- Aprendizado supervisionado e não supervisionado; regressão linear e logística; árvores e ensembles.
- Função de perda, gradiente descendente, overfitting, regularização, validação cruzada.
- Métricas: precisão, recall, F1, matriz de confusão, AUC. Pandas, NumPy e scikit-learn na prática.

**Deep learning (3 semanas)**

- Redes neurais, ativações, backpropagation, otimizadores (SGD, Adam).
- PyTorch: tensores, autograd, laço de treino.
- Redes convolucionais e recorrentes, só o suficiente para entender a evolução até os transformers.

**LLMs por dentro (3 semanas)**

- Tokenização (BPE), embeddings, atenção, multi-head attention, arquitetura transformer.
- Pré-treino, ajuste por instruções (SFT), RLHF, RLAIF e Constitutional AI.
- Leis de escala, modelos de raciocínio, mixture of experts, janelas de contexto longas.
- Noções de interpretabilidade: o que os pesquisadores conseguem ver dentro do modelo.

**Fontes gratuitas**

- 3Blue1Brown: séries "Essence of Linear Algebra", "Essence of Calculus" e "Neural Networks" (YouTube).
- Khan Academy para revisar matemática.
- Google Machine Learning Crash Course.
- Machine Learning Specialization do Andrew Ng (Coursera, assistindo como ouvinte sem certificado).
- fast.ai: Practical Deep Learning for Coders.
- Andrej Karpathy: "Neural Networks: Zero to Hero" e "Let's build GPT" (YouTube).
- Hugging Face LLM Course.
- Trilha de IA generativa do Google Cloud Skills Boost (atenção, transformers, encoder-decoder).

**Projeto:** um mini GPT treinado do zero em PyTorch sobre um texto em português, seguindo o Karpathy, com um README explicando cada parte com suas palavras.

**Pronto quando:** você explica a atenção com um desenho e uma conta, e sabe por que um modelo alucina.

## Módulo 18: Modelos abertos, fine-tuning e infraestrutura (IA, 6 semanas)

Objetivo: rodar, adaptar e servir modelos você mesmo, sem depender só de APIs.

**Modelos abertos e locais**

- Ecossistema Hugging Face: Hub, model cards, licenças, Transformers, Datasets.
- Famílias abertas: Llama, Mistral, Qwen, DeepSeek, Gemma (conferir as versões atuais).
- Rodar localmente: Ollama e LM Studio; requisitos de memória; quantização (GGUF, 4 e 8 bits).
- Servir em produção: vLLM e similares; API compatível com a da OpenAI.

**Fine-tuning**

- Quando vale (raramente) versus prompt e RAG (quase sempre).
- Preparação de dataset de instruções; qualidade acima de quantidade.
- LoRA e QLoRA; Unsloth para treinar em GPU gratuita do Google Colab ou do Kaggle.
- Avaliação antes e depois; noções de destilação e de preferência (DPO).

**Infraestrutura e LLMOps**

- Servir um modelo ou agente com FastAPI e Docker; deploy na AWS com Terraform (módulos 12 e 13) ou em Kubernetes (Módulo 15).
- Filas, cache, limites de custo, versionamento de prompts e modelos.
- Monitoramento em produção e rollback, com o que foi visto no Módulo 16.

**Fontes gratuitas**

- Hugging Face LLM Course e documentação do Transformers e do PEFT.
- Documentação do Ollama, do vLLM e do Unsloth (com notebooks prontos para Colab).
- Artigo do LoRA (Hu et al., 2021).

**Projeto:** um modelo pequeno ajustado com LoRA para uma tarefa específica (por exemplo, transformar histórias de usuário em casos de teste no seu formato), comparado com o modelo base e com um prompt bem feito, servido localmente por API.

**Pronto quando:** você decide com dados entre prompt, RAG e fine-tuning para um problema real.

## Módulo 19: Multimodal: imagem, voz e vídeo (IA, 3 semanas)

Objetivo: saber como funcionam e como usar por API os modelos que veem, ouvem, falam e geram mídia.

- **Visão:** entender imagens, gráficos, documentos e telas; OCR com LLMs; limites (contagem, detalhes pequenos).
- **Geração de imagem:** como funcionam os modelos de difusão; geração e edição por API; direitos de uso.
- **Voz:** transcrição (Whisper e similares), síntese de voz, agentes de voz em tempo real e latência.
- **Vídeo:** geração e compreensão de vídeo, noções e limites atuais.
- **Fontes:** documentação de visão e áudio da Anthropic, OpenAI e Gemini; Hugging Face Diffusion Course.
- **Projeto:** um agente que recebe a foto de uma tela com erro e devolve um relatório de bug estruturado, com passos e evidência.

## Módulo 20: Segurança, ética e regulação (IA, 2 semanas)

Objetivo: saber construir e usar IA de forma segura e responsável, e falar disso com propriedade.

- **Segurança de sistemas:** prompt injection, envenenamento de dados, vazamento de segredos, permissões mínimas para agentes, OWASP Top 10 para aplicações com LLM.
- **Alinhamento e segurança de modelos:** o que é alinhamento, Constitutional AI, políticas de escalonamento responsável, avaliações de capacidades perigosas.
- **Ética:** vieses, transparência, direitos autorais, impacto no trabalho.
- **Regulação:** LGPD aplicada a IA, AI Act da União Europeia e o projeto de lei de IA no Brasil (conferir o status atual).
- **Fontes:** OWASP Top 10 for LLM Applications; páginas de pesquisa e segurança da Anthropic, OpenAI e Google DeepMind; site da ANPD sobre IA e dados pessoais.
- **Projeto:** um relatório de red teaming do seu próprio agente do Módulo 9, com ataques, resultados e correções.

## Módulo 21: IA aplicada a QA (QA, 6 semanas)

Objetivo: juntar tudo na sua área e virar referência em IA para qualidade de software.

**IA para testar software**

- Geração de casos de teste a partir de requisitos e histórias de usuário, com critérios de aceite.
- Revisão de requisitos: ambiguidades, lacunas e riscos apontados pela IA.
- Dados de teste sintéticos e mascaramento de dados reais.
- Automação com Playwright ou Selenium assistida por agentes de código; testes que se recuperam de mudança de seletor (self-healing).
- Playwright MCP e agentes de navegador para testes exploratórios.
- Análise de falhas: classificar testes instáveis (flaky), agrupar erros, sugerir causa provável.
- Testes de API gerados a partir de contratos (OpenAPI).
- Agentes de QA no CI: revisão de PR com foco em testes e risco.

**Testar sistemas de IA (a fronteira nova de QA)**

- Estratégia de testes para chatbots, RAG e agentes: evals, golden datasets, regressão de prompt.
- Testes não determinísticos: múltiplas execuções, limiares, testes por propriedade.
- Red teaming e testes de segurança (prompt injection, vazamento, abuso de ferramentas).
- Monitoramento de qualidade em produção.

**Fontes gratuitas**

- Documentação do Playwright e do Playwright MCP.
- Material dos módulos 9 e 14 aplicado a QA.
- Comunidades e conferências de testes que discutem IA (conferir eventos atuais).

**Projeto final (capstone):** um "assistente de QA" que lê uma história de usuário, gera casos de teste, escreve os testes em Playwright, roda no CI, analisa as falhas e publica um relatório, com sua própria suíte de evals medindo a qualidade de cada etapa.

**Pronto quando:** você apresenta esse projeto numa entrevista ou palestra e responde perguntas técnicas sobre cada parte.

## Projeto principal: painel de execuções de teste

Uma API simples que registra e mostra resultados de execuções de teste, publicada como em produção. Ela junta os módulos de DevOps e cloud num único repositório, construído aos poucos dos módulos 6, 8, 10, 13 e 16.

| Parte | Tecnologia | Módulo |
| --- | --- | --- |
| Aplicação e testes | Python, FastAPI, pytest, Postgres | 6 |
| Empacotamento | Dockerfile multi-stage, docker-compose | 8 |
| Pipeline | GitHub Actions: lint, testes, build e publicação da imagem | 10 |
| Infraestrutura | AWS (VPC, EC2, RDS, S3, IAM) criada com Terraform | 12 e 13 |
| Deploy | Pipeline aplica o Terraform e atualiza a EC2; smoke test do Módulo 4 roda depois do deploy | 4, 10 e 13 |
| Monitoramento | Prometheus, Grafana, alertas, SLOs | 16 |

**Pronto quando:** um merge na `main` passa pelos testes, gera a imagem, atualiza a infraestrutura na AWS, roda o smoke test e aparece no painel do Grafana, sem nenhum passo manual. E você consegue destruir e recriar o ambiente inteiro em menos de 30 minutos.

## Projetos de portfólio

| Módulo | Área | Pasta | Projeto | O que prova |
| --- | --- | --- | --- | --- |
| 1 | Base | `modulo-01-cliente-http/` | Cliente HTTP robusto em Docker | Base de engenharia |
| 2 | DevOps | `modulo-02-saude-servidor/` | Script Bash de saúde do servidor e análise de log | Linux, Bash, logs |
| 3 | IA | `modulo-03-prompts/` | Biblioteca de 20 prompts comparados em 3 IAs | Domínio de prompt |
| 4 | DevOps | `modulo-04-checagem-rede/` | Checador de DNS, porta, HTTP e certificado TLS | Redes e diagnóstico |
| 5 | IA | `modulo-05-assistente-arquivos/` | Assistente de arquivos com JSON validado e 2 provedores | Uso de APIs e tool use |
| 6 | DevOps | `painel-testes/` | Projeto principal: API com pytest, feita com PRs | Git em equipe e automação |
| 7 | IA | `modulo-07-rag-docs/` | "Pergunte à documentação" com busca híbrida e 30 perguntas de avaliação | RAG medido |
| 8 | DevOps | `painel-testes/` | Projeto principal: API e Postgres em containers | Docker |
| 9 | IA | `modulo-09-agentes/` | Agente do zero, servidor MCP próprio, versão em LangGraph e Claude Agent SDK, OpenClaw com skill própria | Arquitetura de agentes |
| 10 | DevOps | `painel-testes/` | Projeto principal: pipeline que testa e publica a imagem | CI/CD com testes |
| 11 | IA | `modulo-11-codigo-automacao/` | App feito com Claude Code e fluxo n8n de relatório de testes | Produtividade com agentes e automação |
| 12 | Cloud | `modulo-12-aws-console/` | Deploy manual na AWS, documentado e destruído | Fundamentos de AWS |
| 13 | Cloud | `painel-testes/` | Projeto principal: infraestrutura em Terraform com plan no CI | Infraestrutura como código |
| 14 | IA | `modulo-14-evals/` | Suíte de evals no CI com LLM como juiz | Confiabilidade |
| 15 | Cloud | `modulo-15-kubernetes/` | A imagem do painel rodando em cluster local | Kubernetes |
| 16 | DevOps | `painel-testes/` | Projeto principal: métricas, painel, alerta e SLO | Observabilidade e SRE |
| 17 | IA | `modulo-17-mini-gpt/` | Mini GPT treinado do zero | Fundamentos |
| 18 | IA | `modulo-18-lora/` | Modelo ajustado com LoRA, servido localmente | Modelos abertos |
| 19 | IA | `modulo-19-multimodal/` | Agente que transforma print de erro em relatório de bug | Multimodal |
| 20 | IA | `modulo-20-red-teaming/` | Relatório de red teaming do próprio agente | Segurança |
| 21 | QA | `modulo-21-assistente-qa/` | Assistente de QA completo com evals | Especialização |

O projeto principal fica numa pasta só (`painel-testes/`) e ganha uma tag de versão a cada módulo em que cresce (`modulo-06`, `modulo-08`, `modulo-10`, `modulo-13` e `modulo-16`), para dar para ver a evolução no histórico. Se quiser destacá-lo no portfólio, ele pode virar um repositório próprio no GitHub a partir do Módulo 10.

## README de cada projeto

Todo projeto usa `templates/projeto-README.md` e precisa ter, no mínimo:

- **O que faz:** o problema, em 2 ou 3 frases.
- **Tecnologias:** a lista do que foi usado e para quê.
- **Como rodar:** os comandos completos, do clone até ver funcionando, incluindo como destruir o que foi criado na nuvem.
- **Resultados:** o que foi medido (testes passando, tempo de pipeline, custo na AWS).

Sem emojis, sem chaves ou senhas, e com um `.env.example` mostrando quais variáveis existem, sem os valores reais.

## Cuidados com custo na AWS

- Contas criadas a partir de julho de 2025 escolhem entre um plano gratuito (créditos iniciais, válido por até 6 meses) e um plano pago. Confira as regras atuais em aws.amazon.com/free antes de criar a conta.
- No primeiro dia: MFA no usuário root, alarme de orçamento com valor baixo e um usuário ou papel IAM para o dia a dia.
- Recursos que costumam surpreender na fatura: NAT gateway, load balancer, RDS ligado sem uso, IP público e snapshots esquecidos. Prefira instâncias pequenas do plano gratuito.
- Termine cada sessão com `terraform destroy` (ou apagando pelo console no Módulo 12) e confira o painel de custos.
- Chaves de acesso nunca entram no Git. Use `.env` local (fora do Git), `aws configure` ou login pelo IAM Identity Center, e GitHub Secrets ou OIDC no pipeline.

## Leituras essenciais

| Leitura | Tipo | Ano | Módulo |
| --- | --- | --- | --- |
| Guia de engenharia de prompt (Anthropic, OpenAI, Google) | Documentação | atual | 3 |
| Language Models are Few-Shot Learners (GPT-3) | Artigo | 2020 | 3 |
| Chain-of-Thought Prompting Elicits Reasoning | Artigo | 2022 | 3 |
| Documentação das APIs e OpenAI Cookbook | Documentação | atual | 5 |
| Retrieval-Augmented Generation (Lewis et al.) | Artigo | 2020 | 7 |
| Contextual Retrieval (blog da Anthropic) | Artigo técnico | 2024 | 7 |
| ReAct: Synergizing Reasoning and Acting | Artigo | 2022 | 9 |
| Toolformer | Artigo | 2023 | 9 |
| Building Effective Agents (blog da Anthropic) | Artigo técnico | 2024 | 9 |
| Especificação do Model Context Protocol | Documentação | atual | 9 |
| Boas práticas do Claude Code (blog da Anthropic) | Artigo técnico | atual | 11 |
| Guias de evals da Anthropic e da OpenAI | Documentação | atual | 14 |
| OWASP Top 10 for LLM Applications | Guia | atual | 14 e 20 |
| Attention Is All You Need | Artigo | 2017 | 17 |
| Training language models to follow instructions (InstructGPT) | Artigo | 2022 | 17 |
| Constitutional AI | Artigo | 2022 | 17 e 20 |
| Scaling Laws (Kaplan) e Chinchilla | Artigos | 2020 e 2022 | 17 |
| LoRA: Low-Rank Adaptation | Artigo | 2021 | 18 |
| Denoising Diffusion Probabilistic Models | Artigo | 2020 | 19 |

Os artigos estão disponíveis de graça no arXiv; os textos técnicos, nos blogs de engenharia e pesquisa das empresas.

## Como se manter atualizado

Reserve 2 horas por semana só para novidades; o resto do tempo segue o plano.

- **Fontes primárias:** blogs de notícias, engenharia e pesquisa da Anthropic, OpenAI, Google DeepMind e Meta AI; changelogs das APIs e do Claude Code.
- **Curadoria:** newsletter The Batch (DeepLearning.AI), blog do Simon Willison, podcast Latent Space, página Daily Papers da Hugging Face.
- **Código:** repositórios em alta no GitHub sobre agentes e LLMs.
- **Comunidades:** fóruns e Discords oficiais da Anthropic, OpenAI, Hugging Face e n8n; comunidades brasileiras de IA e de QA.
- **Ritual semanal:** escolha uma novidade, teste em 30 minutos e anote em uma linha se vale entrar no seu trabalho.

## Rotina semanal (sugestão)

- **Segunda a sexta (1 a 2 horas):** 30 minutos de curso ou leitura, o resto construindo o projeto do módulo.
- **Sábado (2 a 3 horas):** avançar o projeto e publicar o progresso no GitHub.
- **Domingo:** descanso, ou 2 horas de novidades da semana.
- **A cada 2 semanas:** revisão com o tutor, um quiz curto e ajuste do ritmo.
- **Fim de cada módulo:** README do projeto e um post no LinkedIn sobre o que aprendeu.

**Semana corrida?** Normal. Volte com uma sessão curta; o roteiro espera. Tópicos opcionais ficam a seu critério, mas o projeto do módulo fica: é ele que transforma estudo em habilidade.
