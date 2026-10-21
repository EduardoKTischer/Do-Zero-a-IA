"""Serve a apresentação Nilo e encaminha o chat para o Langflow local."""
import argparse
import json
import re
import socket
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit, quote
from urllib.request import Request, build_opener, ProxyHandler, HTTPRedirectHandler
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parent

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

OPENER = build_opener(ProxyHandler({}), NoRedirect())

def local_base(value):
    try:
        u = urlsplit(value)
        if (u.scheme != 'http' or u.hostname not in ('127.0.0.1', 'localhost')
                or u.username or u.password or u.path not in ('', '/') or u.query or u.fragment):
            raise ValueError()
        port = u.port or 7860
        if not 1 <= port <= 65535:
            raise ValueError()
        return f'http://127.0.0.1:{port}'
    except (ValueError, TypeError):
        raise ValueError('Use o endereço local do Langflow, por exemplo http://127.0.0.1:7860.')

class Handler(BaseHTTPRequestHandler):
    server_version = 'NiloLocal/1.0'

    def log_message(self, fmt, *args):
        pass  # Não registrar perguntas nem chaves.

    def origin_ok(self):
        port = self.server.server_port
        hosts = (f'127.0.0.1:{port}', f'localhost:{port}')
        origin = self.headers.get('Origin')
        return self.headers.get('Host') in hosts and (not origin or origin in tuple('http://' + h for h in hosts))

    def output(self, code, obj):
        data = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.end_headers()
        try:
            self.wfile.write(data)
        except (BrokenPipeError, ConnectionResetError):
            pass

    def do_GET(self):
        if not self.origin_ok():
            return self.output(403, {'error': 'Abra pelo endereço local exibido no terminal.'})
        path = urlsplit(self.path).path
        if path == '/api/health':
            return self.output(200, {'service': 'nilo-local', 'ready': True})
        if path not in ('/', '/index.html', '/Nilo-Apresentacao.html'):
            return self.output(404, {'error': 'Página não encontrada.'})
        data = (ROOT / 'Nilo-Apresentacao.html').read_bytes()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        if not self.origin_ok():
            return self.output(403, {'error': 'Origem não autorizada para o chat local.'})
        if self.path != '/api/chat':
            return self.output(404, {'error': 'Rota não encontrada.'})
        try:
            size = int(self.headers.get('Content-Length', '0'))
            if not 0 < size <= 65536:
                return self.output(413, {'error': 'A pergunta ou configuração excedeu o limite.'})
            data = json.loads(self.rfile.read(size))
            if not isinstance(data, dict):
                raise ValueError('Pedido inválido.')
            base = local_base(data.get('base', 'http://127.0.0.1:7860'))
            flow = data.get('flow_id', '')
            question = data.get('input_value', '')
            session = data.get('session_id', '')
            key = data.get('api_key', '')
            if not isinstance(flow, str) or not re.fullmatch(r'[A-Za-z0-9_-]{1,128}', flow):
                raise ValueError('Informe um Flow ID ou nome de endpoint válido do Langflow.')
            if not isinstance(question, str) or not question.strip() or len(question) > 12000:
                raise ValueError('Digite uma pergunta com até 12000 caracteres.')
            if not isinstance(session, str) or not re.fullmatch(r'[A-Za-z0-9_-]{1,160}', session):
                raise ValueError('Sessão inválida. Inicie uma nova conversa.')
            if not isinstance(key, str) or len(key) > 4096 or '\n' in key or '\r' in key:
                raise ValueError('Chave inválida.')
            payload = json.dumps({'input_value': question, 'session_id': session,
                                  'input_type': 'chat', 'output_type': 'chat'}).encode()
            headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
            if key:
                headers['x-api-key'] = key
            req = Request(base + '/api/v1/run/' + quote(flow, safe=''), data=payload, headers=headers, method='POST')
            with OPENER.open(req, timeout=120) as response:
                raw = response.read(4 * 1024 * 1024 + 1)
                if len(raw) > 4 * 1024 * 1024:
                    return self.output(502, {'error': 'A resposta do fluxo é muito grande.'})
                result = json.loads(raw)
            return self.output(200, result)
        except HTTPError as exc:
            messages = {401: 'O Langflow recusou a autenticação. Confira a API key.',
                        403: 'O Langflow negou o acesso. Confira a API key e as permissões do fluxo.',
                        404: 'Fluxo não encontrado no Langflow. Confira o endereço e o Flow ID.'}
            return self.output(502, {'error': messages.get(exc.code, f'O Langflow retornou HTTP {exc.code}. Confira o fluxo no Playground.'), 'upstream_status': exc.code})
        except (socket.timeout, TimeoutError):
            return self.output(504, {'error': 'O Langflow excedeu 120 segundos. Confira o modelo e tente uma pergunta menor.'})
        except URLError:
            return self.output(502, {'error': 'Não foi possível conectar ao Langflow local. Confirme se está aberto e confira o endereço.'})
        except (ValueError, TypeError, json.JSONDecodeError) as exc:
            return self.output(400, {'error': str(exc) or 'Pedido ou resposta inválidos.'})
        except Exception:
            return self.output(502, {'error': 'Falha na comunicação local. Confira o terminal e o fluxo no Langflow.'})

def main():
    parser = argparse.ArgumentParser(description='Nilo — apresentação e chat local')
    parser.add_argument('--port', type=int, default=4174)
    parser.add_argument('--no-browser', action='store_true')
    args = parser.parse_args()
    try:
        server = ThreadingHTTPServer(('127.0.0.1', args.port), Handler)
    except OSError:
        raise SystemExit(f'Porta {args.port} ocupada. Feche o servidor antigo ou use --port 4175.')
    url = f'http://127.0.0.1:{args.port}/'
    print(f'Nilo disponível em {url}\nMantenha este terminal aberto. Ctrl+C para encerrar.', flush=True)
    if not args.no_browser:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()

if __name__ == '__main__':
    main()
