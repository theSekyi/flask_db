from flask import Flask,render_template,request,redirect,url_for


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, Flask!'


@app.route('/home',methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        data = request.form['content']
        #return redirect(url_for('index'))
        #print(data)
        #return redirect(request.url)
        if data != '':
            #render_template('home.html',data=data)
            print(data)

        



    return render_template('home.html')

