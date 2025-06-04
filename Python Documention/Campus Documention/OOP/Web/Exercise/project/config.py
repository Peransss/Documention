from flask_mysqldb import MySQL

class Config:
    def __init__(self, app):
        app.secret.key = 
        app.config['MYSQL_HOST'] = 'localhost'
        app.config['MYSQL_USER'] = 'root'
        app.config['MYSQL_PASSWORD'] = ' '
        app.config['MYSQL_DB'] = 'sm_ubm'
        
        self.mysql = MySQL(app)