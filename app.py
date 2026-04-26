from flask import Flask, jsonify, request

app = Flask(__name__)


class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {
            "id": self.id, 
            "title": self.title
        }


events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# Root Route
@app.route("/")
def home():
    return jsonify({"message": 'Welcome to the Event API!'})

# GET ALL events
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([event.to_dict() for event in events])

# CREATE (POST)
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    #validate input
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400
    
    new_id = max(event.id for event in events) + 1 if events else 1
    new_event = Event(new_id, data["title"])
    events.append(new_event)


    return jsonify(new_event.to_dict()), 201


#UPDATE (PATCH)
@app.route("/events/<int:event_id>", methods=["PATCH","DELETE"])
def update_event(event_id):
    data = request.get_json()

    for event in events:
        if event.id == event_id:
            if "title" in data:
                event.title = data["title"]
            return jsonify(event.to_dict())

    return jsonify({"error": "Event not found"}), 404
    

# DELETE
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    global events

    for event in events:
        if event.id == event_id:
            events.remove(event)
            return "", 204
        
    return jsonify({"error": "Event not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
