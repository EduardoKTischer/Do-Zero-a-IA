# Nilo — apresentação e agente local

1. Extraia o ZIP em uma pasta.
2. Abra o Ollama e o Langflow. Confira seu fluxo no Playground.
3. No Windows, execute iniciar_nilo.bat. É necessário Python 3 instalado. Em outro sistema, use python3 servidor_nilo.py.
4. A apresentação abre em http://127.0.0.1:4174/. Mantenha o terminal aberto.
5. Clique em “Pergunte ao Nilo”, abaixo de “Telas” e “Fala”.
6. Em Conexão, informe a URL local do Langflow (normalmente http://127.0.0.1:7860), o Flow ID de Share → API access → v1 e a API key, quando exigida.
7. Clique em “Usar esta conexão” e envie a pergunta.

Enter envia; Shift+Enter cria nova linha. Escape fecha o modal. O chat permanece na mesma aba ao fechar e reabrir. “Nova conversa” inicia outro session_id; a memória do fluxo depende da sua configuração no Langflow. A API key permanece em memória na aba e não é gravada em arquivo ou localStorage.

O servidor local encaminha as perguntas para POST /api/v1/run/{flow_id}. Não substitui nem inicia o Langflow, o Ollama, o banco vetorial ou o modelo. Não há respostas de IA simuladas no pacote. O fluxo e os modelos reais devem ser configurados no computador da demonstração.

Para apenas revisar o visual, abra Nilo-Apresentacao.html. Para conversar, use o iniciador, pois o HTML sozinho não tem o servidor de apoio.

Se a porta estiver ocupada: python servidor_nilo.py --port 4175
Se houver erro 401/403: confira a API key.
Se houver erro 404: confira a URL e o Flow ID.
Se o serviço não responder: confirme que Langflow e Ollama estão abertos.
Para encerrar: Ctrl+C no terminal.

Modelos da oficina: gemma3:1b para geração; bge-m3 para embeddings do RAG. A estrutura do fluxo continua pendente da conferência com os prints do usuário.

API oficial: https://docs.langflow.org/api-flows-run
