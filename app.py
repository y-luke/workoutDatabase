import json

from flask import Flask, jsonify

app = Flask(__name__)


exercises = ['Burpees', 'Push-ups', 'Crunches', 'Squats']


@app.route('/')
def welcome():
    return 'Welcome to Workout Database!'


@app.route('/exercises', methods=['GET'])
def get_exercises():
    return jsonify(exercises)


if __name__ == '__main__':
    app.run()
