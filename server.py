from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key= "this is my key"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # print(request.form)
    session['name']=request.form['name']
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('form.html')




if __name__=='__main__':
    app.run(debug=True)