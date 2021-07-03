from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    title = "Avro.dev"
    return render_template('home.html', title=title)

@app.route('/<error>')
@app.errorhandler(404)
def page_not_found(error):
    title = error
    return render_template('page_not_found.html', error=error, title=title), 404

# Routes Example
# --------------
@app.route('/user/<string:user>')
def user(user):
   return "Hi "+ user

@app.route('/num/<int:n>')
def num(n):
    return "Number: {}".format(n)

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return "ID: {}, Username: {}".format(id, username)

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1, n2):
    return "Result: {}".format(n1 + n2)

@app.route('/default/')
@app.route('/default/<string:dft>')
def dft(dft="default view"):
    return "Value for default is: " + dft
# --------------

if __name__ == '__main__':
    # Note:
    # debug=True, port=1234, host='0.0.0.0'
    app.run(debug=True)
