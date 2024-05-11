from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_time')
def get_time():
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        time = data['time']
        people = data['people']
        return jsonify({'time': time, 'people': people})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
