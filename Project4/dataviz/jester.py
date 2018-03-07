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
    return render_template('radical.html')

@app.route('/jester/', methods=['GET', 'POST'])
def render_message():

    age = request.form['rating']
    try:
        rated_float = float(rating)
    except:
        message = "Number must be between -10 and 10"
        return render_template('radical.html',
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