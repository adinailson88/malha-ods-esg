# Matriz de dados: o que já existe e o que precisa ser buscado

Fonte tabular completa em [`matriz_dados.csv`](matriz_dados.csv) (para uso em planilha). Situação: TENHO (utilizável agora), PARCIAL (existe, com lacuna ou dúvida) e NÃO TENHO. Prioridade: P0 bloqueia a submissão; P1 é necessário para a versão forte; P2 é desejável; P3 é extensão. Esforço: B baixo, M médio, A alto (relativo, não em horas). Os setores indicados são hipóteses de quem detém o dado e precisam ser confirmados pelo autor. Nada foi solicitado a ninguém.

## 1. Resumo

Total de itens: 23. TENHO: 2; PARCIAL: 6; NÃO TENHO: 15. Itens P0 (bloqueiam a submissão): D01, D02, D03, D04, D09, D11, D17, D21, D23.

Leitura: com os dados de hoje é possível construir o painel campus e ano com demanda, valor de OS, área e erro de classificação (D01, D02, D09, D18), o que permite reproduzir o diagnóstico e começar a validação preditiva. Três dados novos destravam o artigo forte e dependem de extração ou de pessoas, não de modelagem: datas de solução e prioridade nativa do GLPI (D03 e D04), número de usuários por campus (D11) e o painel de especialistas com a verificação ética (D17 e D23).

## 2. Itens por prioridade

### P0: bloqueia a submissão

**D01. Chamados de manutenção (data, campus, status, categoria histórica)** (TENHO; esforço B)

1. Uso: Todos os critérios; painel campus, sistema e ano.
2. Onde está ou fonte candidata: chamados.json no hub malha-ia (14.580 chamados, 2015-06 a 2026-10).
3. Problema ou lacuna: Base incremental; 69,9% de linhas vazias; 15 colunas vazias; unidade Maria Felipa só em 2026.
4. Como obter: Congelar versão (data, hash, commit) e publicar agregados; limpar linhas vazias no hub.
5. Quem pode fornecer: Autor (hub).
6. Bloqueia: Todas.

**D02. Classificação por IA (categoria, confiança, executor)** (PARCIAL; esforço M)

1. Uso: Definição de sistema técnico; critério C6.
2. Onde está ou fonte candidata: chamados.json colunas 25, 27 e 28; matriz de confusão no repositório classificacao-chamados.
3. Problema ou lacuna: 40,6% de baixa confiança; mudança de regime desde 2021; 53 categorias versus taxonomia de 39 a 41.
4. Como obter: Usar rótulos revisados por humano do artigo de classificação como referência; reportar por faixa de confiança; simular erro.
5. Quem pode fornecer: Autor (repositório de classificação).
6. Bloqueia: P3 e P4.

**D03. Data de solução e de fechamento do chamado** (NÃO TENHO; esforço M)

1. Uso: C3 tempo de resposta; ODS 9.
2. Onde está ou fonte candidata: GLPI (campos nativos de solução e fechamento; confirmar na instalação da UFSB).
3. Problema ou lacuna: Não extraído para a planilha; coluna de conclusão é None no motor.
4. Como obter: Exportar por API do GLPI ou consulta ao banco; incluir na planilha ou em tabela auxiliar por ID de chamado.
5. Quem pode fornecer: Responsável pela TI e administrador do GLPI.
6. Bloqueia: C3, painel temporal.

**D04. Prioridade, urgência e impacto nativos do GLPI** (NÃO TENHO; esforço M)

1. Uso: C2 severidade, em substituição à criticidade por IA.
2. Onde está ou fonte candidata: GLPI (campos nativos de urgência, impacto e prioridade; confirmar preenchimento real).
3. Problema ou lacuna: Criticidade por IA instável (149 chamados altos; salto em 2026).
4. Como obter: Extrair por ID de chamado; medir preenchimento antes de adotar.
5. Quem pode fornecer: Administrador do GLPI.
6. Bloqueia: C2.

**D09. Área construída e total por campus e ano** (PARCIAL; esforço B)

1. Uso: Normalização de C1 e C5.
2. Onde está ou fonte candidata: patrimonio_imobiliario_campus_ano.json (Area_Utilizacao_m2, 2015 a 2025; soma coincide com a área global até 2021).
3. Problema ou lacuna: Equivalência utilização versus construída a confirmar; sem 2026; Reitoria possivelmente subestimada; sem Maria Felipa.
4. Como obter: Confirmar com o setor de patrimônio e engenharia; projetar 2026 com +5% e rotular a origem.
5. Quem pode fornecer: Setor de patrimônio e de infraestrutura.
6. Bloqueia: C1, C5.

**D11. Número de usuários por campus e ano (estudantes, docentes, técnicos, terceirizados)** (NÃO TENHO; esforço M)

1. Uso: C9; normalização de demanda.
2. Onde está ou fonte candidata: Registros acadêmicos e de pessoal da UFSB (a identificar); microdados públicos do censo da educação superior como alternativa para estudantes por local de oferta (disponibilidade por campus a verificar).
3. Problema ou lacuna: Inexistente nos repositórios; hoje há apenas dados SIMULADOS no repositório de chamados.
4. Como obter: Solicitar à pró-reitoria de planejamento, à de gestão de pessoas e ao registro acadêmico; terceirizados via contratos.
5. Quem pode fornecer: Pró-reitorias de planejamento, de gestão de pessoas e registro acadêmico; fiscais de contrato.
6. Bloqueia: C9, P2.

**D17. Painel de especialistas: validade de conteúdo e comparações pareadas (AHP ou BWM)** (NÃO TENHO; esforço A)

1. Uso: Pesos e validade de conteúdo.
2. Onde está ou fonte candidata: A gerar por questionário.
3. Problema ou lacuna: Depende de lista de especialistas e de verificação ética.
4. Como obter: Montar painel de 8 a 15 especialistas; protocolo; questionário eletrônico; termo de consentimento.
5. Quem pode fornecer: Autor, com apoio do orientador e do CEP.
6. Bloqueia: P1 e pesos.

**D21. Estudos de caso e literatura sobre indicadores ODS em universidades e MCDM com incerteza** (PARCIAL; esforço A)

1. Uso: Revisão e lacuna.
2. Onde está ou fonte candidata: Acervo de 68 referências no Drive e busca sistemática a fazer.
3. Problema ou lacuna: Poucos itens metodológicos de MCDM; busca não sistemática até agora.
4. Como obter: Busca sistemática em bases indexadas com protocolo; fichar no acervo.
5. Quem pode fornecer: Autor.
6. Bloqueia: Lacuna.

**D23. Declarações éticas e autorizações (CEP, LGPD, instituição)** (NÃO TENHO; esforço M)

1. Uso: Conformidade.
2. Onde está ou fonte candidata: CEP da UFSB; encarregado de dados.
3. Problema ou lacuna: Não verificados.
4. Como obter: Consultar o CEP sobre enquadramento; obter autorização institucional.
5. Quem pode fornecer: Autor.
6. Bloqueia: Coleta com especialistas.

### P1: necessário para a versão forte

**D05. Localização e ativo do chamado** (NÃO TENHO; esforço M)

1. Uso: C4 reincidência; C8 espaços coletivos; análise por edificação.
2. Onde está ou fonte candidata: GLPI (localização e item associado; confirmar preenchimento).
3. Problema ou lacuna: COL_LOCAL é None; título livre usado como substituto.
4. Como obter: Extrair campo estruturado; se vazio, abrir validação por amostra de títulos.
5. Quem pode fornecer: Administrador do GLPI e setor de manutenção.
6. Bloqueia: C4, C8.

**D06. Ordens de serviço: número, data, executor, contrato, empenho** (PARCIAL; esforço M)

1. Uso: C5 custo corrente; vínculo com contratação.
2. Onde está ou fonte candidata: Colunas 23 e 24 (título e descrição da OS) e valor na coluna 16; sistema de OS e contratos da UFSB (a identificar).
3. Problema ou lacuna: Só o valor; sem data da OS, sem contrato, sem empenho; 57 OS sem valor.
4. Como obter: Solicitar relatório de OS com data de emissão, execução, contrato e valor ao setor de manutenção e de contratos.
5. Quem pode fornecer: Setor de manutenção e fiscalização de contratos.
6. Bloqueia: C5.

**D07. Natureza do valor e política de preenchimento da coluna Q** (PARCIAL; esforço B)

1. Uso: Interpretação de C5.
2. Onde está ou fonte candidata: Esclarecimento do autor: valor das OS.
3. Problema ou lacuna: Política (quando e por quem se preenche) e defasagem não documentadas.
4. Como obter: Documentar no dicionário de dados com o responsável; comparar extrações sucessivas para detectar atraso.
5. Quem pode fornecer: Autor e setor de manutenção.
6. Bloqueia: C5.

**D15. Plano de manutenção preventiva e cronograma contratual** (NÃO TENHO; esforço M)

1. Uso: C6 razão corretiva; distinção preventiva programada versus demanda.
2. Onde está ou fonte candidata: Contratos e planos de manutenção (NBR 5674) da UFSB.
3. Problema ou lacuna: Preventiva (33% dos chamados) é programada; mistura com demanda espontânea.
4. Como obter: Solicitar planos, periodicidades e contratos vigentes por campus.
5. Quem pode fornecer: Setor de manutenção e de contratos.
6. Bloqueia: C6.

**D18. Rótulos humanos e matriz de confusão do classificador** (TENHO; esforço B)

1. Uso: Propagação do erro de classificação.
2. Onde está ou fonte candidata: Repositório classificacao-chamados (docs e dados da trilha de validação).
3. Problema ou lacuna: Cobertura por categoria e por período a documentar.
4. Como obter: Reutilizar com citação do artigo de classificação.
5. Quem pode fornecer: Autor.
6. Bloqueia: P3.

**D19. Índice de preços para deflacionar valores** (NÃO TENHO; esforço B)

1. Uso: C5 em termos reais.
2. Onde está ou fonte candidata: Índices oficiais de preços (consumo ou construção), a escolher e verificar nas fontes oficiais.
3. Problema ou lacuna: Não consultado.
4. Como obter: Baixar série mensal, escolher base e registrar a fonte.
5. Quem pode fornecer: Autor.
6. Bloqueia: C5.

**D20. Metas e indicadores oficiais dos ODS 9, 11 e 12 (texto oficial)** (NÃO TENHO; esforço B)

1. Uso: Vínculo de critérios a metas.
2. Onde está ou fonte candidata: Documentos oficiais da Agenda 2030 e da adaptação brasileira.
3. Problema ou lacuna: Citados em paráfrase neste desenho.
4. Como obter: Obter texto oficial e registrar versão.
5. Quem pode fornecer: Autor.
6. Bloqueia: P1.

### P2: desejável; eleva o valor

**D08. Despesa de manutenção por natureza e unidade gestora (execução orçamentária)** (NÃO TENHO; esforço M)

1. Uso: Validação externa do custo; C5.
2. Onde está ou fonte candidata: Sistemas públicos de execução orçamentária e de contratos do governo federal (dados abertos; identificar a unidade gestora da UFSB e as naturezas de despesa de serviços, material e obras).
3. Problema ou lacuna: Não consultado; a disponibilidade por campus precisa ser verificada.
4. Como obter: Consulta pública ao portal de transparência e ao Tesouro Gerencial; cruzar com OS.
5. Quem pode fornecer: Setor de orçamento e finanças; consulta pública.
6. Bloqueia: Validação de C5.

**D10. Área por edificação e tipologia** (PARCIAL; esforço A)

1. Uso: Análise por edificação (extensão).
2. Onde está ou fonte candidata: patrimonio_imobiliario.json (180 imóveis, RIP, coordenadas).
3. Problema ou lacuna: Chamados não têm localização para vincular.
4. Como obter: Depende de D05.
5. Quem pode fornecer: Setor de patrimônio.
6. Bloqueia: Extensão.

**D12. Calendário acadêmico real por campus e ano** (NÃO TENHO; esforço B)

1. Uso: Sazonalidade de demanda; covariável do Artigo 2.
2. Onde está ou fonte candidata: PDFs de calendário no site da UFSB (página de calendários da pró-reitoria de graduação); regime semestral desde 2024 e quadrimestral até 2023 (a confirmar na resolução).
3. Problema ou lacuna: Não baixado (site bloqueado na sessão em nuvem).
4. Como obter: Baixar e preencher a aba COV_CALENDARIO do repositório de chamados.
5. Quem pode fornecer: Autor.
6. Bloqueia: Artigo 2.

**D13. Precipitação mensal por município (soma, mm)** (NÃO TENHO; esforço B)

1. Uso: Condicionante ambiental; covariável do Artigo 2.
2. Onde está ou fonte candidata: Reanálise por coordenada (Open-Meteo) ou estações do INMET; coletor já escrito no repositório de chamados.
3. Problema ou lacuna: Não executado (rede bloqueada na sessão).
4. Como obter: Rodar o coletor ou o workflow do repositório de chamados.
5. Quem pode fornecer: Autor.
6. Bloqueia: Artigo 2 e cenários.

**D14. Consumo de energia e de água por campus (kWh, m3)** (NÃO TENHO; esforço M)

1. Uso: C11 eficiência de recursos; pilar ambiental.
2. Onde está ou fonte candidata: Faturas e contratos de concessionárias (a identificar); fiscais de contrato.
3. Problema ou lacuna: Não levantado; pode haver múltiplos medidores por campus.
4. Como obter: Solicitar série mensal por campus aos fiscais e ao setor financeiro.
5. Quem pode fornecer: Fiscais de contrato e setor financeiro.
6. Bloqueia: C11 (opcional).

**D16. Laudos de inspeção predial e condição das edificações** (NÃO TENHO; esforço M)

1. Uso: Validação convergente; condição física.
2. Onde está ou fonte candidata: Setor de engenharia e de infraestrutura (a identificar).
3. Problema ou lacuna: Existência e cobertura desconhecidas.
4. Como obter: Perguntar ao setor se há laudos ou vistorias por edificação.
5. Quem pode fornecer: Setor de engenharia e infraestrutura.
6. Bloqueia: Validação.

### P3: extensão

**D22. Dados externos de comparação (segunda instituição)** (NÃO TENHO; esforço A)

1. Uso: Validade externa (extensão).
2. Onde está ou fonte candidata: Instituição federal parceira (a identificar).
3. Problema ou lacuna: Sem parceria definida.
4. Como obter: Contato institucional; acordo de dados.
5. Quem pode fornecer: Autor e orientador.
6. Bloqueia: Extensão.

## 3. Modelo de solicitação de dados (texto-base para o autor adaptar)

Assunto: solicitação de dados para pesquisa de doutorado em governança da manutenção predial.

Prezados, no âmbito do doutorado em Biossistemas (UFSB), estou desenvolvendo um estudo sobre priorização da manutenção predial alinhada aos ODS 9, 11 e 12, com uso exclusivamente de dados agregados e sem identificação de pessoas. Solicito, para o período de 2018 a 2026 e por campus, [lista dos itens, com o formato desejado: planilha, colunas, periodicidade]. Os dados serão tratados conforme a LGPD, usados apenas em agregados e referenciados na publicação; coloco-me à disposição para detalhar o protocolo e para compartilhar os resultados com a unidade. Agradeço antecipadamente.

Observações: (i) adaptar o tom e o encaminhamento à rotina da instituição; (ii) registrar a data e o número do processo da solicitação; (iii) quando o dado for de acesso público, citar a fonte oficial em lugar de solicitar; (iv) o autor administra o sistema de chamados e deve declarar esse fato nas publicações.

## 4. Sequência sugerida de obtenção

1. Primeira semana: confirmar D09 (área construída) e a posição das colunas da planilha; solicitar D03, D04 e D05 ao administrador do GLPI; baixar D12 e rodar D13.
2. Em paralelo: iniciar D11 (usuários) e D15 (planos de manutenção) nas pró-reitorias e no setor de manutenção; consultar o CEP (D23).
3. Após a resposta do CEP: montar o painel de especialistas (D17).
4. Em paralelo e sem dependência de terceiros: congelar D01, D02 e D18, escolher D19 e D20, e iniciar a busca sistemática D21.
