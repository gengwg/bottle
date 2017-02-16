from bottle import Bottle, run, template, get, request, redirect, abort, static_file

app = Bottle()

@app.route('/hello')
#@get('/hello')
def hello():
    return "Hello World!"


# $ curl http://localhost:8080/hello/action=are/name=buddy
# Hello buddy, how are you?
@app.route('/hello/action=:action/name=:name')
def greet(action='test', name='Stranger'):
    return template('Hello {{name}}, how {{action}} you?', name=name, action=action)


# curl "http://localhost:8080/forum?id=1&page=5"
@app.route('/forum')
def display_forum():
    forum_id = request.query.id
    page = request.query.page or '1'
    return template('Forum ID: {{id}} (page {{page}})', id=forum_id, page=page)


# curl -L http://localhost:8080/redirect
@app.route('/redirect')
def redirect_to_hello():
    redirect('/hello')


# curl http://localhost:8080/static/test
# wget http://localhost:8080/static/image.png
@app.route('/static/:filename')
def serve_static(filename):
    return static_file(filename, root='/tmp')


run(app, host='localhost', port=8080, reloader=True)

