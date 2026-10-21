# Do Zero à IA

## Roteiro da oficina local

Versão 2 para revisão de conteúdo | 21 de outubro de 2026. Oficina prática com Ollama, gemma3:1b, bge-m3 e Langflow. A T05 foi removida. A prática começa na T06 e as inserções usam sufixos para preservar os IDs anteriores. São 20 telas; o número de posição pode diferir do ID.

Este roteiro e a prévia HTML foram atualizados juntos. Os comandos de terminal usam PowerShell no Windows; os demais passos são executados no Langflow já instalado. Internet é necessária para os downloads iniciais. Os modelos, componentes e o fluxo devem ser ensaiados no computador real antes da oficina. A revisão não comprova que a integração local já foi executada.

Preserve os IDs ao revisar. Exemplo: T09C — alterar o prompt de resposta.

## T01 — Abertura

### Texto para a tela

Do Zero à IA: Execute seu próprio LLM. Construa a próxima camada: um agente local.

### Texto corrido para apresentação

Quanto da nossa experiência com inteligência artificial depende de serviços que estão fora do nosso computador? Hoje vamos olhar para as peças que permitem executar um modelo localmente e conectá-lo a uma aplicação. O Nilo vai acompanhar esse caminho: primeiro como personagem da apresentação e, na demonstração local, como interface para o fluxo criado no Langflow. A proposta é entender o papel de cada componente e observar o que o sistema realmente consegue fazer.

### Orientação de montagem

Preservar a primeira tela e sua identidade visual. Eduardo Kober Tischer. Semana Acadêmica TSI 2026, IFFar Campus Panambi, 21 de outubro de 2026, às 19h.

### Minha revisão

[Escreva aqui.]

### Status

A revisar

## T02 — Apresentação e trajetória

### Texto para a tela

Eduardo Kober Tischer em destaque. Analista de Automação e IA. Logomarca da Kepler Weber abaixo do cargo. Formação no quadro à direita.

### Texto corrido para apresentação

Sou Eduardo Kober Tischer, Analista de Automação e IA na Kepler Weber. Sou formado em Sistemas para Internet pelo IFFar Campus Panambi e pós-graduado em Ciência de Dados e Inteligência Artificial. Atualmente curso o mestrado em Modelagem Matemática e Computacional na UNIJUÍ. O LinkedIn estará disponível pelo QR Code para quem quiser acompanhar meu trabalho.

### Orientação de montagem

Abaixo do nome em destaque, exibir o cargo Analista de Automação e IA. Identificar a empresa somente pela logomarca oficial, sem repetir Kepler Weber em texto. Manter a formação no quadro à direita. Instituição da pós-graduação ainda a confirmar. LinkedIn: https://www.linkedin.com/in/ektischer/

### Minha revisão

[Escreva aqui.]

### Status

A revisar

## T03 — Por que executar localmente

### Texto para a tela

IA também pode rodar no seu computador. Controle do ambiente, integração com sistemas e limites de hardware.

### Texto corrido para apresentação

Executar um modelo localmente significa realizar a inferência no próprio computador. Depois de instalar os programas e baixar os arquivos necessários, podemos testar algumas tarefas sem depender de uma conexão com a internet. Isso dá mais controle sobre o ambiente e sobre o caminho dos dados, mas exige atenção à memória disponível e ao tempo de resposta. No nosso caso, a proposta é usar CPU e RAM. O modelo e o tamanho do contexto precisam caber nessa realidade. Se o fluxo chamar um serviço externo, essa parte continuará dependendo de rede.

### Orientação de montagem

Relacionar com o notebook da demonstração. Não apresentar desempenho ou funcionamento offline como já testados.

### Minha revisão

[Escreva aqui.]

### Status

A revisar

## T04 — Das redes neurais aos LLMs

### Texto para a tela

LLMs são redes neurais especializadas em linguagem. O treinamento ajusta os parâmetros; a geração estima probabilidades de próximos tokens com base no contexto.

### Texto corrido para apresentação

Uma rede neural artificial combina camadas de operações com parâmetros ajustados a partir de exemplos. Essa família de modelos pode trabalhar com imagens, números, áudio e texto. Os LLMs atuais pertencem a essa família e são especializados em linguagem; muitos usam a arquitetura Transformer. Em modelos como o Gemma, uma tarefa central do pré-treinamento é prever o próximo token. O modelo compara sua previsão com o texto de referência, mede o erro e usa esse sinal para ajustar parâmetros. Na geração, os parâmetros aprendidos são usados para estimar uma distribuição de probabilidades para o próximo token, considerando a instrução e o contexto disponível. A estratégia de seleção determina o token escolhido, e o processo se repete. Por exemplo, a continuação de “O aluno abriu o…” pode mudar conforme o contexto fale de leitura ou de computadores. Isso não torna a continuação um fato verificado. Uma resposta provável e fluente ainda pode estar errada.

### Passos

1. Rede neural artificial: família de modelos com parâmetros aprendidos.
2. Treinamento: exemplos → previsão → erro → ajuste dos parâmetros.
3. Geração: contexto → probabilidades dos próximos tokens → seleção e continuação.

### Resultado para conferir

Distinguir o aprendizado dos parâmetros do uso do modelo para gerar uma resposta.

### Orientação de montagem

A explicação de treinamento e probabilidade está integrada à relação entre rede neural e LLM nesta página. Não criar novamente a T05. Para geração comum, escrever um prompt não altera os pesos. Não usar percentuais inventados no exemplo.

### Minha revisão

[Escreva aqui.]

### Status

A revisar

## T06 — Preparar os modelos no Ollama

### Texto para a tela

Vamos executar Gemma 3 1B e preparar bge-m3 para o RAG.

### Texto corrido para apresentação

Com Ollama e Langflow já instalados, abrimos o PowerShell e verificamos o Ollama. Depois baixamos os dois modelos e conferimos a lista. O Gemma vai gerar as respostas. O bge-m3 transforma textos e perguntas em vetores para apoiar a busca. Os downloads exigem internet e devem ser preparados antes do encontro. LM Studio e llama.cpp são alternativas de execução; o laboratório segue com Ollama.

### Bloco para executar

```powershell
ollama --version
ollama pull gemma3:1b
ollama pull bge-m3
ollama list
```

### Resultado para conferir

Os dois modelos aparecem em ollama list.

### Orientação de montagem

Início da prática na T06. Programas previamente instalados. Se ollama não for reconhecido, abrir um terminal novo após a instalação. Escolher exatamente gemma3:1b.

### Minha revisão

[Escreva aqui.]

### Status

A revisar

## T06A — Executar com CPU no Windows

### Texto para a tela

No computador da demonstração, usar CPU e RAM.

### Texto corrido para apresentação

Para o notebook da demonstração, vamos iniciar o serviço sem a GPU NVIDIA. Primeiro encerramos o Ollama pelo ícone da bandeja, para não deixar um serviço antigo ocupando a porta. Em uma janela do PowerShell definimos as variáveis e iniciamos o servidor. Essa janela permanece aberta. Os comandos de teste serão digitados em uma segunda janela. Se aparecer que a porta já está em uso, precisamos encerrar o serviço antigo antes de tentar novamente.

### Bloco para executar

```powershell
$env:CUDA_VISIBLE_DEVICES="-1"
$env:OLLAMA_VULKAN="0"
ollama serve
```

### Passos

1. Encerrar Ollama na bandeja do Windows.
2. Executar estes comandos no terminal A.
3. Manter A aberto; usar outro PowerShell para os próximos passos.

### Resultado para conferir

Após carregar o modelo, conferir CPU na coluna PROCESSOR de ollama ps.

### Orientação de montagem

Etapa específica do Windows com NVIDIA. CUDA_VISIBLE_DEVICES é aplicada ao processo servidor, não apenas ao terminal do cliente. Não altera permanentemente o sistema. Confirmar CPU na versão instalada.

### Minha revisão

[Escreva aqui.]

### Status

A revisar

## T06B — Conversar com Gemma no terminal

### Texto para a tela

Primeiro uma resposta local. Depois, o fluxo visual.

### Texto corrido para apresentação

Em uma segunda janela, executamos o Gemma e digitamos uma pergunta curta. Por exemplo: explique o que é uma API em três frases. Observamos o tempo de resposta e avaliamos se a explicação faz sentido. O comando /bye é digitado dentro do chat para sair. De volta ao PowerShell, ollama ps mostra o modelo carregado e o processador utilizado. Antes de uma etapa que precise de memória, podemos descarregar o Gemma com ollama stop. Isso não apaga o modelo baixado.

### Bloco para executar

```powershell
ollama run gemma3:1b
```

### Passos

1. No chat: Explique o que é uma API em 3 frases.
2. No chat: /bye
3. No PowerShell: ollama ps
4. Para liberar memória: ollama stop gemma3:1b

### Resultado para conferir

Resposta recebida e execução em CPU conferida.

### Orientação de montagem

Ainda estamos demonstrando geração de texto, sem recuperação de documentos. Ensaiar com o notebook real; comandos não foram executados nele por esta revisão.

### Minha revisão

[Escreva aqui.]

### Status

A revisar

## T06C — Conectar o chat ao Langflow

### Texto para a tela

Chat Input → Ollama → Chat Output.

### Texto corrido para apresentação

No Langflow, criamos um fluxo vazio e adicionamos a entrada de chat, o componente Ollama e a saída de chat. No Ollama, informamos o endereço local e selecionamos gemma3:1b, atualizando a lista se necessário. Conectamos a mensagem de entrada ao modelo e a resposta do modelo à saída de chat. Abrimos o Playground e repetimos a pergunta do terminal. Isso permite conferir a ligação entre a interface visual e o executor local.

### Passos

1. Ollama Base URL: http://127.0.0.1:11434
2. Model Name: gemma3:1b
3. Ligar Chat Input → Input do Ollama.
4. Ligar saída Message ou Model Response → Chat Output.
5. Abrir Playground e enviar uma pergunta.

### Resultado para conferir

O Playground recebe uma resposta do Gemma.

### Orientação de montagem

Em versões com Language Model, selecionar o provedor Ollama. Os nomes de portas variam. Para chat simples usar a saída de resposta Message, não a porta LanguageModel destinada a outros componentes. localhost pressupõe mesmo computador, sem containers.

### Minha revisão

[Escreva aqui.]

### Status

A revisar

## T07 — O que torna um sistema um agente

### Texto para a tela

Objetivo, decisão, ferramenta e verificação. Um chat com LLM não demonstra sozinho um agente.

### Texto corrido para apresentação

Um modelo pode produzir uma explicação sem executar nenhuma ação fora do texto. Em um sistema agente, o modelo participa da escolha de passos e ferramentas para cumprir um objetivo, dentro das possibilidades oferecidas pela aplicação. Por exemplo, para responder uma pergunta sobre um cálculo, pode selecionar uma calculadora, receber o resultado e formular a resposta. O programa executa a chamada; o modelo não ganha acesso às ferramentas apenas por conhecê-las. Se o fluxo só recebe texto e devolve texto, demonstramos um chat. Para demonstrar um agente, precisamos observar uma ferramenta real sendo selecionada e utilizada.

### Orientação de montagem

Exibir apenas ferramentas efetivamente configuradas. O nome Agent de um componente não comprova execução de ferramentas. Com Gemma 3 1B, manter o chat e o RAG como prática principal. Não depender de tool calling para concluir o laboratório.

### Minha revisão

[Escreva aqui.]

### Status

A revisar

## T08 — Engenharia de Prompt

### Texto para a tela

Papel, tarefa, contexto, público e formato. Escolha a abordagem: zero-shot, few-shot, passo a passo ou interativo.

### Texto corrido para apresentação

Engenharia de Prompt é a prática de formular, testar e ajustar instruções para uma tarefa. Podemos organizar o pedido em cinco partes. Papel define a perspectiva; tarefa diz o que fazer; contexto fornece informações e limites; público indica quem vai ler; formato descreve a entrega. Essas partes formam um guia, não uma ordem obrigatória. As abordagens também variam. Zero-shot apresenta o pedido sem exemplos. Few-shot inclui alguns exemplos de entrada e saída para orientar o padrão, sem retreinar o modelo. Passo a passo divide o trabalho em etapas que podemos conferir. Na abordagem interativa, o sistema faz perguntas, recebe feedback e ajusta a próxima etapa. Podemos combinar essas estratégias: pedir ao Nilo que primeiro faça uma pergunta sobre nossa dificuldade e, depois da resposta, apresente apenas o próximo passo do laboratório. No Playground, vamos comparar um pedido aberto com um pedido estruturado, mantendo o mesmo modelo e verificando o resultado.

### Bloco para executar

```text
Papel: voce e um tutor de TSI.
Tarefa: explique uma API REST.
Contexto: o aluno conhece HTTP, mas nunca criou uma API.
Publico: estudante iniciante de TSI.
Formato: ate 4 frases, com uma analogia simples.
```

### Passos

1. Papel: Qual atuação ou perspectiva o modelo deve adotar?
2. Tarefa: O que ele deve fazer?
3. Contexto: Quais informações e limites precisa considerar?
4. Público: Para quem a resposta será escrita?
5. Formato: Como a resposta deve ser entregue?
6. Zero-shot: Pedido sem exemplos de resposta.
7. Few-shot: Alguns exemplos para orientar o padrão.
8. Passo a passo: Dividir a tarefa em etapas e conferir os resultados.
9. Interativo: Perguntar, receber feedback e ajustar a próxima etapa.
10. No Playground, comparar “Explique APIs” com o pedido estruturado.

### Resultado para conferir

Comparar clareza, formato e correção; exemplos no prompt não alteram os pesos.

### Orientação de montagem

Página 10 da sequência atual, ID T08 preservado. “Etapas do prompt” é um guia de composição, não uma regra universal. Few-shot usa exemplos de entrada e saída. Passo a passo pede etapas e resultados verificáveis; não promete acesso ao raciocínio interno. As abordagens podem ser combinadas.

### Minha revisão

[Escreva aqui.]

### Status

A revisar

## T09 — RAG e os dois modelos

### Texto para a tela

Embeddings são representações numéricas do texto. bge-m3 cria os vetores, Chroma recupera os trechos e Gemma gera a resposta.

### Texto corrido para apresentação

Embeddings são representações numéricas de um texto, organizadas em um vetor de números. O modelo aprende representações que ajudam a comparar textos por proximidade de significado, sem depender apenas de palavras iguais. No nosso RAG, dividimos os documentos em trechos e usamos bge-m3 para criar os embeddings. O banco vetorial armazena cada vetor junto do trecho e de seus metadados, como o arquivo de origem. Na consulta, a pergunta passa pelo mesmo modelo de embeddings. O banco compara o vetor da pergunta com os vetores armazenados e recupera trechos próximos, que serão enviados como contexto ao Gemma. No exemplo visual, escolhemos uma pergunta sobre executar o Gemma: os trechos sobre Ollama e CPU são destacados. Ao trocar para uma pergunta sobre buscar documentos, o destaque muda para embeddings e Chroma. As posições do desenho são simuladas para explicar a ideia; os embeddings reais têm muitas dimensões. Proximidade na busca ajuda a recuperar candidatos, mas a resposta e as fontes continuam exigindo conferência.

### Passos

1. Preparação: documento → trechos → bge-m3 → Chroma.
2. Consulta: pergunta → bge-m3 → busca no Chroma.
3. Resposta: trechos + pergunta → gemma3:1b.

### Resultado para conferir

As funções de embeddings, recuperação e geração estão separadas.

### Orientação de montagem

Escolha de implementação: Chroma local. Conferir previamente a presença do componente na instalação do Langflow. Não usar um provedor de embeddings externo no template. Incluir a visualização didática do banco vetorial, com cinco trechos armazenados, uma pergunta e dois resultados destacados. Os botões Ollama e RAG alternam o exemplo. Não apresentar as posições simuladas como embeddings calculados nem como uma projeção real do bge-m3.

### Minha revisão

[Escreva aqui.]

### Status

A revisar

## T09B — Carregar o documento no Langflow

### Texto para a tela

Read File → Split Text → Chroma DB, com Ollama Embeddings.

### Texto corrido para apresentação

Vamos criar uma coleção local com um documento curto de teste. No fluxo de carga, conectamos Read File ao Split Text e os trechos à entrada Ingest Data do Chroma. Em Ollama Embeddings, selecionamos bge-m3 e a URL local do Ollama; sua saída vai para a entrada Embedding do Chroma. Definimos um nome de coleção e um diretório persistente. Executamos o componente Chroma para indexar o documento e inspecionamos os trechos. No fluxo de consulta usaremos exatamente a mesma coleção, diretório e modelo de embeddings.

### Passos

1. Ollama Embeddings: bge-m3; Base URL http://127.0.0.1:11434.
2. Read File → Split Text → Chroma Ingest Data.
3. Ollama Embeddings → Chroma Embedding.
4. Collection Name: nilo_oficina; Persist Directory: caminho local absoluto.
5. Começar com chunk 400 e overlap 60; ajustar após inspecionar.
6. Carregar o TXT de exemplo e executar Run component no Chroma.

### Resultado para conferir

O texto foi dividido e gravado na coleção local.

### Orientação de montagem

Tamanhos de chunk são pontos de partida, não valores universais. Guardar o caminho absoluto escolhido para reutilizá-lo na consulta. Usar arquivo TXT para evitar dependência de OCR. Não reindexar o mesmo arquivo repetidamente sem controle de duplicatas.

### Minha revisão

[Escreva aqui.]

### Status

A revisar

## T09C — Consultar os trechos e gerar a resposta

### Texto para a tela

Buscar primeiro. Montar o contexto. Responder com Gemma.

### Texto corrido para apresentação

No fluxo de consulta, ligamos a pergunta à entrada Search Query do Chroma e ao campo pergunta do Prompt. Conectamos Ollama Embeddings com bge-m3 ao Chroma e reutilizamos a mesma coleção e diretório da carga. Os resultados da busca passam por um Parser para virar texto, preservando o campo text e a identificação da fonte quando disponível. Esse texto alimenta contexto no Prompt. A saída do Prompt vai para Ollama com gemma3:1b e a resposta vai para Chat Output. Começamos recuperando até três trechos e verificamos se são pertinentes.

### Bloco para executar

```text
Responda somente com o contexto abaixo.
Se a resposta nao estiver nele, diga que nao encontrou.
Contexto: {contexto}
Pergunta: {pergunta}
```

### Passos

1. Chat Input → Chroma Search Query e Prompt pergunta.
2. bge-m3 → Chroma Embedding; mesma coleção e diretório.
3. Chroma Search Results → Parser → Prompt contexto.
4. Prompt → Ollama gemma3:1b → Chat Output.
5. Número de resultados: começar com 3 e conferir os trechos.

### Resultado para conferir

A busca retorna trechos e o Gemma responde a partir deles.

### Orientação de montagem

O bloco é um Prompt Template, não um comando de terminal. Configurar o Parser conforme a saída Data ou DataFrame da versão instalada. Conferir no output o campo text e metadados. A instrução reduz respostas sem apoio, mas não garante fidelidade.

### Minha revisão

[Escreva aqui.]

### Status

A revisar

## T09D — Verificar se o RAG funcionou

### Texto para a tela

Conferir a resposta e o trecho que a sustenta.

### Texto corrido para apresentação

Vamos usar um documento fictício com informações específicas que conseguimos conferir. Perguntamos o código do laboratório e o horário de atendimento, ambos presentes no texto. Depois fazemos uma pergunta que o documento não responde. Inspecionamos os resultados recuperados e comparamos a resposta com a fonte. Se o sistema inventar uma resposta, registramos a falha e revisamos o prompt e a recuperação. Não basta receber uma frase correta: precisamos observar que a busca realmente entregou a evidência usada.

### Passos

1. Perguntar: Qual é o código do laboratório?
2. Perguntar: Em que dia e horário ocorre o atendimento de testes?
3. Perguntar: Qual é o orçamento anual? Essa informação não está no TXT.
4. Inspecionar Search Results e comparar com o arquivo original.

### Resultado para conferir

Evidência recuperada conferida; pergunta sem resposta testada.

### Orientação de montagem

Documento de teste fictício incluído na prévia, disponível para download. Referências esperadas: NILO-427; terças-feiras das 14h às 16h. Não há orçamento no arquivo. Não confundir esses dados com regras reais do evento.

### Minha revisão

[Escreva aqui.]

### Status

A revisar

## T10 — Fine tuning e adaptação

### Texto para a tela

Fine-tuning continua o treinamento com exemplos específicos. RAG fornece contexto durante a consulta.

### Texto corrido para apresentação

No fine-tuning, partimos de um modelo existente e continuamos seu treinamento com um conjunto de exemplos. Esse processo pode ajudar a adaptar padrões de resposta, estilo ou comportamento para uma tarefa. Diferentemente do RAG, ele envolve modificar parâmetros treináveis. Para uma pergunta sobre documentos que mudam com frequência, recuperar os trechos atuais costuma ser um caminho a considerar. Para adaptar um comportamento recorrente, o fine-tuning pode ser uma alternativa, desde que haja dados adequados e avaliação. As duas técnicas podem coexistir. Nenhuma delas elimina, por si só, as respostas incorretas.

### Orientação de montagem

Conceito de fine-tuning em comparação com o RAG que acabamos de montar. Não haverá treinamento de modelo durante a oficina.

### Minha revisão

[Escreva aqui.]

### Status

A revisar

## T11 — Skills e procedimentos reutilizáveis

### Texto para a tela

Uma Skill reúne instruções e recursos para uma tarefa recorrente. Seu uso depende do suporte da aplicação.

### Texto corrido para apresentação

Uma Skill pode funcionar como um procedimento reutilizável: ela descreve como realizar uma tarefa e pode incluir exemplos, arquivos ou scripts de apoio. Pense em uma revisão de relatório que sempre exige verificar estrutura, linguagem e referências. Em vez de explicar esse processo do início a cada conversa, podemos organizá-lo como uma habilidade que uma aplicação compatível carrega quando necessário. Isso não significa treinar o modelo nem alterar seus pesos. Também não significa que qualquer ferramenta leia automaticamente um arquivo chamado SKILL.md. O mecanismo de descoberta e execução precisa existir no ambiente.

### Passos

1. No Prompt do RAG, acrescentar: identifique a pergunta; confira os trechos; responda com a evidência; indique quando faltar informação.
2. Testar novamente a pergunta sem resposta.

### Orientação de montagem

Usar a analogia do manual de bancada. Distinguir procedimento, ferramenta executável e treinamento. Nesta prática, aplicar o procedimento no Prompt demonstra instruções reutilizáveis; não afirmar que Langflow carregou uma Skill nativa.

### Minha revisão

[Escreva aqui.]

### Status

A revisar

## T12 — MCP e APIs

### Texto para a tela

APIs oferecem acesso a funcionalidades. MCP padroniza a integração de aplicações de IA com ferramentas e contexto.

### Texto corrido para apresentação

Uma API define como um sistema oferece acesso a dados ou funcionalidades. O Model Context Protocol, ou MCP, estabelece um padrão de comunicação para aplicações de IA integrarem ferramentas e fontes de contexto. Um servidor MCP pode, por exemplo, disponibilizar uma ferramenta que consulta uma API já existente. Por isso, MCP e API não são sinônimos, e o protocolo não substitui todas as APIs. Ele organiza uma camada de integração. Conectar um servidor também não torna a aplicação autônoma: continuam necessários lógica de execução, permissões adequadas e verificação dos resultados.

### Bloco para executar

```powershell
Invoke-RestMethod "http://127.0.0.1:11434/api/tags"
```

### Passos

1. Executar no PowerShell para listar os modelos pela API.
2. Relacionar essa chamada à URL usada no Langflow.
3. Apresentar MCP como próximo passo de integração, sem exigir instalação nesta oficina.

### Resultado para conferir

A API local retorna a lista de modelos.

### Orientação de montagem

Exemplo conceitual: aplicação de IA → servidor MCP → API de um sistema. Não apresentar MCP como integrado ao laboratório sem configuração e teste.

### Minha revisão

[Escreva aqui.]

### Status

A revisar

## T13 — Laboratório com Nilo

### Texto para a tela

Na versão local, Nilo conversa pelo Langflow e Ollama. Na versão pública, oferece dicas previamente escritas.

### Texto corrido para apresentação

A apresentação agora tem um ponto de acesso ao agente em qualquer tela. No canto superior direito, o botão Pergunte ao Nilo abre o chat em um modal. Para conectar, iniciamos o pacote local e informamos em Conexão o endereço do Langflow, o Flow ID e a API key exigida pela instalação. A pergunta segue para o fluxo, que usa os modelos e documentos configurados. A resposta retorna para o mesmo modal. Podemos fechar o chat, continuar a apresentação e reabrir a conversa na mesma aba. Se o serviço estiver indisponível, a interface mostra a falha e permite conferir a configuração.

### Passos

1. Abrir Ollama e Langflow e validar o fluxo no Playground.
2. Extrair Nilo-Laboratorio-Local.zip e executar iniciar_nilo.bat.
3. Clicar em Pergunte ao Nilo, abaixo de Telas e Fala.
4. Em Conexão, informar endereço local, Flow ID e a API key exigida pelo Langflow.
5. Enviar a pergunta e conferir o retorno no modal.

### Orientação de montagem

O modal mantém a apresentação na tela atual. Enter envia, Shift+Enter cria outra linha, Escape fecha. A conversa usa um session_id próprio; o histórico do fluxo depende da configuração no Langflow. A chave fica apenas em memória nesta aba. O pacote local inclui o servidor de apoio e requer Python 3, Ollama e Langflow instalados. O fluxo real precisa ser ensaiado no computador do usuário.

### Minha revisão

[Escreva aqui.]

### Status

A revisar

## T13A — Fontes de consulta e estudo

Para continuar os estudos, o guia da Unsloth apresenta fundamentos de fine-tuning, e o Hugging Face reúne modelos, datasets e recursos da comunidade. Para consultar as ferramentas e os requisitos de execução, use os sites oficiais de llama.cpp, Ollama, LM Studio e Python. Nesta oficina seguimos com Ollama; llama.cpp e LM Studio são alternativas. Os links podem ser abertos diretamente pela apresentação.

### Consulta e estudo

- [Unsloth](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide) — Guia de fine-tuning de LLMs
- [Hugging Face](https://huggingface.co/) — Modelos, datasets e comunidade

### Requisitos e ferramentas

- [llama.cpp](https://github.com/ggml-org/llama.cpp) — Execução de LLMs em C/C++
- [Ollama](https://ollama.com/) — Modelos e execução local
- [LM Studio](https://lmstudio.ai/) — Aplicação para usar modelos locais
- [Python](https://www.python.org/downloads/) — Downloads oficiais do Python

## T14 — Encerramento e próximo experimento

### Texto para a tela

Gemma respondendo, documento indexado e busca verificada. Seu próximo experimento começa daqui.

### Texto corrido para apresentação

O próximo passo pode ser simples: escolher uma tarefa útil, executar um modelo compatível com o computador e criar um critério para avaliar a resposta. Depois podemos acrescentar documentos, uma ferramenta ou um procedimento reutilizável, conforme a necessidade. O importante é saber o que cada camada faz e observar o comportamento do sistema em testes reais. O Nilo serve como ponto de partida para esse percurso. Vamos encerrar com perguntas e com o convite para transformar uma ideia pequena em um experimento que vocês consigam explicar, executar e verificar.

### Orientação de montagem

Exibir QR Code real do LinkedIn. Abrir espaço para perguntas e indicar o material de apoio.

### Minha revisão

[Escreva aqui.]

### Status

A revisar

## Documento fictício para o RAG

```text
MANUAL FICTICIO DO LABORATORIO NILO
Documento de exemplo para testar RAG. As informacoes abaixo sao inventadas para a oficina e nao descrevem regras reais do evento.

IDENTIFICACAO
O codigo do laboratorio e NILO-427. Os participantes devem informar esse codigo ao registrar um teste. O objetivo do ambiente e praticar a execucao local de modelos e a consulta a documentos, verificando as respostas com base no texto original.

ATENDIMENTO
O atendimento de testes ocorre as tercas-feiras, das 14h as 16h. Esse horario pertence somente a este manual ficticio. Para registrar uma duvida, anote a pergunta, os trechos recuperados e a resposta gerada.

PROCEDIMENTO
Antes de um novo teste, confirme qual documento esta na colecao. Depois da consulta, compare a resposta com o trecho recuperado. Se a informacao nao estiver no documento, registre que nao foi encontrada. Este manual nao informa orcamento anual.
```

## Referências de apoio

- Gemma 3: https://ollama.com/library/gemma3
- bge-m3: https://ollama.com/library/bge-m3
- CPU e GPU: https://docs.ollama.com/gpu
- Embeddings API: https://docs.ollama.com/api/embed
- Ollama no Langflow: https://docs.langflow.org/bundles-ollama
- Fluxo RAG: https://docs.langflow.org/chat-with-rag
- Chroma no Langflow: https://docs.langflow.org/bundles-chroma
