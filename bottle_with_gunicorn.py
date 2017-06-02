from bottle import Bottle, run

# The line sets the "app" object for the WSGI server to run.
app = Bottle ()

# use @app.route instead of @route
@app.route('/')
def index():
    return '<h1>Hello Bottle!</h1>'

# must have this 'main' for using gunicorn with multiple workers
if __name__ == "__main__":
    run(app, host='localhost', port=8080, reloader=True, debug=True)

# Run it:
# gunicorn -w 4 -b 127.0.0.1:8080 --log-file=/tmp/gunicorn.log bottle_with_gunicorn:app

