from flask import Flask, flash, redirect, render_template, request, url_for, session
from config import Config
import os, pdfkit

class Portal:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = '!@#$123456&*()'
        self.con = Config()
        self.routes()
        
    def routes(self):
        @self.app.route('/testdb')
        def test_db():
            try:
                if self.con.mysql is not None:
                    return "Database connection succesful!"
            except Exception as e:
                return f"Database connection failed: {e}"
        
        # Account    
        @self.app.route('/data-account')
        def readAccount():
            cur         = self.con.mysql.cursor()
            cur.execute('SELECT * FROM account')
            data        = cur.fetchall()
            cur.close()
            return render_template('readAccount.html',data=data)
        
        @self.app.route('/create-account/')
        def createAccount():
            return render_template('createAccount.html')

        @self.app.route('/create-account/process', methods=['POST'])
        def createAccountProcess():
            if request.method == 'POST':
                email       = request.form['email']
                username    = request.form['username']
                fullname    = request.form['fullname']
                bio         = request.form['bio']
                password    = request.form['password']
                cur         = self.con.mysql.cursor()
                try:
                    cur.execute('INSERT INTO account (email, username, fullname, bio, password) VALUES (%s, %s, %s, %s, md5(%s))', (email,username,fullname,bio,password))
                    self.con.mysql.commit()
                    flash('Account created successfully!', 'success')
                except Exception as e:
                    flash("Account creation failed: "+ str({e}), 'error')
                cur.close()
                return redirect(url_for('readAccount'))
                # return redirect('data-account')
        
        @self.app.route('/update-account/<string:email>')
        def updateAccount(email):
            cur         = self.con.mysql.cursor()
            cur.execute('SELECT * FROM account WHERE email = %s', (email,))
            data        = cur.fetchone()
            cur.close()
            return render_template('updateAccount.html',data=data)

        @self.app.route('/update-account/process', methods=['POST'])
        def updateAccountProcess():
            if request.method == 'POST':
                email       = request.form['email']
                username    = request.form['username']
                fullname    = request.form['fullname']
                bio         = request.form['bio']
                password    = request.form['newpass']
                cur         = self.con.mysql.cursor()
                try:
                    if password=="":
                        cur.execute('UPDATE account SET username = %s, fullname = %s, bio = %s WHERE email = %s', (username,fullname,bio,email))
                    else:
                        cur.execute('UPDATE account SET username = %s, fullname = %s, bio = %s, password = md5(%s) WHERE username = %s', (username,fullname,bio,password,email))
                    
                    self.con.mysql.commit()
                    flash('Account updated successfully!', 'success')
                except Exception as e:
                    flash("Account updated failed: "+ str({e}), 'error')
                cur.close()
                return redirect(url_for('readAccount'))
        
        @self.app.route('/delete-account/<string:email>')
        def deleteAccount(email):
            cur         = self.con.mysql.cursor()
            try:
                cur.execute('DELETE FROM account WHERE email = %s', (email,))
                self.con.mysql.commit()
                flash('Account deleted successfully!', category='success')
            except Exception as e:
                flash("Account deleted failed: "+ str({e}), category='error')
            cur.close()
            return redirect(url_for('readAccount'))
        # End Account
        
        # Posting
        @self.app.route('/data-posting')
        def readPosting():
            cur         = self.con.mysql.cursor()
            cur.execute('SELECT * FROM posting')
            data        = cur.fetchall()
            cur.close()
            return render_template('readPosting.html',data=data)
        
        @self.app.route('/create-posting/')
        def createPosting():
            cur         = self.con.mysql.cursor()
            cur.execute('SELECT username, fullname FROM account')
            data        = cur.fetchall()
            cur.close()
            return render_template('createPosting.html',data=data)
        
        @self.app.route('/create-posting/process', methods=['POST'])
        def createPostingProcess():
            if request.method == 'POST':
                title       = request.form['title']
                image       = request.files['image']
                content     = request.form['content']
                published   = request.form['published']
                userpost    = request.form['userpost']
                cur         = self.con.mysql.cursor()
                try:
                    image.save(os.path.join("sm_ubm\\static\\upload_image", image.filename))
                    cur.execute('INSERT INTO posting (title, image, content, publish_date, userpost) VALUES (%s, %s,%s, %s, %s)', (title, image.filename, content, published, userpost))
                    self.con.mysql.commit()
                    flash('Posting created successfully!', 'success')
                except Exception as e:
                    flash("Posting creation failed: "+ str({e}), 'error')
                cur.close()
                return redirect(url_for('readPosting'))
        
        @self.app.route('/update-posting/<int:id>')
        def updatePosting(id):
            cur         = self.con.mysql.cursor()
            cur.execute('SELECT * FROM posting WHERE idposting = %s', (id,))
            dtpost        = cur.fetchone()
            
            cur.execute('SELECT username, fullname FROM account')
            dtuser        = cur.fetchall()
            cur.close()
            return render_template('updatePosting.html',dtpost=dtpost,dtuser=dtuser)
        
        @self.app.route('/update-posting/process', methods=['POST'])
        def updatePostingProcess():
            if request.method == 'POST':
                idposting   = request.form['idposting']
                title       = request.form['title']
                old_image   = request.form['oldimage']
                image       = request.files['image']
                content     = request.form['content']
                published   = request.form['published']
                userpost    = request.form['userpost']
                cur         = self.con.mysql.cursor()
                try:
                    if image.filename=="":
                        cur.execute('UPDATE posting SET title = %s, content = %s, publish_date = %s, userpost = %s WHERE idposting = %s', (title,content,published,userpost,idposting))
                    else:
                        os.remove(os.path.join("sm_ubm\\static\\upload_image", old_image))
                        image.save(os.path.join("sm_ubm\\static\\upload_image", image.filename))
                        cur.execute('UPDATE posting SET title = %s, image = %s, content = %s, publish_date = %s, userpost = %s WHERE idposting = %s', (title,image.filename,content,published,userpost,idposting))
                    self.con.mysql.commit()
                    flash('Posting updated successfully!', 'success')
                except Exception as e:
                    flash("Posting updated failed: "+ str({e}), 'error')
                cur.close()
                return redirect(url_for('readPosting'))
        
        @self.app.route('/delete-posting/<int:id>')
        def deletePosting(id):
            cur         = self.con.mysql.cursor()
            try:
                cur.execute('SELECT image FROM posting WHERE idposting = %s', (id,))
                data = cur.fetchone()
                os.remove(os.path.join("sm_ubm\\static\\upload_image", data[0]))
                cur.execute('DELETE FROM posting WHERE idposting = %s', (id,))
                self.con.mysql.commit()
                flash('Posting deleted successfully!', category='success')
            except Exception as e:
                flash("Posting deleted failed: "+ str({e}), category='error')
            cur.close()
            return redirect(url_for('readPosting'))
        # End Posting 
        
        @self.app.route('/')
        def index():
            if session.get('username') is not None:
                return render_template('index.html')
            else:
                return redirect(url_for('login'))    
        
        @self.app.route('/login', methods=['GET', 'POST'])
        def login():
            if request.method == 'POST':
                email       = request.form['email']
                password    = request.form['password']
                cur         = self.con.mysql.cursor()
                try:
                    cur.execute('SELECT * FROM account WHERE email=%s AND password=md5(%s)', (email,password))
                    self.con.mysql.commit()
                    data        = cur.fetchone()
                    cur.close()
                    session['username'] = data[1]
                    return redirect(url_for('index'))
                except Exception as e:
                    flash("Login failed: "+ str({e}), 'error')
                    return render_template('login.html')
            return render_template('login.html')
        
        @self.app.route('/logout')
        def logout():
            session.pop('username', None)
            return redirect(url_for('login'))
        
        @self.app.route('/report-account')
        def pdf():
            cur         = self.con.mysql.cursor()
            cur.execute('SELECT * FROM account')
            data        = cur.fetchall()
            cur.close()
            rendered = render_template('reportAccount.html', data=data)
            configpdf = pdfkit.configuration(wkhtmltopdf = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
            pdfkit.from_string(rendered, 'sm_ubm/static/pdf/report.pdf',configuration= configpdf)
            flash('Success Download Report', 'success')
            return redirect(url_for('readPosting'))
        
    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    portal = Portal()
    portal.run()