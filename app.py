import json

from flask import Flask, request, render_template, jsonify, url_for

app = Flask(__name__)


exercises = [{'name': 'Burpees', 'area': 'Cardio'},
             {'name': 'Push-ups', 'area': 'Arms'},
             {'name': 'Crunches', 'area': 'Core'},
             {'name': 'Squats', 'area': 'Legs'}]


@app.route('/')
def welcome():
    return render_template('home.html')


@app.route('/exercises', methods=['GET'])
def get_exercises():
    if request.method == 'GET':
        return jsonify(exercises)

@app.route('/exercises', methods=['POST'])
def add_exercise():
    if request.method == 'POST':
        new_exercise = request.get_json()
        exercises.append(new_exercise)
        return jsonify(exercises)

@app.route('/exercises/<string:name>', methods=['GET'])
def get_one_exercise(name):
    if request.method == 'GET':
        one_exercise = exercises[0]
        for i,q in enumerate(exercises):
            if q['name'] == name:
                one_exercise = exercises[i]
        return jsonify(one_exercise)

@app.route('/exercises/<string:name>', methods=['DELETE'])
def delete_one_exercise(name):
    if request.method == 'DELETE':
        for i,q in enumerate(exercises):
            if q['name'] == name:
                del exercises[i]
        return jsonify(exercises)


if __name__ == '__main__':
    app.run()
