from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Create a list called 'events' with a couple of sample event dictionaries
# Each dictionary should have an 'id' and a 'title'
events =[
    {'id': 1, 'title': 'scuba'},
    {'id': 2,  'title': 'roadtrip'}
]

# TASK: Create a route for "/"
# This route should return a JSON welcome message
@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message':'Welcome'})


# TASK: Create a GET route for "/events"
# This route should return the full list of events as JSON
@app.route('/events', methods=['GET'])
def get_event():
    return jsonify(events)

# TASK: Create a POST route for "/events"
@app.route('/events', methods=['POST'])
def create_event():
    # This route should:
    # 1. Get the JSON data from the request
    data = request.get_json() 
    # 2. Validate that "title" is provided
    if 'title' not in data:
        return jsonify({'error': 'title not found'}), 400
    

    # 3. Create a new event with a unique ID and the provided title
    new_id = max([event['id'] for event in events]) + 1 if events else 1
    new_event = {'id': new_id, 'title': data['title']}
    

    # 4. Add the new event to the events list
    events.append(new_event)
    # 5. Return the new event with status code 201
    return jsonify(new_event), 201

if __name__ == "__main__":
    app.run(debug=True ,port=5003)
