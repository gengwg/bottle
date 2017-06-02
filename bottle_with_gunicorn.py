from bottle import Bottle, run

app = Bottle ()

@app.route('/')
def index():
    return '<h1>Hello Bottle!</h1>'

if __name__ == "__main__": # must have this for using gunicorn with multiple workers
    run(app, host='localhost', port=8080, reloader=True, debug=True)

# gunicorn -w 4 -b 127.0.0.1:8080 --log-file=/tmp/gunicorn.log bottle_with_gunicorn:app

