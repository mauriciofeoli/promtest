---
tipo: plano
status: referência (só alterar quando você pedir)
atualizado: 2026-10-23
---

# Trilha de DevOps e cloud: do terminal à produção observada

## Como usar esta trilha

São 9 etapas em cerca de 27 semanas, estudando 1 a 2 horas por dia, só com fontes gratuitas. Cada etapa tem objetivo, tópicos, fontes, um projeto pequeno e um critério de "pronto". Os projetos vão crescendo até formar o projeto principal: uma aplicação em Docker, publicada na AWS com Terraform, com pipeline de CI/CD e monitoramento.

- **Trilha paralela:** ela não substitui o [[plano]] de IA. As mesmas regras valem aqui: um projeto por etapa, prática antes da teoria (70/30) e só avançar com o "pronto quando" atendido.
- **Ordem:** cada etapa usa a anterior. Kubernetes só entra depois de Docker estar firme.
- **Sem duplicar a Fase 0:** terminal básico, Python do zero, Git básico e Docker básico já estão na Fase 0 do plano de IA. Aqui você parte do que aprendeu lá e vai mais fundo, com foco em servidor, automação e produção.
- **Atualização:** ferramentas, preços e cursos mudam rápido. Itens marcados "(conferir)" são verificados quando você chegar neles.
- **Custo:** os estudos são gratuitos. O único gasto possível é a AWS (etapas 6, 7 e no projeto principal). Veja "Cuidados com custo na AWS" antes de criar a conta.

## Como encaixar com o plano de IA

Estudar as duas trilhas ao mesmo tempo, no mesmo 1 a 2 horas por dia, dobra o prazo de cada uma. Escolha uma destas formas e avise o tutor:

1. **Depois da Fase 0 de IA:** a Fase 0 já cobre o começo das etapas 1, 3 e 4. É a forma mais natural de emendar.
2. **Intercalada:** uma semana de IA, uma de DevOps. É mais lenta, mas mantém as duas vivas.
3. **Antes de IA:** a trilha inteira primeiro, se o objetivo de curto prazo for uma vaga de DevOps, SRE ou QA de infraestrutura.

## Cronograma

| Etapa | Tema | Duração | Semanas |
| --- | --- | --- | --- |
| 1 | Linux e terminal | 3 sem | 1 a 3 |
| 2 | Redes | 2 sem | 4 a 5 |
| 3 | Git e scripting | 3 sem | 6 a 8 |
| 4 | Docker | 3 sem | 9 a 11 |
| 5 | CI/CD com GitHub Actions | 2 sem | 12 a 13 |
| 6 | AWS | 4 sem | 14 a 17 |
| 7 | Terraform | 3 sem | 18 a 20 |
| 8 | Kubernetes | 4 sem | 21 a 24 |
| 9 | Observabilidade e SRE | 3 sem | 25 a 27 |

## Etapa 1: Linux e terminal (3 semanas)

Objetivo: se virar num servidor Linux só pelo terminal, sem interface gráfica. Quase toda nuvem roda Linux.

**Tópicos**

- **Ambiente:** WSL2 com Ubuntu no Windows (o Linux de verdade, dentro do seu computador). Diferença entre o PowerShell da Fase 0 e o Bash.
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

**Projeto:** `devops-1-saude-servidor`. Um script Bash que verifica a saúde da máquina (disco, memória, processos que mais consomem) e analisa um arquivo de log (quantos erros, quais os mais frequentes), gera um relatório em texto e roda sozinho pelo `cron`.

**Pronto quando:** você entra numa máquina por SSH com chave, acha por que um serviço caiu lendo os logs e escreve um script Bash que falha de forma clara quando algo dá errado.

## Etapa 2: Redes (2 semanas)

Objetivo: entender o caminho de uma requisição, do navegador até o servidor, e saber diagnosticar onde ela quebra.

**Tópicos**

- **TCP/IP:** endereço IP, máscara e sub-rede (notação CIDR, como `10.0.0.0/16`), IP público e privado, TCP versus UDP, o aperto de mão de 3 vias.
- **Portas:** o que é uma porta, as mais comuns (22, 80, 443, 5432), `ss -tulpn` para ver o que está escutando.
- **DNS:** como um nome vira IP, registros A, CNAME, MX e TXT, TTL e cache, `dig` e `nslookup`.
- **HTTP e HTTPS:** métodos, status, headers, `curl -v`; TLS, certificados e o que o cadeado garante. A Fase 0 já cobre HTTP do ponto de vista de quem consome uma API; aqui o foco é o lado do servidor e o diagnóstico.
- **Load balancer:** distribuir tráfego entre servidores, camada 4 versus camada 7, health check.
- **Firewall:** regras de entrada e saída, `ufw` no Linux, a ideia que a AWS usa nos security groups.
- **Diagnóstico:** `ping`, `traceroute`, `curl`, `dig`, `nc` (netcat). Ordem de investigação: o nome resolve? a porta abre? o serviço responde?

**Fontes gratuitas**

- Cloudflare Learning Center (cloudflare.com/learning): DNS, HTTP, TLS, load balancing e firewall, com textos curtos.
- MDN Web Docs sobre HTTP (developer.mozilla.org/pt-BR/docs/Web/HTTP).
- Aulas de redes do "The Missing Semester" e manual do `dig` e do `curl`.

**Projeto:** `devops-2-checagem-rede`. Um script em Python que recebe uma lista de sites e, para cada um, verifica se o DNS resolve, se a porta abre, o status HTTP, o tempo de resposta e quantos dias faltam para o certificado TLS vencer. Gera um relatório e termina com código de erro se algo falhar. Esse script vira o smoke test pós-deploy do projeto principal.

**Pronto quando:** dado "o site não abre", você descobre em poucos minutos se o problema é DNS, rede, porta, certificado ou a aplicação.

## Etapa 3: Git e scripting (3 semanas)

Objetivo: trabalhar como numa equipe de engenharia: histórico limpo, branches, pull requests e scripts que automatizam tarefas repetitivas.

**Tópicos**

- **Git do dia a dia** (além do básico da Fase 0): branches e `merge`, conflitos e como resolver, `rebase` simples, `git stash`, desfazer com segurança (`restore`, `revert`, `reset`), `.gitignore`, tags de versão.
- **GitHub:** pull request com revisão, issues, proteção da branch `main`, mensagens de commit claras.
- **Python para automação:** ler argumentos (`argparse`), variáveis de ambiente, chamar comandos do sistema (`subprocess`), ler e escrever JSON e CSV, chamar APIs (`requests` ou `httpx`), logs com `logging`.
- **Testes do próprio script:** `pytest` para funções de automação; o seu lado QA entra aqui.
- **Bash ou Python:** Bash para colar comandos curtos; Python quando houver lógica, dados ou testes.
- **Uma API pequena:** o que é um endpoint, FastAPI ou Flask para expor dados por HTTP.

**Fontes gratuitas**

- Pro Git em português (git-scm.com/book/pt-br).
- GitHub Skills (skills.github.com): cursos práticos dentro do próprio GitHub.
- "Automate the Boring Stuff with Python" (automatetheboringstuff.com), gratuito para ler online.
- Documentação do pytest e do FastAPI (fastapi.tiangolo.com/pt).

**Projeto:** `devops-painel-testes` (início do projeto principal). Uma API pequena em Python que registra e lista execuções de teste (nome da suíte, quantos passaram, quantos falharam, duração), com testes em `pytest`, desenvolvida com branches e pull requests. Junto, um script que lê um relatório JUnit XML e envia os resultados para a API.

**Pronto quando:** você resolve um conflito de merge sem medo, abre um PR com descrição e testes, e automatiza em Python uma tarefa que antes fazia à mão.

## Etapa 4: Docker (3 semanas)

Objetivo: empacotar qualquer aplicação para rodar igual em qualquer máquina. A Fase 0 de IA apresenta o Docker; aqui você escreve e otimiza as próprias imagens.

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

**Projeto:** `devops-painel-testes`, etapa 4. A API ganha um `Dockerfile` multi-stage rodando sem `root` e um `docker-compose.yml` com a API e o Postgres. Os dados sobrevivem a `docker compose down`, e a API só sobe depois que o banco estiver saudável.

**Pronto quando:** você escreve um Dockerfile do zero, explica cada linha e sobe a aplicação com o banco usando um único comando.

## Etapa 5: CI/CD com GitHub Actions (2 semanas)

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

**Projeto:** `devops-painel-testes`, etapa 5. Um workflow que, a cada PR, roda lint e testes (unitários e de integração com Postgres) e bloqueia o merge se falhar; a cada merge na `main`, constrói e publica a imagem no GitHub Container Registry. O workflow fica em `.github/workflows/` na raiz do repositório, filtrado pela pasta do projeto.

**Pronto quando:** um PR com um teste quebrado é bloqueado sozinho, e o merge na `main` gera uma imagem nova sem você rodar nada.

## Etapa 6: AWS (4 semanas)

Objetivo: entender os blocos básicos da nuvem e publicar a aplicação de forma segura, primeiro pelo console, para saber o que o Terraform vai automatizar depois.

**Tópicos**

- **Conta e custo:** plano gratuito, alarme de orçamento (AWS Budgets), região, o que cobra por hora e o que cobra por uso.
- **IAM:** usuário root só para o essencial e com MFA; usuários, grupos, papéis (roles) e políticas; menor privilégio; chaves de acesso com rotação; IAM Identity Center para login no terminal (conferir a forma recomendada atual).
- **VPC:** sub-redes públicas e privadas, internet gateway, tabelas de rota, security groups (o firewall da etapa 2), NAT e por que ele custa.
- **EC2:** instâncias, AMIs, tipos, par de chaves e SSH (a etapa 1 de novo), user data para instalar Docker na subida.
- **S3:** buckets, objetos, bloqueio de acesso público, versionamento, ciclo de vida.
- **RDS:** Postgres gerenciado, sub-rede privada, backup, acesso só a partir da aplicação.
- **AWS CLI:** os mesmos passos pelo terminal.

**Fontes gratuitas**

- AWS Skill Builder (skillbuilder.aws): AWS Cloud Practitioner Essentials e os cursos gratuitos de fundamentos (conferir o catálogo gratuito atual).
- Documentação oficial da AWS para IAM, VPC, EC2, S3 e RDS, com os tutoriais "Getting started".
- Página do plano gratuito (aws.amazon.com/free) (conferir antes de criar a conta).

**Projeto:** `devops-6-aws-console`. Publicar a imagem do painel de testes numa EC2 dentro de uma VPC própria, com o banco no RDS em sub-rede privada e relatórios guardados no S3, tudo criado pelo console e documentado passo a passo no README (com prints), usando um usuário IAM com permissões mínimas. No fim, apagar tudo e conferir a fatura.

**Pronto quando:** você desenha a arquitetura num papel (VPC, sub-redes, security groups, EC2, RDS, S3), explica por que o banco não fica na sub-rede pública e não deixa nenhum recurso esquecido gerando custo.

## Etapa 7: Terraform (3 semanas)

Objetivo: criar a mesma infraestrutura da etapa 6 com código versionado, revisável e reproduzível, em vez de cliques.

**Tópicos**

- **Infraestrutura como código:** por que (revisão em PR, histórico, repetir em outro ambiente); declarativo versus imperativo.
- **Ciclo básico:** `init`, `fmt`, `validate`, `plan`, `apply`, `destroy`; ler um `plan` antes de aplicar.
- **Linguagem (HCL):** providers, resources, data sources, variables, outputs, `locals`.
- **Estado (state):** o que é, por que não vai para o Git, estado remoto em S3 com trava (conferir a forma atual de locking).
- **Organização:** módulos, um diretório por ambiente, versões fixas de provider.
- **Segurança:** credenciais fora do código, `.tfvars` sensíveis fora do Git, varredura com ferramentas como Checkov ou tfsec (conferir).
- **Terraform no CI:** `plan` automático no PR e `apply` só com aprovação.
- **OpenTofu:** a alternativa de código aberto compatível; saber que existe.

**Fontes gratuitas**

- HashiCorp Developer: tutoriais "Get Started - AWS" (developer.hashicorp.com/terraform/tutorials).
- Documentação do provider AWS no Terraform Registry (registry.terraform.io).

**Projeto:** `devops-painel-testes`, etapa 7. A infraestrutura da etapa 6 reescrita em Terraform, num módulo de rede e num de aplicação, com estado remoto em S3. O pipeline da etapa 5 ganha um job que roda `terraform plan` em cada PR. Um `terraform destroy` apaga tudo no fim de cada sessão de estudo.

**Pronto quando:** você cria e destrói o ambiente inteiro com dois comandos e explica o que cada linha do `plan` vai mudar antes de aplicar.

## Etapa 8: Kubernetes (4 semanas)

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

**Projeto:** `devops-8-kubernetes`. A imagem publicada pelo pipeline do painel de testes rodando num cluster `kind`, com Deployment de 2 réplicas, Service, ConfigMap, Secret, probes e limites de recursos, mais o Postgres. Teste de QA no fim: apagar um Pod de propósito e mostrar que o cluster recria; fazer uma atualização com erro e voltar com rollback.

**Pronto quando:** você sobe a aplicação no cluster só com manifestos escritos por você e diagnostica um Pod que não inicia usando `describe` e `logs`.

## Etapa 9: Observabilidade e SRE (3 semanas)

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

**Projeto:** `devops-painel-testes`, etapa 9. A API passa a expor métricas; Prometheus e Grafana sobem pelo `docker-compose` e também na EC2; um painel mostra requisições, erros e latência; um alerta dispara quando a taxa de erro passa do limite; o README define 2 SLIs e seus SLOs e mostra o orçamento de erro.

**Pronto quando:** você provoca uma falha de propósito, vê o alerta disparar, encontra a causa pelo painel e pelos logs e escreve um postmortem curto.

## Projeto principal: painel de execuções de teste

Uma API simples que registra e mostra resultados de execuções de teste, publicada como em produção. Ela junta tudo da trilha num único repositório, construído aos poucos das etapas 3 a 9.

| Parte | Tecnologia | Etapa |
| --- | --- | --- |
| Aplicação e testes | Python, FastAPI, pytest, Postgres | 3 |
| Empacotamento | Dockerfile multi-stage, docker-compose | 4 |
| Pipeline | GitHub Actions: lint, testes, build e publicação da imagem | 5 |
| Infraestrutura | AWS (VPC, EC2, RDS, S3, IAM) criada com Terraform | 6 e 7 |
| Deploy | Pipeline aplica o Terraform e atualiza a EC2; smoke test da etapa 2 roda depois do deploy | 5, 7 e 2 |
| Monitoramento | Prometheus, Grafana, alertas, SLOs | 9 |

**Pronto quando:** um merge na `main` passa pelos testes, gera a imagem, atualiza a infraestrutura na AWS, roda o smoke test e aparece no painel do Grafana, sem nenhum passo manual. E você consegue destruir e recriar o ambiente inteiro em menos de 30 minutos.

## Projetos de portfólio

| Etapa | Pasta | Projeto | O que prova |
| --- | --- | --- | --- |
| 1 | `devops-1-saude-servidor/` | Script Bash de saúde do servidor e análise de log, agendado no cron | Linux, Bash, logs |
| 2 | `devops-2-checagem-rede/` | Checador de DNS, porta, HTTP e certificado TLS | Redes e diagnóstico |
| 3 | `devops-painel-testes/` | Início do projeto principal: API com pytest, feita com PRs | Git em equipe e automação |
| 4 | `devops-painel-testes/` | API e Postgres em containers | Docker |
| 5 | `devops-painel-testes/` | Pipeline que testa e publica a imagem | CI/CD com testes |
| 6 | `devops-6-aws-console/` | Deploy manual documentado e depois destruído | Fundamentos de AWS |
| 7 | `devops-painel-testes/` | Infraestrutura em Terraform com plan no CI | Infraestrutura como código |
| 8 | `devops-8-kubernetes/` | A imagem do painel rodando em cluster local | Kubernetes |
| 9 | `devops-painel-testes/` | Métricas, painel, alerta e SLO | Observabilidade e SRE |

Os projetos das etapas 1, 2, 6 e 8 ficam em pastas próprias. O projeto principal fica numa pasta só e ganha uma tag de versão a cada etapa (`etapa-3`, `etapa-4` e assim por diante), para dar para ver a evolução no histórico. Se quiser destacá-lo no portfólio, ele pode virar um repositório próprio no GitHub a partir da etapa 5.

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
- Termine cada sessão com `terraform destroy` (ou apagando pelo console na etapa 6) e confira o painel de custos.
- Chaves de acesso nunca entram no Git. Use `.env` local (fora do Git), `aws configure` ou login pelo IAM Identity Center, e GitHub Secrets ou OIDC no pipeline.

## Rotina semanal

A mesma do [[plano]]: 30 minutos de curso ou leitura por dia e o resto construindo; sábado para avançar o projeto e publicar no GitHub; revisão com o tutor a cada 2 semanas.

**Atrasou?** Corte tópicos opcionais (Helm, OpenTelemetry, OpenTofu, HPA), nunca o projeto da etapa.
