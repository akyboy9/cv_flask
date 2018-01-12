from flask import request, render_template, redirect, Flask

app = Flask(__name__)

#inital template routing

@app.route('/')
def index():
    return render_template('index.html')

#Post method for aquiring .jpg from html input

@app.route('/index', methods = ['GET','POST'])
def index_submit():
    if request.method == 'POST':
        image = request.form['filename']
        print image
        return redirect('/success')

#SUCCESUFL REDIRECT

@app.route('/success')
def success():
    return render_template('redirect.html')

#RETURN BACK TO INITIAL

@app.route('/redirect', methods = ['GET', 'POST'])
def go_back():
    if request.method == 'POST':
        return redirect('/')

if __name__ == "__main__":
    # Setting this to debug for production purposes only
    # remove this before actual deployment
    app.debug = True
    app.run()
