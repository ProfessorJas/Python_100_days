from flask import Flask
from flask import request

app = Flask(__name__)       # create an application

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>/<age>')
def user(name, age):
    return '<h1>Hola, %s, you\'re %s years old. </h1>' % (name, age)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/users/', defaults={'page': 1})
@app.route('/users/page/<int:page>')
def show_users(page):
    return request.url

@app.route('/job/')
@app.route('/work/')
def show_works():
    return 'This is works page.'

@app.before_first_request
def first_quest():
    return "<h1>This runs first.</h1>"


if __name__ == "__main__":
    app.run(debug=True)