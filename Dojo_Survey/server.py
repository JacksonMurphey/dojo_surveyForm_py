from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "asfd123123"

@app.route('/')
def start():

    return render_template('index.html')

@app.route('/user_info', methods=['POST'])
def userInfo():
    
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    session['contest'] = request.form['contest']
    
    
    print(request.form)
    return redirect('/results')

@app.route('/results')
def results():
    

    return render_template('result.html' )


if __name__=='__main__':
    app.run(debug=True)