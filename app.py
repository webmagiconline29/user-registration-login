from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage for user data (Replace with a database in a real application)
users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        users.append({'username': username, 'password': password})
        return redirect(url_for('login'))
    else:
        return "Username and password are required."

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage for user data (Replace with a database in a real application)
users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        users.append({'username': username, 'password': password})
        return redirect(url_for('login'))
    else:
        return "Username and password are required."

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
