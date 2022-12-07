from flask import Flask, render_template, url_for



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/404')
def error():
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

