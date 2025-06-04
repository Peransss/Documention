from flask import Flask, render_template

class Example:
    def __init__(self):
        self.app = Flask(__name__)
        self.routes()
        
    def routes(self):
        @self.app.route('/')
        def index():
            return render_template('home.html')
        
        @self.app.route('/kevin')
        def halkevin():
            hobi = 'Main Gitar'
            food = ['Sayur Hijau', 'Ayam Goreng', 'Pisang Coklat']
            return render_template('about.html', hob=hobi, fo=food)
    
        @self.app.route('/kevin')
        def haikevin():
            return 'Hai Saya Kevin'
        
    def run(self):
        self.app.run(debug=True)
        
if __name__ == '__main__':
    example = Example()
    example.run()

    