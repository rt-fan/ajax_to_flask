from flask import Flask, render_template
import json


app = Flask(__name__)


@app.route('/')
def index():
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        time = data['time']
        people = data['people']
        return render_template('index.html', time=time, people=people)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
