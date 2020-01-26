from flask import Flask


app=Flask(__name__)


@app.route('/')
def index():

    return 'hello there im smart homes'

@app.route('/turn-on')
def on():
    return 'turning on now ..'
@app.route('/turn-off')
def off():
    return 'turning off now ..'
if __name__ == '__main__':
    app.run(port=80,debug=True)