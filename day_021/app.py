from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>!Hola Amigo!</h1>"

@app.route('/user/<username>')
def indejajax(username):
    return render_template('index.html', username=username)

@app.route('/template/')
def template():
    name = 'Jinjia2 ninja'
    myindex = 1
    mylist = [1, 2, 3, 4]
    # mydict = {
    #     key:'age',
    #     value:'25'   
    # }
    mytuple = (1, 2, 3, 4)

    return render_template('template.html', name=name, myindex=myindex, mylist=mylist, mytuple=mytuple)

if __name__ == "__main__":
    app.run(debug=True)