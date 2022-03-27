from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html' , times = 3)

@app.route('/play/<int:times>')
def play(times):
    return render_template('index.html' , times = times)

@app.route('/play/<int:times>/<string:color>')
def color(times,color):
    return render_template('index.html' , times = times , color = color)


if __name__ =="__main__":
    app.run(debug=True)
