from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index1():
    return render_template('index1.html')

@app.route('/blog')
def blog1():
    return render_template('blog1.html')

@app.route('/contacts')
def contacts1():
    return render_template('contacts1.html')

if __name__ == '__main__':
    app.run(debug=True)