from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd
import random
from collections import defaultdict
from surprise import dump



app = Flask(__name__)


#model = pickle.load( open( "noshow.p", "rb" ), encoding='latin1' )
model = dump.load("/Users/kaitlin/recommender.p")[1]

# import jokelist from a csv
df = pd.read_csv('/Users/kaitlin/ds/metis/metisgh/Puryear_Metis/Project4/dataviz/cleanedjokes.csv', 
                      header=0, 
                      sep=',', 
                      index_col=0, 
                      parse_dates=True, 
                      encoding=None, 
                      tupleize_cols=None, 
                      infer_datetime_format=False)
jokelist = list(df.column)
#newjokeid = 15
#joketoscreen = jokelist[newjokeid]


# so jokes do not get told twice
already_said = [20, 15, 1]

# initialize a random user. Input random ratings for each joke between -5 to 5
person_init = []
for i in range(100):
    person_init.append((1, str(i), random.randint(-5,5)))

jokeid=15

#######
# all the work gets done here
def person_inputs(rating):
    jokeid=15
        # update person_init with inputed ratings, then apply the model
    person_init[jokeid] = (1, str(jokeid), float(rating))
    predictions = model.test(person_init)

        # model returns the top predicted joke id
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))
        
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:2]
    newjokeid = top_n[uid][1][0]
    newjokeid = int(newjokeid)

        # test if the joke has already been said, then return new joke id
    if newjokeid in already_said:
        newjokeid = random.randint(0,100)
        already_said.append(newjokeid)
    else:
        #newjokeid = random.randint(0,100)
        already_said.append(newjokeid)

        # return joke (as a string) from the joke id
    return newjokeid



@app.route('/')
def entry_page():
    jokeid = 15
    joketoscreen = jokelist[jokeid]
    return render_template('radical.html',joketoscreen=joketoscreen)


@app.route('/tell_me_a_joke/', methods=['GET', 'POST'])
def render_message():

    #personaljokeid = person_inputs(rating)
    #joketoscreen = jokelist[personaljokeid]
    
    rating = request.form['rating']
    rated_float = float(rating)
    
    #already_said = [20, 15]
    personaljokeid = person_inputs(rated_float)
    joketoscreen = jokelist[personaljokeid]    
    return render_template('radical.html',joketoscreen=joketoscreen)

    # prob_json, prob = patients(age_float, schol_bool, text_bool, woman_bool, delta_float, problems_bool)


    
    #if prob["score"]>=0.4:
        # message = ("Percent likelihood of patient arrival: {:.2f}%".format(prob["score"]*100)+" You can expect your patient to arrive")
    # else:
        #message = ("Percent likelihood of patient arrival: {:.2f}%".format(prob["score"]*100)+" You should not expect your patient to arrive")
    #return render_template('awesome.html',
                           #message=message, probability=prob["score"])






if __name__ == '__main__':
    app.run(debug=True)