from flask import Flask, request    # import pakage


app = Flask(__name__)               # create an application

@app.route('/')
def index():                        # define the funtion for the root
    return '<h1>Hola Amigo!</h1>'

@app.route('/hello')
def hello():
    return "Say hello"

@app.route('/user/<name>')
def user(name):
    return '<h1>Hola, %s!</h1>' % name

@app.route('/users/<name>/<age>')
def users(name, age):
    return "<h1> Hello, %s, you're %s years old" % (name, age)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/post/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "do_the_login()"
    else:
        return "show_the_login_form()"

@app.route('/job/')
@app.route('/work/')
def show_works():
    return 'This is Work page.'

@app.route('/show_users/', defaults={'page':1})
@app.route('/show_users/page/<int:page>')
def show_users(page):
    pass


if __name__ == "__main__":
    app.run(debug=True)             # start the application