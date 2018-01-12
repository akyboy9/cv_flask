from flask import request, render_template, redirect, Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index', methods = ['GET','POST'])
def index_submit():
    if request.method == 'POST':
        image = request.form['filename']
        print image
    return render_template('index.html')



if __name__ == "__main__":
    # Setting this to debug for production purposes only
    # remove this before actual deployment
    app.debug = True
    app.run()
