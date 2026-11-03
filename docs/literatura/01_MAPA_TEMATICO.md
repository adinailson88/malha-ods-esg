# Mapa temático: o que a literatura diz, onde está a lacuna e como usar cada frente no artigo

Elaborado em 03/11/2026 a partir de buscas dirigidas e de leituras de resumos e registros; nenhum texto integral foi lido nesta etapa, e as afirmações abaixo valem como mapa de leitura, não como revisão concluída. Os identificadores R01 a R51 remetem a `02_REFERENCIAS_VERIFICADAS.md`. O objeto de medida adotado é o índice de prioridade de manutenção (ver `docs/auditoria/03_DESENHO_DO_ESTUDO_A1.md`).

## 1. As dez frentes de literatura do artigo

### T1. Priorização de manutenção em campi e edificações públicas

O que se encontrou: estudos de caso isolados, sobretudo de universidades da Ásia, que ponderam critérios de serviço (segurança, saúde, conforto, acessibilidade), condição física e custo por AHP com questionários, e índices de condição por componente; um estudo de priorização de manutenção diferida em campus de grande porte usa o índice de condição das instalações (razão entre custo de manutenção diferida e custo de reposição) e relata redução do índice abaixo de 0,1 após a estratégia (R41); um precedente conceitual de índice de criticidade de sistemas prediais por MCDA (R42); revisão de aprendizado de máquina em manutenção predial (R40). A universidade de Toronto publica modelo de priorização de manutenção diferida em que a condição física pesa 45% (relatório institucional, V3).
Controvérsia e lacuna: os estudos priorizam alternativas de um prédio ou de um campus, raramente tratam incerteza dos pesos e da normalização, e não validam a priorização contra resultados posteriores. Uma instituição pública multicampi brasileira com dados reais de chamados não aparece nos resultados buscados.
Uso no artigo: seção 2 (estado da arte de priorização), justificativa do índice de condição e de criticidade como comparadores, e da validação preditiva como diferencial.

### T2. Gestão de facilities sustentável

O que se encontrou: revisões indicam que a pesquisa em gestão de facilities sustentável é predominantemente ambiental e que abordagens estratégicas integradas são limitadas (R34); o campo atingiu certa maturidade (R35); agrupamentos recentes incluem planejamento, instalações inteligentes e energia (R36 e R37).
Lacuna: poucas ligações explícitas entre dados operacionais de manutenção e metas dos ODS.
Uso: seção 2 e discussão; ancora a dimensão de governança do pré-projeto.

### T3. ODS em universidades: o que os instrumentos medem e o que não medem

O que se encontrou: os rankings de impacto de universidades pontuam o ODS 9 sobretudo por receita de pesquisa com a indústria, empresas derivadas e patentes, o ODS 11 por pesquisa, patrimônio e artes e por práticas sustentáveis, e o ODS 12 por pesquisa, medidas operacionais, resíduos reciclados e relatório de sustentabilidade (R26, edição de 2025); o ranking de universidades verdes agrupa indicadores em infraestrutura, energia, resíduos, água, transporte e educação (R27, via fonte secundária). Revisões sistemáticas sobre ODS no ensino superior mostram concentração geográfica e foco em ensino e pesquisa, e indicam barreiras de implementação (R28 a R30); há quadros de indicadores para IES (R31) e estudos brasileiros com 61 (caso da UFSCar, via busca), 73 e 171 indicadores (R31 e R33, V3).
Lacuna provisória e relevante: a operação e a manutenção da infraestrutura física como fonte de evidência para o ODS 9 não têm, nos instrumentos localizados, uma métrica baseada em registros de manutenção. É o espaço que o artigo ocupa, desde que a revisão sistemática o confirme.
Uso: introdução (problema e lacuna), seção 2 (instrumentos existentes), quadro de vínculo entre critérios e metas.

### T4. Indicadores compostos e robustez

O que se encontrou: o manual da OECD e do Centro Comum de Pesquisa da Comissão Europeia define a construção em etapas, com robustez e sensibilidade como passo próprio (R01); Saisana, Saltelli e Tarantola (R02) propõem análise conjunta de incerteza e de sensibilidade e mostram que escolhas de modelagem se propagam aos postos; Saltelli e colaboradores (R04) mostram, por sensibilidade global, discrepâncias entre pesos declarados e importância efetiva; Greco e colaboradores (R03) revisam ponderação, agregação e robustez; Goldstein e Spiegelhalter (R05) mostram que rankings de instituições devem vir com intervalos, porque a incerteza dos postos é grande.
Debates: agregação compensatória contra não compensatória; críticas ao índice dos ODS por média simples (um artigo de 2025 em Sustainable Development propõe regras híbridas, V3).
Lacuna: a literatura de indicadores compostos raramente trata o erro de classificação de dados administrativos como fonte de incerteza.
Uso: espinha metodológica do artigo (seções 3 e 4); justificativa de apresentar intervalos de postos e perfil por ODS.

### T5. Decisão multicritério: pesos, incerteza, inversão de ranking e tempo

O que se encontrou: SMAA-2 (R08) trabalha com pesos incertos e entrega índices de aceitabilidade de postos, e a revisão de aplicações (R11) cataloga 118 artigos; o método Best-Worst (R12) reduz o número de comparações; a agregação de julgamentos de especialistas pelo AIJ e AIP (R13) é referência para painéis; o TOPSIS pode inverter ranking quando se altera o conjunto de alternativas (R14, R18); há guia de escolha de método MCDA para avaliação de sustentabilidade (R15); comparação de métodos fuzzy em priorização de manutenção de ativos de infraestrutura (R20). Trabalhos de MCDA temporal tratam séries como critérios e discutem normalização variável no tempo, mas, nos resultados da busca, não tratam previsões como critérios.
Lacuna provisória: aplicação de SMAA a priorização de manutenção de ativos construídos não foi localizada (o conteúdo do catálogo de R11 não foi examinado); critérios previstos em MCDA temporal não apareceram.
Uso: seção 3 (justificativa de SMAA e de BWM ou AHP), seção 4 (inversão de ranking e escolha de método), proposta de C10 (critério previsto).

### T6. Dados administrativos de chamados: qualidade, viés de notificação e classificação

O que se encontrou: dimensões de qualidade de dados que vão além da acurácia (R07); a propensão a reportar varia entre territórios e distorce decisões orientadas por dados (R44, solicitações 311 em cidade norte-americana); mineração textual de ordens de serviço para frequência de falhas (R38); aprendizado profundo sobre dados de sistemas de manutenção (R39, R51).
Lacuna: o viés de notificação em chamados de manutenção universitária e seu efeito sobre rankings de unidades não aparecem nos resultados; este estudo tem dados para medi-lo (diferença de 2 a 3 vezes na proporção de chamados com OS entre campi).
Uso: seção 3 (indicadores de qualidade de registro), seção 4 (efeito sobre postos), discussão (limites e viés).

### T7. Validade de conteúdo e consenso de especialistas

O que se encontrou: índice de validade de conteúdo, seus limites e a necessidade de corrigir concordância ao acaso (R23); recomendações sobre número de especialistas e limiar (R24); desenho de estudos Delphi (R25).
Uso: seção 3 (painel e validação), seção de ética e desenho; justifica a escolha do número de especialistas e dos limiares do protocolo.

### T8. Contexto regulatório e institucional brasileiro

Ver `03_CONTEXTO_BRASIL.md`: Lei 14.133/2021 (desenvolvimento sustentável como princípio e estudo técnico preliminar com impactos ambientais), plano de logística sustentável, acórdãos do TCU sobre manutenção predial em IFES, normas da ABNT, projeto de lei arquivado de política nacional de manutenção predial, e estudos brasileiros de indicadores em universidades.
Uso: introdução (relevância pública), discussão (uso do índice em ETP e TR e em prestação de contas).

### T9. Teoria: biossistemas construídos

O que se encontrou: ecologia urbana integra o componente humano e institucional aos processos ecológicos (R47); fundamentos de ecossistema e de sistemas vivos (R48, do pré-projeto).
Uso: quadro conceitual (Figura 1) e discussão; a literatura não oferece uma definição operacional de "biossistema construído" em manutenção predial, o que o pré-projeto pode propor com cautela (evitar metáfora sem consequência empírica; vincular a componentes físico, humano, tecnológico e ambiental mensuráveis).

### T10. Ciência aberta, relato e reprodutibilidade

R45 (princípios FAIR) e R46 (PRISMA 2020). Uso: pacote de replicação, declaração de dados e relato da revisão sistemática.

## 2. Debates que o artigo deve assumir e posição recomendada

1. Desempenho ou prioridade: adotar prioridade de manutenção (direção dos critérios coerente com alocação de recursos) e dizer por quê.
2. Compensação: mostrar o perfil por ODS e testar agregação geométrica; discutir a crítica às médias simples (T4).
3. Pesos: comparar iguais, objetivos (entropia ou CRITIC) e elicitados (AHP ou BWM); relatar a distância entre pesos declarados e importância efetiva (R04).
4. Ranking: relatar intervalos de postos e aceitabilidade, não posto pontual (R05, R08).
5. Validade: conteúdo, convergente e preditiva; a preditiva é o diferencial frente aos estudos de caso (T1).
6. Transparência contra aprendizado de máquina: justificar o índice transparente e posicionar modelos preditivos como critério (C10).
7. Escala e viés: normalizar por exposição e tratar a propensão a reportar (R44).

## 3. Lacunas identificadas, com o limite de cada uma

| Lacuna | Como foi encontrada | Limite |
|---|---|---|
| Métricas de ODS 9, 11 e 12 em rankings de universidades não usam registros de manutenção | página metodológica do ranking de impacto de 2025 | rankings mudam de ano para ano; consultar outras edições e o GreenMetric no site oficial |
| Revisões de facilities sustentável apontam predomínio ambiental e pouca integração estratégica | resumo de R34 | período coberto de 2007 a 2012 e outras revisões mais recentes a ler |
| Priorização de manutenção em universidades sem incerteza e sem validação preditiva | casos localizados (AHP com questionários e índice de condição) | amostra pequena de resultados de busca, não sistemática |
| SMAA aplicado a ativos construídos não localizado | busca geral | conteúdo do catálogo de aplicações (R11) não examinado |
| MCDA temporal com critérios previstos não localizado | busca geral | revisão específica ainda necessária |
| Viés de notificação em manutenção universitária não localizado | busca geral | existe em solicitações urbanas (R44) |
| Mineração de ordens de serviço sem priorização multicritério alinhada aos ODS | resultados de busca | cobertura parcial |

Todas as lacunas são provisórias e só valem para o artigo depois da revisão sistemática protocolada em `docs/auditoria/07_REVISAO_DE_LITERATURA.md`.

## 4. Temas adicionais para enriquecer o artigo

1. Equidade entre campi: distribuição de recursos de manutenção entre unidades de portes diferentes e a literatura de universidades multicampi (o acervo tem trabalho sobre dilemas das universidades multicampi); conecta com a normalização por exposição e com a leitura de "onde intervir primeiro".
2. Manutenção diferida e índice de condição das instalações (T1): oferecer um comparador de condição física e uma ponte com a gestão patrimonial.
3. Resiliência climática: chuva e calor como condicionantes da demanda (covariáveis do Artigo 2 e cenários).
4. Governança pública: alinhamento aos indicadores e às auditorias do Tribunal de Contas da União (ver `03_CONTEXTO_BRASIL.md`).
5. Dimensão social: satisfação do usuário e acessibilidade (o GLPI padrão tem pesquisa de satisfação; verificar uso).
6. Eficiência de recursos: consumo de energia e água por área, que ligaria o índice ao ODS 12 de modo mais direto (dado a obter).
7. Gêmeos digitais e BIM como horizonte: tratar como trabalho futuro, não como contribuição.
