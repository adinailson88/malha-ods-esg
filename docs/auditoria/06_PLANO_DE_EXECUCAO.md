# Plano de execução

Sequência de trabalho para levar o eixo ODS/ESG de seu estado atual ao artigo de primeiro estrato descrito em `03_DESENHO_DO_ESTUDO_A1.md`. As durações são relativas (semanas contadas a partir do início da execução) e dependem da disponibilidade do autor e de terceiros; não foram estimadas em horas por falta de dados sobre essa disponibilidade. Responsáveis: Autor (decisões, contatos, ética, texto final); Claude local (implementação de código, análises, rascunhos, conferências); Terceiros (setores da instituição, especialistas). A atividade 7 do cronograma do pré-projeto (integrar e priorizar por MCDM com análise de sensibilidade) está prevista para o ano 3 do doutorado; este plano antecipa as etapas técnicas que não dependem de terceiros.

## Fase 0. Estabilização (semanas 1 e 2; não depende de terceiros)

Objetivo: tornar o que existe correto, reprodutível e organizado.

1. Confirmar na planilha a razão preventiva e a coluna de criticidade (Autor). Corrigir `COL_CRITICIDADE_OUT` e a cadeia de exportação da razão, no hub e neste repositório, em branch e PR (Autor aprova; Claude local implementa).
2. Congelar a versão de dados: registrar data, commit do hub e hash de `chamados.json`; gerar `dados/congelado/` com agregados por campus, sistema e ano (Claude local).
3. Implementar o cálculo canônico em código versionado: `scripts/replicacao/pontuar.py` com normalização, soma ponderada, TOPSIS e PROMETHEE II; testes em `tests/` que reproduzem o painel atual e o diagnóstico (Claude local).
4. Usar `Area_Utilizacao_m2` do patrimônio por campus e ano (após D09) e projetar 2026 (+5%); ativar a densidade; atualizar `modelo_area_campus.json` (Claude local; Autor confirma).
5. Higiene do repositório: itens da seção 5 de `02_AUDITORIA_DADOS_CODIGO.md` (remoções, mover referências, `CITATION.cff`, `LICENSE`, workflows, Pages) com aprovação item a item (Autor decide).
6. Atualizar `docs/auditoria/dados/auditoria_base.json` e regenerar `protocolo_zuur.json` e `analise_gam.json` (Claude local).

Critério de saída: um comando reproduz o diagnóstico e os escores atuais; testes passam; os números do manuscrito antigo foram substituídos por saída de código; lista de decisões de higiene registrada.

## Fase 1. Dados (semanas 1 a 8; em paralelo à fase 0)

1. Enviar as solicitações de dados prioritárias (D03, D04, D05, D06, D11, D15) (Autor); registrar data e protocolo.
2. Consultar o CEP da UFSB sobre o painel de especialistas e a LGPD sobre os agregados (D23) (Autor).
3. Baixar calendário (D12) e coletar precipitação (D13) (Autor ou workflow); selecionar o índice de preços (D19) e obter o texto oficial dos ODS (D20) (Autor).
4. Montar a lista de especialistas (D17) (Autor e orientador).
5. Iniciar a busca sistemática da literatura (D21), com protocolo e registro de decisões (Autor, com apoio do Claude local para triagem e fichamento).

Critério de saída: dados D03, D04 e D11 recebidos ou decisão registrada de prosseguir sem eles (com o conjunto mínimo de critérios C1, C2*, C5, C6 e C7, sendo C2* a criticidade por IA com ressalva).

## Fase 2. Construção do painel e indicadores (semanas 3 a 8)

1. Construir `painel_prioridade` (campus, sistema e ano) por script, com sinalizadores de qualidade (Claude local).
2. Implementar versões por confiança de classificação e a simulação de erro com a matriz de confusão (Claude local, usando o repositório de classificação).
3. Separar contratação ("Posto de trabalho") do custo corrente; deflacionar; calcular C1 a C8 conforme a disponibilidade (Claude local; Autor valida decisões).
4. Reexecutar a exploração de dados (correlação, multicolinearidade, zeros estruturais) sobre o painel (Claude local).

Critério de saída: painel congelado e documentado no dicionário de dados; relatório de qualidade por campus e período.

## Fase 3. Protocolo e especialistas (semanas 4 a 12)

1. Redigir o protocolo de estudo com hipóteses, definições, limiares, plano de sensibilidade e regra para resultados negativos; pré-registrar antes da análise principal (Autor e Claude local).
2. Elaborar o instrumento de validade de conteúdo e de comparações pareadas; piloto com dois ou três especialistas (Claude local redige; Autor aplica).
3. Coletar as respostas do painel após a aprovação ética; calcular validade de conteúdo, autovetores, consistência e agregação (Claude local).

Critério de saída: vetor de pesos com intervalo e razão de consistência aceitável; lista de indicadores aprovados por validade de conteúdo; protocolo pré-registrado.

## Fase 4. Análise (semanas 9 a 16)

1. Índice por esquema de normalização, pesos e método; perfil por ODS (Claude local).
2. Incerteza conjunta (Monte Carlo e SMAA-2), decomposição por fonte e métricas de estabilidade (Claude local).
3. Validação convergente (ordenação às cegas por especialistas, se aprovada) e preditiva (origem móvel) (Claude local; Autor interpreta).
4. Integração opcional de previsões dos Artigos 2 e 3 como C10 (depende de reexecução do hub e de covariáveis reais).
5. Mapa de prioridade (opcional).

Critério de saída: todas as tabelas e figuras previstas geradas por script; relatório de resultados com versão do dado; verificação dos critérios de aceite (seção 18 do desenho).

## Fase 5. Redação (semanas 12 a 22; sobrepõe-se à análise)

1. Revisão sistemática concluída e tabela de lacunas (T1) (Autor, com Claude local).
2. Primeira versão em inglês, seção por seção, conforme `05_PLANO_DE_REDACAO.md`, com matriz de afirmações (Claude local redige; Autor revisa e reescreve no próprio estilo).
3. Revisão interna por especialista externo ao projeto; revisão de língua (Autor).
4. Escolha do periódico, adaptação às normas, carta e declarações (Autor).
5. Release arquivado e identificador persistente; verificação final (Claude local e Autor).

Critério de saída: manuscrito completo, pacote de replicação e checklist de submissão da seção 11 do plano de redação cumpridos.

## Portões de decisão

| Portão | Quando | Pergunta | Se a resposta for não |
|---|---|---|---|
| G0 | fim da fase 0 | O cálculo canônico reproduz o painel e os testes passam? | Corrigir antes de qualquer análise |
| G1 | fim da fase 1 | Chegaram prioridade nativa e datas de solução, usuários e aprovação ética? | Prosseguir com o conjunto mínimo e declarar a limitação, ou adiar a coleta com especialistas |
| G2 | fim da fase 3 | Há consistência e validade de conteúdo suficientes? | Rodada adicional de consulta; se persistir, usar incerteza total de pesos (SMAA) sem elicitação |
| G3 | fim da fase 4 | Os critérios de aceite 3 a 5 foram cumpridos? | Reposicionar o artigo como estudo de robustez e de incerteza, sem afirmação preditiva |
| G4 | antes da submissão | O checklist está completo e há revisão externa? | Não submeter |

## Registro de riscos

| Risco | Probabilidade | Impacto | Resposta |
|---|---|---|---|
| Dados do GLPI não disponíveis ou vazios | média | alto | decidir o conjunto mínimo; documentar; usar criticidade por IA com ressalva e análise de sensibilidade |
| Painel de especialistas com baixa adesão | média | alto | ampliar a rede; usar BWM (menos comparações); SMAA sem elicitação |
| Ética exige prazo longo | média | médio | iniciar o contato imediatamente; adiar apenas a coleta |
| Classificação por sistema com erro excessivo | média | alto | painel por campus e ano; versões por confiança |
| Resultado preditivo fraco | alta | médio | declarar; ênfase em robustez e incerteza |
| Artigos 2 e 3 atrasam | média | médio | tornar C10 opcional |
| Conflito de interesses questionado | baixa | médio | protocolo pré-registrado e declaração |
| Saldo de créditos da nuvem expira em 05/11/2026 | certa | médio | continuar localmente; repositório documentado; nada depende de sessão em nuvem |
| Mudança de orientação ou de coautoria | desconhecida | alto | o autor deve informar; não presumido |

## Estrutura-alvo do repositório

1. Raiz: `README.md` (resumo, reprodução em três comandos, link do artigo), `CITATION.cff`, `LICENSE`, `CLAUDE.md`, `AGENTS.md`, `index.html`, `dashboard.html`.
2. `docs/`: `manuscrito/` (versão em português e em inglês), `auditoria/` (este conjunto), `metodologia/`, `referencias/` e `README.md` com índice.
3. `dados/`: snapshots do hub; `dados/congelado/` com agregados da versão do artigo e hash.
4. `scripts/replicacao/`: construção do painel, pontuação, pesos, sensibilidade e figuras; `scripts/diagnostico/` e `scripts/auditoria/` (já existentes).
5. `protocolo/`: protocolo pré-registrado, instrumentos de especialistas, termo de consentimento (sem dados pessoais).
6. `tests/`: reprodução do painel, indicadores e regressões.
7. `.github/workflows/`: sincronização diária, testes e publicação do painel restrita a arquivos publicáveis.

## Próximos dez passos (para a primeira semana de trabalho local)

1. Abrir a planilha e conferir a razão preventiva (0,234 ou 925) e a coluna de criticidade (AD ou AE).
2. Confirmar se `Area_Utilizacao_m2` equivale à área construída e se CJA, CPF e CSC são Jorge Amado, Paulo Freire e Sosígenes Costa.
3. Pedir ao administrador do GLPI quais campos de solução, fechamento, prioridade, urgência, impacto e localização existem e estão preenchidos.
4. Consultar o CEP da UFSB sobre o painel de especialistas.
5. Informar o status da orientação e a coautoria.
6. Decidir a lista de higiene do repositório (seção 5 do documento de auditoria).
7. Escolher a licença de código e de dados.
8. Decidir se o objeto do artigo é prioridade de manutenção (recomendado) e confirmar os critérios mínimos (C1, C2, C3, C5, C6 e C7).
9. Pedir ao Claude local a implementação da fase 0 (cálculo canônico, testes e congelamento).
10. Reservar tempo para a busca sistemática da literatura (D21).
