from cheroot import wsgi
from send_reply import app 

addr = '0.0.0.0', 5000
serv = wsgi.WSGIPathInfoDispatcher({'/': app})
server = wsgi.Server(addr, app)

if __name__ == '__main__':
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()
