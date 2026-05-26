from flask import Flask, jsonify, render_template, request
import json
import os

app = Flask(__name__, 
            template_folder='frontend/templates',
            static_folder='frontend/static')

# Load projects from JSON
def load_projects():
    with open('data/projects.json', 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    projects = load_projects()
    return render_template('index.html', projects=projects)

@app.route('/api/projects')
def get_projects():
    return jsonify(load_projects())

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    # In a real app, you would send an email or save to DB
    print(f"Received contact request from {data.get('email')}: {data.get('message')}")
    return jsonify({"status": "success", "message": "Message received!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
