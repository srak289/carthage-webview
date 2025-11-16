import asyncio

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application, url

from .views import ApiHandler, FileHandler, JSHandler

from tornado.log import enable_pretty_logging
enable_pretty_logging()

define('port', default=9000, help='port to listen on')

async def amain():
    """Construct and serve the tornado application."""
    app = Application([
        ('/', FileHandler),
        (r'/(.+\.js)', JSHandler),
        (r'/(.+)', FileHandler),
        (r'/api/(.+)', ApiHandler)
        #(r'/static/(.+)', FileHandler)
    ])
    app.listen(options.port)
    print(f'Listening on http://localhost: {options.port}')
    await asyncio.Future()
