from flask import Flask, render_template, request, session, redirect
import secrets

app = Flask(__name__)
app.secret_key = str(secrets.randbits(64))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user', methods=['POST']) 
def create_user():
    session['name'] = request.form['fullname']
    session['email'] = request.form['email']
    return redirect("/show")

@app.route('/show')
def show():
    return render_template('show.html')
    
if __name__ == "__main__":
    app.run(debug=True)