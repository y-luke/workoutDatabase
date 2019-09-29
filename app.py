import json
from flask import Flask

app = Flask (__name__)

exercises = ['Burpees', 'Push-ups', 'Crunches', 'Squats']

@app.route('/')
def welcome():
    return('Welcome to Workout Database!')

@app.route('/exercises')
def get_exercises():
    return json.dumps(exercises)

if __name__ == '__main__':
    app.run()