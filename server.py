from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['yourname'] = request.form['name']
    session['yourdojo'] = request.form['dojo']
    session['lang'] = request.form['favorite_lang']
    session['comment'] = request.form['comment']
    return redirect('/result')


@app.route('/result')
def result():
    return render_template('result.html')




if __name__ == "__main__":
    app.run(debug=True)
