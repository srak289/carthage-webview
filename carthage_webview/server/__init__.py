from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application, url

from .views import ApiHandler, FileHandler, JSHandler

from tornado.log import enable_pretty_logging
enable_pretty_logging()

define('port', default=9000, help='port to listen on')

def main():
    """Construct and serve the tornado application."""
    app = Application([
        ('/', FileHandler),
        (r'/(.+\.js)', JSHandler),
        (r'/(.+)', FileHandler),
        (r'/api/(.+)', ApiHandler)
        #(r'/static/(.+)', FileHandler)
    ])
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    print(f'Listening on http://localhost: {options.port}')
    IOLoop.current().start()
