# Auditoria dos dados, do código e do repositório

Escopo: tudo que sustenta os números do artigo. Evidências reproduzíveis por `python scripts/auditoria/auditar_base.py <caminho>/malha-ia/dados/chamados.json` (saída em `docs/auditoria/dados/auditoria_base.json`) e por `python scripts/diagnostico/mcdm_sensibilidade.py <caminho>/malha-ia/dados/chamados.json`. Base lida: `malha-ia/dados/chamados.json` (commit `526abb8`, 03/11/2026). Nenhum texto de chamado foi copiado; somente contagens e proporções. A planilha viva e o Apps Script não puderam ser acessados na sessão de auditoria.

## 1. A base de chamados

### 1.1 Estrutura e integridade

1. 48.418 linhas de dados, das quais 33.838 (69,9%) estão totalmente vazias; 14.580 chamados com data de abertura, entre 2015-06 e 2026-10, sem identificador duplicado e com todas as datas em formato ISO (`AAAA-MM-DD hh:mm`).
2. 30 colunas, 15 sem nome e sem nenhum valor (índices 4, 5, 6, 8, 9, 10, 11, 13, 14, 15, 17, 18, 19, 21 e 26): são resíduos de mesclagem de células da planilha. As colunas com conteúdo são: ID (0), título (1), data (2), status (3), campus (7), categoria histórica (12), valor (16), descrição GLPI (22), título e descrição da ordem de serviço (23 e 24), classificação por IA (25), confiança da IA (27), executor da classificação (28) e criticidade por IA (29).
3. Preenchimento: título 14.578, descrição GLPI 14.570, título da OS 2.459, descrição da OS 2.421; todas as demais colunas com conteúdo estão completas.
4. Status: 13.828 fechados, 549 solucionados, 155 em processamento (atribuído), 10 em processamento (planejado), 13 pendentes e 25 novos.
5. Não existem na extração: data de solução ou de fechamento, localização e ativo, solicitante (por desenho, por privacidade), prioridade, urgência e impacto nativos do GLPI, SLA e avaliação de satisfação. O GLPI padrão registra datas de solução e de fechamento, urgência, impacto, prioridade e localização; confirmar na instalação da UFSB quais estão preenchidos e se podem ser extraídos.

### 1.2 Distribuição por campus e período

| Campus | Chamados | Primeiro ano | Observação |
|---|---|---|---|
| Sosígenes Costa | 4.245 | 2016 | série estável a partir de 2018 |
| Jorge Amado | 3.946 | 2015 | série estável a partir de 2018 |
| Paulo Freire | 3.924 | 2015 | série estável a partir de 2018 |
| Reitoria | 2.454 | 2015 | unidade administrativa |
| Maria Felipa (Jequié) | 11 | 2026 | unidade nova, inadequada para comparação |

O recorte analítico recomendado é 2018 a 2025 (oito anos completos), com 2026 parcial até outubro, porque 2015 a 2017 são anos de adoção do sistema (28, 172 e 533 chamados).

### 1.3 Classificação por IA e qualidade das categorias

1. 53 categorias distintas na coluna de classificação por IA, contra a taxonomia de 39 a 41 categorias citada nos documentos do artigo de classificação (os dois números aparecem em documentos diferentes); a coincidência textual exata entre categoria histórica e categoria da IA é de 36,6%, afetada por diferenças de taxonomia.
2. Executor registrado: 5.921 chamados "LSTM_BAIXA_CONF" (40,6%), 4.744 "Reclass_LSTM", 3.796 "LSTM", 107 "RF_Fallback_BAIXA_CONF" e 12 "SemClassificador". A confiança informada (coluna 27) tem mediana de 0,94 e o quinto percentil de 0,20.
3. A fração de chamados com a etiqueta de baixa confiança varia no tempo: de 2% a 6% de 2018 a 2020, de 29% a 48% em 2021 e de 50% a 80% de 2022 a 2026, nos quatro campi principais. Os indicadores derivados da classificação (infraestrutura crítica, preventiva e corretiva) herdam essa mudança de regime.
4. Criticidade por IA: 12.477 baixa, 1.954 média e 149 alta. A criticidade alta oscila entre 0 e 16 ocorrências por campus e ano até 2019, entre 0 e 4 de 2020 a 2025 e chega a 12 e 13 em 2026 (Jorge Amado e Paulo Freire), compatível com mudança de critério.

### 1.4 Ordens de serviço e valor

1. 2.459 chamados têm título ou descrição de OS; 2.402 têm valor positivo; 57 têm OS sem valor; nenhum chamado tem valor sem OS. A coluna de valor é, portanto, o valor das ordens de serviço (esclarecimento do autor, confirmado nos dados).
2. Participação das OS com valor por ano: de 9% a 19% em Jorge Amado e de 20% a 34% em Paulo Freire de 2020 a 2025, o que denuncia práticas de registro distintas entre campi.
3. Concentração: o 1% maior valor de OS responde por 42,2% de R$ 20,23 milhões; 93 chamados de "Posto de trabalho" respondem por 52,6% do total e por 50% a 61% do valor de cada campus.
4. Os valores são nominais (sem deflator) e atribuídos ao mês de abertura do chamado, não ao de execução ou pagamento.

## 2. Auditoria indicador por indicador

| Indicador | Definição no código | Problema de construto | Problema de dado ou de código | Veredito |
|---|---|---|---|---|
| `N_chamados_total` | contagem por campus | confunde demanda, propensão a reportar e porte; direção "minimizar" contestável | sem normalização por área ou usuários | manter como insumo, nunca como critério direto; usar por 1.000 m2 e por usuário |
| `N_infra_critica` | contém "elétric", "hidráulic", "telhado" etc. na categoria IA | mede especialidade técnica (30,6% da base, inclui troca de lâmpada e quadros preventivos), não criticidade | herda erro de classificação; colinear com volume | substituir por criticidade explícita (prioridade nativa do GLPI ou critério de especialistas por sistema essencial) |
| `Tempo_medio_resolucao_dias` | requer data de conclusão | adequado ao ODS 9 e à governança | coluna de conclusão `None`; extração do GLPI pendente | extrair `solvedate` e `closedate` do GLPI |
| `Taxa_resolucao_no_prazo` | requer conclusão e SLA fixo por criticidade (3, 7 e 15 dias) | SLA fixo arbitrário | idem; depende de criticidade por IA | usar metas de SLA do GLPI ou normativas, se existirem |
| `N_criticos_alta` | criticidade igual a "alta" na coluna de índice 30 | depende da criticidade por IA (ver 1.3) | índice 30 não existe (a coluna está no 29); resulta sempre zero | corrigir o índice e tratar a quebra de regime de 2026 |
| `N_em_espaco_coletivo` | título contém uma de dez expressões | sensibilidade e especificidade desconhecidas; "contextual" com ótimo em 0,5 sem fundamento | busca textual em título livre | validar contra amostra rotulada; preferir localização estruturada do GLPI |
| `Densidade_chamados_por_1000m2` | chamados por área do campus | adequado | `_ler_area_atual_por_campus` devolve dicionário vazio (stub); resulta sempre zero | usar `Area_Utilizacao_m2` do patrimônio por campus e ano |
| `Razao_preventiva_corretiva` | proporção de preventivas entre classificados | corretiva por exclusão (sem rótulo explícito); herda erro de IA | snapshot traz a contagem de preventivas | corrigir a cadeia de exportação e recalcular; preferir marcação explícita de preventiva pelo plano de manutenção |
| `Valor_total_gasto_R$` | soma da coluna Q | é valor de OS em 16,5% dos chamados; 50% a 61% é contratação | nominal; sem deflator; atribuído à abertura | separar contratação; deflacionar; normalizar por área |
| `N_chamados_repetidos` | requer chave de local | adequado ao ODS 12 (retrabalho) | `COL_LOCAL` é `None` | extrair localização e ativo do GLPI |

Resultado do exame: dos dez indicadores, nenhum está pronto para um artigo de primeiro estrato sem reconstrução da definição, da fonte ou da normalização.

## 3. Auditoria do código

1. `motor_ods.py` (copia do eixo; o hub executa a cópia do hub):
   1. Linha 152: `COL_CRITICIDADE_OUT = 30` com comentário "AD"; a coluna AD tem índice 29. A condição `len(l) > 30` é falsa para todas as 14.580 linhas do JSON.
   2. Linha 155: `COL_DATA_CONCLUSAO = None` e linha 156: `COL_LOCAL = None` desligam três indicadores.
   3. Linhas 236 a 250: `_ler_area_atual_por_campus` sempre devolve `{}` (o comentário reconhece "densidade fica 0").
   4. Linhas 357 e 358: `pd.to_datetime(..., dayfirst=True)` sem a correção de inversão de dia e mês já aplicada no hub (PR malha-ia#6); a cópia do eixo diverge do hub.
   5. A taxonomia da razão preventiva usa a substring "preventiv" e corretiva por exclusão (documentado, provisório).
   6. As listas de padrões de infraestrutura crítica e de espaço coletivo são constantes no código, sem teste de sensibilidade e sem versionamento de regra.
   7. O motor grava a aba por `aba.clear()` seguido de `update`, de modo que uma falha entre as duas operações deixa a aba vazia; a falha de gravação é capturada e apenas impressa (`except Exception`), de modo que o workflow termina com sucesso mesmo sem gravar.
2. `dashboard.html` (943 linhas, Chart.js 4.4.1 por CDN): contém a única implementação de soma ponderada e TOPSIS (`calcularScores` na linha 489, `calcularTOPSIS` na linha 531); a regra de quase-lacuna (valor dominante em N-1 das N unidades) está na função `avaliarIndicadores` (linha 394); `normalizarValor` (linha 482) implementa min–max com inversão e a função "contextual". Não há teste automatizado; a lógica não é verificável fora do navegador (esta auditoria a reproduziu em Python).
3. Ausências: testes unitários, dependências com versão fixa para o que roda neste repositório (o `requirements.txt` é do motor completo, com TensorFlow, e o workflow instala apenas pandas), pacote de replicação congelado, `LICENSE`, ambiente reprodutível.
4. `scripts/gerar_patrimonio_imobiliario.py` exige o secret `GCP_SA_KEY` e compartilhamento da planilha com a conta de serviço; não foi possível verificar se o secret está configurado nem o último resultado do workflow `patrimonio_imobiliario.yml`.

## 4. Auditoria dos dados derivados e dos contratos

1. `dados/indicadores_ods.json`: ver as inconsistências em 2 (razão como contagem). `dados/modelo_area_campus.json`: todos os campos "pendente", embora a área exista no patrimônio.
2. `dados/patrimonio_imobiliario*.json`: 180 registros de imóveis, de 2015 a 2025, com RIP, endereço, cidade, áreas de terreno e de utilização, valores e coordenadas. A soma das áreas de utilização por ano coincide com a área construída global de `area_manutencao.json` de 2015 a 2021, é 0,3% maior de 2022 a 2024 e 4,8% maior em 2025. O vínculo entre imóveis e chamados não existe (os chamados não têm localização), o que impede análise por edificação.
3. `dados/pesos_*.json`, `classificacao_ods_esg.json`, `multiplicadores_importancia_chamado.json` e `regras_peso_chamado_ods_esg.json`: contratos de pontuação por chamado e por família técnica; apenas `pesos_ods.json` é usado no painel; os demais não são consumidos por nenhum código e não têm proveniência.
4. `dados/analise_gam.json` e `dados/protocolo_zuur.json` são de 18/06/2026 (derivados do snapshot de junho) e precisam ser regenerados.

## 5. Auditoria do repositório (higiene e apresentação)

| Item | Situação | Ação proposta (nada executado) |
|---|---|---|
| `PREENCHER_AREA_CAMPUS_PATRIMONIO_IMOBILIARIO.txt` | modelo de preenchimento obsoleto: a área existe no patrimônio | remover, ou converter em instrução na planilha após decidir a fonte |
| `Referência Bibliográfica - Drive/` | README de 100 KB com nome acentuado e espaços, publicado no Pages | mover para `docs/referencias/` e manter só o índice; fichas completas ficam no Drive |
| `CITATION.cff` | aponta para `adinailson88-jpg/malha-ia`, título "Malha IA", sem licença | reescrever para este repositório e para o artigo; adicionar DOI de arquivamento quando existir |
| `LICENSE` | inexistente (README informa "Informação insuficiente para verificar") | o autor escolhe licença de código e de dados (por exemplo MIT para código e CC BY 4.0 para dados) |
| `.github/workflows/atualizar-dados-hub.yml` | cron a cada 30 minutos | reduzir para diário; gera commits de bot em excesso |
| `.github/workflows/ods_indicadores.yml` | duplica as etapas de sincronização do workflow anterior | fundir ou remover; o nome sugere recálculo, mas só sincroniza |
| `pages.yml` | publica a raiz inteira, inclusive `motor_ods.py`, docs e referências | publicar apenas `index.html`, `dashboard.html` e `dados/` |
| `motor_ods.py` | cópia divergente do hub | sincronizar com o hub e corrigir os pontos da seção 3; ou removê-la e deixar só o script de pontuação do eixo |
| `execucao_offline/requirements.txt` | dependências do motor completo | separar `requirements-eixo.txt` (numpy, pandas) do `requirements-motor.txt` |
| `docs/` | 15 documentos, três deles repetidos em outros repositórios (GAM, Zuur, contrato) | manter um índice em `docs/README.md` e marcar o manuscrito, a metodologia e a auditoria como núcleo |
| `dashboard.html` | um arquivo de 43 KB com lógica e visual misturados | extrair a pontuação para módulo testável (JS ou Python) e gerar os JSON de score no pipeline |
| testes | inexistentes | criar `tests/` com a reprodução de soma ponderada e TOPSIS, testes de regressão de indicadores e do parse de datas |
| `dados_csv/` | espelho dos JSON | manter, desde que gerado por script e com cabeçalho de origem |
| `.gitignore` | cobre credenciais e artefatos locais | adequado |

## 6. Apresentação do repositório para fins de artigo

Para que o repositório funcione como material suplementar de primeiro estrato, ele deve apresentar na raiz: (i) um `README.md` com resumo do estudo, estrutura, instruções de reprodução em três comandos e link para o artigo; (ii) `CITATION.cff` correto; (iii) `LICENSE`; (iv) um release versionado com os dados congelados e o DOI de arquivamento (a integração do GitHub com o Zenodo permite emitir DOI a partir de um release; a configuração é do autor); (v) um diretório `replicacao/` com um script único que reconstrói todas as tabelas e figuras do artigo a partir do dado congelado; (vi) a pasta `docs/auditoria/` como registro de decisões. O painel pode permanecer como produto, desde que o texto indique a versão do dado que ele exibe.
