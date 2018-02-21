from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd


app = Flask(__name__)


model = pickle.load( open( "noshow.p", "rb" ), encoding='latin1' )

def patients(age, scholarship, text_sent, woman, delta, problems):
    features = [[age,scholarship,False,False,False,False,text_sent,woman,delta,problems]]
    score = model.predict_proba(features)
    results = {"score":score[0,1]}
    return jsonify(results), results


@app.route('/')
def entry_page():
    return render_template('awesome.html')

@app.route('/patient_status/', methods=['GET', 'POST'])
def render_message():

    age = request.form['age']
    try:
        age_float = float(age)
    except:
        message = "Enter a number"
        return render_template('awesome.html',
                               message=message)

    delta = request.form['delta']
    try:
        delta_float = float(delta)
    except:
        message = "Enter a number"
        return render_template('awesome.html',
                               message=message)

    scholarship = request.form['scholarship'] 
    try:
        schol_bool = bool(scholarship)
    except:
        message = "Enter True or False"
        return render_template('awesome.html',
                               message=message) 

    text = request.form['text_sent']
    try:
        text_bool = bool(text)
    except:
        message = "Enter True or False"
        return render_template('awesome.html',
                               message=message)

    woman = request.form['woman']
    try:
        woman_bool = bool(woman)
    except:
        message = "Enter True or False"
        return render_template('awesome.html',
                               message=message)

    problems = request.form['problems']
    try:
        problems_bool = bool(problems)
    except:
        message = "Enter True or False"
        return render_template('awesome.html',
                               message=message)

    prob_json, prob = patients(age_float, schol_bool, text_bool, woman_bool, delta_float, problems_bool)


    
    if prob["score"]>=0.4:
        message = ("Percent likelihood of patient arrival: {:.2f}%".format(prob["score"]*100)+" You can expect your patient to arrive")
    else:
        message = ("Percent likelihood of patient arrival: {:.2f}%".format(prob["score"]*100)+" You should not expect your patient to arrive")

    return render_template('awesome.html',
                           message=message, probability=prob["score"])






if __name__ == '__main__':
    app.run(debug=True)