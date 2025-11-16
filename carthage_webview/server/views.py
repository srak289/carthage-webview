from tornado.web import RequestHandler

from pathlib import Path

FILE_ROOT = Path(__file__).parent.parent/'static'

class FileHandler(RequestHandler):
    def get(self, path='index.html'):
        with open(str(FILE_ROOT/path), 'rb') as f:
            self.write(f.read())

class JSHandler(FileHandler):
    def prepare(self):
        self.set_header("Content-Type", 'application/javascript; charset="utf-8"')

class ApiHandler(RequestHandler):
    def get(self):
        self.write('Hello')
