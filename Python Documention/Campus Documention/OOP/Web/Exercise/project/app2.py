from flask import Flask
from config import Config

class Portal:
    def __init__(self):
        self.app = Flask(__name__)
        self.con = Config(self.app)
        self.routes()
        
    def routes(self):
        @self.app.route('/testdb')
        def test_db():
            try:
                if self.con.mysql.connection is not None:
                    return 'Database connection succesful!'
            expect Exception as e:
                return f'Database connection failed : {e}'