---
tipo: plano
status: referência (só alterar quando você pedir)
atualizado: 2026-10-23
---

# Plano de estudos: IA do zero ao avançado, com DevOps e cloud

## Como usar este plano

O estudo segue um roteiro único de 21 blocos: as 12 fases de IA deste arquivo e as 9 etapas de DevOps e cloud de [[trilha-devops]], intercaladas para que cada bloco prepare o seguinte. Cada bloco tem objetivo, tópicos, fontes gratuitas, um projeto e um critério de "pronto". Não há prazo fixo: o roteiro anda na velocidade em que você aprende (veja "Ritmo").

- **Nomes:** "Fase" é um bloco de IA (Fase 0 a 11); "Etapa" é um bloco de DevOps e cloud (Etapa 1 a 9). O detalhe das fases está aqui; o das etapas, em [[trilha-devops]].

- **Nível de partida:** iniciante absoluto em programação. A Fase 0 foi reescrita para ensinar terminal, Python e Git do zero antes de qualquer coisa de IA; as fases seguintes contam com isso.
- **Ordem:** prática antes da teoria profunda. Você constrói com APIs e agentes (fases 2 a 6) antes de estudar matemática e redes neurais (fase 7), porque a teoria fica mais clara depois de ver o modelo errar na prática.
- **Regra 70/30:** 70% do tempo construindo, 30% assistindo ou lendo.
- **Um projeto por bloco:** publicado no GitHub, com um post curto no LinkedIn sobre o que aprendeu. Os projetos de IA e de DevOps se conectam (veja "Como os projetos se conectam").
- **Com o tutor:** em cada tópico, peça explicação, exercícios, revisão de código ou resumo de artigo.
- **Atualização:** ferramentas e cursos mudam rápido. Itens marcados "(conferir)" são verificados quando você chegar neles.
- **Custo:** todas as fontes são gratuitas. O único gasto possível é o uso de APIs pagas por uso, evitável com cotas grátis e modelos locais (Ollama).

## Roteiro

A ordem abaixo é a ordem de estudo: fases de IA (detalhadas neste arquivo) e etapas de DevOps e cloud (detalhadas em [[trilha-devops]]) num caminho só. Um bloco só começa quando o anterior estiver com o projeto pronto e o "pronto quando" atendido. A estimativa considera 1 a 2 horas por dia e dá só uma noção do tamanho de cada bloco; não é prazo.

| Ordem | Bloco | Tema | Estimativa | Por que aqui |
| --- | --- | --- | --- | --- |
| 1 | Fase 0 | Base técnica | 6 sem | Ponto de partida: terminal, Python, Git, HTTP e Docker do zero |
| 2 | Etapa 1 | Linux e terminal | 3 sem | Aprofunda o terminal da Fase 0 enquanto está fresco; servidores e agentes rodam em Linux |
| 3 | Fase 1 | Prompt e uso avançado | 4 sem | Não depende de infraestrutura e traz IA logo no começo |
| 4 | Etapa 2 | Redes | 2 sem | Prepara a Fase 2: chamar APIs exige entender DNS, HTTPS, portas e timeouts |
| 5 | Fase 2 | APIs de modelos | 4 sem | Usa o HTTP da Fase 0 e as redes da Etapa 2 |
| 6 | Etapa 3 | Git e scripting | 3 sem | Os projetos crescem: branches, PRs, pytest e o início do projeto principal de DevOps |
| 7 | Fase 3 | RAG e dados | 4 sem | Bancos vetoriais sobem com o Docker básico da Fase 0 |
| 8 | Etapa 4 | Docker | 3 sem | A Fase 4 roda o OpenClaw isolado em container |
| 9 | Fase 4 | Agentes, MCP e OpenClaw | 6 sem | Usa Linux (Etapa 1) e Docker (Etapa 4) para isolar agentes |
| 10 | Etapa 5 | CI/CD com GitHub Actions | 2 sem | A Fase 5 usa agentes de código no CI e a Fase 6 roda evals no pipeline |
| 11 | Fase 5 | Agentes de código e automação | 4 sem | Claude Code em modo headless no pipeline da Etapa 5; n8n em Docker |
| 12 | Etapa 6 | AWS | 4 sem | Primeira nuvem, feita à mão antes de automatizar |
| 13 | Etapa 7 | Terraform | 3 sem | Fecha o deploy do projeto principal de DevOps |
| 14 | Fase 6 | Evals e confiabilidade | 4 sem | Suíte de evals rodando no pipeline da Etapa 5 |
| 15 | Etapa 8 | Kubernetes | 4 sem | Docker já firme; prepara a infraestrutura da Fase 8 |
| 16 | Etapa 9 | Observabilidade e SRE | 3 sem | Completa a observabilidade de IA da Fase 6 com métricas, alertas e SLOs |
| 17 | Fase 7 | Fundamentos de ML e LLMs por dentro | 12 sem | Bloco teórico longo, com a base de engenharia já completa |
| 18 | Fase 8 | Modelos abertos e fine-tuning | 6 sem | Serve modelos com Docker, Kubernetes, Terraform e monitoramento |
| 19 | Fase 9 | Multimodal | 3 sem | Usa as APIs e os agentes das fases anteriores |
| 20 | Fase 10 | Segurança, ética e regulação | 2 sem | Red teaming dos agentes e revisão de segurança da infraestrutura |
| 21 | Fase 11 | IA aplicada a QA | 6 sem | Projeto final no CI, com deploy e monitoramento |

## Ritmo

O ritmo é seu. Não há prazo nem meta de velocidade: o objetivo é continuar estudando porque gosta, não cumprir um calendário.

- **Continuidade acima de velocidade:** uma sessão curta vale mais que nenhuma. Se o tempo do dia for pouco, o tutor propõe algo que caiba (uma revisão, um exercício, um trecho de documentação). Depois de uma pausa, a volta começa com uma revisão leve, sem cobrança.
- **O que fica registrado:** sessões, minutos e tópicos concluídos, na seção "Ritmo" de `progresso.md`. Serve para planejar o tamanho de cada sessão e para você ver o caminho já feito, não para medir atraso. Um tópico está concluído quando você fez o exercício sem receber a resposta pronta e, se houve quiz, acertou pelo menos 4 de 5.
- **Dentro da sessão:** se você acerta de primeira, o tutor avança e oferece desafios; se erra o mesmo ponto duas vezes, divide o tópico em partes menores e passa mais exercícios. O projeto e o "pronto quando" de cada bloco nunca são pulados.
- **Sem previsão de término:** as estimativas do roteiro dão só uma noção do tamanho de cada bloco. Ninguém compara o seu avanço com datas.
- **Revisão quinzenal:** olha o que você aprendeu e o que precisa voltar; se quiser, ajusta o que vem a seguir.

## Como os projetos se conectam

| Projeto | Usa | É usado por |
| --- | --- | --- |
| Fase 0: cliente HTTP em Docker | | Etapa 2: a checagem de rede reaproveita o tratamento de erros e retries |
| Etapas 3 a 9: painel de execuções de teste (projeto principal de DevOps) | Etapas 1 e 2 | Fases 6 e 11: a mesma estrutura de pipeline e deploy |
| Fase 4: OpenClaw com skill própria | Etapas 1 e 4: Linux e container isolado | Fase 10: red teaming |
| Fase 5: app feito com Claude Code | Etapa 5: pipeline com testes | |
| Fase 6: suíte de evals no CI | Etapa 5: GitHub Actions | Etapa 9: métricas de qualidade no Grafana |
| Fase 8: modelo servido por API | Etapas 4, 7, 8 e 9 | Fase 11 |
| Fase 11: assistente de QA | Etapas 5, 7 e 9: CI, deploy e monitoramento | |

## Fase 0: Base técnica (6 semanas)

Objetivo: ter a caixa de ferramentas de quem constrói com IA, partindo do zero absoluto. O plano assume iniciante: sem experiência prévia em programação, Python, Git ou Docker. O conhecimento de QA entra como ponte nos exemplos (testar uma API, achar bug, pensar em cenários), mas nenhuma ferramenta é tida como conhecida.

**Tópicos (nesta ordem; cada um só começa quando o anterior estiver firme)**

1. **Terminal básico:** o que é o terminal, abrir, navegar entre pastas, criar e apagar arquivos, rodar comandos, ler mensagens de erro. Aprofundado na Etapa 1.
2. **Python do zero:** instalar e rodar, variáveis, texto, números, listas e dicionários, `if`, `for`, funções, ler e escrever arquivos, erros e `try/except`.
3. **Git e GitHub básico:** o que é versionar, `init`, `add`, `commit`, `push`, ler o histórico, branches, pull request. Aprofundado na Etapa 3.
4. **Python para IA:** ambientes virtuais (`uv`, venv), instalar bibliotecas, JSON e CSV, variáveis de ambiente e segredos (`.env`), tipagem, dataclasses e Pydantic, `async/await`.
5. **HTTP e APIs:** o que é uma API, métodos, status, headers, autenticação por chave, JSON, paginação, rate limit, retries com backoff, webhooks. O lado de redes e servidor vem na Etapa 2.
6. **Docker:** o que é um container, imagens, volumes, `docker compose` (vai rodar n8n, bancos vetoriais e modelos locais). Dockerfile próprio e boas práticas vêm na Etapa 4.
7. **SQL básico:** `SELECT`, `JOIN`, `GROUP BY`; base para bancos vetoriais como o pgvector.
8. **Jupyter Notebooks:** para experimentos rápidos.
9. **TypeScript (opcional):** a segunda linguagem do AI engineer, útil para interfaces e agentes em Node. Fica a seu critério.

**Fontes gratuitas:** Kaggle Learn (Python, Pandas, SQL); tutorial oficial do Python em português (docs.python.org/pt-br/3/tutorial); documentação do `uv` (docs.astral.sh/uv); documentação do Git (git-scm.com/book/pt-br) e do Docker (docs.docker.com/get-started).

**Projeto:** um script em Python que consome uma API pública, trata erros e retries, e salva o resultado em JSON, rodando dentro de um container Docker.

**Pronto quando:** você sobe um serviço com docker compose e escreve um cliente HTTP robusto sem consultar tutorial.

## Fase 1: Usuário avançado e engenharia de prompt (4 semanas)

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

## Fase 2: Construir com APIs de modelos (4 semanas)

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

## Fase 3: RAG, embeddings e dados (4 semanas)

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

## Fase 4: Agentes, MCP, frameworks e OpenClaw (6 semanas)

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

## Fase 5: Agentes de código e automação (4 semanas)

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

## Fase 6: Evals, observabilidade e confiabilidade (4 semanas)

Objetivo: provar com números que um sistema de IA funciona. Evals são os testes unitários da engenharia de IA, e é aqui que seu background de QA vira vantagem.

**Tópicos**

- Golden datasets: conjuntos de casos com resposta esperada, versionados.
- Tipos de avaliação: por código (regras, regex, schema), por comparação, por humano e LLM como juiz (LLM-as-judge), com calibração do juiz.
- Métricas: acurácia, fidelidade, relevância, taxa de alucinação, sucesso de tarefa em agentes, custo e latência.
- Testes de regressão de prompt e de modelo: um alarme quando a nota cai.
- Avaliação de agentes: trajetória (ferramentas certas na ordem certa), não só a resposta final.
- Observabilidade: tracing de chamadas, logs de ferramentas, custo por requisição. A parte de infraestrutura (Prometheus, Grafana, alertas, SLO) vem na Etapa 9.
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

**Projeto:** uma suíte de evals no CI para o projeto da Fase 3 ou 4, com golden dataset, LLM como juiz calibrado, tracing e um relatório de regressão a cada mudança de prompt.

**Pronto quando:** você mostra um gráfico de qualidade antes e depois de uma mudança e explica uma falha silenciosa que os evals pegaram.

## Fase 7: Fundamentos de ML, deep learning e LLMs por dentro (12 semanas)

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

## Fase 8: Modelos abertos, fine-tuning e infraestrutura (6 semanas)

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

- Servir um modelo ou agente com FastAPI e Docker; deploy na AWS com Terraform (Etapas 6 e 7) ou em Kubernetes (Etapa 8).
- Filas, cache, limites de custo, versionamento de prompts e modelos.
- Monitoramento em produção e rollback, com o que foi visto na Etapa 9.

**Fontes gratuitas**

- Hugging Face LLM Course e documentação do Transformers e do PEFT.
- Documentação do Ollama, do vLLM e do Unsloth (com notebooks prontos para Colab).
- Artigo do LoRA (Hu et al., 2021).

**Projeto:** um modelo pequeno ajustado com LoRA para uma tarefa específica (por exemplo, transformar histórias de usuário em casos de teste no seu formato), comparado com o modelo base e com um prompt bem feito, servido localmente por API.

**Pronto quando:** você decide com dados entre prompt, RAG e fine-tuning para um problema real.

## Fase 9: Multimodal: imagem, voz e vídeo (3 semanas)

Objetivo: saber como funcionam e como usar por API os modelos que veem, ouvem, falam e geram mídia.

- **Visão:** entender imagens, gráficos, documentos e telas; OCR com LLMs; limites (contagem, detalhes pequenos).
- **Geração de imagem:** como funcionam os modelos de difusão; geração e edição por API; direitos de uso.
- **Voz:** transcrição (Whisper e similares), síntese de voz, agentes de voz em tempo real e latência.
- **Vídeo:** geração e compreensão de vídeo, noções e limites atuais.
- **Fontes:** documentação de visão e áudio da Anthropic, OpenAI e Gemini; Hugging Face Diffusion Course.
- **Projeto:** um agente que recebe a foto de uma tela com erro e devolve um relatório de bug estruturado, com passos e evidência.

## Fase 10: Segurança, ética e regulação (2 semanas)

Objetivo: saber construir e usar IA de forma segura e responsável, e falar disso com propriedade.

- **Segurança de sistemas:** prompt injection, envenenamento de dados, vazamento de segredos, permissões mínimas para agentes, OWASP Top 10 para aplicações com LLM.
- **Alinhamento e segurança de modelos:** o que é alinhamento, Constitutional AI, políticas de escalonamento responsável, avaliações de capacidades perigosas.
- **Ética:** vieses, transparência, direitos autorais, impacto no trabalho.
- **Regulação:** LGPD aplicada a IA, AI Act da União Europeia e o projeto de lei de IA no Brasil (conferir o status atual).
- **Fontes:** OWASP Top 10 for LLM Applications; páginas de pesquisa e segurança da Anthropic, OpenAI e Google DeepMind; site da ANPD sobre IA e dados pessoais.
- **Projeto:** um relatório de red teaming do seu próprio agente da Fase 4, com ataques, resultados e correções.

## Fase 11: IA aplicada a QA (6 semanas)

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
- Material das fases 4 e 6 aplicado a QA.
- Comunidades e conferências de testes que discutem IA (conferir eventos atuais).

**Projeto final (capstone):** um "assistente de QA" que lê uma história de usuário, gera casos de teste, escreve os testes em Playwright, roda no CI, analisa as falhas e publica um relatório, com sua própria suíte de evals medindo a qualidade de cada etapa.

**Pronto quando:** você apresenta esse projeto numa entrevista ou palestra e responde perguntas técnicas sobre cada parte.

## Leituras essenciais

| Leitura | Tipo | Ano | Fase |
| --- | --- | --- | --- |
| Guia de engenharia de prompt (Anthropic, OpenAI, Google) | Documentação | atual | 1 |
| Language Models are Few-Shot Learners (GPT-3) | Artigo | 2020 | 1 |
| Chain-of-Thought Prompting Elicits Reasoning | Artigo | 2022 | 1 |
| Documentação das APIs e OpenAI Cookbook | Documentação | atual | 2 |
| Retrieval-Augmented Generation (Lewis et al.) | Artigo | 2020 | 3 |
| Contextual Retrieval (blog da Anthropic) | Artigo técnico | 2024 | 3 |
| ReAct: Synergizing Reasoning and Acting | Artigo | 2022 | 4 |
| Toolformer | Artigo | 2023 | 4 |
| Building Effective Agents (blog da Anthropic) | Artigo técnico | 2024 | 4 |
| Especificação do Model Context Protocol | Documentação | atual | 4 |
| Boas práticas do Claude Code (blog da Anthropic) | Artigo técnico | atual | 5 |
| Guias de evals da Anthropic e da OpenAI | Documentação | atual | 6 |
| OWASP Top 10 for LLM Applications | Guia | atual | 6 e 10 |
| Attention Is All You Need | Artigo | 2017 | 7 |
| Training language models to follow instructions (InstructGPT) | Artigo | 2022 | 7 |
| Constitutional AI | Artigo | 2022 | 7 e 10 |
| Scaling Laws (Kaplan) e Chinchilla | Artigos | 2020 e 2022 | 7 |
| LoRA: Low-Rank Adaptation | Artigo | 2021 | 8 |
| Denoising Diffusion Probabilistic Models | Artigo | 2020 | 9 |

Os artigos estão disponíveis de graça no arXiv; os textos técnicos, nos blogs de engenharia e pesquisa das empresas.

## Como se manter atualizado

Reserve 2 horas por semana só para novidades; o resto do tempo segue o plano.

- **Fontes primárias:** blogs de notícias, engenharia e pesquisa da Anthropic, OpenAI, Google DeepMind e Meta AI; changelogs das APIs e do Claude Code.
- **Curadoria:** newsletter The Batch (DeepLearning.AI), blog do Simon Willison, podcast Latent Space, página Daily Papers da Hugging Face.
- **Código:** repositórios em alta no GitHub sobre agentes e LLMs.
- **Comunidades:** fóruns e Discords oficiais da Anthropic, OpenAI, Hugging Face e n8n; comunidades brasileiras de IA e de QA.
- **Ritual semanal:** escolha uma novidade, teste em 30 minutos e anote em uma linha se vale entrar no seu trabalho.

## Projetos de portfólio

| Fase | Projeto | O que prova |
| --- | --- | --- |
| 0 | Cliente HTTP robusto em Docker | Base de engenharia |
| 1 | Biblioteca de 20 prompts comparados em 3 IAs | Domínio de prompt |
| 2 | Assistente de arquivos com JSON validado e 2 provedores | Uso de APIs e tool use |
| 3 | "Pergunte à documentação" com busca híbrida e 30 perguntas de avaliação | RAG medido |
| 4 | Agente do zero, servidor MCP próprio, versão em LangGraph e Claude Agent SDK, OpenClaw com skill própria | Arquitetura de agentes |
| 5 | App feito com Claude Code e fluxo n8n de relatório de testes | Produtividade com agentes e automação |
| 6 | Suíte de evals no CI com LLM como juiz | Confiabilidade |
| 7 | Mini GPT treinado do zero | Fundamentos |
| 8 | Modelo ajustado com LoRA, servido localmente | Modelos abertos |
| 9 | Agente que transforma print de erro em relatório de bug | Multimodal |
| 10 | Relatório de red teaming do próprio agente | Segurança |
| 11 | Assistente de QA completo com evals | Especialização |

Os projetos das etapas de DevOps e cloud estão em [[trilha-devops]], na seção "Projetos de portfólio". Cada projeto ganha um README com o problema, as tecnologias, como rodar, os resultados medidos e o que você faria diferente.

## Rotina semanal (sugestão)

- **Segunda a sexta (1 a 2 horas):** 30 minutos de curso ou leitura, o resto construindo o projeto do bloco.
- **Sábado (2 a 3 horas):** avançar o projeto e publicar o progresso no GitHub.
- **Domingo:** descanso, ou 2 horas de novidades da semana.
- **A cada 2 semanas:** revisão com o tutor, um quiz curto e ajuste do ritmo.
- **Fim de cada bloco:** README do projeto e um post no LinkedIn sobre o que aprendeu.

**Semana corrida?** Normal. Volte com uma sessão curta; o roteiro espera. Tópicos opcionais ficam a seu critério, mas o projeto do bloco fica: é ele que transforma estudo em habilidade.
