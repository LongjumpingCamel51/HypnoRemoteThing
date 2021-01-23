import os, http.server, threading, json, queue, socketserver
from urllib.parse import unquote

try:
  PORT = int(os.environ['PORT'])
except Exception as e:
  PORT = 4080

COMMAND_QUEUE = queue.Queue()

with open('sub.htm', 'rb') as f:
  SUB_HTM = f.read()

with open('dom.htm', 'rb') as f:
  DOM_HTM = f.read()

class Handler(http.server.BaseHTTPRequestHandler):
  def respond(s, type, content):
    s.send_response(200)
    s.send_header('Content-type', type)
    s.end_headers()
    s.wfile.write(content)

  def do_GET(s):
    path = s.path.encode()
    spath = s.path.split('/')
    try:
      if spath[1] == 'sub': return s.respond('text/html', SUB_HTM)
      if spath[1] == 'dom': return s.respond('text/html', DOM_HTM)
      if spath[1] == 'get_command': return s.respond('application/json', json.dumps(COMMAND_QUEUE.get()).encode())

      # XXX shouldn't use GET to do something that mutates data but I'm too lazy to do it the right way
      if spath[1] == 'put_command':
        COMMAND_QUEUE.put(unquote(spath[2]).strip())
        return s.respond('application/json', b'"OK"')
    except IndexError:
      pass

    s.respond('text/html', b"If you're seeing this, the server is working but you have entered an invalid path.<br><br>You entered: " + path)

class Server(socketserver.ThreadingMixIn, http.server.HTTPServer):
  pass

def main():
  httpd = Server(('', PORT), Handler)
  httpd.serve_forever()

if __name__ == '__main__':
  main()
