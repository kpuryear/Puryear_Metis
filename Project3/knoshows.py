import pickle
import pandas as pd

model = pickle.load( open( "noshow.p", "rb" ), encoding='latin1' )

def patients(age, scholarship, text_sent, woman, delta, problems):
    features = [age,scholarship,False,False,False,False,text_sent,woman,delta,problems]
    score = model.predict_proba(features)
    results = {"score":score[1]}
    return flask.jsonify(results)
