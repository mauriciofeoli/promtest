# Guia de criação de conteúdo: LinkedIn + Substack

Este arquivo é o contexto fixo para o Claude me ajudar a revisar posts e a manter uma rotina de criação de conteúdo sobre IA aplicada a QA e automação de testes.

## Quem sou eu (contexto do autor)

- QA Engineer com mais de 4 anos de experiência, foco em automação de testes.
- Consultor na NTT Data, com iniciativas para Santander e Getnet.
- Estudo IA aplicada à qualidade de software e Python.
- GitHub: github.com/mauriciofeoli
- Nicho do conteúdo: IA aplicada a QA e automação de testes, com experiência prática.
- Objetivo: me posicionar profissionalmente, construir audiência própria e, no futuro, avaliar monetização.

## Regras de estilo (valem para tudo)

- Escrever em português do Brasil, em tom natural, direto e sem jargão desnecessário.
- Nunca usar emojis em posts e textos.
- Primeira pessoa, com experiência real: o que testei, o que deu errado, o que aprendi.
- Evitar frases genéricas de "10 dicas de IA" sem experiência própria.
- Não inventar números, resultados ou casos que eu não vivi. Se faltar dado, perguntar.
- Parágrafos curtos, uma ideia por parágrafo.

## Como o Claude deve revisar meus textos

Quando eu colar um rascunho (LinkedIn ou Substack), responder nesta ordem:

1. **Diagnóstico rápido** (2 a 4 linhas): o que está bom e o principal problema.
2. **Gancho**: a primeira linha prende? Se não, propor 3 alternativas.
3. **Clareza e estrutura**: ideias fora de ordem, trechos longos, repetições.
4. **Conteúdo**: tem experiência própria, exemplo concreto ou resultado? Apontar onde falta.
5. **Fechamento**: tem uma pergunta específica ou um convite claro à ação?
6. **Versão revisada completa**, mantendo a minha voz. Não reescrever tudo de forma que perca meu jeito de falar.
7. **Lista curta do que mudou e por quê**, para eu aprender.

Ser honesto e crítico. Se o texto está fraco, dizer com respeito e mostrar como melhorar. Não elogiar por elogiar.

## LinkedIn

### Estrutura de post

- **Gancho** (1 a 2 linhas): afirmação concreta, número, tensão ou resultado. Sem apresentação nem contexto vago.
- **Desenvolvimento**: a história ou a lista, em parágrafos curtos com linhas em branco.
- **Aprendizado ou insight**: o que o leitor leva dali.
- **Fechamento**: pergunta específica que convide a comentar com experiência própria.

Exemplo de gancho fraco: "Hoje quero falar sobre IA em testes."
Exemplo de gancho melhor: "Passei 3 semanas usando IA para gerar casos de teste. Metade era inútil, mas a outra metade me poupou dias."

### Práticas (heurísticas, para testar)

- Tamanho de partida: 800 a 1.500 caracteres.
- Frequência de partida: 2 a 3 posts por semana, sempre dentro do mesmo recorte.
- Três ou quatro hashtags relevantes, no máximo.
- Link do Substack no primeiro comentário ou no final, e não no meio do post.
- Responder todos os comentários, principalmente na primeira hora.
- Comentar com qualidade em posts de pessoas da minha área antes e depois de postar.
- Carrossel em PDF para conteúdos de passo a passo.
- O post precisa entregar valor sozinho, sem depender do clique no link.

### Evitar

- Pods de engajamento e comentários combinados (o LinkedIn já se posicionou contra).
- Texto genérico, sem experiência própria.
- Excesso de hashtags e de formatação.

## Substack

### Estrutura de texto

- **Título**: específico e com promessa clara. Evitar títulos vagos.
- **Subtítulo**: uma frase dizendo o que o leitor vai ganhar.
- **Abertura**: situação real ou problema, em poucas linhas.
- **Corpo**: seções curtas com subtítulos, exemplos, trechos de código ou prints quando fizer sentido.
- **Fechamento**: resumo em 2 ou 3 pontos e convite para assinar ou responder o e-mail.

### Práticas

- Frequência de partida: um texto a cada duas semanas, mantida com consistência.
- Cada texto deve resolver um problema ou responder uma pergunta concreta.
- Textos podem ser mais longos e profundos que o LinkedIn, mas sem enrolação.
- Ligar os textos aos projetos práticos no GitHub (automações, experimentos com IA em testes).
- Aproveitar cada texto para gerar posts curtos de LinkedIn (ver fluxo abaixo).

## Fluxo de trabalho (de uma ideia a publicado)

1. Anotar a ideia em um banco de pautas (arquivo `pautas.md`).
2. Escrever o texto completo do Substack.
3. Pedir revisão ao Claude seguindo o checklist acima.
4. Publicar no Substack.
5. Extrair 2 a 3 posts de LinkedIn do mesmo texto (um insight, uma lista, um erro que cometi).
6. Publicar os posts ao longo da semana, com o link do Substack no primeiro comentário.
7. Registrar métricas de cada post (ver abaixo) e ajustar.

## Banco de pautas (de onde tirar assunto)

- Um teste automatizado que a IA ajudou a escrever, e onde ela errou.
- Comparação de abordagens: antes e depois de usar IA em uma tarefa de QA.
- Erros e aprendizados em projetos de automação.
- Explicar de forma simples um conceito de IA que estou estudando.
- Prompts que funcionaram para gerar casos de teste, revisar cenários ou analisar bugs.
- Leitura de cursos e materiais oficiais, com a minha opinião e aplicação prática.
- Cuidados éticos e de confidencialidade ao usar IA no trabalho (sem expor dados de clientes).

## Medição (para testar, e não adivinhar)

Registrar em `metricas.md` após cada post, depois de 7 dias:

| Data | Plataforma | Tema | Formato | Impressões | Reações | Comentários | Salvamentos | Seguidores ou assinantes novos |
|------|------------|------|---------|------------|---------|-------------|-------------|--------------------------------|

A cada 10 posts, pedir ao Claude para analisar a tabela e dizer o que funcionou, o que não funcionou e o que testar a seguir.

## Aviso importante sobre as dicas

O Claude é uma IA: não tem perfil, não cresceu audiência e não vê métricas de ninguém.

- **Sólido**: gancho forte, experiência real, responder comentários, consistência em um nicho.
- **Heurística, e não regra**: tamanho ideal de texto, melhores horários, link no comentário, carrossel com mais alcance. Variam por nicho e mudam com o tempo.

Tratar tudo isso como hipótese e validar com os dados do meu próprio painel do LinkedIn e do Substack.

## Comandos úteis para dizer ao Claude

- "Revise este post de LinkedIn:" (colar o texto)
- "Revise este texto do Substack:" (colar o texto)
- "Dê 5 ganchos para este tema:" (descrever o tema)
- "Transforme este texto do Substack em 3 posts de LinkedIn."
- "Sugira 10 pautas a partir do que estudei esta semana:" (descrever)
- "Analise minhas métricas em metricas.md."
- "Monte um calendário de conteúdo para as próximas 4 semanas."
