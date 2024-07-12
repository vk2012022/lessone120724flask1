from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index1():
    return render_template('index1.html', active_page='index')

@app.route('/blog')
def blog1():
    return render_template('blog1.html', active_page='blog')

@app.route('/contacts')
def contacts1():
    return render_template('contacts1.html', active_page='contacts')

if __name__ == '__main__':
    app.run(debug=True)
