# Flask Full CRUD API

##  Overview

This project is a RESTful API built with Flask that performs full CRUD (Create, Read, Update, Delete) operations on an in-memory list of events. It demonstrates handling JSON data, HTTP methods, and proper API design.

---

##  Features

* Create events using POST
* Retrieve all events using GET
* Update an event using PATCH
* Delete an event using DELETE
* JSON-based request and response handling
* Proper HTTP status codes

---

##  Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <repo-folder>
```

### 2. Create a virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install flask
```

### 4. Run the application

```bash
python3 app.py
```

Server will start at:

```
http://127.0.0.1:5000/
```

---

##  API Endpoints

### 🔹 GET /

Returns a welcome message

**Response**

```json
{
  "message": "Welcome to the Event API!"
}
```

---

### 🔹 GET /events

Returns all events

**Response**

```json
[
  { "id": 1, "title": "Tech Meetup" },
  { "id": 2, "title": "Python Workshop" }
]
```

---

### 🔹 POST /events

Creates a new event

**Request Body**

```json
{
  "title": "Hackathon"
}
```

**Response**

* Status: 201 Created

```json
{
  "id": 3,
  "title": "Hackathon"
}
```

---

### 🔹 PATCH /events/{id}

Updates an existing event

**Example**

```
PATCH /events/1
```

**Request Body**

```json
{
  "title": "Hackathon 2025"
}
```

**Response**

```json
{
  "id": 1,
  "title": "Hackathon 2025"
}
```

---

###  DELETE /events/{id}

Deletes an event

**Example**

```
DELETE /events/2
```

**Response**

* Status: 204 No Content
* No response body

---

---

##  Technologies Used

* Python 3
* Flask

