import json

from flask import Flask, request, render_template, url_for

app = Flask(__name__)


exercises = ['Burpees', 'Push-ups', 'Crunches', 'Squats']


@app.route('/')
def welcome():
    return render_template('home.html')


@app.route('/exercises', methods=['GET'])
def get_exercises():
    if request.method == 'GET':
        return json.dumps(exercises)


if __name__ == '__main__':
    app.run()
